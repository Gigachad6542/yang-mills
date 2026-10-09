"""T80 part 4: how (R) fails in the abelian Gaussian model, and the corrected
Z-local form with an exponentially decaying tail.

Single coarse bond Z = {c}.  Write t = V_c, V^Z = V - t e_c, w = Qm e_c
(the column of the quadratic form Q(V) = (1/2) V^T Qm V), q = Qm_cc < 0.
Then, exactly,

    D(V) := Q(V) - Q(V^Z) = t w^T V^Z + (1/2) q t^2 .

On ker(A_Z) (the 4 coarse plaquettes at c flat in V) w^T V^Z = ell(theta_far),
a linear functional of the far fluxes theta_far = (flux of V off the
plaquettes touching c), independent of the gauge, and t is a free gauge
parameter, so

    inf_t D = - ell(theta_far)^2 / (2 |q|)  <  0   unless ell = 0.

The script computes, on the n^3 torus built from the Bloch kernel:
  1. kappa(r) = sup  -D / A_flux  over V in ker(A_Z) with all flux at
     Chebyshev distance >= r from c  (the violation per unit of far flux
     energy), by a generalised eigenvalue problem;
  2. ell_* = sup { w^T V : V_c = 0, near flux = 0, |theta_x| <= 1 for the far
     plaquettes } (a linear programme), and the small-field loss
     Lambda = ell_*^2 / (2|q|):  for |theta_x| <= p/sqrt(beta) at all far
     plaquettes,   beta * D >= - Lambda p^2;
  3. the corrected inequality   D + C A_Z + C_T T_m >= 0  with
     T_m(V) = (1/2) sum_{x far} e^{-m d(x,Z)} theta_x(V)^2:
     the least C_T for several (m, C), and the near constant C_0 = |q|/4.
"""
import itertools
import os
import sys
import time

import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t80_abelian_fibre as ab  # noqa: E402
import t80_bloch_kernel as bk  # noqa: E402
import t80_gaussian_Q as gq  # noqa: E402


def e_(mu):
    v = np.zeros(3, dtype=int)
    v[mu] = 1
    return v


def setup(L, n, Z):
    T, dc, labels = bk.coarse_plaq_matrix(n)
    M, gap = bk.M_from_bloch(L, n)
    Dc = dc.T @ dc
    Qm = Dc - L * M
    nb = Dc.shape[0]
    near = np.array([any(b in Z for b in lab[3]) for lab in labels])
    dist = gq.dist_plaq_bond(n, labels, Z)
    P = np.eye(nb)
    for b in Z:
        P[T.bond_index[b], T.bond_index[b]] = 0.0
    Dd = Qm - P.T @ Qm @ P
    Dd = 0.5 * (Dd + Dd.T)
    dZ = dc[near]
    Dz = dZ.T @ dZ
    return dict(L=L, n=n, T=T, dc=dc, labels=labels, M=M, Dc=Dc, Qm=Qm, Dd=Dd,
                Dz=Dz, near=near, dist=dist, nb=nb, Z=Z)


def part_kappa(S, rs):
    dc, dist, Dd, near = S["dc"], S["dist"], S["Dd"], S["near"]
    out = []
    for rr in rs:
        mask = dist < rr - 1e-9
        rows = dc[mask]
        Nr, _ = gq.nullspace_eigh(rows.T @ rows)
        X = Nr.T @ Dd @ Nr
        A = Nr.T @ S["Dc"] @ Nr
        kap = gq.min_ratio(X, A)
        out.append((rr, -kap))
    return out


def part_lp(S):
    """ell_* by linear programming."""
    Z = next(iter(S["Z"]))
    n, T, dc, near = S["n"], S["T"], S["dc"], S["near"]
    nb = S["nb"]
    ci = T.bond_index[Z]
    w = S["Qm"][:, ci]
    q = w[ci]
    far = ~near
    A_eq = [dc[near]]
    b_eq = [np.zeros(near.sum())]
    e = np.zeros((1, nb))
    e[0, ci] = 1.0
    A_eq.append(e)
    b_eq.append(np.zeros(1))
    A_eq = np.vstack(A_eq)
    b_eq = np.concatenate(b_eq)
    Fm = dc[far]
    A_ub = np.vstack([Fm, -Fm])
    b_ub = np.ones(A_ub.shape[0])
    res = linprog(-w, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                  bounds=[(-1e3, 1e3)] * nb, method="highs")
    assert res.status == 0, res.message
    ell = -res.fun
    return ell, q, res.x


