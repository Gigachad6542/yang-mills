"""T80 part 5: where Proposition 64.3 loses, in the abelian Gaussian model.

Z = {c0}, c0 = (y0, last axis).  V^Z carries a unit flux on one coarse bond c'
(the situation of Part 4 of t80_abelian_fibre.py), V = V^Z + r e_{c0}.  The
transport of Theorem 64.2 is, in the abelian model, the shift sigma of the L^2
crossing links of c0 by r (q(sigma) = r e_{c0}; asserted).  All numbers are in
units of beta_N (beta_{N+1} = L beta_N), for the quantity

    Delta := [D_N(V) - D_N(V^Z)] / beta_N .

  exact      Delta = Q(V) - Q(V^Z) = r w^T V^Z + q r^2 / 2     (Gaussian fibre)
  Jensen     Delta_J = A_N(V) - A_N(V^Z) - L E_{mu_{V^Z}}[dA]   (eq. (7.1) of
             note 64); E[dA] is evaluated exactly (dA is quadratic and the
             fibre mean is the classical minimiser)
  loss       exact - Delta_J = (L/2) r^2 sigma^T C^T Sigma C sigma  >= 0
             (Sigma = beta * conditional covariance of the fine fluxes);
             asserted equal to the difference.
  Prop 64.3  RHS(7.2) with G_eta evaluated at the classical minimiser
             (E[G_eta] is only larger):
             -[(1+eta)L^2-1] A_Z(V) - L G_eta^cl.
"""
import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t80_abelian_fibre as ab  # noqa: E402
import t80_bloch_kernel as bk  # noqa: E402


def e_(mu):
    v = np.zeros(3, dtype=int)
    v[mu] = 1
    return v


def run(L, n, etas=(0.25, 0.5)):
    print(f"\n=== L = {L}, n = {n} ===")
    T, C, Q = ab.build(L, n)
    FS = ab.FibreSolver(T, C, Q)
    nc = Q.shape[0]
    M, _ = bk.M_from_bloch(L, n)
    Tc, dc, labels = bk.coarse_plaq_matrix(n)
    Dc = dc.T @ dc
    Qm = Dc - L * M
    y0 = (0, 0, 0)
    Z = {(y0, 2)}
    ci = T.bond_index[(y0, 2)]
    # the shift sigma of the crossing links of c0
    sigma = np.zeros(T.nl)
    for xi in itertools.product(range(L), repeat=2):
        x = np.array([L * y0[0] + xi[0], L * y0[1] + xi[1], L * y0[2] + L - 1])
        sigma[T.idx(x, 2)] = 1.0
    e = np.zeros(nc)
    e[ci] = 1.0
    assert np.abs(Q @ sigma - e).max() < 1e-12, "q(sigma) != e_c0"
    Csig = C @ sigma
    changed = np.nonzero(np.abs(Csig) > 1e-12)[0]
    # conditional covariance of the fine fluxes on the changed plaquettes
    CK = C @ FS.K
    Wt = (CK[changed] @ FS.Wp) / np.sqrt(FS.lam)
    Sig = Wt @ Wt.T
    # Part-4 style loop functionals
    typeA = ab.type_A_rows(T, y0, 2)
    corners = ab.corner_rows(T, C, Z)
    pZ = [(y, mu, nu) for y in itertools.product(range(n), repeat=3)
          for mu, nu in ((0, 1), (0, 2), (1, 2))
          if any(b in Z for b in ab.coarse_plaq_bonds(n, y, mu, nu))]
    near = np.array([any(b in Z for b in lab[3]) for lab in labels])
    dZ = dc[near]
    print(f"  {len(changed)} changed fine plaquettes (4 coarse plaquettes x L "
          f"layers = {4*L}); q = Qm_cc = {Qm[ci, ci]:.4f}")
    hdr = "  c'                r     exact   Jensen   loss   Prop64.3(eta=" + \
        ", ".join(str(x) for x in etas) + ")"
    print(hdr)
    for cp in [((0, 0, 0), 0), ((0, 0, 1), 1), ((1, 0, 0), 2)]:
        if cp == (y0, 2):
            continue
        Vp = np.zeros(nc)
        Vp[T.bond_index[cp]] = 1.0
        if 0.5 * np.sum((dZ @ Vp) ** 2) == 0:
            continue
        Acl = FS.solve(Vp)
        SA = sum((m @ Acl) ** 2 + (nn @ Acl) ** 2 for m, nn in typeA)
        Sk = sum(32 * sum(np.max((k @ Acl) ** 2) for k in cd["kap"])
                 for cd in corners)
        Sl = sum(8 * sum((lr @ Acl) ** 2 for lr in cd["Lam"]) for cd in corners)
        for r in (-1.0, -0.5, 0.5, 1.0):
            V = Vp + r * e
            exact = r * (Qm[:, ci] @ Vp) + 0.5 * Qm[ci, ci] * r * r
            AN = lambda W: 0.5 * W @ Dc @ W
            dA = float((C @ Acl) @ (r * Csig) + 0.5 * np.sum((r * Csig) ** 2))
            Jens = AN(V) - AN(Vp) - L * dA
            loss = 0.5 * L * r * r * (Csig[changed] @ Sig @ Csig[changed])
            assert abs(exact - (Jens + loss)) < 1e-9, (exact, Jens, loss)
            AZV = 0.5 * np.sum((dZ @ V) ** 2)
            P64 = []
            for eta in etas:
                G = SA + (1 + 1 / eta) * (Sk + Sl)
                P64.append(-((1 + eta) * L * L - 1) * AZV - L * G)
            print(f"  {str(cp):16s} {r:+.1f}  {exact:+8.4f} {Jens:+8.4f} "
                  f"{loss:7.4f}   " + "  ".join(f"{x:+10.2f}" for x in P64)
                  + f"    [A_Z(V) = {AZV:.3f}, A_Z(V^Z) = {0.5*np.sum((dZ@Vp)**2):.3f}]")


if __name__ == "__main__":
    run(2, 3)
    run(3, 3)
