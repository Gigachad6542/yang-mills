"""T79: exact fibre transport for all three bond axes (note 64 Section 8).

Conventions are those of t47/t74/t77: d = 3, periodic, SU(2), U = (U_rest, b),
q = Balaban's average CMP 98 (42).  The in-block contour gamma(y, x) runs
coordinate 0 first, then 1, then 2.  (Balaban's (1.7) runs the LAST coordinate
first and coordinate 1 last: the repo labelling is the reversal i -> 2 - i,
checked in Part 0.)  "Last axis" below = the axis traversed last by gamma
(repo index 2, Balaban's coordinate 1).

Part 0  Dictionary.  With a contour that traverses the axes in order
        (o_1, o_2, o_3), Y_{c,x} is independent of t = x_mu - y_mu exactly for
        mu = o_3 (the axis traversed last).  Checked for the repo order and
        for Balaban's order (2, 1, 0) (his coordinate 3 first).
Part 1  Structure (Lemma 8.1).  Y_x = delta_x Y_{x0} eps_x with
        delta_x = gamma(y,x) run(0->t)^{-1} gamma(y,y+xi)^{-1}; after the
        left translation u_xi -> a0^{-1} R a0 u_xi (xi != 0) one has
        Y'_x = delta_x R delta_x^{-1} Y_x.  delta = 1 for the last axis.
Part 2  The approximate transport T~_R on near-flat fibre configurations
        (all three axes, L = 2, 3).  Translate the non-private crossing links
        of the bonds in Z, then solve the private link by Newton so that
        q(T~ U) = R q(U) on Z.  Prints: q exactness, Newton residual, the
        quantities kappa, s, r' of Lemma 8.3, the bounds d(X', R X) <=
        2 (L^2-1) (kappa + s), J_max, the Jacobian ratio j, and that T~_{R^-1}
        inverts T~_R.
Part 3  Changed plaquettes (Lemma 8.4): sum of type-A and corner differences
        equals A(T~U) - A(U); type-A bound A(h') <= (|M|+|N|+rho)^2/2; corner
        bound with delta'.
Part 4  Failure of the exact recipe: q error of the pure translation map with
        the reference path t = 0, against the commutator defect.
Part 5  How far a single Haar sample is from the good set (Newton success
        and r' <= eps pi / 2 against sigma).
Part 6  Constants c_L, J_max, log(J_max/c_L), r'_max.
"""
import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t47_average_jacobian as t  # noqa: E402
import t74_extension_check as t74  # noqa: E402
import t77_transport_check as t77  # noqa: E402
from t74_extension_check import I2, Torus, dist  # noqa: E402

rng = np.random.default_rng(79)


def adag(a):
    return a.conj().T


def Aplaq(P):
    return 1 - np.real(P[0, 0] + P[1, 1]) / 2


def e_(mu):
    v = np.zeros(3, dtype=int)
    v[mu] = 1
    return v


def comm_dist(d, R):
    """d(d R d^-1, R) = distance of the commutator [d, R] from 1."""
    return dist(d @ R @ adag(d), R)


def gamma_ord(y, x, order):
    pts = [list(y)]
    cur = list(y)
    for mu in order:
        step = 1 if x[mu] >= cur[mu] else -1
        while cur[mu] != x[mu]:
            cur[mu] += step
            pts.append(list(cur))
    return pts


def transverse(L, mu):
    for a in itertools.product(range(L), repeat=3):
        if a[mu] == 0:
            yield np.array(a)


def window(T, L, mu, y0, ap, t_, order=(0, 1, 2)):
    """x = y0 + ap + t_ e_mu.  Returns (A, Ap, u, Y) with Y = A u Ap the
    contour product Gamma_{c,x}; A = gamma(y,x) + mu-run to the tail,
    Ap = mu-run (t steps) from the head + reversed gamma(y', x')."""
    y0 = np.array(y0)
    em = e_(mu)
    ap = np.array(ap)
    x = y0 + ap + t_ * em
    P1 = gamma_ord(list(y0), list(x), order) + [list(x + k * em)
                                                for k in range(1, L - t_)]
    tail = y0 + ap + (L - 1) * em
    head = tail + em
    xp = x + L * em
    P3a = [list(head + k * em) for k in range(1, t_ + 1)]
    gp = gamma_ord(list(y0 + L * em), list(xp), order)[::-1]
    A = T.path(P1)
    Ap = T.path([list(head)] + P3a + gp[1:])
    u = T.get(tail, mu)
    return A, Ap, u, A @ u @ Ap