def part_tail(S, ms, Cs):
    dc, dist, near, Dd, Dz = S["dc"], S["dist"], S["near"], S["Dd"], S["Dz"]
    rows = []
    for m in ms:
        wts = np.where(near, 0.0, np.exp(-m * dist))
        Tm = dc.T @ (wts[:, None] * dc)
        for C in Cs:
            kap = gq.min_ratio(Dd + C * Dz, Tm)
            rows.append((m, C, -kap if np.isfinite(kap) else np.inf))
    return rows


def run(L, n, Z, rs, ms, Cs, label):
    t0 = time.time()
    S = setup(L, n, Z)
    ci = S["T"].bond_index[sorted(Z)[0]]
    q = S["Qm"][ci, ci]
    print(f"\n--- L={L}, n={n}, Z = {label}: Qm_cc = q = {q:.5f}, "
          f"C_0(1 bond) = |q|/4 = {abs(q)/4:.5f}  (setup {time.time()-t0:.1f}s)")
    ev = np.linalg.eigvalsh(S["Qm"])
    print(f"    Q <= 0 on this torus: max eig Qm = {ev[-1]:.2e}")
    kap = part_kappa(S, rs)
    print("    violation per unit far-flux energy,  kappa(r) = sup -D/A_flux "
          "(flux at distance >= r):")
    prev = None
    for rr, k in kap:
        rat = f"  ratio {k/prev:.4f}" if prev and prev > 1e-12 and k > 1e-14 else ""
        print(f"        r >= {rr:4.1f}: kappa = {k:.5e}{rat}")
        prev = k
    if len(Z) == 1:
        ell, q2, _ = part_lp(S)
        print(f"    LP: ell_* = sup w^T V (|theta_far| <= 1, near flux 0, V_c = 0) = "
              f"{ell:.5f};  small-field loss Lambda = ell_*^2/(2|q|) = "
              f"{ell**2/(2*abs(q)):.5f}   [beta*D >= -Lambda p^2 when "
              f"beta*theta_x^2 <= p^2 at every far plaquette]")
    rows = part_tail(S, ms, Cs)
    print("    least C_T with  D + C A_Z + C_T T_m >= 0   (T_m weight e^{-m d}):")
    print("        m \\ C   " + "  ".join(f"{C:10.2f}" for C in Cs))
    for m in ms:
        print(f"        {m:5.2f}  " + "  ".join(
            f"{r[2]:10.4f}" for r in rows if r[0] == m))
    return S


def explicit_example(L, n=16):
    """The simplest explicit violation of (R).  Z = {c}, c = ((0,0,0), axis 2).
    V = e_b + t * d(lambda), lambda = delta at the head vertex of c, b a coarse
    bond that shares no plaquette with c.  Then t = V_c, the four coarse
    plaquettes at c are flat in V (A_Z(V) = 0), V^Z = V - t e_c and, exactly,
        D(V) = Q(V) - Q(V^Z) = (1/2)|q| t^2 + t Q_bc ,   q = Q_cc < 0,
    so  min_t D = - Q_bc^2 / (2|q|)  at  t = -Q_bc/|q|.  Q_bc is read off the
    Bloch kernel on the n^3 torus."""
    stQ, stC = bk.stencils(L)
    ks = bk.kgrid(n)
    Qk, D, M, gap = bk.Qhat(stQ, stC, L, ks)
    q = np.fft.ifftn(Qk.reshape(n, n, n, 3, 3), axes=(0, 1, 2)).real
    c = ((0, 0, 0), 2)
    qcc = q[0, 0, 0, 2, 2]
    # bonds sharing a plaquette with c
    share = set()
    for y in itertools.product(range(n), repeat=3):
        for mu, nu in ((0, 1), (0, 2), (1, 2)):
            bs = ab.coarse_plaq_bonds(n, y, mu, nu)
            if c in bs:
                share.update(bs)
    rr = lambda v: min(v, n - v)
    best = {}
    for y in itertools.product(range(n), repeat=3):
        for mu in range(3):
            b = (y, mu)
            if b in share:
                continue
            cheb = max(rr(int(v) % n) for v in y)
            Qbc = q[y[0] % n, y[1] % n, y[2] % n, mu, 2]
            if cheb not in best or abs(Qbc) > abs(best[cheb][0]):
                best[cheb] = (Qbc, b)
    print(f"\n[explicit counterexample, L={L}] q = Q_cc = {qcc:.5f}; "
          f"V = e_b + t d(lambda_head(c)), A_Z(V) = 0, min_t D = -Q_bc^2/(2|q|):")
    for cheb in sorted(best):
        if cheb < 1 or cheb > 6:
            continue
        Qbc, b = best[cheb]
        print(f"    b at Chebyshev distance {cheb} from c, best b = {b}: Q_bc = "
              f"{Qbc:+.6f}, t* = {-Qbc/abs(qcc):+.6f}, min D = "
              f"{-Qbc**2/(2*abs(qcc)):+.3e}")
    return best


