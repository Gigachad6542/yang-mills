"""T80: exact Gaussian (abelian) fibre measure for note 67.

Model.  3D torus, coarse side n, block size L, fine side s = n L.  Fine link
variables are real angles A(x,mu) (the non-compact lift of U(1)); the fine
action is beta/2 * sum_p (dA)_p^2 with (dA)_p = A(x,mu)+A(x+e_mu,nu)
-A(x+e_nu,mu)-A(x,nu).  Balaban's average CMP 98 (42) is LINEAR in this lift:
(qA)(c) = L^-3 sum_{x in B(y)} A(Gamma_{c,x}), contour sums of angles.
The fibre {qA = V'} with the Wilson (Gaussian) weight is a Gaussian measure:
mean = classical constrained minimiser A_cl, covariance = (beta H_K)^+ on the
complement of the gauge zero modes (gauge transformations equal to 0 at the
block corners).  All functionals used are gauge invariant (plaquettes and
closed loops based at block corners); this is asserted.

Linear algebra: eigh only (no pinv, no lstsq).  The zero modes of the
reduced Hessian are counted and compared with the predicted number
(L^3 - 1) n^3.

Parts
 1  Dimension counts, gauge invariance, exact conditional variances:
    max_q beta Var(theta_q | fibre) <= 1  (Gaussian conditioning).
 2  Classical fine fluxes for V' = flux theta_0 on one coarse bond:
    E[beta_{N+1} A_q] = beta_{N+1} theta_cl,q^2 / 2 + beta Var/2.
    The classical term grows with beta_{N+1}: (EQ') of note 64 fails.
 3  Lemma 67.1 style check (coarse flux <= K * sum of fine fluxes) in the
    Gaussian model, and the fraction of the coarse flux carried by the
    L corner plaquettes of note 64 Lemma 64.1 (U0-type) vs the spread.
 4  The quantity G_eta of note 64 Prop 64.3 at the classical minimiser
    for Z = {one last-axis bond}: R_G(eta) = L G_eta^cl / A_Z(V^Z) against
    the slack (1-eta) L^2 - 1 of the dropped term.
"""
import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t74_extension_check as t74  # noqa: E402


def e_(mu):
    v = np.zeros(3, dtype=int)
    v[mu] = 1
    return v


class AbTorus:
    def __init__(self, L, n):
        self.L, self.n, self.s = L, n, L * n
        self.nl = 3 * self.s ** 3

    def idx(self, x, mu):
        s = self.s
        x = [int(c) % s for c in x]
        return ((x[0] * s + x[1]) * s + x[2]) * 3 + mu

    def row(self, pts):
        """Row vector r with (r . A) = sum of angles along the path."""
        r = np.zeros(self.nl)
        for p, q in zip(pts[:-1], pts[1:]):
            d = np.array(q) - np.array(p)
            mu = int(np.nonzero(d)[0][0])
            if d[mu] == 1:
                r[self.idx(p, mu)] += 1.0
            else:
                r[self.idx(q, mu)] -= 1.0
        return r

    def plaq_matrix(self):
        s = self.s
        rows = []
        self.plaq_index = {}
        for x in itertools.product(range(s), repeat=3):
            for mu, nu in ((0, 1), (0, 2), (1, 2)):
                r = np.zeros(self.nl)
                r[self.idx(x, mu)] += 1
                r[self.idx(np.array(x) + e_(mu), nu)] += 1
                r[self.idx(np.array(x) + e_(nu), mu)] -= 1
                r[self.idx(x, nu)] -= 1
                self.plaq_index[(x, mu, nu)] = len(rows)
                rows.append(r)
        return np.array(rows)

    def q_matrix(self):
        """Rows: coarse bonds (y,mu); (qA)_c = L^-3 sum_x contour sums."""
        L, n = self.L, self.n
        rows = []
        self.bond_index = {}
        for y in itertools.product(range(n), repeat=3):
            for mu in range(3):
                y0 = [L * c for c in y]
                r = np.zeros(self.nl)
                for a in itertools.product(range(L), repeat=3):
                    x = [y0[i] + a[i] for i in range(3)]
                    r += self.row(t74.contour(L, mu, y0, x))
                self.bond_index[(y, mu)] = len(rows)
                rows.append(r / L ** 3)
        return np.array(rows)


