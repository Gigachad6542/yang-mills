"""T71: scalar checks for note 65 (CMP 119 Sect. 3 at d = 3 with R = identity).

No linear algebra is involved: everything is the exact 3D coupling flow
    g_j^2 = g^2 L^(j-K),   j = 0..K,   g_K = g  (CMP 109 p. 259: g_k^2 = g^2 L^k eps),
written in terms of lam_j = log g_j^{-2} = lam_K + (K-j) log L.
Balaban's constants (A_0, A_1, B_3, M, delta, ...) are not specified in the
paper ("sufficiently large/small"), so the numbers below test only the
d-dependent inequalities in CMP 119 (2.6)-(2.9), (3.8), (3.17)-(3.19) and the
exponent bookkeeping of (2.31), (2.43)-(2.46), (3.67); they do not verify
Balaban's constants.

Parts
  A  The 4D inequalities (2.6)-(2.9) evaluated on the 3D flow.
  B  The single-step constants of (3.8): 4D as printed vs the 3D replacement.
  C  Compatibility of the cube sizes R_j (smallest power of L >= lam_j^r):
     R_{k+1} >= R_k / L (single step) and R_m <= L^(n-m) R_n.
  D  Exponent bookkeeping: marginal volume exponent 4-d, sums over scales.
  E  Elementary lemma: sum over creation scales is dominated by the current scale.
  F  exp(-c p_0(g)^2) <= (g p_0(g))^q for small g, and p_0 >= 5r versus (d+1) r.
  G  Exact linear algebra (eigh): the invariants of the tensor Pi_{mu nu,kappa lambda}
     of CMP 119 (3.55)-(3.61) under reflections and permutations, d = 2, 3, 4.
  H  The 4D inequalities (2.7b), (2.9b) on chains of length of order R_n (the
     unprocessed-domain regime of note 49 sect. 1), on the exact 3D flow.
"""
import math
from fractions import Fraction

LN = math.log


def flow(lamK, K, L):
    ell = LN(L)
    return [lamK + (K - j) * ell for j in range(K + 1)]


def R_of(lam, r, L):
    """Smallest power of L that is >= lam^r (CMP 119 (2.5)); returns the exponent."""
    target = lam ** r
    e = 0
    while L ** e < target:
        e += 1
    return e


