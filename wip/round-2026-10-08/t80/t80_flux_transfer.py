"""T80: checks for note 67 (Lemma 67.1: the coarse flux of the block average is
bounded by the fine plaquette angles; Lemma 67.3: the Jacobian blows up at the
boundary of the existence domain).  d = 3, periodic, SU(2), Balaban's average
CMP 98 (42).  Helpers of t47_average_jacobian.py and t74_extension_check.py.

Part 1  Lemma 67.1.  For every fine configuration U and V' = q(U), every
        coarse plaquette p (corner y, plane mu nu), with bonds c_1..c_4 in loop
        order V'(dp) = V'_1 V'_2 V'_3^-1 V'_4^-1:
        (a) d(V'_c, X_c) <= (1-eps) kappa_c,  kappa_c = max_x d(Y_{c,x}, X_c);
        (b) d(X_1 X_2 X_3^-1 X_4^-1, 1) <= sum of theta_q over the L^2 plaquettes
            of the planar L x L face at the base layer;
        (c) kappa_c <= (8L-6) * sum_{q in Q_c} theta_q, Q_c = plaquettes of the
            box (transverse [0,L-1]^2, mu in [0,2L-1]) around the bond;
        (d) theta_p <= K_L sum_{q in Q(p)} theta_q,  K_L = 1 + 4 (1-eps)(8L-6);
        (e) sum_{q in Q(p)} A_q >= c_L A_N(V'(dp)),
            c_L = 4/(pi^2 K_L^2 |Q(p)|).
        Tested on Haar-random, near-flat and U0-type fine configurations.
Part 2  Lemma 67.3.  Near the cut X -> -Y_j the Jacobian J of Phi_Y diverges
        like delta^-2 (delta = pi - |h_j|).  Analytic J (closed form) is
        compared with finite differences away from the cut, then J delta^2 is
        printed for delta -> 0.
"""
import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t47_average_jacobian as t  # noqa: E402
import t74_extension_check as t74  # noqa: E402
from t74_extension_check import I2, Torus  # noqa: E402

rng = np.random.default_rng(80)


def e_(mu):
    v = np.zeros(3, dtype=int)
    v[mu] = 1
    return v


def adag(a):
    return a.conj().T


def theta_of(P):
    """Stable geodesic distance d(P, 1) on SU(2): atan2(|vector part|, a0)."""
    a0 = np.real(P[0, 0] + P[1, 1]) / 2
    av = np.array([np.imag(P[0, 1] + P[1, 0]) / 2,
                   np.real(P[0, 1] - P[1, 0]) / 2,
                   np.imag(P[0, 0] - P[1, 1]) / 2])
    return float(np.arctan2(np.linalg.norm(av), a0))


def dist(a, b):
    return theta_of(a @ b.conj().T)


def ratio(lhs, rhs, tol=1e-9):
    """lhs/rhs for a claimed inequality lhs <= rhs; if rhs is below rounding
    level the claim is lhs <= tol (ratio 0 or inf)."""
    if rhs > tol:
        return lhs / rhs
    return 0.0 if lhs <= tol else float("inf")


def plaq_angles(T):
    """theta for every fine plaquette, key (x tuple mod s, mu, nu), mu<nu."""
    s = T.s
    out = {}
    for x in itertools.product(range(s), repeat=3):
        for mu, nu in ((0, 1), (0, 2), (1, 2)):
            P = (T.get(x, mu) @ T.get(np.array(x) + e_(mu), nu)
                 @ adag(T.get(np.array(x) + e_(nu), mu))
                 @ adag(T.get(x, nu)))
            out[(x, mu, nu)] = theta_of(P)
    return out


def plaq_key(T, x, mu, nu):
    x = tuple(int(c) % T.s for c in x)
    return (x, mu, nu) if mu < nu else (x, nu, mu)


def box_plaquettes(T, corner, ranges):
    """All plaquettes with all four vertices in corner + prod [0, r_i]."""
    out = set()
    c = np.array(corner)
    for a in itertools.product(*[range(r + 1) for r in ranges]):
        for mu, nu in ((0, 1), (0, 2), (1, 2)):
            a2 = np.array(a) + e_(mu) + e_(nu)
            if all(a2[i] <= ranges[i] for i in range(3)):
                out.add(plaq_key(T, c + np.array(a), mu, nu))
    return out