def bond_windows(T, L, mu, y0, order=(0, 1, 2)):
    """All windows x in S for the bond (y0, mu): list of dicts."""
    out = []
    ref = {}
    for ap in transverse(L, mu):
        if not ap.any():
            continue
        A0, Ap0, u0, Y0 = window(T, L, mu, y0, ap, 0, order)
        ref[tuple(ap)] = (A0, Ap0, Y0)
        for t_ in range(L):
            A, Ap, u, Y = window(T, L, mu, y0, ap, t_, order)
            out.append(dict(xi=tuple(ap), t=t_, A=A, Ap=Ap, Y=Y,
                            delta=A @ adag(A0), eps=adag(Ap0) @ Ap, Y0=Y0))
    e = np.zeros(3, dtype=int)
    e[mu] = 1
    W = T.path([list(np.array(y0) + k * e) for k in range(L)])
    X = T.path([list(np.array(y0) + k * e) for k in range(L + 1)])
    return out, W, X, ref


def tail_key(T, L, mu, y0, ap):
    return T.key(np.array(y0) + np.array(ap) + (L - 1) * e_(mu), mu)


# ---------------------------------------------------------------------------
def part0():
    print("[Part 0] contour order dictionary: Y_{c,x} independent of t iff mu "
          "is the axis traversed last")
    for L in (2, 3):
        s = 3 * L
        T = Torus(s)
        for x in itertools.product(range(s), repeat=3):
            for mu in range(3):
                T.U[(x, mu)] = t74.rand_su2()
        for order in ((0, 1, 2), (2, 1, 0)):
            res = []
            for mu in range(3):
                worst = 0.0
                for ap in transverse(L, mu):
                    if not ap.any():
                        continue
                    ys = [window(T, L, mu, (0, 0, 0), ap, t_, order)[3]
                          for t_ in range(L)]
                    worst = max(worst, max(np.abs(ys[0] - y).max()
                                           for y in ys))
                res.append(worst)
            # check the decomposition against the direct contour (repo order)
            if order == (0, 1, 2):
                mu = 1
                ap = np.array([1, 0, 1])
                Y1 = window(T, L, mu, (0, 0, 0), ap, L - 1)[3]
                Y2 = T.path(t74.contour(L, mu, [0, 0, 0],
                                        list(ap + (L - 1) * e_(mu))))
                chk = np.abs(Y1 - Y2).max()
            else:
                chk = float("nan")
            print(f"  L={L} order {order}: max_t-variation of Y for mu=0,1,2 = "
                  f"{res[0]:.1e}, {res[1]:.1e}, {res[2]:.1e}"
                  f"   (decomposition check vs contour(): {chk:.1e})")
            last = order[-1]
            assert res[last] < 1e-12
            assert all(res[m] > 1e-3 for m in range(3) if m != last)


# ---------------------------------------------------------------------------
def part1(L):
    print(f"\n[Part 1, L={L}] Y_x = delta_x Y_x0 eps_x; translation gives "
          f"Y'_x = delta_x R delta_x^-1 Y_x")
    n = 3
    s = n * L
    T = Torus(s)
    for x in itertools.product(range(s), repeat=3):
        for mu in range(3):
            T.U[(x, mu)] = t74.rand_su2()
    y0 = (L, L, L)
    for mu in range(3):
        ws, W, X, ref = bond_windows(T, L, mu, y0)
        Rm = t74.rand_su2()
        # translated configuration (xi != 0 only)
        T2 = Torus(s)
        T2.U = {k: v.copy() for k, v in T.U.items()}
        for ap, (A0, Ap0, Y0) in ref.items():
            k = tail_key(T, L, mu, y0, ap)
            T2.U[k] = adag(A0) @ Rm @ A0 @ T.U[k]
        ws2, _, _, _ = bond_windows(T2, L, mu, y0)
        err_dec = max(np.abs(w["Y"] - w["delta"] @ w["Y0"] @ w["eps"]).max()
                      for w in ws)
        err_tr = max(np.abs(w2["Y"] - w["delta"] @ Rm @ adag(w["delta"]) @ w["Y"]
                            ).max() for w, w2 in zip(ws, ws2))
        dmax = max(dist(w["delta"], I2) for w in ws)
        dcomm = max(comm_dist(w["delta"], Rm) for w in ws)
        errRY = max(dist(w2["Y"], Rm @ w["Y"]) for w, w2 in zip(ws, ws2))
        print(f"  axis {mu}: |Y - delta Y0 eps| = {err_dec:.1e}; "
              f"|Y' - delta R delta^-1 Y| = {err_tr:.1e}; "
              f"max d(delta,1) = {dmax:.3f}; max d([delta,R],1) = {dcomm:.3f}; "
              f"max d(Y', R Y) = {errRY:.3f}")
        assert err_dec < 1e-11 and err_tr < 1e-11
        if mu == 2:
            assert dmax < 1e-12
        else:
            assert dmax > 1e-3