def part_A(L, beta0, p, p0, r, lamK, K, title):
    lam = flow(lamK, K, L)
    ell = LN(L)
    logg = [-0.5 * x for x in lam]                       # log g_j
    logeps = [logg[j] + p0 * LN(lam[j]) for j in range(K + 1)]   # log eps_j, A_0 = 1
    Re = [R_of(lam[j], r, L) for j in range(K + 1)]      # exponent of L
    lb = LN(1 + beta0)
    rows = {}

    def record(name, test):
        bad = []
        tot = 0
        for m in range(K):
            for n in range(m + 1, K + 1):
                tot += 1
                if not test(m, n, n - m):
                    bad.append(n - m)
        rows[name] = (len(bad), tot, (min(bad) if bad else None))

    record("(2.6a) g_n <= (1+b0)(n-m)^(1/2) g_m",
           lambda m, n, s: logg[n] - logg[m] <= lb + 0.5 * LN(s) + 1e-12)
    record("(2.6b) g_m <= (1+b0) g_n",
           lambda m, n, s: logg[m] - logg[n] <= lb + 1e-12)
    record("(2.7a) lam_n^p <= (1+b0) lam_m^p",
           lambda m, n, s: p * (LN(lam[n]) - LN(lam[m])) <= lb + 1e-12)
    record("(2.7b) lam_m^p <= (1+b0)(n-m)^b0 lam_n^p",
           lambda m, n, s: p * (LN(lam[m]) - LN(lam[n])) <= lb + beta0 * LN(s) + 1e-12)
    record("(2.8a) eps_n <= (1+b0)(n-m)^(1/2) eps_m",
           lambda m, n, s: logeps[n] - logeps[m] <= lb + 0.5 * LN(s) + 1e-12)
    record("(2.8b) eps_m <= (1+b0)^2 (n-m)^b0 eps_n",
           lambda m, n, s: logeps[m] - logeps[n] <= 2 * lb + beta0 * LN(s) + 1e-12)
    record("(2.9a) R_n <= L R_m",
           lambda m, n, s: Re[n] <= Re[m] + 1)
    record("(2.9b) R_m <= (L+1)(n-m)^b0 R_n",
           lambda m, n, s: Re[m] * ell <= LN(L + 1) + beta0 * LN(s) + Re[n] * ell + 1e-12)
    print(f"\n[Part A] {title}: L={L}, beta0={beta0}, p={p}, p0={p0}, r={r}, "
          f"lam_K=log g^-2={lamK}, K={K}")
    for name, (nb, tot, smin) in rows.items():
        print(f"   {name:48s} violated for {nb:5d} of {tot:5d} pairs (m<n)"
              + (f"; smallest violating n-m = {smin}" if smin else ""))
    # 3D replacements (exact flow): g_n = L^((n-m)/2) g_m, lam_m = lam_n + (n-m) ln L
    mx6 = max(logg[n] - logg[m] - 0.5 * (n - m) * ell for m in range(K) for n in range(m + 1, K + 1))
    mx8 = max(logeps[n] - logeps[m] - 0.5 * (n - m) * ell for m in range(K) for n in range(m + 1, K + 1))
    mx7 = max(p * (LN(lam[m]) - LN(lam[n])) - (n - m) * ell
              for m in range(K) for n in range(m + 1, K + 1))
    print(f"   3D replacements: max log[g_n/(L^((n-m)/2) g_m)] = {mx6:.3e} (0 means equality), "
          f"max log[eps_n/(L^((n-m)/2) eps_m)] = {mx8:.3e} (<= 0), "
          f"max log[(lam_m/lam_n)^p / L^(n-m)] = {mx7:.3e} (<= 0)")
    # single step ratios
    r1 = [math.exp(logeps[k + 1] - logeps[k]) for k in range(K)]
    print(f"   single step eps_(k+1)/eps_k over k=0..K-1: min {min(r1):.4f}, max {max(r1):.4f}; "
          f"L^(1/2) = {L**0.5:.4f}; (1+beta0) = {1+beta0:.4f}")
    g1 = [math.exp(logg[k + 1] - logg[k]) for k in range(K)]
    print(f"   single step g_(k+1)/g_k = {min(g1):.6f} .. {max(g1):.6f} (= L^(1/2) exactly)")
    return Re


def part_A_Kscan(L, beta0, p, lamK):
    """(2.7b) at (m,n) = (0,K): first K for which it fails."""
    ell = LN(L)
    first = None
    for K in range(1, 200000):
        lam0 = lamK + K * ell
        if p * (LN(lam0) - LN(lamK)) > LN(1 + beta0) + beta0 * LN(K):
            first = K
            break
    print(f"   (2.7b) at (m,n)=(0,K), p={p}, lam_K={lamK}: first failing K = {first}")


def part_A_Rscan(L, beta0, r, lamK):
    """(2.9b) R_m <= (L+1)(n-m)^b0 R_n at (m,n) = (0,K): first K for which it fails."""
    ell = LN(L)
    eK = R_of(lamK, r, L)
    first = None
    for K in range(1, 200000):
        e0 = R_of(lamK + K * ell, r, L)
        if (e0 - eK) * ell > LN(L + 1) + beta0 * LN(K) + 1e-12:
            first = K
            break
    print(f"   (2.9b) at (m,n)=(0,K), r={r}, lam_K={lamK}: first failing K = {first}")


def part_A_eps_condition():
    """3D (2.8b): eps_m/eps_n = L^(-s/2) (1+s ell/lam_n)^p0 <= exp(-s ell (1/2 - p0/lam_n)) <= 1 if lam_n >= 2 p0."""
    print("   3D (2.8b) with room (eps_m <= eps_n) holds when lam_n >= 2 p0, since 1+x <= e^x:")
    for p0, L in ((10, 2), (10, 3)):
        worst = -float('inf')
        lam_n = 2.0 * p0
        for s in range(1, 400):
            worst = max(worst, -0.5 * s * LN(L) + p0 * LN(1 + s * LN(L) / lam_n))
        print(f"     p0={p0}, L={L}, lam_n=2 p0={lam_n}: max_s log[eps_m/eps_n] = {worst:.4e} (<= 0)")