def tube_box(T, L, mu, y0):
    """Q_c: box with transverse extent [0, L-1], mu extent [0, 2L-1]."""
    rg = [L - 1, L - 1, L - 1]
    rg[mu] = 2 * L - 1
    return box_plaquettes(T, y0, rg)


def face_plaquettes(T, L, y0, mu, nu):
    out = set()
    for a in range(L):
        for b in range(L):
            out.add(plaq_key(T, np.array(y0) + a * e_(mu) + b * e_(nu), mu, nu))
    return out


def straight(T, L, mu, y0):
    return T.path([list(np.array(y0) + k * e_(mu)) for k in range(L + 1)])


def make_config(T, L, n, kind):
    s = n * L
    if kind == "haar":
        for x in itertools.product(range(s), repeat=3):
            for mu in range(3):
                T.U[(x, mu)] = t74.rand_su2()
    elif kind == "nearflat":
        for x in itertools.product(range(s), repeat=3):
            for mu in range(3):
                T.U[(x, mu)] = t.expm(0.3 * rng.normal(size=(1, 3)))[0]
    elif kind == "U0":
        Vc = {(x, mu): t74.rand_su2()
              for x in itertools.product(range(n), repeat=3)
              for mu in range(3)}
        for x in itertools.product(range(s), repeat=3):
            for mu in range(3):
                y = tuple(c // L for c in x)
                a = [c % L for c in x]
                T.U[(x, mu)] = Vc[(y, mu)].copy() if a[mu] == L - 1 else I2.copy()
    elif kind == "abelian_spread":
        # exp(i phi sigma_3) with smooth random angles of size ~0.15/L^2
        for x in itertools.product(range(s), repeat=3):
            for mu in range(3):
                ph = rng.normal() * 0.6 / L ** 2
                T.U[(x, mu)] = t.expm(np.array([[0.0, 0.0, ph]]))[0]


def part1(L, n, kinds, trials):
    eps = float(L) ** -2
    K_L = 1 + 4 * (1 - eps) * (8 * L - 6)
    s = n * L
    print(f"\n[Part 1, L={L}, coarse side {n}] eps = {eps:.4f}, "
          f"K_L = 1 + 4(1-eps)(8L-6) = {K_L:.3f}")
    worst = dict(a=0, b=0, c=0, d=0, e=1e9)
    best_ratio = 1e9
    sample_nQ = 0
    for kind in kinds:
        for _ in range(trials):
            T = Torus(s)
            make_config(T, L, n, kind)
            th = plaq_angles(T)
            Vp = {}
            Xs = {}
            kap = {}
            for y in itertools.product(range(n), repeat=3):
                for mu in range(3):
                    y0 = tuple(L * c for c in y)
                    V = t74.q_full(T, L, mu, y0)
                    X = straight(T, L, mu, y0)
                    Vp[(y, mu)], Xs[(y, mu)] = V, X
                    kp = 0.0
                    for a in itertools.product(range(L), repeat=3):
                        x = np.array(y0) + np.array(a)
                        Y = T.path(t74.contour(L, mu, list(y0), list(x)))
                        kp = max(kp, dist(Y, X))
                    kap[(y, mu)] = kp
                    # (a)
                    lhs = dist(V, X)
                    worst["a"] = max(worst["a"], ratio(lhs, (1 - eps) * kp))
                    # (c)
                    Qc = tube_box(T, L, mu, y0)
                    rhs = (8 * L - 6) * sum(th[k] for k in Qc)
                    worst["c"] = max(worst["c"], ratio(kp, rhs))
            for y in itertools.product(range(n), repeat=3):
                for mu, nu in ((0, 1), (0, 2), (1, 2)):
                    ym = tuple((np.array(y) + e_(mu)) % n)
                    yn = tuple((np.array(y) + e_(nu)) % n)
                    bonds = [(y, mu), (ym, nu), (yn, mu), (y, nu)]
                    Vb = [Vp[b] for b in bonds]
                    Xb = [Xs[b] for b in bonds]
                    Vdp = Vb[0] @ Vb[1] @ adag(Vb[2]) @ adag(Vb[3])
                    Xdp = Xb[0] @ Xb[1] @ adag(Xb[2]) @ adag(Xb[3])
                    thp = theta_of(Vdp)
                    y0 = tuple(L * c for c in y)
                    face = face_plaquettes(T, L, y0, mu, nu)
                    # (b)
                    worst["b"] = max(worst["b"], ratio(
                        theta_of(Xdp), sum(th[k] for k in face)))
                    # Q(p)
                    Qp = set(face)
                    starts = [np.array(y) * L, np.array(y) * L + L * e_(mu),
                              np.array(y) * L + L * e_(nu), np.array(y) * L]
                    mus = [mu, nu, mu, nu]
                    for i in range(4):
                        Qp |= tube_box(T, L, mus[i], tuple(starts[i]))
                    sample_nQ = max(sample_nQ, len(Qp))
                    S1 = sum(th[k] for k in Qp)
                    S2 = sum(th[k] ** 2 for k in Qp)
                    # (d)
                    worst["d"] = max(worst["d"], ratio(thp, K_L * S1))
                    # (e)
                    SA = sum(2 * np.sin(th[k] / 2) ** 2 for k in Qp)
                    AN = 2 * np.sin(thp / 2) ** 2
                    cL = 4 / (np.pi ** 2 * K_L ** 2 * len(Qp))
                    if AN > 1e-12:
                        worst["e"] = min(worst["e"], SA / (cL * AN))
                        best_ratio = min(best_ratio, SA / AN)
        print(f"  {kind:15s}: done")
    cL = 4 / (np.pi ** 2 * K_L ** 2 * sample_nQ)
    print(f"  max of LHS/RHS: (a) {worst['a']:.4f}, (b) {worst['b']:.4f}, "
          f"(c) {worst['c']:.4f}, (d) {worst['d']:.4f}  (all <= 1 required)")
    nq_formula = 4 * 2 * L * (L - 1) * (3 * L - 2) + L * L
    print(f"  max |Q(p)| over the planes = {sample_nQ} (formula bound 4 |Q_c| + L^2 "
          f"= {nq_formula}); c_L(using the formula bound) = "
          f"{4 / (np.pi ** 2 * K_L ** 2 * nq_formula):.3e}; "
          f"c_L(using the observed max |Q(p)|) = {cL:.3e}; "
          f"min over samples of sum_Q A_q / (c_L A_N(V'(dp))) = {worst['e']:.3e} "
          f"(>= 1 required); min over samples of sum_Q A_q / A_N(V'(dp)) = "
          f"{best_ratio:.4f}")
    assert max(worst["a"], worst["b"], worst["c"], worst["d"]) <= 1 + 1e-12
    assert worst["e"] >= 1


# ---------------------------------------------------------------- Part 2
def cross_matrix(h):
    return np.array([[0, -h[2], h[1]], [h[2], 0, -h[0]], [-h[1], h[0], 0]])


def fun_ad(g, h):
    """g(ad h) as a 3x3 real matrix, ad h = 2 [h]_x, for g real-analytic with
    g(conj z) = conj g(z):  g(0) P + Re g(2 i th) (I-P) + Im g(2 i th) [hat h]_x."""
    th = np.linalg.norm(h)
    if th < 1e-9:
        # series: use the value at small th via the same formula on a tiny h
        h = np.array([1e-9, 0.0, 0.0])
        th = 1e-9
    hh = h / th
    P = np.outer(hh, hh)
    z = g(2j * th)
    return (g(0.0 + 0j) * P + np.real(z) * (np.eye(3) - P)
            + np.imag(z) * cross_matrix(hh))


def f_phi(z):
    z = complex(z)
    if abs(z) < 1e-12:
        return 1.0 + 0j
    return z / (1 - np.exp(-z))


def f_psi(z):
    z = complex(z)
    if abs(z) < 1e-12:
        return 1.0 + 0j
    return (1 - np.exp(-z)) / z


def jac_analytic(Ys, ps, X):
    hs = [t.logm((Y @ adag(X))[None])[0] for Y in Ys]
    w = sum(p * h for p, h in zip(ps, hs))
    M = sum(p * fun_ad(f_phi, h) for p, h in zip(ps, hs))
    return np.linalg.det(np.eye(3) - fun_ad(f_psi, w) @ M), hs


def part2():
    print("\n[Part 2] Jacobian of Phi_Y: analytic formula vs finite differences,"
          " then blow-up at the cut")
    worst = 0.0
    for _ in range(200):
        k = int(rng.integers(2, 6))
        L = int(rng.choice([2, 3]))
        eps = float(L) ** -2
        ps = list(rng.dirichlet(np.ones(k)) * (1 - eps))
        X = t74.rand_su2()
        Ys = [t74.rand_su2() for _ in range(k)]
        Ja, _ = jac_analytic(Ys, ps, X)
        Jf = t74.jac_det(Ys, ps, X)
        worst = max(worst, abs(Ja - Jf) / max(abs(Jf), 1e-9))
    print(f"  max relative |J_analytic - J_finite-difference| over 200 random "
          f"cases (Haar Y, X) = {worst:.1e}")
    assert worst < 1e-5
    # global bound ||D^-1|| <= (1-eps) pi / (eps sin(eps pi)), D = I - psi(ad w) M
    worstD = 0.0
    for _ in range(400):
        k = int(rng.integers(2, 6))
        L = int(rng.choice([2, 3, 4]))
        eps = float(L) ** -2
        ps = list(rng.dirichlet(np.ones(k)) * (1 - eps))
        X = t74.rand_su2()
        Ys = [t74.rand_su2() for _ in range(k)]
        hs = [t.logm((Y @ adag(X))[None])[0] for Y in Ys]
        w = sum(p * h for p, h in zip(ps, hs))
        M = sum(p * fun_ad(f_phi, h) for p, h in zip(ps, hs))
        D = np.eye(3) - fun_ad(f_psi, w) @ M
        nrm = np.linalg.norm(np.linalg.inv(D), 2)
        bound = (1 - eps) * np.pi / (eps * np.sin(eps * np.pi))
        worstD = max(worstD, nrm / bound)
    print(f"  max over 400 random cases of ||D^-1|| / [(1-eps) pi/(eps sin(eps pi))]"
          f" = {worstD:.4f} (<= 1 required; Lemma 67.4)")
    assert worstD <= 1
    # blow-up: X = -exp(-i delta n.sigma) Y_j  =>  Y_j X^{-1} = -exp(i delta n.sigma)
    print("  J(X) at X -> -Y_j  (delta = pi - |h_j|), random other Y_k; "
          "L = 2, 3; printed: delta, J, J delta^2")
    for L in (2, 3):
        eps = float(L) ** -2
        k = 4
        ps = list(rng.dirichlet(np.ones(k)) * (1 - eps))
        Ys = [t74.rand_su2() for _ in range(k)]
        nvec = rng.normal(size=3)
        nvec /= np.linalg.norm(nvec)
        j = 0
        rows = []
        for delta in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5):
            X = -(t.expm(-delta * nvec[None, :])[0]) @ Ys[j]
            J, hs = jac_analytic(Ys, ps, X)
            dj = np.pi - np.linalg.norm(hs[j])
            rows.append((delta, dj, J, J * dj ** 2))
        for r in rows:
            print(f"    L={L} p_j={ps[j]:.4f}: delta = {r[0]:.0e} (pi-|h_j| = "
                  f"{r[1]:.3e})  J = {r[2]:.4e}  J*delta^2 = {r[3]:.5f}")
        slope = np.polyfit(np.log([r[1] for r in rows[-3:]]),
                           np.log([r[2] for r in rows[-3:]]), 1)[0]
        print(f"    L={L}: log-log slope of J versus delta over the last three "
              f"points = {slope:.4f} (predicted -2)")
        assert abs(slope + 2) < 0.05