# ---------------------------------------------------------------------------
def consts(L):
    eps = float(L) ** -2
    cL = eps ** 3 * (np.sin(eps * np.pi) / ((1 - eps) * np.pi)) ** 2
    Jmax = (1 + (1 - eps) * np.pi / 2) ** 3
    return eps, cL, Jmax


def transport(T, L, n, Z, R, V_target, tol=1e-12):
    """Approximate transport: translate non-private crossing links of Z-bonds,
    solve private links.  Returns (T2, info dict per bond) or raises."""
    eps, cL, Jmax = consts(L)
    s = T.s
    T2 = Torus(s)
    T2.U = {k: v.copy() for k, v in T.U.items()}
    info = {}
    for (y, mu), Rc in Z.items():
        y0 = np.array([L * c for c in y])
        ws, W, X, ref = bond_windows(T, L, mu, y0)
        for ap, (A0, Ap0, Y0) in ref.items():
            k = tail_key(T, L, mu, y0, ap)
            T2.U[k] = adag(A0) @ Rc @ A0 @ T.U[k]
        ws2, _, _, _ = bond_windows(T2, L, mu, y0)
        Ys2 = [w["Y"] for w in ws2]
        ps = [1.0 / L ** 3] * len(Ys2)
        Vt = V_target[(y, mu)]
        X2, res = t74.newton(Ys2, ps, Vt, Rc @ X)
        kb = tail_key(T, L, mu, y0, (0, 0, 0))
        T2.U[kb] = adag(W) @ X2
        Ys = [w["Y"] for w in ws]
        kappa = max(dist(Y, X) for Y in Ys)
        sc = max(dist(w["delta"], I2) for w in ws)
        rp = (2 - eps) * kappa + 2 * sc
        Vz = adag(Rc) @ Vt  # = q(U)_c
        J0 = t74.jac_det(Ys, ps, X)
        J1 = t74.jac_det(Ys2, ps, X2)
        info[(y, mu)] = dict(res=res, kappa=kappa, s=sc, rp=rp,
                             dXR=dist(X2, Rc @ X), J0=J0, J1=J1,
                             dX2V=dist(X2, Vt),
                             dY2V=max(dist(Y, Vt) for Y in Ys2),
                             dYX2=max(dist(Y, X2) for Y in Ys2),
                             R0=X2 @ adag(X), Rc=Rc, Vz=Vz)
    return T2, info


