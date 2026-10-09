"""T80 part 3: Bloch (Fourier) computation of the kernel M of A_min in the
abelian Gaussian fibre model, for any coarse torus size n.

A(L y + a, nu) = e^{i k.y} u(a, nu)  (y a coarse cell, a in [0,L)^3, k in
(2 pi/n) Z_n^3).  For each k the fine plaquette map C^(k) (3L^3 x 3L^3) and
the average q^(k) (3 x 3L^3) are the real-space matrices of t80_abelian_fibre
with every column weighted by e^{i k.(cell offset)}.  A_min is the Schur
complement M^(k) (3 x 3, Hermitian) of H^(k) = C^(k)+ C^(k) on {q^(k) u = v}:
no pseudo-inverse is used; the L^3 - 1 gauge zero modes per k are removed by
eigh and counted.

Outputs
  * check against the real-space M (t80_gaussian_Q) for (L, n) = (2, 3), (3, 3)
  * the sign of  Q^(k) = d^+ d - L M^(k)  (is Q <= 0 for all k, also k -> 0?)
  * the real-space kernel  M(r)  and the column  w = Qm e_c  on a large torus,
    and its exponential decay rate m_w;
  * the sup of  -Q/A_N  (Theorem 64.1: L^2 - 1)
"""
import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t80_abelian_fibre as ab  # noqa: E402


