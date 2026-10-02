"""T27: abelian 4D check of minimizer regularity (D2) of note 34.

Fine torus (Z/(n0*M))^4, M = L^m, Gaussian action ||dA||^2. The minimizer of
||dA||^2 with prescribed level-m block fluxes Phi_m (note 19 (2.1)) is the
Gaussian conditional mean E[F | Phi_m]. Its level-(m-1) block fluxes are

    Phi_{m-1} = G Phi_m,

with G a kernel that is translation invariant under level-m shifts. We
compute G exactly in Fourier space (alias sums, eigh pseudo-inverse) and
report

    S = max_{child offset u, orientation a} sum_{Y, b} |G_ab(u, Y)|,
    C_I = L^2 S,

so that |Phi_{m-1}|_inf <= C_I L^-2 |Phi_m|_inf. This is one valid
representation of the minimizer map on exact Phi_m, so S is an upper bound
for the best constant. (D2) asks C_I to be bounded uniformly in m; the chain
lemma of note 34 needs rho_L = L^2/(2 C_I) > 1.
"""

from __future__ import annotations

import itertools
import sys
import numpy as np

PLAQ = tuple((mu, nu) for mu in range(4) for nu in range(mu + 1, 4))


def dirichlet(q, M):
    q = np.asarray(q, dtype=float)
    den = 1.0 - np.exp(-1j * q)
    out = np.empty(q.shape, dtype=complex)
    reg = np.abs(den) >= 1e-13
    out[~reg] = M
    out[reg] = (1.0 - np.exp(-1j * M * q[reg])) / den[reg]
    return out


def what(p, M):
    """w_a(p) of note 19 (2.3) for all six orientations; p shape (4, N)."""
    d = [dirichlet(p[j], M) for j in range(4)]
    base = d[0] * d[1] * d[2] * d[3] / M**4
    return np.stack([base * d[mu] * d[nu] for mu, nu in PLAQ])  # (6, N)


def projector(p):
    """P_2(p), shape (6, 6, N)."""
    r = np.exp(1j * p) - 1.0
    r2 = np.sum(np.abs(r) ** 2, axis=0)
    E = np.zeros((6, 4, p.shape[1]), dtype=complex)
    for ia, (mu, nu) in enumerate(PLAQ):
        E[ia, nu] += r[mu]
        E[ia, mu] -= r[nu]
    safe = np.where(r2 > 1e-24, r2, 1.0)
    P = np.einsum("ajN,bjN->abN", E, E.conj()) / safe
    P[:, :, r2 <= 1e-24] = 0.0
    return P


def pinv_h(C, rel=1e-9, absolute=1e-14):
    w, V = np.linalg.eigh(C)
    keep = (w > rel * w.max()) & (w > absolute)
    return (V[:, keep] / w[keep]) @ V[:, keep].conj().T


def kernel(L, m, n0):
    M = L**m
    M1 = M // L
    ells = np.array(list(itertools.product(range(M), repeat=4))).T  # (4, M^4)
    child = ells % L  # child index l' of each alias
    child_id = ((child[0] * L + child[1]) * L + child[2]) * L + child[3]
    offs = np.array(list(itertools.product(range(L), repeat=4))).T  # (4, L^4)
    nK = n0**4
    H = np.zeros((L**4, n0, n0, n0, n0, 6, 6), dtype=complex)
    for kidx in itertools.product(range(n0), repeat=4):
        K = 2 * np.pi * np.array(kidx, dtype=float) / n0
        p = (K[:, None] + 2 * np.pi * ells) / M
        wM = what(p, M)
        wM1 = what(p, M1) if M1 > 1 else np.ones((6, p.shape[1]), dtype=complex)
        P = projector(p)
        cov = np.einsum("aN,abN,bN->ab", wM.conj(), P, wM) / M**8
        cinv = pinv_h(cov)
        cross_terms = np.einsum("aN,abN,bN->abN", wM1.conj(), P, wM) / (M1**4 * M**4)
        B = np.zeros((L**4, 6, 6), dtype=complex)
        np.add.at(B, child_id, np.moveaxis(cross_terms, 2, 0))
        B = B @ cinv  # (L^4 children, 6, 6)
        # H_u(K) = L^-4 sum_l' exp(i (K + 2 pi l') . u / L) B_l'(K)
        Kp = (K[:, None] + 2 * np.pi * offs) / L  # child momenta, (4, L^4)
        phase = np.exp(1j * (offs.T @ Kp))  # [u, l']
        H[(slice(None),) + kidx] = np.einsum("ul,lab->uab", phase, B) / L**4
    G = np.fft.ifftn(H, axes=(1, 2, 3, 4))
    return G


