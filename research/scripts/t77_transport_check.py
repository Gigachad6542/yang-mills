"""T77: checks for note 64 Section 7 (exact left-translation transport T_R).

Uses the helpers of t74_extension_check.py / t47_average_jacobian.py.
d = 3, periodic, SU(2).  U = (U_rest, b), q = Balaban's average CMP 98 (42).

Part 1  Covariance  Phi_{RY}(R X) = R Phi_Y(X)  and  J_{RY}(R X) = J_Y(X)
        (random Y_j, R, X).
Part 2  Transport on a fibre.  Coarse torus 3^3, L = 2, 3.  Sample U_rest
        near 1 (links exp(i sigma g.sigma)), solve every private link so that
        q(U) = 1 (fibre over V^Z = 1).  Pick a set Z of bonds in the LAST axis
        direction (mu = 2) and R_c random.  Apply
            u_x  ->  a_x^{-1} R_c a_x u_x       (every crossing link of c in Z,
                                                 the private link included)
        with a_x the in-block path from y to the tail of the crossing link.
        Check q(T U) = V with V_c = R_c on Z and 1 elsewhere (to rounding).
Part 3  Plaquette algebra.  For type-A plaquettes (two crossing links of one
        bond): a_1 h a_1^-1 = M N and a_1 h' a_1^-1 = R M R^-1 N with M, N
        closed loops at y, and A(h') <= (d(M,1) + d(N,1))^2 / 2.
        For corner plaquettes: h' is within the sum of the four link
        displacement distances of V(dp) (conjugated), printed.
Part 4  Failure for mu not the last axis: the same recipe with the reference
        path a_x (t = 0) does not give q(T U) = V; the error is printed.
"""
import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t47_average_jacobian as t  # noqa: E402
import t74_extension_check as t74  # noqa: E402
from t74_extension_check import I2, Torus, dist, one  # noqa: E402

rng = np.random.default_rng(77)


def su2_small(sigma):
    return t.expm(sigma * rng.normal(size=(1, 3)))[0]


def adag(a):
    return a.conj().T


def Aplaq(P):
    return 1 - np.real(P[0, 0] + P[1, 1]) / 2


def e_(mu):
    v = np.zeros(3, dtype=int)
    v[mu] = 1
    return v


def a_points(L, mu, y, aperp):
    """In-block path from y to the tail of the crossing link at transverse
    offset aperp (aperp[mu] = 0): gamma(y, x) with x mu-coordinate 0, then
    L-1 steps along mu."""
    y = np.array(y)
    x = y + np.array(aperp)
    pts = t74.gamma(list(y), list(x))
    for k in range(1, L):
        pts.append(list(x + k * e_(mu)))
    return pts


def transverse_offsets(L, mu):
    for a in itertools.product(range(L), repeat=3):
        if a[mu] == 0:
            yield np.array(a)


def build_fibre(L, n, sigma, Vtarget):
    """Random near-flat U_rest, private links solved so that q(U) = Vtarget."""
    s = n * L
    T = Torus(s)
    priv = set()
    for y in itertools.product(range(n), repeat=3):
        for mu in range(3):
            priv.add((tuple(np.array(y) * L + (L - 1) * e_(mu)), mu))
    for x in itertools.product(range(s), repeat=3):
        for mu in range(3):
            T.U[(x, mu)] = I2.copy() if (x, mu) in priv else su2_small(sigma)
    for y in itertools.product(range(n), repeat=3):
        for mu in range(3):
            y0 = tuple(L * c for c in y)
            W, Ys, _ = t74.bond_data(T, L, mu, y0)
            ps = [1.0 / L ** 3] * len(Ys)
            V = Vtarget[(y, mu)]
            X, res = t74.newton(Ys, ps, V, V.copy())
            assert res < 1e-10, res
            T.U[(tuple(np.array(y0) + (L - 1) * e_(mu)), mu)] = adag(W) @ X
    return T


def q_all(T, L, n):
    out = {}
    for y in itertools.product(range(n), repeat=3):
        for mu in range(3):
            out[(y, mu)] = t74.q_full(T, L, mu, tuple(L * c for c in y))
    return out