def build(L, n):
    T = AbTorus(L, n)
    C = T.plaq_matrix()
    Q = T.q_matrix()
    return T, C, Q


class FibreSolver:
    """Precomputes the kernel of Q and the eigen-decomposition of the reduced
    Hessian H_K once; solve(Vp) then gives the classical minimiser."""

    def __init__(self, T, C, Q):
        self.T, self.C, self.Q = T, C, Q
        nl, nc = T.nl, Q.shape[0]
        self.H = C.T @ C
        self.QQt = Q @ Q.T
        w, U = np.linalg.eigh(Q.T @ Q)
        zero = w < 1e-9
        assert zero.sum() == nl - nc, (zero.sum(), nl - nc)
        assert np.sort(w[~zero]).min() > 1e-6
        self.K = U[:, zero]
        HK = self.K.T @ self.H @ self.K
        lam, W = np.linalg.eigh(HK)
        n_zero = int((lam < 1e-9).sum())
        pred = (T.L ** 3 - 1) * T.n ** 3
        assert n_zero == pred, (n_zero, pred)
        pos = lam >= 1e-9
        gap = lam[pos].min()
        assert gap > 1e-6, gap
        self.Wp, self.lam = W[:, pos], lam[pos]
        self.info = dict(n_zero=n_zero, gap=gap, lam_max=lam.max(), pred=pred,
                         zero_modes=W[:, ~pos])
        self.Zm = W[:, ~pos]

    def solve(self, Vp):
        Ap = self.Q.T @ np.linalg.solve(self.QQt, Vp)
        assert np.abs(self.Q @ Ap - Vp).max() < 1e-10
        rhs = -self.K.T @ (self.H @ Ap)
        assert np.abs(self.Zm.T @ rhs).max() < 1e-9
        z = self.Wp @ ((self.Wp.T @ rhs) / self.lam)
        Acl = Ap + self.K @ z
        assert np.abs(self.Q @ Acl - Vp).max() < 1e-9
        return Acl


def variances(Fmat, K, Wp, lam, Zmodes):
    """Var (times beta) of the linear functionals Fmat @ A on the fibre;
    asserts gauge invariance (Fmat K annihilates the gauge zero modes)."""
    FK = Fmat @ K
    assert np.abs(FK @ Zmodes).max() < 1e-9, "functional not gauge invariant"
    Wt = (FK @ Wp) / np.sqrt(lam)
    return (Wt ** 2).sum(axis=1)


def coarse_plaq_bonds(n, y, mu, nu):
    ym = tuple((np.array(y) + e_(mu)) % n)
    yn = tuple((np.array(y) + e_(nu)) % n)
    return [(tuple(y), mu), (ym, nu), (yn, mu), (tuple(y), nu)]


def coarse_flux(Vp, T, y, mu, nu):
    b = coarse_plaq_bonds(T.n, y, mu, nu)
    ix = [T.bond_index[k] for k in b]
    return Vp[ix[0]] + Vp[ix[1]] - Vp[ix[2]] - Vp[ix[3]]


def face_cell(T, y, mu, nu):
    """The L^3 fine plaquettes (plane mu nu, L x L face x L layers) of the
    coarse plaquette (y, mu, nu)."""
    L = T.L
    rho = 3 - mu - nu
    out = []
    for a in range(L):
        for b in range(L):
            for r in range(L):
                x = np.array(y) * L + a * e_(mu) + b * e_(nu) + r * e_(rho)
                m, nn = (mu, nu) if mu < nu else (nu, mu)
                x = tuple(int(c) % T.s for c in x)
                out.append(T.plaq_index[(x, m, nn)])
    return out


def sign_plane(mu, nu):
    return 1.0 if mu < nu else -1.0