def part1b(L=3, sigma=0.3):
    """Lemma 67.2: the cone triangle tau = gamma(y,v) e_nu gamma(y,v+e_nu)^-1 is
    a product of (conjugated) plaquettes, one per step of gamma(y,v) along an
    axis a > nu, in the plane (nu, a) with corner at the tail of that step."""
    n = 2
    s = n * L
    worst = 0.0
    cnt = 0
    for kind in ("haar", "nearflat"):
        T = Torus(s)
        make_config(T, L, n, kind)
        th = plaq_angles(T)
        y = np.array([0, 0, 0])
        for v in itertools.product(range(L + 1), repeat=3):
            for nu in range(3):
                v2 = np.array(v) + e_(nu)
                if v2[nu] > L:
                    continue
                pts = t74.gamma(list(y), list(v))
                tau = (T.path(pts) @ T.get(np.array(v), nu)
                       @ adag(T.path(t74.gamma(list(y), list(v2)))))
                P = []
                for k in range(len(pts) - 1, 0, -1):
                    a = int(np.nonzero(np.array(pts[k]) - np.array(pts[k - 1]))[0][0])
                    if a <= nu:
                        break
                    P.append(plaq_key(T, pts[k - 1], nu, a))
                assert len(P) == sum(v[a] - y[a] for a in range(nu + 1, 3))
                assert len(set(P)) == len(P)
                lhs = theta_of(tau)
                rhs = sum(th[q] for q in P)
                worst = max(worst, ratio(lhs, rhs))
                cnt += 1
    print(f"\n[Part 1b, L={L}] cone triangles: {cnt} triangles tested; max of "
          f"d(tau,1) / sum_{{flipped plaquettes}} theta_q = {worst:.4f} (<= 1 required)")
    assert worst <= 1 + 1e-12


