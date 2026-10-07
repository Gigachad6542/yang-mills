"""T68: two-scale convergence of the induced coarse kernel of G_M = (Lambda_M + a w w^*)^{-1}.

Alias model of note 41 section 5: for coarse momentum K the fine alias space
is C^{B_M}, Lambda_M = diag(lam_M(n)), lam_M = sum_j (2M sin(q_j/2M))^2,
q = K + 2 pi n, w_M(n) = prod_j Phi_M(q_j)^{e_j},
Phi_M(q) = (1/M) sum_{s<M} e^{-i q s/M}.
Prints sup_K |Xi_M - Xi_2M| for pairings Xi = <u, G_M v>, and the Laplacian
resolvent gap sup_n |1/lam_M - 1/lam_inf|.  G_M is built from numpy.linalg.eigh
(dense) and from the Schur-complement formula of note 41 section 5; the two
agree.  No pseudoinverse is used.
"""
import itertools
import numpy as np


def window(Kj, M):
    lo = int(np.ceil((-np.pi * M - Kj) / (2 * np.pi) + 1e-12))
    ns = np.arange(lo, lo + M)
    q = Kj + 2 * np.pi * ns
    assert np.all(q > -np.pi * M - 1e-9) and np.all(q <= np.pi * M + 1e-9)
    return ns, q


def Phi(q, M):
    s = np.arange(M)
    return np.exp(-1j * np.outer(q, s) / M).sum(axis=1) / M


def build(K, M, e):
    d = len(K)
    qs, ph = [], []
    for j in range(d):
        ns, q = window(K[j], M)
        qs.append(q)
        ph.append(Phi(q, M) ** e[j])
    grids = np.meshgrid(*qs, indexing="ij")
    lam = sum((2 * M * np.sin(g / (2 * M))) ** 2 for g in grids).ravel()
    w = ph[0]
    for j in range(1, d):
        w = np.multiply.outer(w, ph[j])
    qn = sum(g ** 2 for g in grids).ravel()
    return lam, w.ravel(), int(np.argmin(qn))


def pairings_dense(K, M, a, e1, e2):
    lam, w1, i0 = build(K, M, e1)
    _, w2, _ = build(K, M, e2)
    Km = np.diag(lam).astype(complex) + a * np.outer(w1, w1.conj())
    mu, V = np.linalg.eigh(Km)
    assert mu.min() > 0
    G = (V / mu) @ V.conj().T
    return np.array([w1.conj() @ G @ w1, w1.conj() @ G @ w2, G[i0, i0]])


def pairings_schur(K, M, a, e1, e2):
    lam, w1, i0 = build(K, M, e1)
    _, w2, _ = build(K, M, e2)
    m = np.ones(lam.size, bool)
    m[i0] = False
    lp, wp, w0 = lam[m], w1[m], w1[i0]
    tau = a * np.sum(np.abs(wp) ** 2 / lp)
    s = lam[i0] + a * abs(w0) ** 2 / (1 + tau)
    y = wp / lp
    Sib = a * np.conj(w0) * y / (1 + tau)  # S^{-1} b

    def pair(u, v):
        up, vp, u0, v0 = u[m], v[m], u[i0], v[i0]
        Siv = np.sum(up.conj() * vp / lp) - a * np.vdot(up, y) * np.vdot(y, vp) / (1 + tau)
        cu = np.vdot(Sib, up)
        cv = np.vdot(Sib, vp)
        return (np.conj(u0) * v0 - np.conj(u0) * cv - np.conj(cu) * v0) / s + Siv + np.conj(cu) * cv / s

    e0 = np.zeros(lam.size, complex)
    e0[i0] = 1
    return np.array([pair(w1, w1), pair(w1, w2), pair(e0, e0)])


if __name__ == "__main__":
    a = 1.0
    print("== Laplacian resolvent gap (d=1, K=pi): sup_{n!=0} |1/lam_M - 1/lam_inf| ==")
    for M in (4, 8, 16, 32, 64, 128):
        ns, q = window(np.pi, M)
        keep = np.abs(q) > 1e-9
        lm = (2 * M * np.sin(q[keep] / (2 * M))) ** 2
        gap = np.max(np.abs(1 / lm - 1 / q[keep] ** 2))
        print(f"M={M:4d}  gap={gap:.3e}  gap*M^2={gap*M*M:.3f}")
    print("== Schur formula vs dense eigh ==")
    for d, M in ((2, 8), (2, 16), (4, 4), (4, 6)):
        K = np.array([0.7, 2.9, -1.3, 0.2][:d])
        for e1, e2 in (((1,) * d, (2,) * d), ((1,) * d, (1,) * d)):
            A = pairings_dense(K, M, a, e1, e2)
            B = pairings_schur(K, M, a, e1, e2)
            print(f"d={d} M={M} e={e1[0]},{e2[0]}: max|dense-schur| = {np.max(np.abs(A-B)):.2e}")
    for d, Ms, vals in ((2, (2, 4, 8, 16, 32, 64), np.linspace(-np.pi, np.pi, 5)),
                        (4, (2, 4, 8, 16, 32), np.array([0.9, 2.2, -1.4]))):
        print(f"== d={d}: sup_K |Xi_M - Xi_2M|, Xi = (<w1,G w1>, <w1,G w2>, G_00), a={a} ==")
        Ks = [np.array(k) for k in itertools.product(vals, repeat=d)]
        prev, pd = None, None
        for M in Ms:
            cur = [pairings_schur(K, M, a, (1,) * d, (2,) * d) for K in Ks]
            if prev is not None:
                dd = np.max([np.abs(x - y) for x, y in zip(cur, prev)], axis=0)
                msg = f"M={M//2:3d}->{M:3d}: " + "  ".join(f"{v:.3e}" for v in dd)
                if pd is not None:
                    msg += "   ratios " + " ".join(f"{p/v:.2f}" for p, v in zip(pd, dd))
                print(msg, flush=True)
                pd = dd
            prev = cur