def apply_T(T, L, n, R, mu_only=None):
    """Return new torus: crossing links of bonds with R[(y,mu)] set are
    left-multiplied by a^{-1} R a."""
    T2 = Torus(T.s)
    T2.U = {k: v.copy() for k, v in T.U.items()}
    for (y, mu), Rc in R.items():
        y0 = np.array([L * c for c in y])
        for ap in transverse_offsets(L, mu):
            pts = a_points(L, mu, y0, ap)
            a = T.path(pts)
            tail = y0 + ap + (L - 1) * e_(mu)
            k = T.key(tail, mu)
            T2.U[k] = adag(a) @ Rc @ a @ T.U[k]
    return T2


def coarse_action(Vq, n):
    tot = 0.0
    for y in itertools.product(range(n), repeat=3):
        for mu, nu in ((0, 1), (0, 2), (1, 2)):
            ym = tuple((np.array(y) + e_(mu)) % n)
            yn = tuple((np.array(y) + e_(nu)) % n)
            P = (Vq[(y, mu)] @ Vq[(ym, nu)] @ adag(Vq[(yn, mu)])
                 @ adag(Vq[(y, nu)]))
            tot += Aplaq(P)
    return tot


def part1():
    print("[Part 1] covariance Phi_{RY}(RX) = R Phi_Y(X), J invariance")
    worst_phi = worst_J = 0.0
    for _ in range(300):
        L = int(rng.choice([2, 3]))
        eps = L ** -2.0
        k = int(rng.integers(2, 7))
        ps = list(rng.dirichlet(np.ones(k)) * (1 - eps))
        X = t74.rand_su2()
        Ys = [su2_small(0.6) @ X for _ in range(k)]
        R = t74.rand_su2()
        P1, _ = t74.phiw(Ys, ps, X)
        P2, _ = t74.phiw([R @ Y for Y in Ys], ps, R @ X)
        worst_phi = max(worst_phi, np.abs(R @ P1 - P2).max())
        J1 = t74.jac_det(Ys, ps, X)
        J2 = t74.jac_det([R @ Y for Y in Ys], ps, R @ X)
        worst_J = max(worst_J, abs(J1 - J2) / max(abs(J1), 1e-12))
    print(f"  max |R Phi_Y(X) - Phi_RY(RX)| = {worst_phi:.1e}; "
          f"max relative |J_Y(X) - J_RY(RX)| = {worst_J:.1e}")
    assert worst_phi < 1e-12 and worst_J < 1e-4