def part2_3(L, n, sigma, trials, label=""):
    eps, cL, Jmax = consts(L)
    print(f"\n[Parts 2,3, L={L}] coarse side {n}, sigma = {sigma}; "
          f"eps pi/2 = {eps*np.pi/2:.4f}, c_L = {cL:.3e}, J_max = {Jmax:.3f}")
    for tr in range(trials):
        Vt0 = {(y, mu): t77.su2_small(0.15)
               for y in itertools.product(range(n), repeat=3)
               for mu in range(3)}
        T = t77.build_fibre(L, n, sigma, Vt0)
        # Z: one full coarse plaquette (axes 0, 1) + other axes
        Zb = [((0, 0, 0), 0), ((1, 0, 0), 1), ((0, 1, 0), 0), ((0, 0, 0), 1),
              ((1, 1, 1), 2), ((2, 1, 0), 0), ((0, 2, 1), 1), ((2, 2, 2), 2)]
        Z = {b: t74.rand_su2() for b in Zb}
        Vtar = {k: (Z[k] @ Vt0[k] if k in Z else Vt0[k]) for k in Vt0}
        T2, info = transport(T, L, n, Z, Z, Vtar)
        # q exactness on every bond
        q2 = t77.q_all(T2, L, n)
        qerr = max(np.abs(q2[k] - Vtar[k]).max() for k in Vtar)
        q0 = t77.q_all(T, L, n)
        qerr0 = max(np.abs(q0[k] - Vt0[k]).max() for k in Vt0)
        print(f"  trial {tr}: max|q(U) - Vt| = {qerr0:.1e}; "
              f"max|q(T~U) - R Vt| = {qerr:.1e}  (|Z| = {len(Z)}, axes "
              f"{sorted(set(b[1] for b in Z))})")
        assert qerr0 < 1e-9 and qerr < 1e-11
        for axis in (0, 1, 2):
            sel = [v for (k, v) in info.items() if k[1] == axis]
            if not sel:
                continue
            kap = max(v["kappa"] for v in sel)
            sc = max(v["s"] for v in sel)
            rp = max(v["rp"] for v in sel)
            ok = all(v["rp"] <= eps * np.pi / 2 for v in sel)
            bound = max(v["dXR"] / (2 * (L * L - 1) * (v["kappa"] + v["s"]) + 1e-300)
                        for v in sel)
            jr = [v["J0"] / v["J1"] for v in sel]
            dYr = max(v["dYX2"] / (v["rp"] / eps) for v in sel)
            print(f"    axis {axis}: kappa<= {kap:.4f}, s<= {sc:.4f}, "
                  f"r'<= {rp:.4f} (<= eps pi/2: {ok}); Newton res <= "
                  f"{max(v['res'] for v in sel):.1e}; "
                  f"d(X',RX)/[2(L^2-1)(kappa+s)] <= {bound:.3f}; "
                  f"max d(Y',X')/(r'/eps) = {dYr:.3f}; J/J' in "
                  f"[{min(jr):.5f}, {max(jr):.5f}]")
            assert ok and bound <= 1 + 1e-9 and dYr <= 1 + 1e-9
            assert all(v["J1"] <= Jmax and v["J0"] >= cL for v in sel)
        # last-axis: X' = R X exactly
        if any(k[1] == 2 for k in info):
            e2 = max(np.abs(v["R0"] - v["Rc"]).max()
                     for k, v in info.items() if k[1] == 2)
            print(f"    last axis: |X'X^-1 - R| = {e2:.1e} (exact translation)")
            assert e2 < 1e-9
        # inverse
        Zinv = {b: adag(Rm) for b, Rm in Z.items()}
        T3, info3 = transport(T2, L, n, Zinv, Zinv, Vt0)
        inv_err = max(np.abs(T3.U[k] - T.U[k]).max() for k in T.U)
        print(f"    T~_(R^-1) T~_R U = U: max link difference {inv_err:.1e}")
        assert inv_err < 1e-9
        # --- Part 3
        part3(T, T2, L, n, Z, Vt0, Vtar, info)


