"""T74: checks for note 64 (large-field lower bound for D_N).

Uses the helpers of t47_average_jacobian.py (SU(2) as a0 + i a.sigma,
d(U,1) = theta with (1/2) tr U = cos theta).  3D, periodic.

Part 1  (Lemma 64.1)  The extension U0(V): in-block links = 1, every crossing
        link of the coarse bond c equals V_c.  Checks q(U0) = V (CMP 98 (42))
        and A_fine(U0) = L * A_coarse(V) on a 3^3 coarse torus, L = 2, 3.
Part 2  (Lemma 64.2, 64.3)  Perturb every non-private fine link of U0 by
        exactly r (worst case), r = min(1/beta, r_max); solve each private link
        by Newton so that q(U) = V; check existence, d(X,V) <= (1-eps) r_Y/eps,
        d(Y_j,V) <= r_Y = (7L-6) r, J <= J_max, d(b,V_c) <= r_b, and the
        action increase beta_{N+1} (A(U) - A(U0)) <= 4 n_c ((L^3-1) + R_b).
Part 3  Elementary facts: Lipschitz bound for (1/2) tr, Haar volume of a
        ball, J <= (1 + (1-eps) pi/2)^3 when all |h_j| <= pi/2 (stress test).
Part 4  The constants quoted in the note.
"""
import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t47_average_jacobian as t  # noqa: E402

rng = np.random.default_rng(74)
I2 = np.eye(2, dtype=complex)


def one(a):
    return a[None, :, :]


def dist(a, b):
    """geodesic distance on SU(2) (single matrices)."""
    z = a @ b.conj().T
    return float(np.arccos(np.clip(np.real(z[0, 0] + z[1, 1]) / 2, -1, 1)))


def rand_su2(r_exact=None):
    if r_exact is None:
        return t.haar(1)[0]
    h = rng.normal(size=(1, 3))
    h *= r_exact / np.linalg.norm(h)
    return t.expm(h)[0]


class Torus:
    def __init__(self, s):
        self.s = s
        self.U = {}

    def key(self, x, mu):
        return (tuple(c % self.s for c in x), mu)

    def get(self, x, mu):
        return self.U[self.key(x, mu)]

    def path(self, pts):
        out = I2.copy()
        for p, q in zip(pts[:-1], pts[1:]):
            d = np.array(q) - np.array(p)
            mu = int(np.nonzero(d)[0][0])
            if d[mu] == 1:
                out = out @ self.get(p, mu)
            else:
                out = out @ self.get(q, mu).conj().T
        return out

    def action(self):
        s = self.s
        tot = 0.0
        for x in itertools.product(range(s), repeat=3):
            for mu, nu in ((0, 1), (0, 2), (1, 2)):
                ex = np.eye(3, dtype=int)
                xm = tuple(np.array(x) + ex[mu])
                xn = tuple(np.array(x) + ex[nu])
                P = (self.get(x, mu) @ self.get(xm, nu)
                     @ self.get(xn, mu).conj().T @ self.get(x, nu).conj().T)
                tot += 1 - np.real(P[0, 0] + P[1, 1]) / 2
        return tot


def gamma(y, x):
    pts = [list(y)]
    cur = list(y)
    for mu in range(3):
        step = 1 if x[mu] >= cur[mu] else -1
        while cur[mu] != x[mu]:
            cur[mu] += step
            pts.append(list(cur))
    return pts


def contour(L, mu, y, x):
    e = [0, 0, 0]
    e[mu] = 1
    yp = [y[i] + L * e[i] for i in range(3)]
    xc = [x[i] + L * e[i] for i in range(3)]
    p1 = gamma(y, x)
    seg = [[x[i] + tt * e[i] for i in range(3)] for tt in range(1, L + 1)]
    p3 = gamma(yp, xc)[::-1][1:]
    return p1 + seg + p3