def part_B():
    print("\n[Part B] constant in (3.8):  rho/L^2 + 2/5 < 1  (2/10 (1+4/10 eps_k) <= 4/10 as printed)")
    b0 = Fraction(1, 10)
    print("   4D as printed: rho = 2(1+beta0)  (2(1+b0)L^-2 + 4/10 < 1)")
    for L in (2, 3, 4, 5, 6, 8):
        c4 = 2 * (1 + b0) / L ** 2 + Fraction(2, 5)
        print(f"     L={L}: 2(1+b0)/L^2 + 2/5 = {c4} = {float(c4):.4f}  <1: {c4 < 1}")
    print("   3D replacement: eps_(k+1) <= L^(1/2) eps_k  =>  rho = L^(1/2)(1+beta0)")
    print("     condition (1+b0) < (3/5) L^(3/2)  <=>  (1+b0)^2 < (9/25) L^3  <=>  900 L^3 > 3025 (exact, b0=1/10)")
    for L in (2, 3, 4, 5, 6, 8):
        exact = 900 * L ** 3 > 3025
        val = (1 + float(b0)) / L ** 1.5 + 0.4
        print(f"     L={L}: 900 L^3 = {900*L**3} > 3025: {exact};  (1+b0) L^(-3/2) + 2/5 = {val:.4f}")
    print("   printed constant 2(1+b0) = %.4f versus L^(1/2) (the single-step ratio eps_(k+1)/eps_k <= L^(1/2) on the 3D flow):" % float(2 * (1 + b0)))
    for L in (2, 3, 4, 5, 6, 8):
        print(f"     L={L}: L^(1/2) = {L**0.5:.4f}; L^(1/2) <= 2(1+b0): {L**0.5 <= float(2*(1+b0))}; "
              f"L^(1/2)(1+0.2 eps_k eta) <= 2(1+b0) needs eps_k eta <= {(float(2*(1+b0))/L**0.5 - 1)/0.2:.3f}")
    print("   so the printed constant 2(1+b0) covers L <= 4 (with eps_k eta small); for L >= 5 it is read as L^(1/2)(1+b0).")


def part_C(L, r, lamK, K):
    ell = LN(L)
    lam = flow(lamK, K, L)
    Re = [R_of(lam[j], r, L) for j in range(K + 1)]
    # single step: R_{k+1} >= R_k / L  <=> e_{k+1} >= e_k - 1
    single_bad = [k for k in range(K) if Re[k + 1] < Re[k] - 1]
    # physical monotonicity: R_m <= L^(n-m) R_n  <=> e_m <= (n-m) + e_n
    phys_bad = [(m, n) for m in range(K) for n in range(m + 1, K + 1) if Re[m] > (n - m) + Re[n]]
    lam_min = ell / (1 - L ** (-1.0 / r))
    print(f"   L={L}, r={r}, lam_K={lamK}, K={K}: R_K = L^{Re[K]}, R_0 = L^{Re[0]}; "
          f"single-step violations of R_(k+1)>=R_k/L: {len(single_bad)}; "
          f"violations of R_m<=L^(n-m)R_n: {len(phys_bad)}; "
          f"sufficient lam_K >= ell/(1-L^(-1/r)) = {lam_min:.3f}: {lamK >= lam_min}")


def part_C2(L, r, lamK, K):
    """Domain growth: D_j = sum_{u>=0} (R_{j-u}/R_j) L^-u (extension of a persisting domain, in j-units, per layer-unit)."""
    ell = LN(L)
    lam = flow(lamK, K, L)
    Re = [R_of(lam[j], r, L) for j in range(K + 1)]
    D = []
    for j in range(K + 1):
        D.append(sum(float(L) ** (Re[j - u] - Re[j] - u) for u in range(j + 1)))
    bound = None
    if lamK > r:
        bound = L / (1 - L ** (-(1 - r / lamK)))
    print(f"   L={L}, r={r}, lam_K={lamK}, K={K}: max_j D_j = {max(D):.4f}  "
          f"(analytic bound L/(1-L^-(1-r/lam_K)) = {bound if bound is None else round(bound, 4)})")