def part3(T, T2, L, n, Z, Vt0, Vtar, info, eta=0.5):
    eps = float(L) ** -2
    # Rhat for every (bond, xi): Rhat = A u' u^-1 A^-1 (reference path t = 0)
    def Rhat(mu, y0, ap):
        A, Ap, u, Y = window(T, L, mu, y0, ap, 0)
        k = tail_key(T, L, mu, y0, ap)
        return A @ T2.U[k] @ adag(T.U[k]) @ adag(A)

    worstA_id = 0.0
    worstA = -1e9
    dsumA = 0.0
    for (y, mu), Rc in Z.items():
        y0 = np.array([L * c for c in y])
        for nu in range(3):
            if nu == mu:
                continue
            for a1 in transverse(L, mu):
                a2 = a1 + e_(nu)
                if a2[nu] > L - 1:
                    continue
                p1 = t77.a_points(L, mu, y0, a1)
                p2 = t77.a_points(L, mu, y0, a2)
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
                R1, R2 = Rhat(mu, y0, a1), Rhat(mu, y0, a2)
                worstA_id = max(worstA_id,
                                np.abs(a @ h @ adag(a) - M @ N).max(),
                                np.abs(a @ h_ @ adag(a)
                                       - R1 @ M @ adag(R2) @ N).max())
                rho = dist(R1, Rc) + dist(R2, Rc)
                dsumA += Aplaq(h_) - Aplaq(h)
                worstA = max(worstA, Aplaq(h_)
                             - (dist(M, I2) + dist(N, I2) + rho) ** 2 / 2)
    print(f"    type A: identity defect {worstA_id:.1e}; max [A(h') - "
          f"(|M|+|N|+rho)^2/2] = {worstA:.2e} (<= 0)")
    assert worstA_id < 1e-11 and worstA <= 1e-12

    # corner plaquettes of coarse plaquettes touching Z
    worst_id = 0.0
    worst_ineq = -1e9
    worst_dp = -1e9
    cnt = 0
    dsumC = 0.0
    V0 = Vt0
    for y in itertools.product(range(n), repeat=3):
        for mu, nu in ((0, 1), (0, 2), (1, 2)):
            rho_ax = 3 - mu - nu
            ym = tuple((np.array(y) + e_(mu)) % n)
            yn = tuple((np.array(y) + e_(nu)) % n)
            bonds = [(y, mu), (ym, nu), (yn, mu), (y, nu)]
            if not any(b in Z for b in bonds):
                continue
            starts = [np.array(y) * L, np.array(y) * L + L * e_(mu),
                      np.array(y) * L + L * e_(nu), np.array(y) * L]
            mus = [mu, nu, mu, nu]
            for r in range(L):
                ap = [(L - 1) * e_(nu) + r * e_(rho_ax), r * e_(rho_ax),
                      r * e_(rho_ax), (L - 1) * e_(mu) + r * e_(rho_ax)]
                dat = [window(T, L, mus[i], starts[i], ap[i], 0)
                       for i in range(4)]
                A_ = [d[0] for d in dat]
                Ap_ = [d[1] for d in dat]
                Y_ = [d[3] for d in dat]
                Rh = [Rhat(mus[i], starts[i], ap[i]) for i in range(4)]
                s0 = np.array(y) * L + (L - 1) * (e_(mu) + e_(nu)) + r * e_(rho_ax)
                plq = [list(s0), list(s0 + e_(mu)),
                       list(s0 + e_(mu) + e_(nu)), list(s0 + e_(nu)), list(s0)]
                h, h_ = T.path(plq), T2.path(plq)
                L2i = adag(Ap_[0]) @ adag(A_[1])
                L24 = adag(Ap_[1]) @ Ap_[2]
                L3 = A_[2] @ Ap_[3]
                L1 = A_[3] @ adag(A_[0])
                Hh = (Y_[0] @ L2i @ Y_[1] @ L24 @ adag(Y_[2]) @ L3
                      @ adag(Y_[3]) @ L1)
                Hp = ((Rh[0] @ Y_[0]) @ L2i @ (Rh[1] @ Y_[1]) @ L24
                      @ adag(Rh[2] @ Y_[2]) @ L3 @ adag(Rh[3] @ Y_[3]) @ L1)
                worst_id = max(worst_id,
                               np.abs(A_[0] @ h @ adag(A_[0]) - Hh).max(),
                               np.abs(A_[0] @ h_ @ adag(A_[0]) - Hp).max())
                Vb = [Vtar[b] for b in bonds]
                Vtb = [V0[b] for b in bonds]
                Vdp = Vb[0] @ Vb[1] @ adag(Vb[2]) @ adag(Vb[3])
                Vtdp = Vtb[0] @ Vtb[1] @ adag(Vtb[2]) @ adag(Vtb[3])
                Lam = [dist(Lm, I2) for Lm in (L2i, L24, L3, L1)]
                delta = sum(dist(Y_[i], Vtb[i]) for i in range(4)) + sum(Lam)
                deltap = sum(dist(Rh[i] @ Y_[i], Vb[i]) for i in range(4)) + sum(Lam)
                # theoretical bound for delta' (Lemma 8.4(b))
                kap = []
                for i in range(4):
                    ws, W, X, ref = bond_windows(T, L, mus[i], starts[i])
                    kap.append(max(dist(w["Y"], X) for w in ws))
                rhos = [dist(Rh[i], Z.get(bonds[i], I2)) for i in range(4)]
                dp_bound = (sum((2 - eps) * kap[i] + rhos[i] for i in range(4))
                            + sum(Lam))
                worst_dp = max(worst_dp, deltap - dp_bound)
                lhs = Aplaq(h_) - Aplaq(h)
                dsumC += lhs
                rhs = ((1 + eta) * Aplaq(Vdp) - (1 - eta) * Aplaq(Vtdp)
                       + (1 + eta) / eta * max(deltap, delta) ** 2)
                worst_ineq = max(worst_ineq, lhs - rhs)
                cnt += 1
    print(f"    corner ({cnt} fine corner plaquettes): chain identity defect "
          f"{worst_id:.1e}; max [A(h')-A(h) - RHS(eta=1/2)] = {worst_ineq:.3f}"
          f" (<= 0); max[delta' - bound] = {worst_dp:.1e} (<= 0)")
    assert worst_id < 1e-11 and worst_ineq <= 1e-12 and worst_dp <= 1e-9
    dA = T2.action() - T.action()
    print(f"    all changed plaquettes: type A + corner = {dsumA + dsumC:.10f};"
          f" A(T~U) - A(U) = {dA:.10f}")
    assert abs(dsumA + dsumC - dA) < 1e-9