def bond_data(T, L, mu, y):
    """W_c, list of Y_{c,x} for x in S (off the central line), n links."""
    e = np.zeros(3, dtype=int)
    e[mu] = 1
    central = [tuple(np.array(y) + tt * e) for tt in range(L)]
    Wpts = [list(np.array(y) + tt * e) for tt in range(L)]  # y .. y+(L-1)e
    W = T.path(Wpts)
    Ys, nlinks = [], 0
    for a in itertools.product(range(L), repeat=3):
        x = tuple(np.array(y) + np.array(a))
        if x in central:
            continue
        pts = contour(L, mu, list(y), list(x))
        nlinks = max(nlinks, len(pts) - 1)
        Ys.append(T.path(pts))
    return W, Ys, nlinks


def q_full(T, L, mu, y):
    """CMP 98 (42) for one bond, all x in B(y)."""
    e = np.zeros(3, dtype=int)
    e[mu] = 1
    X = T.path([list(np.array(y) + tt * e) for tt in range(L + 1)])
    w = np.zeros(3)
    for a in itertools.product(range(L), repeat=3):
        x = np.array(y) + np.array(a)
        Y = T.path(contour(L, mu, list(y), list(x)))
        w += t.logm(one(Y @ X.conj().T))[0] / L ** 3
    return t.expm(w[None, :])[0] @ X


def phiw(Ys, ps, X):
    w = sum(p * t.logm(one(Y @ X.conj().T))[0] for Y, p in zip(Ys, ps))
    return t.expm(w[None, :])[0] @ X, w


def newton(Ys, ps, V, X0, iters=80):
    X = X0
    for _ in range(iters):
        P, _ = phiw(Ys, ps, X)
        r = t.logm(one(P @ V.conj().T))[0]
        if np.linalg.norm(r) < 1e-13:
            break
        Jm = np.zeros((3, 3))
        for a in range(3):
            ee = np.zeros((1, 3))
            ee[0, a] = 1e-6
            Pp, _ = phiw(Ys, ps, t.expm(ee)[0] @ X)
            Jm[:, a] = (t.logm(one(Pp @ V.conj().T))[0] - r) / 1e-6
        st = np.linalg.solve(Jm, -r)
        nr = np.linalg.norm(st)
        if nr > 0.3:
            st *= 0.3 / nr
        X = t.expm(st[None, :])[0] @ X
    P, _ = phiw(Ys, ps, X)
    res = np.linalg.norm(t.logm(one(P @ V.conj().T))[0])
    return X, res


def jac_det(Ys, ps, X, h=1e-6):
    P0, _ = phiw(Ys, ps, X)
    cols = []
    for a in range(3):
        ee = np.zeros((1, 3))
        ee[0, a] = h
        Pp, _ = phiw(Ys, ps, X @ t.expm(ee)[0])
        Pm, _ = phiw(Ys, ps, X @ t.expm(-ee)[0])
        dp = t.logm(one(P0.conj().T @ Pp))[0]
        dm = t.logm(one(P0.conj().T @ Pm))[0]
        cols.append((dp - dm) / (2 * h))
    return np.linalg.det(np.stack(cols, axis=1))


def consts(L):
    eps = float(L) ** -2
    rY = lambda r: (7 * L - 6) * r  # noqa: E731
    rmax = eps * np.pi / (2 * (7 * L - 6))
    Rb = (L - 1) + (L * L - 1) * (7 * L - 6)
    Jmax = (1 + np.pi / 2) ** 3
    return eps, rmax, Rb, Jmax