def part2_3(L, n, sigma, trials):
    print(f"\n[Parts 2,3, L={L}] coarse side {n}, sigma = {sigma}")
    for tr in range(trials):
        one_V = {(y, mu): su2_small(0.15)
                 for y in itertools.product(range(n), repeat=3)
                 for mu in range(3)}
        T = build_fibre(L, n, sigma, one_V)
        qerr0 = max(np.abs(v - one_V[k]).max()
                    for k, v in q_all(T, L, n).items())
        bonds = [(y, 2) for y in itertools.product(range(n), repeat=3)]
        pick = rng.choice(len(bonds), size=4, replace=False)
        R = {bonds[i]: t74.rand_su2() for i in pick}
        T2 = apply_T(T, L, n, R)
        Vtar = {k: R.get(k, I2) @ one_V[k] for k in one_V}
        q2 = q_all(T2, L, n)
        qerr = max(np.abs(q2[k] - Vtar[k]).max() for k in Vtar)
        print(f"  trial {tr}: max|q(U)-Vt| = {qerr0:.1e}; "
              f"max|q(T U) - R Vt| = {qerr:.1e}  (|Z| = {len(R)} bonds, mu = 2)")
        assert qerr0 < 1e-9 and qerr < 1e-9
        # --- Part 3: type A plaquettes ---
        worstA = worstid = 0.0
        dsumA = 0.0
        for (y, mu), Rc in R.items():
            y0 = np.array([L * c for c in y])
            for nu in range(3):
                if nu == mu:
                    continue
                for a1 in transverse_offsets(L, mu):
                    a2 = a1 + e_(nu)
                    if a2[nu] > L - 1:
                        continue
                    p1 = a_points(L, mu, y0, a1)
                    p2 = a_points(L, mu, y0, a2)
                    t1 = list(y0 + a1 + (L - 1) * e_(mu))
                    h1 = list(np.array(t1) + e_(mu))
                    h2 = list(np.array(h1) + e_(nu))
                    t2 = list(np.array(t1) + e_(nu))
                    plq = [t1, h1, h2, t2, t1]
                    Mpts = p1 + [h1, h2, t2] + p2[::-1][1:]
                    Npts = p2 + [t1] + p1[::-1][1:]
                    h, h_ = T.path(plq), T2.path(plq)
                    M, N = T.path(Mpts), T.path(Npts)
                    a = T.path(p1)
                    # identities
                    worstid = max(worstid,
                                  np.abs(a @ h @ adag(a) - M @ N).max(),
                                  np.abs(a @ h_ @ adag(a)
                                         - Rc @ M @ adag(Rc) @ N).max(),
                                  np.abs(T2.path(Mpts) - Rc @ M @ adag(Rc)).max())
                    dsumA += Aplaq(h_) - Aplaq(h)
                    m, nn = dist(M, I2), dist(N, I2)
                    worstA = max(worstA, Aplaq(h_) - (m + nn) ** 2 / 2)
        print(f"    type A: max identity defect = {worstid:.1e}; "
              f"max [A(h') - (d(M,1)+d(N,1))^2/2] = {worstA:.1e} (<= 0)")
        assert worstid < 1e-12 and worstA <= 1e-12
        # --- corner plaquettes: sum of fine corner actions vs L * coarse ---
        Vq = q2
        Ac_V = coarse_action(Vq, n)
        Ac_flat = 0.0
        Af = T2.action()
        Af0 = T.action()
        print(f"    fine action after T: {Af:.4f} (before: {Af0:.4f}); "
              f"L * A_N(V) = {L * Ac_V:.4f}; "
              f"difference (fine - L A_N(V)) = {Af - L * Ac_V:.4f}")
        dsumC = corner_check(T, T2, L, n, R, one_V, Vtar)
        tot = Af - Af0
        print(f"    all changed plaquettes: sum_A + sum_corner = "
              f"{dsumA + dsumC:.10f}; A(T U) - A(U) = {tot:.10f}")
        assert abs(dsumA + dsumC - tot) < 1e-9


def ycross(T, L, mu, y0, aperp):
    """A = path y->tail, Ap = path head->end corner, u, Y = A u Ap."""
    y0 = np.array(y0)
    aperp = np.array(aperp)
    pts = a_points(L, mu, y0, aperp)
    tail = y0 + aperp + (L - 1) * e_(mu)
    head = tail + e_(mu)
    yend = y0 + L * e_(mu)
    gp = t74.gamma(list(yend), list(yend + aperp))[::-1]  # head -> yend
    A = T.path(pts)
    Ap = T.path(gp)
    u = T.get(tail, mu)
    return A, Ap, u, A @ u @ Ap