def report(L, m, n0, delta=0.0):
    G = kernel(L, m, n0)
    imag = np.abs(G.imag).max()
    A = np.abs(G.real)
    if delta:
        idx = np.arange(n0)
        dist = np.minimum(idx, n0 - idx)
        D = np.maximum.reduce(np.meshgrid(dist, dist, dist, dist, indexing="ij"))
        A = A * np.exp(delta * D)[None, :, :, :, :, None, None]
    rows = A.sum(axis=(1, 2, 3, 4, 6))  # (u, a)
    S = rows.max()
    # tail: fraction of row mass at coarse distance >= n0//2 - 1
    return S, L**2 * S, imag


if __name__ == "__main__":
    cases = [(2, 1, 8), (2, 2, 8), (2, 3, 6), (3, 1, 8), (3, 2, 6), (2, 2, 10)]
    for L, m, n0 in cases:
        S, CI, im = report(L, m, n0)
        Sd, CId, _ = report(L, m, n0, delta=0.5)
        print(f"L={L} m={m} n0={n0}: S={S:.5f}  C_I=L^2 S={CI:.4f}  "
              f"rho_L=L^2/(2C_I)={L**2/(2*CI):.4f}  "
              f"weighted(delta=.5) C_I={CId:.4f}  max|imag|={im:.1e}", flush=True)


# ---------------------------------------------------------------------------
# Norm restricted to exact coarse fluxes: l1-minimal extension (LP).
# Functionals vanishing on exact 2-forms of the coarse torus are
# Phi -> <c, d'Phi> + sum_b h_b sum_Y Phi_b(Y).  The operator norm of a row g on
# exact Phi in the sup norm is min_{c,h} ||g - d'^T c - h||_1.

TRIP = tuple(t for t in itertools.combinations(range(4), 3))


def bianchi_matrix(n0):
    import scipy.sparse as sp
    N = n0**4
    idx = np.arange(N).reshape((n0,) * 4)
    rows, cols, vals = [], [], []
    pl = {a: i for i, a in enumerate(PLAQ)}
    for it, (l, mu, nu) in enumerate(TRIP):
        # (d'Phi)_{l mu nu} = d_l Phi_{mu nu} - d_mu Phi_{l nu} + d_nu Phi_{l mu}
        for sign, dirn, a in ((1, l, (mu, nu)), (-1, mu, (l, nu)), (1, nu, (l, mu))):
            ia = pl[a]
            shifted = np.roll(idx, -1, axis=dirn)  # Y + e_dirn
            r = it * N + idx.ravel()
            rows += [r, r]
            cols += [ia * N + shifted.ravel(), ia * N + idx.ravel()]
            vals += [np.full(N, sign, float), np.full(N, -sign, float)]
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                         shape=(4 * N, 6 * N))


def exact_norm(g, n0, Dm=None):
    """min ||g - D^T c - h||_1 over 3-forms c and per-orientation constants h."""
    import scipy.sparse as sp
    from scipy.optimize import linprog
    N = n0**4
    if Dm is None:
        Dm = bianchi_matrix(n0)
    nphi = 6 * N
    H = sp.kron(sp.eye(6), np.ones((N, 1)))  # (6N, 6)
    Amat = sp.hstack([Dm.T, H]).tocsr()  # residual = g - Amat z
    nz = Amat.shape[1]
    I = sp.eye(nphi)
    # variables [z (free), t (>=0)]:  g - Az <= t,  -(g - Az) <= t
    A_ub = sp.vstack([sp.hstack([-Amat, -I]), sp.hstack([Amat, -I])]).tocsr()
    b_ub = np.concatenate([-g, g])
    cost = np.concatenate([np.zeros(nz), np.ones(nphi)])
    bounds = [(None, None)] * nz + [(0, None)] * nphi
    res = linprog(cost, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")
    return res.fun, res.status


def exact_report(L, m, n0, rows=None):
    """Exact-restricted row norms; rows = list of (u_index, a) or None for all."""
    G = kernel(L, m, n0).real  # (u, Y0..Y3, a, b)
    Dm = bianchi_matrix(n0)
    out = []
    targets = rows if rows is not None else [(u, a) for u in range(L**4) for a in range(6)]
    for u, a in targets:
        g = np.moveaxis(G[u, :, :, :, :, a, :], -1, 0)  # (b, Y) ; G maps Phi(Y_0 - D)
        # G[u, D, a, b] multiplies Phi_b(Y0 - D); reindex to Phi_b(Y) at Y0 = 0.
        g = g[:, (-np.arange(n0)) % n0][:, :, (-np.arange(n0)) % n0][:, :, :, (-np.arange(n0)) % n0][:, :, :, :, (-np.arange(n0)) % n0]
        val, st = exact_norm(g.reshape(-1), n0, Dm)
        out.append((u, a, val, st, np.abs(g).sum()))
    return out
