"""T7 computation: exact terminal flux covariance of 3D noncompact U(1)
lattice gauge theory under Balaban's linear block average.

Fine torus (Z/n)^3, n = n0*M, M = L^N, spacing eps_N = eps0/M, action
(beta/2)|dA|^2 with beta = 1/(g^2 eps_N).  Units: g^2 eps0 = 1, so 1/beta = 1/M.
Fine flux covariance: (1/beta) * projection onto im d = ker(Bianchi) (p != 0).
Terminal flux Phi_j(Y) = sum_x w_j(x - Y) B_j(x) with w_j = (M-box average) *
(M x M square perpendicular to j); this is d_c(Q^N A) (t7_kernel_check.py).

Terminal Fourier covariance at terminal momentum K in (2 pi/n0) Z^3:
  C_jk(K) = M^{-4} sum_{m in [0,M)^3} P_jk(p) conj(w_j(p)) w_k(p),
  p = (K + 2 pi m)/M,  P_jk = delta_jk - conj(r_j) r_k/|r|^2,  r_j = e^{i p_j} - 1.
"""
import sys, itertools, numpy as np

def D(q, M):  # sum_{t<M} e^{-i q t}
    q = np.asarray(q, dtype=float)
    out = np.empty(q.shape, dtype=complex)
    small = np.abs(np.exp(-1j*q) - 1) < 1e-13
    out[small] = M
    e = np.exp(-1j*q[~small])
    out[~small] = (1 - e**M) / (1 - e)
    return out

def terminal_cov(K, M, gamma=0.0, kind=None):
    """3x3 terminal covariance at terminal momentum K (array of 3).
    gamma/kind: optional fine-action defect, multiplying the fine inverse
    covariance on im d by (1 + gamma*lam(p)):
      kind='dim4q' : lam = 1/beta = 1/M (O(1) lattice-unit defect, no beta)
      kind='dim6'  : lam = |r|^2      (beta-weighted |nabla B|^2)
    """
    m = np.arange(M)
    p = [(K[i] + 2*np.pi*m)/M for i in range(3)]
    Dm = [D(p[i], M) for i in range(3)]
    P0, P1, P2 = np.meshgrid(p[0], p[1], p[2], indexing='ij')
    r = [np.exp(1j*P0)-1, np.exp(1j*P1)-1, np.exp(1j*P2)-1]
    r2 = sum(np.abs(x)**2 for x in r)
    zero = r2 < 1e-24
    r2s = np.where(zero, 1.0, r2)
    box = (Dm[0][:, None, None]*Dm[1][None, :, None]*Dm[2][None, None, :]) / M**3
    w = []
    for j in range(3):
        f = box.copy()
        for i in range(3):
            if i != j:
                sh = [None, None, None]; sh[i] = slice(None)
                f = f * Dm[i][tuple(sh)]
        w.append(f)
    fac = np.ones_like(r2)
    if kind == 'dim4q':
        fac = 1.0/(1.0 + gamma/M) * fac
    elif kind == 'dim6':
        fac = 1.0/(1.0 + gamma*r2)
    C = np.zeros((3, 3), dtype=complex)
    for j in range(3):
        for k in range(3):
            Pjk = (1.0 if j == k else 0.0) - np.conj(r[j])*r[k]/r2s
            Pjk = np.where(zero, 0.0, Pjk)
            C[j, k] = np.sum(fac*Pjk*np.conj(w[j])*w[k]) / M**4
    return C

def all_K(n0):
    ks = 2*np.pi*np.arange(n0)/n0
    return [np.array(K) for K in itertools.product(ks, repeat=3)]

def table(n0, L, Nmax, **kw):
    Ks = all_K(n0); prev = None; rows = []
    for N in range(0, Nmax+1):
        M = L**N
        C = np.array([terminal_cov(K, M, **kw) for K in Ks])
        if prev is not None:
            d = np.abs(C - prev).max()
            rows.append((N, M, d))
        prev = C
    return rows, C

if __name__ == '__main__':
    n0 = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    for L, Nmax in [(2, 7), (3, 4)]:
        rows, C = table(n0, L, Nmax)
        print(f"n0={n0} L={L}: sup_K max_jk |C_N - C_(N-1)|, and successive ratio")
        last = None
        for N, M, d in rows:
            print(f"  N={N} M={M:4d}  diff={d:.4e}" + (f"  ratio={last/d:.3f}" if last else ""))
            last = d
        print(f"  |C| scale: max|C_N| = {np.abs(C).max():.4f}")