def verify_formula(L, n):
    """Exact identities on the full quadratic forms, for random V:
      (i)  D(V) = t w^T V^Z + (1/2) q t^2           (all V; V^Z = V - t e_c)
      (ii) on ker(A_Z):  D(V) = (1/2)|q| t^2 + t w^T V ."""
    Z = {((0, 0, 0), 2)}
    S = setup(L, n, Z)
    ci = S["T"].bond_index[next(iter(Z))]
    w = S["Qm"][:, ci]
    q = w[ci]
    rng = np.random.default_rng(7)
    e1 = e2 = 0.0
    Nz, _ = gq.nullspace_eigh(S["Dz"])
    for _ in range(20):
        V = rng.normal(size=S["nb"])
        t = V[ci]
        V0 = V.copy()
        V0[ci] = 0.0
        D = 0.5 * V @ S["Dd"] @ V
        e1 = max(e1, abs(D - (t * (w @ V0) + 0.5 * q * t * t)))
        V = Nz @ rng.normal(size=Nz.shape[1])
        t = V[ci]
        D = 0.5 * V @ S["Dd"] @ V
        e2 = max(e2, abs(D - (0.5 * abs(q) * t * t + t * (w @ V))))
    print(f"[formula] L={L}, n={n}: max error of (i) {e1:.2e}, of (ii) {e2:.2e} "
          f"(20 random V each); q = {q:.5f}")


def explicit_constants(L, n, ms):
    """The constants of the proved inequality (Proposition 67.5), Z = {c}:
        D(V) >= - C_near A_Z(V) - C_T T_m(V),
        C_near = 2 |u_near|^2 / |q|,   C_T = 2 sum_far u_x^2 e^{m d_x} / |q|,
    where u is the flux-space representative of w = Qm e_c (dc^T u = w) that
    minimises sum_x e^{m d_x} u_x^2 (weighted minimum-norm solution, eigh)."""
    Z = {((0, 0, 0), 2)}
    S = setup(L, n, Z)
    ci = S["T"].bond_index[next(iter(Z))]
    w = S["Qm"][:, ci]
    q = w[ci]
    dc, dist, near = S["dc"], S["dist"], S["near"]
    out = []
    for m in ms:
        W = np.exp(m * dist)
        G = dc.T @ (dc / W[:, None])
        ev, U = np.linalg.eigh(0.5 * (G + G.T))
        pos = ev > 1e-9
        x = U[:, pos] @ ((U[:, pos].T @ w) / ev[pos])
        assert np.abs(U[:, ~pos].T @ w).max() < 1e-9      # w orthogonal to ker d
        u = (dc @ x) / W
        assert np.abs(dc.T @ u - w).max() < 1e-9
        Cn = 2 * np.sum(u[near] ** 2) / abs(q)
        CT = 2 * np.sum(u[~near] ** 2 * np.exp(m * dist[~near])) / abs(q)
        out.append((m, Cn, CT))
    print(f"[explicit constants, L={L}, n={n}]  (C_near, C_T) for m = "
          + ", ".join(f"{m}: ({Cn:.3f}, {CT:.3f})" for m, Cn, CT in out)
          + f";  C_0 = |q|/4 = {abs(q)/4:.4f}"
          + ";  N_m = sum_far exp(-m d) = "
          + ", ".join(f"{m}: {np.exp(-m*dist[~near]).sum():.2f}" for m in ms))
    return out