def part_D():
    print("\n[Part D] exponent bookkeeping (CMP 119 (2.31), (2.43)-(2.46), (3.67)); n-j = s")
    print("   per point z of the j-lattice the remainder after the counterterm is O((L^-s)^(5-b)) (3.67),")
    print("   the F^2 term itself O((L^-s)^4) (3.57)-(3.66); the number of z per unit n-cell is L^(s d).")
    for d in (4, 3):
        print(f"   d={d}: summed remainder exponent 5-d-b = {5-d}-b" + (" (only with a counterterm, absent at d = 3)" if d == 3 else "") + f"; summed F^2 (marginal) exponent 4-d = {4-d}")
    n = 60
    for d, L in ((4, 2), (3, 2), (3, 3)):
        tot = sum(float(L) ** (-(4 - d) * s) for s in range(n + 1))
        lim = 1.0 / (1 - L ** (-(4 - d))) if d == 3 else float('inf')
        print(f"   d={d}, L={L}: sum_(s=0..{n}) L^(-(4-d)s) = {tot:.6f}   (limit n->inf: {lim})")
    for d, L in ((4, 2), (3, 2), (3, 3)):
        print(f"   d={d}, L={L}: L^d - 1 = {L**d - 1} non-central sites per block; d^2 = {d*d}")
    print("   => d=4: the marginal sum grows like n (needs the beta_j counterterm and g_j^kappa0 factors);")
    print("      d=3: it is a convergent geometric series, no coupling counterterm is needed, (2.43) holds with exponent 1 (beta = 1 in (2.43)'s own notation).")


def part_E():
    print("\n[Part E] Lemma 65.2: sum_(s>=0) L^(d s) exp(-c (lam + s ell)^q) <= C0 exp(-c lam^q),")
    print("         C0 = sum_(s>=0) exp(s d ell - c (s ell)^q) < inf for q > 1  (superadditivity (a+b)^q >= a^q + b^q)")
    for (d, L, c, q) in ((3, 2, 1.0, 20), (3, 2, 1.0, 4), (3, 2, 0.1, 4), (3, 3, 0.1, 4), (4, 2, 0.1, 4)):
        ell = LN(L)
        C0 = sum(math.exp(s * d * ell - c * (s * ell) ** q) for s in range(0, 400)
                 if s * d * ell - c * (s * ell) ** q > -700)
        print(f"   d={d}, L={L}, c={c}, q={q}: C0 = {C0:.6g}")
    # direct check for q = 4 at moderate lam (plain floats are exact enough here)
    d, L, c, q = 3, 2, 0.1, 4
    ell = LN(L)
    C0 = sum(math.exp(s * d * ell - c * (s * ell) ** q) for s in range(0, 400))
    for lam in (1.0, 2.0, 3.0, 5.0):
        lhs = sum(math.exp(s * d * ell - c * (lam + s * ell) ** q) for s in range(0, 400))
        rhs = C0 * math.exp(-c * lam ** q)
        print(f"   direct check d=3,L=2,c=0.1,q=4, lam={lam}: lhs = {lhs:.6e} <= rhs = {rhs:.6e}: {lhs <= rhs * (1 + 1e-12)}")


def part_F():
    print("\n[Part F] (i) exp(-c p_0(g)^2) <= (g p_0(g))^q for lam = log g^-2 >= lam_*(q);")
    print("   p_0(g) = A_0 lam^p0 (CMP 119 p. 244; p. 246 text after (1.1)), g = exp(-lam/2). Take A_0 = 1 (A_0 >= 1 only helps).")
    print("   Condition: c lam^(2 p0) >= q (lam/2 - p0 ln lam).  Sufficient: c lam^(2 p0) >= q lam/2,")
    print("   i.e. lam >= (q/(2c))^(1/(2 p0 - 1)) (and lam >= 1).  lam_* below = last sign change of the exact condition on a grid of step 1e-3.")
    for (c, p0) in ((0.5, 10), (0.25, 10), (0.25, 15)):
        for q in (5, 10, 100, 1000):
            ok = lambda lam: c * lam ** (2 * p0) >= q * (lam / 2 - p0 * LN(lam))
            lam = 4.0
            while not ok(lam):
                lam += 1.0            # (never loops: LHS grows like lam^(2 p0))
            lam_last_bad = None
            x = 0.5
            while x < lam:            # scan [0.5, lam) for failures; lam_* = last failing grid point + 1e-3
                if not ok(x):
                    lam_last_bad = x
                x += 1e-3
            lam_star = (lam_last_bad + 1e-3) if lam_last_bad is not None else 0.5
            suff = max(1.0, (q / (2 * c)) ** (1.0 / (2 * p0 - 1)))
            print(f"     c={c}, p0={p0}, q={q}: lam_* = {lam_star:.3f} (g^2 <= {math.exp(-lam_star):.3e}); "
                  f"sufficient closed form lam >= {suff:.3f}; closed form >= lam_*: {suff >= lam_star - 1e-9}")
    print("   (iii) polynomial degree r d + 1 of the summed domain volumes versus 2 p_0 >= 10 r and (d+1) r:")
    for r in (2, 3):
        for d in (3, 4):
            print(f"     r={r}, d={d}: r d + 1 = {r*d+1} <= (d+1) r = {(d+1)*r} < 2 p_0 >= {10*r}")
    print("   (ii) CMP 119 p. 246 (text after (1.1)): p_0 >= 5 r.  Entropy-vs-weight needs 2 p_0 > (d+1) r (note 49 sect. 5).")
    for r in (2, 3):
        p0min = 5 * r
        for d in (3, 4):
            print(f"     r={r}, d={d}: need p_0 > {(d+1)*r/2}; p. 246 gives p_0 >= {p0min}; "
                  f"2 p_0 / ((d+1) r) >= {2*p0min/((d+1)*r):.2f}")