def part1_2_3(L, n, theta0=1.0):
    print(f"\n[Parts 1-3, L={L}, coarse side n={n}] fine side {L*n}")
    T, C, Q = build(L, n)
    FS = FibreSolver(T, C, Q)
    nc = Q.shape[0]
    # unconditional plaquette variance (projection) for comparison
    Hfull = C.T @ C
    lamF, WF = np.linalg.eigh(Hfull)
    posF = lamF > 1e-9
    CW = (C @ WF[:, posF]) / np.sqrt(lamF[posF])
    var_uncond = (CW ** 2).sum(axis=1)

    y0 = (0, 0, 0)
    # V' = flux theta0 on the coarse bond (y0, 0) (axis 0)
    Vp = np.zeros(nc)
    Vp[T.bond_index[(y0, 0)]] = theta0
    Acl = FS.solve(Vp)
    K, Wp, lam, info = FS.K, FS.Wp, FS.lam, FS.info
    print(f"  Part 1: dim ker Q = {K.shape[1]}, gauge zero modes of H_K = "
          f"{info['n_zero']} (predicted (L^3-1)n^3 = {info['pred']}), "
          f"spectral gap of H_K = {info['gap']:.4f}, max eigenvalue "
          f"{info['lam_max']:.3f}")
    varq = variances(C, K, Wp, lam, info["zero_modes"])
    print(f"  Part 1: max_q beta Var(theta_q | fibre) = {varq.max():.6f}; "
          f"unconditional max_q beta Var = {var_uncond.max():.6f} (<= 1: "
          f"projection); conditional <= unconditional: "
          f"{bool((varq <= var_uncond + 1e-9).all())}")
    assert varq.max() <= 1 + 1e-9 and (varq <= var_uncond + 1e-9).all()
    th = C @ Acl
    # Part 2: classical fluxes on the cell of the coarse plaquette (y0, 0, 2)
    mu, nu = 0, 2
    thp = coarse_flux(Vp, T, y0, mu, nu)
    cell = face_cell(T, y0, mu, nu)
    cl_cell = sum(th[i] ** 2 for i in cell)
    cl_all = (th ** 2).sum()
    var_cell = sum(varq[i] for i in cell)
    uniform = thp / L ** 2
    print(f"  Part 2: coarse plaquette p=(y0,{mu},{nu}) flux theta_p = {thp:+.3f}; "
          f"fine plaquettes of its cell: {len(cell)} (= L^3); "
          f"sum theta_cl^2 over the cell = {cl_cell:.5f}; "
          f"uniform-spread value L^3 (theta_p/L^2)^2 = "
          f"{len(cell) * uniform ** 2:.5f}")
    print(f"          total classical fine energy sum_q theta_cl^2 = {cl_all:.5f}"
          f" over all plaquettes; coarse sum_p theta_p^2 = "
          f"{sum(coarse_flux(Vp,T,y,m,nn)**2 for y in itertools.product(range(n),repeat=3) for m,nn in ((0,1),(0,2),(1,2))):.5f}")
    cn = sum(coarse_flux(Vp, T, y, m, nn) ** 2
             for y in itertools.product(range(n), repeat=3)
             for m, nn in ((0, 1), (0, 2), (1, 2)))
    print(f"          min fine action / coarse action, L*sum th^2 / sum thp^2 = "
          f"{L * cl_all / cn:.5f}  (A_N(V) term: T1 = beta_N A_N - beta_N+1 A_min; "
          f"this ratio is the coefficient of -T1 + A_N)")
    # E[beta A_q] = beta th^2/2 + beta var/2 ; show scaling for two betas
    for beta in (10.0, 1000.0, 100000.0):
        eA = beta * (th ** 2).max() / 2 + varq.max() / 2
        print(f"          beta_(N+1) = {beta:9.1f}: max_q E[beta A_q] = "
              f"{beta*(th**2).max()/2:12.3f} (classical) + <= {varq.max()/2:.3f} "
              f"(fluct)  [theta_cl,max = {np.abs(th).max():.5f}]")
    # Part 3: Lemma 67.1 (Gaussian): theta_p <= K sum |theta_q| ; best constant
    # here = |theta_p| / sum over all fine plaquettes |theta_cl|
    print(f"  Part 3: |theta_p| / sum_q |theta_cl,q| (all q) = "
          f"{abs(thp)/np.abs(th).sum():.4f}; corner plaquettes (a=b=L-1, "
          f"L of them): classical flux each = "
          f"{[round(float(th[face_cell(T,y0,mu,nu)[(L-1)*L*L+(L-1)*L+r]]),5) for r in range(L)]}"
          f" vs concentrated value theta_p = {thp:+.3f}")
    return T, C, Q