def part1_part2(L, beta, trials):
    n = 3  # coarse torus side
    s = n * L
    eps, rmax, Rb, Jmax = consts(L)
    r = min(1.0 / beta, rmax)
    rY = (7 * L - 6) * r
    print(f"\n[L={L}] coarse side {n}, fine side {s}, beta_(N+1) = {beta}, "
          f"r = {r:.5f} (r_max = {rmax:.5f}), r_Y = {rY:.5f}, "
          f"eps pi = {eps*np.pi:.4f}")
    nc = 3 * n ** 3
    worst = dict(q=0, ratio=0, d=0, J=0, db=0, dact=0, dY=0, res=0, nl=0)
    for tr in range(trials):
        # coarse configuration (Haar: typically large field)
        Vc = Torus(n)
        for x in itertools.product(range(n), repeat=3):
            for mu in range(3):
                Vc.U[(x, mu)] = rand_su2()
        # U0
        T0 = Torus(s)
        for x in itertools.product(range(s), repeat=3):
            for mu in range(3):
                y = tuple(c // L for c in x)
                a = [c % L for c in x]
                T0.U[(x, mu)] = Vc.U[(y, mu)].copy() if a[mu] == L - 1 else I2.copy()
        Ac, Af = Vc.action(), T0.action()
        errq = 0.0
        for y in itertools.product(range(n), repeat=3):
            for mu in range(3):
                qv = q_full(T0, L, mu, tuple(L * c for c in y))
                errq = max(errq, np.abs(qv - Vc.U[(y, mu)]).max())
        worst["q"] = max(worst["q"], errq)
        worst["ratio"] = max(worst["ratio"], abs(Af - L * Ac) / max(Ac, 1))
        # perturb non-private links by exactly r
        T = Torus(s)
        priv = set()
        for y in itertools.product(range(n), repeat=3):
            for mu in range(3):
                e = np.zeros(3, dtype=int)
                e[mu] = 1
                priv.add((tuple(np.array(y) * L + (L - 1) * e), mu))
        for k, v in T0.U.items():
            T.U[k] = v if k in priv else rand_su2(r) @ v
        # solve private links
        for y in itertools.product(range(n), repeat=3):
            for mu in range(3):
                y0 = tuple(L * c for c in y)
                W, Ys, nl = bond_data(T, L, mu, y0)
                worst["nl"] = max(worst["nl"], nl)
                V = Vc.U[(y, mu)]
                ps = [1.0 / L ** 3] * len(Ys)
                X, res = newton(Ys, ps, V, V)
                worst["res"] = max(worst["res"], res)
                dY = max(dist(Yj, V) for Yj in Ys)
                worst["dY"] = max(worst["dY"], dY / rY)
                worst["d"] = max(worst["d"],
                                 dist(X, V) / ((1 - eps) * dY / eps))
                worst["J"] = max(worst["J"], abs(jac_det(Ys, ps, X)) / Jmax)
                b = W.conj().T @ X
                e = np.zeros(3, dtype=int)
                e[mu] = 1
                T.U[(tuple(np.array(y0) + (L - 1) * e), mu)] = b
                worst["db"] = max(worst["db"], dist(b, V) / (Rb * r))
        # full check q(U) = V and action
        err2 = 0.0
        for y in itertools.product(range(n), repeat=3):
            for mu in range(3):
                qv = q_full(T, L, mu, tuple(L * c for c in y))
                err2 = max(err2, np.abs(qv - Vc.U[(y, mu)]).max())
        worst["q"] = max(worst["q"], err2)
        dact = beta * (T.action() - Af) / (4 * nc * ((L ** 3 - 1) + Rb))
        worst["dact"] = max(worst["dact"], dact)
        print(f"  trial {tr}: A_c = {Ac:.3f}, A_f(U0) = {Af:.3f} "
              f"(L*A_c = {L*Ac:.3f}); max|qU0-V| = {errq:.1e}; "
              f"max|qU-V| = {err2:.1e}; beta*dA/bound = {dact:.4f}")
    print(f"  worst over trials: max links per contour = {worst['nl']} "
          f"(7L-6 = {7*L-6}); Newton residual {worst['res']:.1e}; "
          f"d(Y_j,V)/r_Y = {worst['dY']:.3f}; "
          f"d(X,V)/((1-eps)d_Y/eps) = {worst['d']:.3f}; "
          f"J/J_max = {worst['J']:.4f}; d(b,V)/(R_b r) = {worst['db']:.4f}; "
          f"|A_f(U0) - L A_c|/max(A_c,1) = {worst['ratio']:.1e}")
    assert worst["q"] < 1e-9 and worst["ratio"] < 1e-9
    assert worst["d"] <= 1 and worst["J"] <= 1 and worst["db"] <= 1
    assert worst["dact"] <= 1 and worst["dY"] <= 1 and worst["res"] < 1e-9


def part3():
    print("\n[Part 3] elementary facts")
    m1 = m2 = 0.0
    for _ in range(20000):
        a, b, c, d = (rand_su2() for _ in range(4))
        m1 = max(m1, abs(np.real(np.trace(a)) / 2 - np.real(np.trace(b)) / 2)
                 - dist(a, b))
        m2 = max(m2, dist(a @ b, c @ d) - dist(a, c) - dist(b, d))
    print(f"  max of | (1/2)tr a - (1/2)tr b | - d(a,b) = {m1:.1e} (<= 0 expected)")
    print(f"  max of d(ab,cd) - d(a,c) - d(b,d) = {m2:.1e} (<= 0 expected)")
    # Haar volume of a ball
    r = np.linspace(1e-4, 1.0, 2000)
    vol = (r - np.sin(r) * np.cos(r)) / np.pi
    print(f"  min over r in (0,1] of vol(B_r)/r^3 = {np.min(vol / r**3):.5f} "
          f"(1/6 = {1/6:.5f})")
    smp = t.haar(400000)
    th = np.arccos(np.clip(np.real(smp[:, 0, 0] + smp[:, 1, 1]) / 2, -1, 1))
    for rr in (0.3, 1.0):
        print(f"  Haar fraction d<={rr}: MC {np.mean(th <= rr):.5f}, "
              f"formula {(rr - np.sin(rr)*np.cos(rr))/np.pi:.5f}")
    # stress test of the Jacobian bound
    worst = 0.0
    for L in (2, 3, 4):
        eps = L ** -2.0
        for _ in range(400):
            k = rng.integers(2, 8)
            ps = rng.dirichlet(np.ones(k)) * (1 - eps)
            X = rand_su2()
            Ys = []
            for _j in range(k):
                h = rng.normal(size=(1, 3))
                h *= (np.pi / 2) * rng.uniform() ** (0.3) / np.linalg.norm(h)
                Ys.append(t.expm(h)[0] @ X)
            J = abs(jac_det(Ys, list(ps), X))
            worst = max(worst, J / (1 + (1 - eps) * np.pi / 2) ** 3)
    print(f"  stress test (|h_j| <= pi/2): max J/(1+(1-eps)pi/2)^3 = {worst:.4f}")
    assert m1 < 1e-12 and m2 < 1e-12 and worst <= 1


def part4():
    print("\n[Part 4] constants (a_0 = 1: A = sum_p (1 - (1/2) tr U_p))")
    print("  L  eps   r_max=eps*pi/(2(7L-6))  beta_*=1/r_max  R_b  "
          "J_max   c_0   e_ent(per bond)  C_-")
    for L in (2, 3, 4):
        eps, rmax, Rb, Jmax = consts(L)
        c0 = ((L ** 3 - 1) * np.log(6) + np.log(Jmax)
              + 4 * ((L ** 3 - 1) + Rb))
        print(f"  {L}  {eps:.4f}  {rmax:.5f}              {1/rmax:8.2f}"
              f"      {Rb:4d}  {Jmax:.3f}  {c0:7.2f}  {3*(L**3-1):3d}"
              f"              {L*L-1}")


if __name__ == "__main__":
    part3()
    part1_part2(2, 100.0, 3)
    part1_part2(3, 400.0, 1)
    part4()
