"""T84 (note 68): checks for the surplus induction of Prop. 68.1 (CMP 122 II (1.80)-(1.88) at R = identity).

Pure standard library. Every number quoted in research/68-large-field-gas-d3.md is printed here
(output: t84_surplus_checks.out).

Balaban's constants (A_0, A_1, gamma_0, c_E, M, ...) are not specified in the papers. Part A therefore
evaluates the thresholds of Prop. 68.1 for *sample* constants (marked as such); the exponents are the
content. Part B runs the recursion (1.83)/(1.85) of II on a toy geometry and checks the invariant
(68.1), kappa >= Phi + lambda D + c_* P^2, on random histories; the toy geometry is not Balaban's, it
only has the properties the proof uses (S monotone and union-compatible, d' = number of cells so that
d' is subadditive, a bounded dilation constant for new regions). Part C checks Lemma 65.2 for the
constants of Part A.

Part A  exponent condition 2 p_0 > (d+2) r and the threshold x_K >= Lambda_1^{1/(2 p_0 - (d+2) r)}.
Part B  random histories on the toy geometry: the invariant of Prop. 68.1 and the exactness of fact (a).
Part C  Lemma 65.2: sum over creation scales for the weight exp(-c_* x^{2 p_0}).
"""
import math
import random

# ---------------------------------------------------------------- Part A
print("PART A. Prop. 68.1: (CC)  c_* P_m^2 >= C_c(lambda) R_m^(d+2) for all m <= K.")
print("  With R_m <= L x_m^r, P_m = x_m^p0, x_m >= x_K, it holds once x_K^(2 p0 - (d+2) r) >= Lambda_1 = C_c L^(d+2)/c_*.")
print("  The merge step needs c_* P^2 >= 2 d c_E M^d R^(d+1), which follows from (CC) because C_S = 3*126^d >= 2d.")
d = 3
L = 13
cEMd = 1.0                      # SAMPLE: c_E M^d := 1 (Balaban's O(1))
gamma0, A1 = 0.5, 1.0           # SAMPLE: gamma_0 = 1/2 (p. 380 'we may take gamma_0 = 1/2'), A_1 = 1
c0 = 0.5 * gamma0 * A1 ** 2     # c_0 = (1/2) gamma_0 A_1^2 (II p. 381)
cstar = c0 / (4 * 14 ** d)      # c_* = c_0/(4 * 14^d)
CS = 3 * 126 ** d               # (Gm-S)
CPhi = cEMd * CS
CV = 3 * 2 ** (d - 1) * (CS + 1)
print(f"  sample constants: d = {d}, L = {L}, c_E M^d = {cEMd}, c_0 = {c0}, c_* = {cstar:.4e}, C_S = {CS}, C_V = {CV}")
print(f"  C_S >= 2d: {CS >= 2 * d};  (d+2)r/2 < (d+1)r for r = 1..4: {all((d + 2) * r / 2 < (d + 1) * r for r in (1, 2, 3, 4))}")
print("| lambda | r | p_0 | 2p_0 - (d+2)r | Lambda_1 | x_K threshold | g^2 = e^-x_K |")
print("|---|---|---|---|---|---|---|")
for lam in (0.0, 10.0, 100.0):
    Cc = cEMd + CPhi + lam * CV
    Lam1 = Cc * L ** (d + 2) / cstar
    for (r, p0) in ((2, 10), (2, 11), (3, 15), (2, 5)):
        a = 2 * p0 - (d + 2) * r
        if a > 0:
            xth = max(1.0, Lam1 ** (1.0 / a))
            print(f"| {lam:g} | {r} | {p0} | {a} | {Lam1:.3e} | {xth:.2f} | {math.exp(-xth):.2e} |")
        else:
            print(f"| {lam:g} | {r} | {p0} | {a} | {Lam1:.3e} | no threshold (a <= 0) | - |")
print("  row (r, p_0) = (2, 5) is not CMP 119's p_0 >= 5r: it has 2p_0 = (d+2)r (equality), where (CC) is a constant inequality.")
print("  CMP 119 p. 246: p_0 >= 5r, e.g. (r, p_0) = (2, 10), (3, 15): margin 2p_0 - 5r = 5r.")
print()

# ---------------------------------------------------------------- Part B
# Toy geometry. d' = number of cells (so d'+1 = cells + 1), V = cells (R = 1).
# S(Z) = dilate(coarsen(Z, Lt), w). Monotone and union-compatible. New region Q gets domain dilate(Q, 2).
Lt, w = 2, 1
Kt = 10
ell = math.log(L)
p0t = 5