def type_A_rows(T, y0, mu):
    """Rows of M and N for every type-A plaquette of the last-axis bond
    (y0, mu): M = a1 u1 nu2 u2^-1 a2^-1, N = a2 nu1^-1 a1^-1 (note 64 L64.5)."""
    L = T.L
    rows = []
    y0 = np.array(y0)
    for nu in range(3):
        if nu == mu:
            continue
        for a1 in itertools.product(range(L), repeat=3):
            a1 = np.array(a1)
            if a1[mu] != 0:
                continue
            a2 = a1 + e_(nu)
            if a2[nu] > L - 1:
                continue

            def apts(ap):
                x = y0 + ap
                pts = t74.gamma(list(y0), list(x))
                for k in range(1, L):
                    pts.append(list(x + k * e_(mu)))
                return pts
            p1, p2 = apts(a1), apts(a2)
            t1 = list(y0 + a1 + (L - 1) * e_(mu))
            h1 = list(np.array(t1) + e_(mu))
            h2 = list(np.array(h1) + e_(nu))
            t2 = list(np.array(t1) + e_(nu))
            Mpts = p1 + [h1, h2, t2] + p2[::-1][1:]
            Npts = p2 + [t1] + p1[::-1][1:]
            rows.append((T.row(Mpts), T.row(Npts)))
    return rows


def ycross_rows(T, L, mu, y0, aperp):
    y0 = np.array(y0)
    aperp = np.array(aperp)
    x = y0 + aperp
    pts = t74.gamma(list(y0), list(x))
    for k in range(1, L):
        pts.append(list(x + k * e_(mu)))
    tail = y0 + aperp + (L - 1) * e_(mu)
    head = tail + e_(mu)
    yend = y0 + L * e_(mu)
    gp = t74.gamma(list(yend), list(yend + aperp))[::-1]
    A = T.row(pts)
    Ap = T.row(gp)
    u = T.row([list(tail), list(head)])
    return A, Ap, u


def kappa_rows(T, L, mu, y0):
    """Rows of Y_{c,x} - X_c for all x in B(y) off the central line, c=(y0,mu)."""
    y0 = np.array(y0)
    X = T.row([list(y0 + t * e_(mu)) for t in range(L + 1)])
    out = []
    for a in itertools.product(range(L), repeat=3):
        x = y0 + np.array(a)
        if all(a[i] == 0 for i in range(3) if i != mu):
            continue
        out.append(T.row(t74.contour(L, mu, list(y0), list(x))) - X)
    return np.array(out)


def corner_rows(T, C, Z):
    """For each coarse plaquette touching Z and each layer r: the rows of
    Lambda_1..Lambda_4 (note 64 Lemma 64.5(b)), kappa rows of the four
    bonds, and the check of the chain identity."""
    L, n = T.L, T.n
    out = []
    for y in itertools.product(range(n), repeat=3):
        for mu, nu in ((0, 1), (0, 2), (1, 2)):
            bonds = coarse_plaq_bonds(n, y, mu, nu)
            if not any(b in Z for b in bonds):
                continue
            rho = 3 - mu - nu
            ym, yn = bonds[1][0], bonds[2][0]
            starts = [np.array(y) * L, np.array(y) * L + L * e_(mu),
                      np.array(y) * L + L * e_(nu), np.array(y) * L]
            for r in range(L):
                ap = [(L - 1) * e_(nu) + r * e_(rho), r * e_(rho),
                      r * e_(rho), (L - 1) * e_(mu) + r * e_(rho)]
                mus = [mu, nu, mu, nu]
                dat = [ycross_rows(T, L, mus[i], starts[i], ap[i])
                       for i in range(4)]
                A_ = [d[0] for d in dat]
                Ap_ = [d[1] for d in dat]
                u_ = [d[2] for d in dat]
                Y_ = [A_[i] + u_[i] + Ap_[i] for i in range(4)]
                L2i = -Ap_[0] - A_[1]
                L24 = -Ap_[1] + Ap_[2]
                L3 = A_[2] + Ap_[3]
                L1 = A_[3] - A_[0]
                s0 = np.array(y) * L + (L - 1) * (e_(mu) + e_(nu)) + r * e_(rho)
                plq = [list(s0), list(s0 + e_(mu)), list(s0 + e_(mu) + e_(nu)),
                       list(s0 + e_(nu)), list(s0)]
                hrow = T.row(plq)
                chain = (Y_[0] + L2i + Y_[1] + L24 - Y_[2] + L3 - Y_[3] + L1)
                # a_1 h a_1^-1 = chain; abelian: conjugation trivial
                assert np.abs(chain - hrow).max() < 1e-12, "chain identity"
                kap = [kappa_rows(T, L, mus[i], starts[i]) for i in range(4)]
                out.append(dict(y=y, mu=mu, nu=nu, r=r, bonds=bonds,
                                Lam=[L2i, L24, L3, L1], kap=kap))
    return out


