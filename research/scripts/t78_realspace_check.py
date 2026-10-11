"""T78 real-space check (note 61 section 6d): on a small torus, the fibre
minimum (6c.1) computed by brute-force linear algebra equals the Fourier
(aliasing) formula of t76/t78, including the factor L per step.

Fine torus (Z/n)^3, n = n_c L (one block step, j = 1).  Plaquette fields
B_a(x) (3 per site, B = curl A with forward differences, Bianchi
sum_a (B_a(x+e_a) - B_a(x)) = 0).  Level-N form H with symbol
H(p) = (1-s) P(p) + s Pi_1(p) on the transverse space (zero elsewhere).  The
coarse kernel is  w_a(x) = b(x_a) prod_{i != a} (b*s)(x_i),  (wB)_a(Y) = sum_x w_a(x-Y) B_a(x), Y in L Z^3.

Definition checked:  Pi(Phi) = L * min { B^T H B : B in ran d, w B = Phi }.
(a) fibre minimum by the null-space method for random closed Phi,
(b) the pseudo-inverse formula  L (w H^+ w^T)^+,
(c) the spectrum of the coarse symbol Pi(K) from t78_kernel_decay (Fourier),
at every coarse momentum K != 0.
"""
import sys, itertools, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from t78_kernel_decay import Pi, P_of, Pi1_of, r_of


def build(L, nc):
    n = nc*L
    sites = list(itertools.product(range(n), repeat=3))
    sid = {x: i for i, x in enumerate(sites)}
    N3 = n**3
    def sh(x, a, k=1):
        y = list(x); y[a] = (y[a]+k) % n; return tuple(y)
    # d: links (a,x) -> plaquettes (j,x): B_j = eps_{jkl} (A_l(x+e_k) - A_l(x))
    d = np.zeros((3*N3, 3*N3))
    eps = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
    for (j, k, l), e in eps.items():
        for x in sites:
            row = j*N3 + sid[x]
            d[row, l*N3 + sid[sh(x, k)]] += e
            d[row, l*N3 + sid[x]] -= e
    # w: fine plaquettes -> coarse plaquettes
    b = np.ones(L)/L; s = np.ones(L); bs = np.convolve(b, s)       # supports 0..L-1, 0..2L-2
    ys = list(itertools.product(range(nc), repeat=3))
    yid = {y: i for i, y in enumerate(ys)}
    w = np.zeros((3*nc**3, 3*N3))
    for a in range(3):
        for y in ys:
            row = a*nc**3 + yid[y]
            for t in itertools.product(range(2*L-1), repeat=3):
                coef = (b[t[a]] if t[a] < L else 0.0)
                for i in range(3):
                    if i != a:
                        coef *= bs[t[i]]
                if coef == 0.0:
                    continue
                x = tuple((L*y[i] + t[i]) % n for i in range(3))
                w[row, a*N3 + sid[x]] += coef
    return n, sites, sid, d, w, ys, yid


def fine_operator(L, n, s, sites, sid):
    a = 2*np.pi*np.arange(n)/n
    Kg = np.stack(np.meshgrid(a, a, a, indexing='ij'), axis=-1).reshape(-1, 3)
    sym = (1-s)*P_of(Kg)
    if s != 0.0:
        sym = sym + s*Pi1_of(Kg, L)
    sym[(np.abs(r_of(Kg)).sum(-1) < 1e-12)] = 0.0
    sym = sym.reshape(n, n, n, 3, 3)
    ker = np.fft.ifftn(sym, axes=(0, 1, 2))
    N3 = n**3
    X = np.array(sites)                                          # (N3,3)
    D = (X[:, None, :] - X[None, :, :]) % n                      # (N3,N3,3)
    H = np.zeros((3*N3, 3*N3), dtype=complex)
    for a_ in range(3):
        for b_ in range(3):
            H[a_*N3:(a_+1)*N3, b_*N3:(b_+1)*N3] = ker[D[..., 0], D[..., 1], D[..., 2], a_, b_]
    return H


def run(L, nc, svals=(0.0, 0.5, 1.0)):
    n, sites, sid, d, w, ys, yid = build(L, nc)
    N3 = n**3
    print(f"L={L} n_c={nc} fine torus {n}^3: {3*N3} plaquette dofs, {3*nc**3} coarse")
    U, sv, Vt = np.linalg.svd(d)
    rk = int((sv > 1e-9).sum()); Ub = U[:, :rk]                  # orthonormal basis of ran d
    print(f"  rank d = {rk}")
    rng = np.random.default_rng(0)
    for s in svals:
        H = fine_operator(L, n, s, sites, sid)
        Hr = (H + H.conj().T)/2
        Hr = Hr.real if np.abs(Hr.imag).max() < 1e-10 else Hr
        # (a) null-space method
        Hc = Ub.T @ Hr @ Ub
        G = w @ Ub                                               # coarse x rk
        Hi = np.linalg.inv(Hc)
        S = G @ Hi @ G.T
        # closed coarse Phi: Phi = w B for random B in ran d
        Bs = Ub @ rng.standard_normal((rk, 5))
        Phi = w @ Bs
        # pseudo-inverse of S on its range
        ev, Vv = np.linalg.eigh((S+S.T)/2)
        keep = ev > 1e-9*ev.max()
        Spinv = (Vv[:, keep]/ev[keep]) @ Vv[:, keep].T
        val_a = L*np.einsum('ik,ij,jk->k', Phi, Spinv, Phi)
        # direct minimization: B = Ub c, minimize c^T Hc c s.t. G c = Phi (least-norm in c-metric)
        c = Hi @ G.T @ (Spinv @ Phi)
        val_direct = L*np.einsum('ik,ij,jk->k', c, Hc, c)
        feas = np.abs(G @ c - Phi).max()
        # (b) Fourier symbol spectra vs real-space coarse kernel
        Pic = L*Spinv                                            # real-space coarse form (3 nc^3 square)
        # translation invariance: Pi_c[(a,y),(b,y')] = k_ab(y'-y); symbol sum_{y'} k_ab(y'-y) e^{-iK(y'-y)} or conj
        Pc = Pic.reshape(3, nc, nc, nc, 3, nc, nc, nc)
        k = Pc[:, 0, 0, 0, :, :, :, :]                           # (3, 3, nc,nc,nc) = k_{ab}(y')
        worst = 0.0
        for Kidx in itertools.product(range(nc), repeat=3):
            if Kidx == (0, 0, 0):
                continue
            K = 2*np.pi*np.array(Kidx)/nc
            ph = np.exp(-1j*(K[0]*np.arange(nc)[:, None, None] + K[1]*np.arange(nc)[None, :, None] + K[2]*np.arange(nc)[None, None, :]))
            symr = np.einsum('abxyz,xyz->ab', k, ph)
            sym_f = Pi(1, s, K[None, :], L)[0]
            e_r = np.sort(np.linalg.eigvalsh((symr+symr.conj().T)/2))
            e_f = np.sort(np.linalg.eigvalsh((sym_f+sym_f.conj().T)/2))
            worst = max(worst, np.abs(e_r - e_f).max())
        print(f"  s={s}: fibre value vs pinv formula max|diff|/scale = {np.abs(val_a-val_direct).max()/val_a.max():.2e}; "
              f"constraint residual {feas:.1e}; Fourier-vs-real-space symbol spectra max diff {worst:.2e}")
        sys.stdout.flush()


if __name__ == '__main__':
    run(2, 4)