def corner_check(T, T2, L, n, R, Vt, Vtar, eta=0.5):
    """Corner plaquettes of coarse plaquettes touching Z:
    chain identity, and A(h') - A(h) <= (1+eta)A(V dp) - (1-eta)A(Vt dp)
    + (1+1/eta) delta^2."""
    worst_id = 0.0
    worst_ineq = -1e9
    cnt = 0
    dsum = 0.0
    for y in itertools.product(range(n), repeat=3):
        for mu, nu in ((0, 1), (0, 2), (1, 2)):
            rho = 3 - mu - nu
            ym = tuple((np.array(y) + e_(mu)) % n)
            yn = tuple((np.array(y) + e_(nu)) % n)
            bonds = [(y, mu), (ym, nu), (yn, mu), (y, nu)]
            if not any(b in R for b in bonds):
                continue
            Rs = [R.get(b, I2) for b in bonds]
            starts = [np.array(y) * L, np.array(ym) * L, np.array(yn) * L,
                      np.array(y) * L]
            # use unwrapped coordinates for the paths (torus handles mod)
            starts[1] = np.array(y) * L + L * e_(mu)
            starts[2] = np.array(y) * L + L * e_(nu)
            for r in range(L):
                ap = [(L - 1) * e_(nu) + r * e_(rho), r * e_(rho),
                      r * e_(rho), (L - 1) * e_(mu) + r * e_(rho)]
                mus = [mu, nu, mu, nu]
                dat = [ycross(T, L, mus[i], starts[i], ap[i]) for i in range(4)]
                A_ = [d[0] for d in dat]
                Ap_ = [d[1] for d in dat]
                Y_ = [d[3] for d in dat]
                s0 = np.array(y) * L + (L - 1) * (e_(mu) + e_(nu)) + r * e_(rho)
                plq = [list(s0), list(s0 + e_(mu)),
                       list(s0 + e_(mu) + e_(nu)), list(s0 + e_(nu)), list(s0)]
                h, h_ = T.path(plq), T2.path(plq)
                L2i = adag(Ap_[0]) @ adag(A_[1])
                L24 = adag(Ap_[1]) @ Ap_[2]
                L3 = A_[2] @ Ap_[3]
                L1 = A_[3] @ adag(A_[0])
                Hh = (Y_[0] @ L2i @ Y_[1] @ L24 @ adag(Y_[2]) @ L3
                      @ adag(Y_[3]) @ L1)
                Hp = ((Rs[0] @ Y_[0]) @ L2i @ (Rs[1] @ Y_[1]) @ L24
                      @ adag(Rs[2] @ Y_[2]) @ L3 @ adag(Rs[3] @ Y_[3]) @ L1)
                worst_id = max(worst_id, np.abs(A_[0] @ h @ adag(A_[0]) - Hh).max(),
                               np.abs(A_[0] @ h_ @ adag(A_[0]) - Hp).max())
                Vb = [Vtar[b] for b in bonds]
                Vtb = [Vt[b] for b in bonds]
                Vdp = Vb[0] @ Vb[1] @ adag(Vb[2]) @ adag(Vb[3])
                Vtdp = Vtb[0] @ Vtb[1] @ adag(Vtb[2]) @ adag(Vtb[3])
                delta = (sum(dist(Y_[i], Vtb[i]) for i in range(4))
                         + sum(dist(Lm, I2) for Lm in (L2i, L24, L3, L1)))
                lhs = Aplaq(h_) - Aplaq(h)
                dsum += lhs
                rhs = ((1 + eta) * Aplaq(Vdp) - (1 - eta) * Aplaq(Vtdp)
                       + (1 + 1 / eta) * delta ** 2)
                worst_ineq = max(worst_ineq, lhs - rhs)
                cnt += 1
    print(f"    corner ({cnt} fine corner plaquettes): chain identity defect "
          f"{worst_id:.1e}; max [A(h')-A(h) - RHS(eta=1/2)] = {worst_ineq:.3e}"
          f" (<= 0)")
    assert worst_id < 1e-11 and worst_ineq <= 1e-12
    return dsum


def part4(L, n, sigma):
    print(f"\n[Part 4, L={L}] mu NOT the last axis: reference path t = 0")
    one_V = {(y, mu): I2.copy()
             for y in itertools.product(range(n), repeat=3) for mu in range(3)}
    T = build_fibre(L, n, sigma, one_V)
    for mu in (0, 1, 2):
        bonds = [((0, 0, 0), mu)]
        R = {bonds[0]: t74.rand_su2()}
        T2 = apply_T(T, L, n, R)
        err = np.abs(t74.q_full(T2, L, mu, (0, 0, 0)) - R[bonds[0]]).max()
        print(f"  mu = {mu}: |q(T U) - R| at the modified bond = {err:.2e}")
    print("  (mu = 2 is exact; mu = 0, 1 are not: the Y_x sharing one crossing"
          " link have different a_x.)")


if __name__ == "__main__":
    part1()
    part2_3(2, 3, 0.02, 2)
    part2_3(3, 3, 0.01, 1)
    part4(2, 3, 0.02)
    part4(3, 3, 0.01)