def part4(L, n, theta0=1.0, etas=(0.1, 0.25, 0.5, 0.75)):
    print(f"\n[Part 4, L={L}, n={n}] G_eta (note 64 Prop 64.3) at the classical "
          f"minimiser, Z = {{(y0, 2)}}")
    T, C, Q = build(L, n)
    FS = FibreSolver(T, C, Q)
    nc = Q.shape[0]
    y0 = (0, 0, 0)
    Z = {(y0, 2)}
    typeA = type_A_rows(T, y0, 2)
    corners = corner_rows(T, C, Z)
    print(f"  {len(typeA)} type-A plaquettes (expected 2 L (L-1) = "
          f"{2*L*(L-1)}), {len(corners)} corner plaquettes "
          f"(4 coarse plaquettes x L layers = {4*L})")
    assert len(typeA) == 2 * L * (L - 1) and len(corners) == 4 * L
    # coarse plaquettes touching Z
    pZ = [(y, mu, nu) for y in itertools.product(range(n), repeat=3)
          for mu, nu in ((0, 1), (0, 2), (1, 2))
          if any(b in Z for b in coarse_plaq_bonds(n, y, mu, nu))]
    assert len(pZ) == 4
    eps = L ** -2.0
    print("  c' (bond carrying the flux)   A_Z(V^Z)   S_A     S_kappa   S_Lam  |"
          "   R_G(eta)=L G/A_Z  for eta = " + ", ".join(f"{e}" for e in etas))
    results = []
    for (yb, mb) in [(yy, mm) for yy in itertools.product(range(n), repeat=3)
                     for mm in range(3)]:
        if (yb, mb) in Z:
            continue
        Vp = np.zeros(nc)
        Vp[T.bond_index[(yb, mb)]] = theta0
        AZ = sum(0.5 * coarse_flux(Vp, T, *p) ** 2 for p in pZ)
        if AZ == 0:
            continue
        Acl = FS.solve(Vp)
        # classical values of all loop functionals
        SA = sum((m @ Acl) ** 2 + (nn @ Acl) ** 2 for m, nn in typeA)
        Sk = 0.0
        Sl = 0.0
        for cd in corners:
            Sk += 32 * sum(np.max((k @ Acl) ** 2) for k in cd["kap"])
            Sl += 8 * sum((lr @ Acl) ** 2 for lr in cd["Lam"])
        R = []
        for eta in etas:
            G = SA + (1 + 1 / eta) * (Sk + Sl)
            R.append(L * G / AZ)
        results.append(((yb, mb), AZ, SA, Sk, Sl, R))
        print(f"  {str((yb, mb)):28s} {AZ:8.4f} {SA:8.4f} {Sk:9.3f} {Sl:8.3f} |"
              + "".join(f" {r:10.2f}" for r in R))
    # feasibility
    print("  slack (1-eta) L^2 - 1 = " + ", ".join(
        f"{(1-e)*L*L-1:.3f}" for e in etas) + f"  (eta <= 1 - L^-2 = {1-eps:.3f})")
    worst = [max(r[5][k] for r in results) for k in range(len(etas))]
    minR = [min(r[5][k] for r in results) for k in range(len(etas))]
    print("  max over c' of R_G = " + ", ".join(f"{w:.2f}" for w in worst))
    print("  min over c' of R_G = " + ", ".join(f"{w:.2f}" for w in minR))
    return results


if __name__ == "__main__":
    part1_2_3(2, 3)
    part1_2_3(3, 3)
    part4(2, 3)
    part4(3, 3)