def brute_force_counterexample(L, n):
    """Independent check of the explicit counterexample with the fine-lattice
    solver of t80_abelian_fibre (no Schur complement, no Bloch kernel):
    V = e_b + t dlambda, b = next bond on the line of c, c = ((0,0,0),2).
    D(V) = [A_N(V) - L A_min(V)] - [A_N(V^Z) - L A_min(V^Z)] with A_min from the
    constrained classical minimiser of the fine action."""
    T, C, Q = ab.build(L, n)
    FS = ab.FibreSolver(T, C, Q)
    Tc, dc, labels = bk.coarse_plaq_matrix(n)
    nb = dc.shape[1]
    c = ((0, 0, 0), 2)
    head = (0, 0, 1)
    b = (head, 2)
    ci = T.bond_index[c]
    lam = np.zeros(nb)
    for mu in range(3):
        yb = tuple((np.array(head) - e_(mu)) % n)
        lam[T.bond_index[(yb, mu)]] += 1.0       # (d lambda)(y, mu) = lambda(y+e_mu) - lambda(y)
        lam[T.bond_index[(head, mu)]] -= 1.0
    assert lam[ci] == 1.0 and np.abs(dc @ lam).max() < 1e-12
    eb = np.zeros(nb)
    eb[T.bond_index[b]] = 1.0

    def Qf(V):
        Acl = FS.solve(V)
        return 0.5 * np.sum((dc @ V) ** 2) - L * 0.5 * np.sum((C @ Acl) ** 2)

    near = np.array([c in lab[3] for lab in labels])
    res = []
    for t in (-0.4, -0.2, 0.0, 0.1, 0.3):
        V = eb + t * lam
        VZ = V.copy()
        VZ[ci] = 0.0
        AZ = 0.5 * np.sum((dc[near] @ V) ** 2)
        res.append((t, AZ, Qf(V) - Qf(VZ)))
    # formula from the Schur complement of the same torus
    M, _ = bk.M_from_bloch(L, n)
    Qm = dc.T @ dc - L * M
    q = Qm[ci, ci]
    Qbc = Qm[T.bond_index[b], ci]
    print(f"[brute force, L={L}, n={n}] q = {q:.5f}, Q_bc = {Qbc:.5f}; "
          f"D(t) = (1/2)|q|t^2 + t Q_bc against the fine-lattice solver:")
    for t, AZ, D in res:
        print(f"    t = {t:+.2f}: A_Z(V) = {AZ:.1e}, D(V) = {D:+.6f}, "
              f"formula {0.5*abs(q)*t*t + t*Qbc:+.6f}")
    tstar = -Qbc / abs(q)
    print(f"    t* = {tstar:+.5f}: D = {-Qbc**2/(2*abs(q)):+.5f}")


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "n12":
    # slow (about 8 minutes): the explicit constants of Proposition 67.5 at n = 12
    explicit_constants(2, 12, (0.0, 1.0, 2.0, 3.0))
elif __name__ == "__main__":
    brute_force_counterexample(2, 4)
    brute_force_counterexample(3, 3)
    verify_formula(2, 4)
    verify_formula(3, 4)
    explicit_example(2)
    explicit_example(3, 12)
    for (L, n) in ((2, 6), (2, 8), (3, 6), (3, 8)):
        explicit_constants(L, n, (0.0, 1.0, 2.0, 3.0))
    y0 = (0, 0, 0)
    Zs = {((y0, 2),): "one last-axis bond"}
    for (L, n, ms, Cs) in ((2, 6, (0.0, 1.0, 2.0, 3.0, 3.4, 3.8),
                            (1.43, 1.5, 2.0, 3.0, 6.0, 20.0)),
                           (2, 8, (0.0, 1.0, 2.0, 3.0, 3.4, 3.8),
                            (1.43, 1.5, 2.0, 3.0, 6.0, 20.0)),
                           (3, 6, (0.0, 1.0, 2.0, 3.0, 3.4),
                            (2.2, 3.0, 5.0, 8.0, 20.0)),
                           (3, 8, (0.0, 1.0, 2.0, 3.0, 3.4),
                            (2.2, 3.0, 5.0, 8.0, 20.0))):
        rs = [1.0 + 0.5 * i for i in range(0, 2 * (n // 2) - 1)]
        run(L, n, {(y0, 2)}, rs, ms, Cs, "{(0,0,0) last axis}")
        if n == 8:
            run(L, n, {(y0, 2), ((0, 0, 1), 2)}, rs, ms, Cs,
                "two collinear last-axis bonds")