def part3():
    print("\n[Part 3] constants of note 67 (Lemma 67.1, Theorem 67.5, Cor 67.6)")
    print("  L  eps    K_L    N_Q(L)   c_L(flux)    c_Jac        c_0(L)     "
          "beta_*(L)")
    for L in (2, 3, 4):
        eps = float(L) ** -2
        K_L = 1 + 4 * (1 - eps) * (8 * L - 6)
        NQ = 8 * L * (L - 1) * (3 * L - 2) + L * L
        cflux = 4 / (np.pi ** 2 * K_L ** 2 * NQ)
        cjac = eps ** 3 * (np.sin(eps * np.pi) / ((1 - eps) * np.pi)) ** 2
        Rb = (L - 1) + (L * L - 1) * (7 * L - 6)
        c0 = ((L ** 3 - 1) * np.log(6) + 3 * np.log(1 + np.pi / 2)
              + 4 * ((L ** 3 - 1) + Rb))
        bstar = 2 * (7 * L - 6) * L * L / np.pi
        print(f"  {L}  {eps:.4f} {K_L:6.1f} {NQ:7d}  {cflux:.3e}  {cjac:.3e}  "
              f"{c0:9.2f}  {bstar:8.2f}")
    print("  Theorem 67.5: E[beta A_q] <= C_log(L, beta) := 6 [3 (L^3-1) log beta"
          " + c_0(L) + log(1/c_Jac)] for V' = 1")
    for L in (2, 3, 4):
        eps = float(L) ** -2
        cjac = eps ** 3 * (np.sin(eps * np.pi) / ((1 - eps) * np.pi)) ** 2
        Rb = (L - 1) + (L * L - 1) * (7 * L - 6)
        c0 = ((L ** 3 - 1) * np.log(6) + 3 * np.log(1 + np.pi / 2)
              + 4 * ((L ** 3 - 1) + Rb))
        bstar = 2 * (7 * L - 6) * L * L / np.pi
        row = []
        for beta in (bstar, 1e3, 1e6, 1e12):
            beta = max(beta, bstar)
            row.append(6 * (3 * (L ** 3 - 1) * np.log(beta) + c0
                            + np.log(1 / cjac)))
        print(f"    L={L}: C_log at beta = max(.,beta_*) in (beta_*, 1e3, 1e6, "
              f"1e12): " + ", ".join(f"{r:.1f}" for r in row))
    print("  Cor 67.6 (island, last axis): beta E[G_eta] <= Gamma_0 |Z| "
          "max_q E[beta A_q],  Gamma_0 = B_L N_loops |W|,")
    print("    B_L = (n_max + 2D)^2 D pi^2/2 (loop energy, Lemma 67.2), "
          "n_max = 8L-6, D = 5L-3,")
    print("    |W| = L(2L-1)^2 + 4L(2L-1)(L-1) plaquettes of the box, "
          "N_loops = 4L(L-1) + 640 L (1 + 1/eta)")
    for L in (2, 3, 4):
        nmax, D = 8 * L - 6, 5 * L - 3
        BL = (nmax + 2 * D) ** 2 * D * np.pi ** 2 / 2
        Wn = L * (2 * L - 1) ** 2 + 4 * L * (2 * L - 1) * (L - 1)
        for eta in (0.5,):
            Nl = 4 * L * (L - 1) + 640 * L * (1 + 1 / eta)
            print(f"    L={L}, eta={eta}: B_L = {BL:.4e}, |W| = {Wn}, "
                  f"N_loops = {Nl:.0f}, Gamma_0 = {BL * Nl * Wn:.4e}")


if __name__ == "__main__":
    part1(2, 3, ["haar", "nearflat", "U0", "abelian_spread"], 2)
    part1(3, 3, ["haar", "nearflat", "U0", "abelian_spread"], 1)
    part1b(2)
    part1b(3)
    part2()
    part3()