def stencils(L):
    """Real-space stencils: dict offset -> matrix, for Q (3 x m) and C (m x m),
    m = 3 L^3.  Offsets are cell offsets (column cell minus row cell)."""
    T = ab.AbTorus(L, 3)
    C = T.plaq_matrix()
    Q = T.q_matrix()
    s = T.s
    m = 3 * L ** 3

    def col_info(col):
        nu = col % 3
        r = col // 3
        x2 = r % s
        x1 = (r // s) % s
        x0 = r // (s * s)
        x = np.array([x0, x1, x2])
        y = x // L
        a = x % L
        return y, a, nu

    def aidx(a, nu):
        return ((int(a[0]) * L + int(a[1])) * L + int(a[2])) * 3 + nu

    def off(y, yrow):
        d = (y - yrow) % 3
        d = np.where(d == 2, -1, d)
        return tuple(int(c) for c in d)

    stQ, stC = {}, {}
    for mu in range(3):
        row = Q[T.bond_index[((0, 0, 0), mu)]]
        for col in np.nonzero(row)[0]:
            y, a, nu = col_info(col)
            o = off(y, np.zeros(3, int))
            stQ.setdefault(o, np.zeros((3, m)))[mu, aidx(a, nu)] += row[col]
    for a_r in itertools.product(range(L), repeat=3):
        for pl, (mu, nu) in enumerate(((0, 1), (0, 2), (1, 2))):
            r_ = T.plaq_index[(tuple(a_r), mu, nu)]
            ri = ((a_r[0] * L + a_r[1]) * L + a_r[2]) * 3 + pl
            for col in np.nonzero(C[r_])[0]:
                y, a, nu2 = col_info(col)
                o = off(y, np.zeros(3, int))
                stC.setdefault(o, np.zeros((m, m)))[ri, aidx(a, nu2)] += C[r_, col]
    return stQ, stC


def build_k(stQ, stC, ks):
    """ks: (K,3) momenta -> Qhat (K,3,m), Chat (K,m,m)."""
    K = ks.shape[0]
    m = next(iter(stC.values())).shape[0]
    Qh = np.zeros((K, 3, m), complex)
    Ch = np.zeros((K, m, m), complex)
    for o, mat in stQ.items():
        Qh += np.exp(1j * ks @ np.array(o))[:, None, None] * mat[None]
    for o, mat in stC.items():
        Ch += np.exp(1j * ks @ np.array(o))[:, None, None] * mat[None]
    return Qh, Ch


def Mhat(stQ, stC, L, ks, chunk=512):
    """M^(k) (3x3 Hermitian) for each k, by batched eigh."""
    out = []
    g = L ** 3 - 1
    gaps = []
    for i0 in range(0, ks.shape[0], chunk):
        k = ks[i0:i0 + chunk]
        Qh, Ch = build_k(stQ, stC, k)
        H = np.einsum("kba,kbc->kac", Ch.conj(), Ch)
        QQ = Qh @ np.swapaxes(Qh.conj(), 1, 2)
        Qpl = np.swapaxes(Qh.conj(), 1, 2) @ np.linalg.inv(QQ)    # Q^+(QQ^+)^-1
        w0, U0 = np.linalg.eigh(np.swapaxes(Qh.conj(), 1, 2) @ Qh)
        m = H.shape[-1]
        Kb = U0[:, :, :m - 3]
        assert np.abs(w0[:, :m - 3]).max() < 1e-9
        HK = np.swapaxes(Kb.conj(), 1, 2) @ H @ Kb
        lam, W = np.linalg.eigh(0.5 * (HK + np.swapaxes(HK.conj(), 1, 2)))
        assert np.abs(lam[:, :g]).max() < 1e-8, np.abs(lam[:, :g]).max()
        gaps.append(lam[:, g].min())
        assert lam[:, g].min() > 1e-6
        Wp = W[:, :, g:]
        lp = lam[:, g:]
        rhs = -np.swapaxes(Kb.conj(), 1, 2) @ H @ Qpl
        z = Wp @ ((np.swapaxes(Wp.conj(), 1, 2) @ rhs) / lp[:, :, None])
        S = Qpl + Kb @ z
        Mk = np.swapaxes(S.conj(), 1, 2) @ H @ S
        out.append(0.5 * (Mk + np.swapaxes(Mk.conj(), 1, 2)))
    return np.concatenate(out), min(gaps)


def dhat(ks):
    """Coarse plaquette map d^(k): (K, 3, 3): rows (01),(02),(12), cols mu."""
    K = ks.shape[0]
    z = np.exp(1j * ks)
    d = np.zeros((K, 3, 3), complex)
    for p, (mu, nu) in enumerate(((0, 1), (0, 2), (1, 2))):
        d[:, p, mu] = 1 - z[:, nu]
        d[:, p, nu] = z[:, mu] - 1
    return d


def Qhat(stQ, stC, L, ks):
    M, gap = Mhat(stQ, stC, L, ks)
    d = dhat(ks)
    D = np.swapaxes(d.conj(), 1, 2) @ d
    return D - L * M, D, M, gap


def kgrid(n):
    k1 = 2 * np.pi * np.arange(n) / n
    return np.array(list(itertools.product(k1, repeat=3)))


def realspace_from_bloch(Mk, n):
    """M[(y,mu),(y',nu)] = n^-3 sum_k e^{ik.(y-y')} Mk[k]_{mu nu}  (tested
    against the direct real-space matrix)."""
    k1 = np.arange(n)
    ks = kgrid(n)
    Mk = Mk.reshape(n, n, n, 3, 3)
    # m(r)_{mu nu} = n^-3 sum_k e^{ik.r} Mk_{mu nu}
    mr = np.fft.ifftn(Mk, axes=(0, 1, 2)) * 1.0      # numpy ifft: n^-1 sum e^{+i}
    return mr                                         # (n,n,n,3,3), index r



class BondLattice:
    """Light-weight stand-in for AbTorus on the coarse lattice only."""

    def __init__(self, n):
        self.n = n
        self.bond_index = {}
        for y in itertools.product(range(n), repeat=3):
            for mu in range(3):
                self.bond_index[(y, mu)] = ((y[0] * n + y[1]) * n + y[2]) * 3 + mu


def M_from_bloch(L, n, stencil_cache={}):
    """The real-space matrix M (3n^3 x 3n^3) of A_min on the n^3 coarse torus,
    from the Bloch decomposition (verified against the fine-lattice
    construction for n = 3 in the check above)."""
    if L not in stencil_cache:
        stencil_cache[L] = stencils(L)
    stQ, stC = stencil_cache[L]
    ks = kgrid(n)
    Mk, gap = Mhat(stQ, stC, L, ks)
    mr = realspace_from_bloch(Mk, n).real          # [r0,r1,r2,mu,nu]
    idx = np.arange(n)
    Y = np.array(list(itertools.product(range(n), repeat=3)))   # (n^3,3)
    diff = (Y[:, None, :] - Y[None, :, :]) % n                  # (N,N,3)
    blk = mr[diff[..., 0], diff[..., 1], diff[..., 2]]          # (N,N,3,3)
    N = n ** 3
    M = np.transpose(blk, (0, 2, 1, 3)).reshape(3 * N, 3 * N)
    return 0.5 * (M + M.T), gap


def coarse_plaq_matrix(n):
    """dc (3n^3 x 3n^3) and labels, same layout as t80_gaussian_Q.coarse_d."""
    T = BondLattice(n)
    rows, labels = [], []
    for y in itertools.product(range(n), repeat=3):
        for mu, nu in ((0, 1), (0, 2), (1, 2)):
            bonds = ab.coarse_plaq_bonds(n, y, mu, nu)
            r = np.zeros(3 * n ** 3)
            for sgn, b in zip((1, 1, -1, -1), bonds):
                r[T.bond_index[b]] += sgn
            rows.append(r)
            labels.append((y, mu, nu, bonds))
    return T, np.array(rows), labels

def check_vs_realspace():
    import t80_gaussian_Q as gq

    # ---- check against real space --------------------------------------
    for (L, n) in ((2, 3), (3, 3)):
        stQ, stC = stencils(L)
        T, C, Qr, FS, Mreal = gq.build_M(L, n)
        ks = kgrid(n)
        Mk, gap = Mhat(stQ, stC, L, ks)
        mr = realspace_from_bloch(Mk, n)
        # build the real-space matrix and compare
        nb = Mreal.shape[0]
        Mb = np.zeros((nb, nb))
        for y in itertools.product(range(n), repeat=3):
            for yp in itertools.product(range(n), repeat=3):
                r = tuple((np.array(y) - np.array(yp)) % n)
                blk = mr[r]
                for mu in range(3):
                    for nu in range(3):
                        Mb[T.bond_index[(y, mu)], T.bond_index[(yp, nu)]] = blk[mu, nu].real
        # the other sign convention
        Mb2 = np.zeros((nb, nb))
        for y in itertools.product(range(n), repeat=3):
            for yp in itertools.product(range(n), repeat=3):
                r = tuple((np.array(yp) - np.array(y)) % n)
                blk = mr[r]
                for mu in range(3):
                    for nu in range(3):
                        Mb2[T.bond_index[(y, mu)], T.bond_index[(yp, nu)]] = blk[mu, nu].real
        print(f"[check] L={L}, n={n}: Bloch gap {gap:.4f}; max|M_bloch - M_real| = "
              f"{np.abs(Mb - Mreal).max():.2e} (convention A), "
              f"{np.abs(Mb2 - Mreal).max():.2e} (convention B); "
              f"max imaginary part of the kernel {np.abs(mr.imag).max():.2e}")


def transverse_ratio(stQ, stC, L, ks):
    """Generalised eigenvalues of Q^(k) with respect to D^(k) on the two
    transverse polarisations (the gauge direction is the null vector of D)."""
    Qk, D, M, gap = Qhat(stQ, stC, L, ks)
    wD, UD = np.linalg.eigh(D)
    out = []
    for i in range(ks.shape[0]):
        Ut = UD[i, :, 1:]
        Dt = Ut.conj().T @ D[i] @ Ut
        Qt = Ut.conj().T @ Qk[i] @ Ut
        out.append(np.linalg.eigvals(np.linalg.solve(Dt, Qt)).real)
    return np.array(out), Qk, gap


def sign_and_decay():
    print("\n[sign of Q = A_N - L A_min, all momenta] Q^(k)/D^(k) on the transverse space")
    for L in (2, 3):
        stQ, stC = stencils(L)
        rng = np.random.default_rng(1)
        ks = rng.uniform(-np.pi, np.pi, size=(4000, 3))
        r, Qk, gap = transverse_ratio(stQ, stC, L, ks)
        print(f"  L={L}: 4000 random k: Q/A_N in [{r.min():.5f}, {r.max():.5f}]; "
              f"max eigenvalue of Q^(k) over all samples {np.linalg.eigvalsh(Qk).max():.1e} "
              f"(0 = the gauge direction); least gap of H_K {gap:.4f}; "
              f"Theorem 64.1: Q/A_N >= {-(L*L-1)}")
        corners = np.array(list(itertools.product((0.0, np.pi), repeat=3)))[1:]
        rc, _, _ = transverse_ratio(stQ, stC, L, corners)
        print(f"        at the 7 nonzero corners k in {{0,pi}}^3: Q/A_N = "
              + ", ".join(f"[{a:.5f},{b:.5f}]" for a, b in zip(rc.min(1), rc.max(1))))
        for dirn in ((1, 0, 0), (1, 1, 0), (1, 1, 1)):
            dv = np.array(dirn, float)
            dv /= np.linalg.norm(dv)
            vals = []
            for eps in (0.2, 0.1, 0.05):
                rr, _, _ = transverse_ratio(stQ, stC, L, (eps * dv)[None, :])
                vals.append(rr.max() / eps ** 2)
            print(f"        small k along {dirn}: max Q/A_N / |k|^2 = "
                  + ", ".join(f"{v:.5f}" for v in vals)
                  + f"   (limit {-(L-1)**2/L**3:.5f} = -(L-1)^2/L^3)")
    print("\n[decay of the kernel Qm(r), Chebyshev radius r; max over the shell]")
    for (L, n) in ((2, 24), (3, 12)):
        stQ, stC = stencils(L)
        ks = kgrid(n)
        Qk, D, M, gap = Qhat(stQ, stC, L, ks)
        q = np.fft.ifftn(Qk.reshape(n, n, n, 3, 3), axes=(0, 1, 2)).real
        rr = np.arange(n)
        rr = np.where(rr > n // 2, rr - n, rr)
        a = np.abs(rr)
        R = np.maximum(np.maximum(a[:, None, None], a[None, :, None]), a[None, None, :])
        prev = None
        rat = []
        print(f"  L={L}, n={n}:")
        for r in range(0, n // 2 + 1):
            v = np.abs(q[R == r]).max()
            ratio = v / prev if prev else float("nan")
            if r >= 3 and r <= n // 2 - 2:
                rat.append(ratio)
            print(f"      r={r:2d}: max|Qm(r)| = {v:.4e}   ratio {ratio:.4f}")
            prev = v
        mw = -np.log(np.mean(rat))
        print(f"      asymptotic ratio {np.mean(rat):.4f} -> decay rate m_w = {mw:.4f} per coarse unit; 2 m_w = {2*mw:.4f}")


if __name__ == "__main__":
    check_vs_realspace()
    sign_and_decay()