def signed_perms(d):
    """All signed permutation matrices (the hyperoctahedral group B_d, order 2^d d!)."""
    import itertools
    import numpy as np
    out = []
    for perm in itertools.permutations(range(d)):
        for signs in itertools.product((1, -1), repeat=d):
            M = np.zeros((d, d))
            for i, pi in enumerate(perm):
                M[pi, i] = signs[i]
            out.append(M)
    return out


def part_G():
    """Invariants of Pi_{mu nu,kappa lambda} (CMP 119 (3.55)-(3.61)) by exact linear algebra.

    Unknown: a d x d x d x d array Pi[mu,nu,kappa,lambda] (the coefficient of
    tr F_{kappa mu} F_{lambda nu} in (3.56)-(3.57)).  Constraints:
      (S)  Pi[mu,nu,k,l] = Pi[nu,mu,l,k]            (E^(2)_{mu nu}(x,y) = E^(2)_{nu mu}(y,x), (3.50))
      (A)  Pi[mu,nu,k,l] = -Pi[k,nu,mu,l] = -Pi[mu,l,k,nu]     (3.55)
      (R)  ((x^4 r) Pi) = Pi for every r in B_d    (3.60): reflections and permutations of the axes
    The null space of the stacked constraint matrix is found from the eigenvalues of the
    symmetric PSD matrix C^T C (numpy.linalg.eigh); no pseudo-inverse is used.
    """
    import numpy as np
    print("\n[Part G] exact linear algebra: invariants of Pi_{mu nu,kappa lambda} under B_d, (3.55)-(3.61)")
    for d in (2, 3, 4):
        n = d ** 4
        idx = lambda a, b, c, e: ((a * d + b) * d + c) * d + e
        I = np.eye(n)

        def perm_matrix(f):
            """Matrix P with (P x)[idx(m,n,k,l)] = x[idx(f(m,n,k,l))]."""
            P = np.zeros((n, n))
            for a in range(d):
                for b in range(d):
                    for c in range(d):
                        for e in range(d):
                            P[idx(a, b, c, e), idx(*f(a, b, c, e))] = 1.0
            return P

        S = perm_matrix(lambda a, b, c, e: (b, a, e, c)) - I                    # (S)
        A1 = perm_matrix(lambda a, b, c, e: (c, b, a, e)) + I                   # Pi + Pi(k,nu,mu,l) = 0
        A2 = perm_matrix(lambda a, b, c, e: (a, e, c, b)) + I                   # Pi + Pi(mu,l,k,nu) = 0
        G = sum((np.kron(np.kron(r, r), np.kron(r, r)) - I).T @ (np.kron(np.kron(r, r), np.kron(r, r)) - I)
                for r in signed_perms(d))
        GR = G
        Gall = GR + S.T @ S + A1.T @ A1 + A2.T @ A2
        w_R = np.linalg.eigvalsh(GR)
        w, V = np.linalg.eigh(Gall)
        nullR = int(np.sum(w_R < 1e-9))
        null = int(np.sum(w < 1e-9))
        gap = float(w[null]) if null < n else float('nan')
        print(f"   d={d}: |B_d| = {len(signed_perms(d))}; invariant 4-tensors under B_d alone: {nullR}; "
              f"with (S),(A): {null} (largest |null eigenvalue| {abs(w[null-1]):.2e}, smallest nonzero eigenvalue {gap:.3f})")
        if null == 1:
            v = V[:, 0]
            v = v / v[idx(1, 1, 0, 0)]                      # normalise Pi_{22,11} = 1 (0-based indices 1,1,0,0)
            Pi = v.reshape(d, d, d, d)
            nz = [(a, b, c, e) for a in range(d) for b in range(d) for c in range(d) for e in range(d)
                  if abs(Pi[a, b, c, e]) > 1e-9]
            # block kappa<mu, lambda<nu  (the sum in (3.57))
            blk = {(a, b, c, e): Pi[a, b, c, e] for a in range(d) for b in range(d) for c in range(d)
                   for e in range(d) if c < a and e < b}
            diag_ok = all(abs(val - 1.0) < 1e-9 for (a, b, c, e), val in blk.items() if (a, c) == (b, e))
            off_ok = all(abs(val) < 1e-9 for (a, b, c, e), val in blk.items() if (a, c) != (b, e))
            print(f"      normalised Pi_(22,11) = 1: nonzero entries = {len(nz)}; in the block kappa<mu, lambda<nu: "
                  f"entries with (mu,kappa) = (nu,lambda) all equal to 1: {diag_ok}; all others 0: {off_ok}; "
                  f"number of pairs kappa<mu = {d*(d-1)//2}")