# ---------------------------------------------------------------------------
def part4(L, n, sigma):
    print(f"\n[Part 4, L={L}] pure translation (no private-link solve): "
          f"q error vs the commutator defect")
    one_V = {(y, mu): I2.copy()
             for y in itertools.product(range(n), repeat=3)
             for mu in range(3)}
    T = t77.build_fibre(L, n, sigma, one_V)
    for mu in (0, 1, 2):
        Rm = t74.rand_su2()
        y0 = (0, 0, 0)
        ws, W, X, ref = bond_windows(T, L, mu, y0)
        T2 = Torus(T.s)
        T2.U = {k: v.copy() for k, v in T.U.items()}
        for ap, (A0, Ap0, Y0) in ref.items():
            k = tail_key(T, L, mu, y0, ap)
            T2.U[k] = adag(A0) @ Rm @ A0 @ T.U[k]
        kb = tail_key(T, L, mu, y0, (0, 0, 0))
        T2.U[kb] = adag(W) @ Rm @ W @ T.U[kb]
        err = np.abs(t74.q_full(T2, L, mu, (0, 0, 0)) - Rm).max()
        dc = max(comm_dist(w["delta"], Rm) for w in ws)
        print(f"  axis {mu}: |q(T U) - R| = {err:.2e}; max d([delta,R],1) = "
              f"{dc:.2e}")
        if mu == 2:
            assert err < 1e-12
        else:
            assert err > 1e-4


def part5(L, n, sigmas, trials):
    eps, cL, Jmax = consts(L)
    print(f"\n[Part 5, L={L}] good-set fraction against sigma (per Z-bond, "
          f"axes 0,1; Newton success and r' <= eps pi/2)")
    for sg in sigmas:
        tot = good = conv = 0
        for tr in range(trials):
            Vt0 = {(y, mu): t77.su2_small(0.15)
                   for y in itertools.product(range(n), repeat=3)
                   for mu in range(3)}
            try:
                T = t77.build_fibre(L, n, sg, Vt0)
            except AssertionError:
                continue
            for (y, mu) in [((0, 0, 0), 0), ((1, 1, 0), 1), ((2, 0, 1), 0),
                            ((0, 2, 2), 1)]:
                Rc = t74.rand_su2()
                y0 = np.array([L * c for c in y])
                ws, W, X, ref = bond_windows(T, L, mu, y0)
                kappa = max(dist(w["Y"], X) for w in ws)
                sc = max(dist(w["delta"], I2) for w in ws)
                rp = (2 - eps) * kappa + 2 * sc
                tot += 1
                good += rp <= eps * np.pi / 2
        print(f"  sigma = {sg}: {good}/{tot} bonds have r' <= eps pi/2 = "
              f"{eps*np.pi/2:.3f}")


def part6():
    print("\n[Part 6] constants")
    print("  L   eps      c_L          J_max    log(J_max/c_L)  r'_max=eps*pi/2"
          "  (2-eps)")
    for L in (2, 3, 4):
        eps, cL, Jmax = consts(L)
        print(f"  {L}  {eps:.4f}  {cL:.4e}  {Jmax:8.3f}  {np.log(Jmax/cL):8.3f}"
              f"        {eps*np.pi/2:.5f}      {2-eps:.4f}")


if __name__ == "__main__":
    part0()
    part1(2)
    part1(3)
    part2_3(2, 3, 0.02, 2)
    part2_3(3, 3, 0.01, 1)
    part4(2, 3, 0.02)
    part4(3, 3, 0.01)
    part5(2, 3, [0.02, 0.05, 0.1, 0.2], 3)
    part6()