def coarsen(cells, f):
    return {(x // f, y // f, z // f) for (x, y, z) in cells}


def dilate(cells, r):
    out = set()
    rg = range(-r, r + 1)
    for (x, y, z) in cells:
        for dx in rg:
            for dy in rg:
                for dz in rg:
                    out.add((x + dx, y + dy, z + dz))
    return out


def S(cells):
    return dilate(coarsen(cells, Lt), w)


def touch(A, B):
    return bool(dilate(A, 1) & B)


def run_history(seed, xK, t, lam, e=1.0, nsteps=Kt, p_new=(0.55, 0.3, 0.15)):
    """Return (min normalized slack, case at min, C_Phi_obs, C_V_obs, counts). Slack of (68.1):
    (kappa - Phi - lam D - c_* Q_m)/(c_* Q_m), Q_m = P_m^2. c_0 is scaled by t."""
    rnd = random.Random(seed)
    c0t = c0 * t
    cs = c0t / (2 * 125)       # toy analogue of c_0/(4*14^d): dilation constant 5^3 = 125, then 1/2
    P = lambda m: (xK + (Kt - m) * ell) ** p0t
    comps = []                 # dicts: cells (scale m-1), kappa, jf
    worst = (1e300, "")
    CPh = 0.0
    CVo = 0.0
    counts = {"old": 0, "new": 0, "merge": 0}
    for m in range(1, nsteps + 1):
        Pm, Qm = P(m), P(m) ** 2
        doms = []              # (cells, kappa_v, j_v, kind)
        for c in comps:
            doms.append((S(c["cells"]), c["kappa"], c["jf"], "old"))
        nnew = rnd.choices([0, 1, 2], weights=p_new)[0]
        for _ in range(nnew):
            if comps and rnd.random() < 0.7:
                base = rnd.choice(doms[:len(comps)])[0]
                bx, by, bz = rnd.choice(sorted(base))
                cx, cy, cz = bx + rnd.randint(-6, 6), by + rnd.randint(-6, 6), bz + rnd.randint(-6, 6)
            else:
                cx, cy, cz = rnd.randint(-8, 8), rnd.randint(-8, 8), rnd.randint(-8, 8)
            Q = {(cx, cy, cz)}
            for _k in range(rnd.randint(0, 2)):
                x, y, z = rnd.choice(sorted(Q))
                dx, dy, dz = rnd.choice([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)])
                Q.add((x + dx, y + dy, z + dz))
            doms.append((dilate(Q, 2), c0t * Qm * (len(Q) + 1), m, "new"))
        # connected components of the domain graph (touch or intersect)
        n = len(doms)
        parent = list(range(n))

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        for a in range(n):
            for b in range(a + 1, n):
                if find(a) != find(b) and touch(doms[a][0], doms[b][0]):
                    parent[find(a)] = find(b)
        groups = {}
        for a in range(n):
            groups.setdefault(find(a), []).append(a)
        newcomps = []
        for g in groups.values():
            Z = set().union(*[doms[a][0] for a in g])
            jf = min(doms[a][2] for a in g)
            kap = sum(doms[a][1] + 2 * P(doms[a][2]) for a in g) - e * len(Z) - 2 * P(jf)   # (1.85)
            # Phi_m(Z) = sum_{n=m+1}^{K} e |S^{n-m}(Z)|, D_m(Z) = max_{m<=n<=K} |S^{n-m}(Z)|
            cur, Phi, D = Z, 0.0, float(len(Z))
            for nn in range(m + 1, nsteps + 1):
                cur = S(cur)
                Phi += e * len(cur)
                D = max(D, float(len(cur)))
            slack = (kap - Phi - lam * D - cs * Qm) / (cs * Qm)
            kind = "old" if (len(g) == 1 and doms[g[0]][3] == "old") else ("new" if len(g) == 1 else "merge")
            counts[kind] += 1
            CPh = max(CPh, Phi / (len(Z) + 1))
            CVo = max(CVo, D / (len(Z) + 1))
            if slack < worst[0]:
                worst = (slack, kind + f" (m={m})")
            newcomps.append({"cells": Z, "kappa": kap, "jf": jf})
        comps = newcomps
    return worst, CPh, CVo, counts


print("PART B. Random histories on the toy geometry (S = dilate(coarsen(., 2), 1), d' = #cells, R = 1, K = 10).")
print("  Recursion: (1.83)/(1.85) as written in II; check s = kappa - Phi >= lambda D + c_* P_m^2 (Prop. 68.1) for every component.")
print("  Sample: x_K = 3, p_0 = 5 (so P_m^2 = x_m^10), e = 1, c_0 = 1/4 scaled by t, lambda = 10, c_* = c_0 t/(2*125).")
xK, lam = 3.0, 10.0
NH = 150


def scan(t, nh=NH):
    totc = {"old": 0, "new": 0, "merge": 0}
    wmin = (1e300, "")
    CPh, CVo = 0.0, 0.0
    for seed in range(nh):
        wst, a, b, cn = run_history(seed, xK, t, lam)
        for k in totc:
            totc[k] += cn[k]
        CPh, CVo = max(CPh, a), max(CVo, b)
        if wst[0] < wmin[0]:
            wmin = wst
    return wmin, CPh, CVo, totc


wmin, CPh, CVo, totc = scan(1.0)
print(f"  t = 1: {NH} histories, components checked {totc}; min normalized slack = {wmin[0]:.4f} ({wmin[1]}) -> invariant {'HOLDS' if wmin[0] >= 0 else 'FAILS'}")
print(f"  observed toy constants: Phi/(d'+1) <= {CPh:.2f}, D/(d'+1) <= {CVo:.2f}")
Cc_toy = 1.0 + CPh + lam * CVo
PK2 = (xK + 0.0 * ell) ** (2 * p0t)                      # P_K^2: the smallest P_m^2 (m = K)
t_pred = Cc_toy / ((c0 / (2 * 125)) * PK2)                # toy (CC) at m = K: c_*(t) P_K^2 >= C_c^toy (R = 1)
print(f"  toy analogue of (CC): c_*(t) P_K^2 >= C_c^toy = e + C_Phi^toy + lambda C_V^toy = {Cc_toy:.2f}  =>  sufficient t >= {t_pred:.3f}")
lo, hi = 1e-6, 1.0                                       # bisection on log t for the empirical threshold
for _ in range(14):
    mid = math.sqrt(lo * hi)
    if scan(mid)[0][0] >= 0:
        hi = mid
    else:
        lo = mid
print(f"  empirical threshold (bisection, {NH} histories): invariant holds for t >= {hi:.4f}; sufficient t from the proof's constants: {t_pred:.3f}"
      f" -> proof's condition is {'sufficient (consistent)' if hi <= t_pred else 'NOT sufficient (inconsistent!)'}")
print("  below the threshold, the first failure:")
print("| t | min normalized slack | at |")
print("|---|---|---|")
for t in (1.0, hi * 1.5, hi * 0.5, hi * 0.1):
    wmin = scan(t)[0]
    print(f"| {t:.4f} | {wmin[0]:.4f} | {wmin[1]} |")
print("  (the failing cases are components with d' large relative to the budget: the creation/merge conditions (CC) of Prop. 68.1.)")
def fact_a(seed, xK, t, e=1.0):
    """Check s_{m+1}(S Z0) = s_m(Z0) exactly for a single seed (no merges), using the definitions
    (1.85) at creation, (1.83) afterwards, and Phi_m(Z) = sum_{n=m+1}^{K} e |S^{n-m}(Z)|."""
    c0t = c0 * t
    P = lambda m: (xK + (Kt - m) * ell) ** p0t
    Q0 = {(0, 0, 0)}
    Z = dilate(Q0, 2)
    kap = c0t * P(1) ** 2 * (len(Q0) + 1) - e * len(Z)           # (1.85), j(Z) = 1
    maxerr = 0.0
    for m in range(1, Kt):
        cur, Phi = Z, 0.0
        for nn in range(m + 1, Kt + 1):
            cur = S(cur)
            Phi += e * len(cur)
        s_m = kap - Phi
        Z2 = S(Z)
        kap2 = kap - e * len(Z2)                                   # (1.83)
        cur, Phi2 = Z2, 0.0
        for nn in range(m + 2, Kt + 1):
            cur = S(cur)
            Phi2 += e * len(cur)
        s_m1 = kap2 - Phi2
        maxerr = max(maxerr, abs(s_m1 - s_m) / max(1.0, abs(s_m)))
        Z, kap = Z2, kap2
    return maxerr


print("PART B2. Fact (a), s_{m+1}(S Z) = s_m(Z): max relative error over one seed region followed for 9 steps =",
      f"{fact_a(0, 3.0, 1.0):.2e}")
print()

# ---------------------------------------------------------------- Part C
print("PART C. Lemma 65.2: sum_{s>=0} L^{ds} exp(-c (lam + s ln L)^q) <= C_0 exp(-c lam^q), C_0 = sum_s exp(s d ln L - c (s ln L)^q).")
print("  For c = c_* (sample, A_0 = 1), q = 2 p_0, d = 3, L = 13 (C_0 - 1 is the s >= 1 contribution):")
for (p0, q) in ((10, 20), (15, 30)):
    C0 = sum(math.exp(s * d * ell - cstar * (s * ell) ** q) for s in range(0, 400))
    ok = []
    for lamv in (1.0, 2.0, 3.0, 5.0):
        lhs = sum(math.exp(s * d * ell - cstar * (lamv + s * ell) ** q) for s in range(0, 400))
        rhs = C0 * math.exp(-cstar * lamv ** q)
        ok.append((lamv, lhs <= rhs * (1 + 1e-12)))
    print(f"  p_0 = {p0}, q = {q}: C_0 = {C0:.10f} (C_0 - 1 = {C0 - 1:.3e}), lemma holds at lambda = 1, 2, 3, 5: {[o[1] for o in ok]}")
# reproduction of note 65's own Part E value, to show the lemma's constant is not trivially 1 in general
ell2 = math.log(2)
C0n = sum(math.exp(s * 3 * ell2 - 0.1 * (s * ell2) ** 4) for s in range(0, 400))
print(f"  reproduction of note 65 Part E: (d, L, c, q) = (3, 2, 0.1, 4): C_0 = {C0n:.3f} (note 65 prints 143.118)")
print("  With the sample constants of Part A the factor L^{ds} is beaten at s = 1 already (c_* (ln L)^q >> d ln L), so only s = 0 survives:")
print("  the sum over creation scales is dominated by the current scale, as in the lemma.")