def part_H():
    ell = LN(2)
    print("\n[Part H] 4D inequalities (2.7b), (2.9b) on chains of length s = R_n (unprocessed-domain regime), exact 3D flow")
    print("   L=2, beta0=0.1, p=2, r=2; lam_n = log g_n^-2; lam_m = lam_n + s ln L; R_n = smallest power of L >= lam_n^r")
    for lam_n in (10.0, 20.0, 50.0, 100.0, 400.0):
        e = R_of(lam_n, 2, 2)
        s = 2 ** e
        lam_m = lam_n + s * ell
        lhs7 = (lam_m / lam_n) ** 2
        rhs7 = 1.1 * s ** 0.1
        em = R_of(lam_m, 2, 2)
        ratio9 = 2.0 ** (em - e)
        rhs9 = 3 * s ** 0.1
        phys = em <= s + e
        print(f"   lam_n={lam_n:6.1f}: s=R_n={s:6d}; (2.7b): (lam_m/lam_n)^p = {lhs7:10.2f} <= {rhs7:6.3f}: {lhs7 <= rhs7}; "
              f"(2.9b): R_m/R_n = {ratio9:10.1f} <= {rhs9:6.3f}: {ratio9 <= rhs9}; physical R_m <= L^s R_n: {phys}")


def main():
    print("T71 scalar checks (see header of this file for scope)")
    print("3D flow: g_j^2 = g^2 L^(j-K), lam_j = log g_j^-2 = lam_K + (K-j) log L (CMP 109 p. 259)")
    # Part A, window large enough to exhibit all behaviours
    part_A(L=2, beta0=0.1, p=2, p0=10, r=2, lamK=400.0, K=60, title="g tiny (lam_K = 400)")
    part_A_Kscan(2, 0.1, 2, 400.0)
    part_A_Kscan(2, 0.1, 20, 400.0)
    part_A_Kscan(2, 0.1, 2, 4000.0)
    part_A_Rscan(2, 0.1, 2, 400.0)
    part_A_Rscan(2, 0.1, 2, 4000.0)
    part_A_eps_condition()
    part_B()
    print("\n[Part C] cube sizes R_j = smallest power of L >= (log g_j^-2)^r  (CMP 119 (2.5))")
    for (L, r, lamK, K) in ((2, 2, 400.0, 60), (2, 2, 30.0, 60), (2, 2, 5.0, 60), (2, 3, 5.0, 60),
                            (3, 2, 5.0, 40), (2, 2, 1.0, 60)):
        part_C(L, r, lamK, K)
    print("   domain growth D_j = sum_u (R_(j-u)/R_j) L^-u (a persisting domain stays within O(m_0 L M R_j D_j) of its seed, j-units):")
    for (L, r, lamK, K) in ((2, 2, 400.0, 60), (2, 2, 30.0, 60), (2, 2, 5.0, 60), (3, 2, 5.0, 40)):
        part_C2(L, r, lamK, K)
    part_D()
    part_E()
    part_F()
    part_G()
    part_H()


if __name__ == "__main__":
    main()
