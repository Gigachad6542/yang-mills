"""T76 check (note 61 section 6c): convexity along the s-orbit in the 3D abelian
Gaussian model of note 18 section 8.

Dimensionless units (g^2 eps_0 = 1, scale covariance): at every level the
Wilson flux precision on the transverse space B(p) is the identity P(p).
One block step (L-fold) acts on flux covariances F (3x3, range B) by

    (G F)(K)_{jk} = L^{-4} sum_{m in [0,L)^3} conj(w_j(p)) F_{jk}(p) w_k(p),
    p = (K + 2 pi m)/L,  w_j = L^{-3} D_j prod_{i != j} D_i^2,

the formula of t7_gauss3d.terminal_cov (there F = P).  The precision is
Pi = F^+ (pseudo-inverse on B).  The step on precisions,
Sigma(Pi) = (G Pi^+)^+, is the Schur complement (min over the fibre), hence
monotone, 1-homogeneous and concave.

Level-N data of the s-orbit:  Pi_s = (1-s) P + s Pi_1,  Pi_1 = (terminal_cov(., L))^+.
We flow it down j = 0..N steps and check, in the Loewner order on B:
  (A1)  Pi_j^(s) >= (1-s) Pi_j^(0) + s Pi_j^(1)           (concavity),
  (A2)  Pi_j^(s) <= Pi_j^(0) + s T_j^(0)[Delta]            (tangent line),
  (A4)  T_j^(1)[Delta] <= T_j^(s)[Delta] <= T_j^(0)[Delta] (tangents ordered),
  and the consistency  Pi_N^(1) = (terminal_cov(., L^(N+1)))^+  (note 18).
Reported: coercivity range of Pi_j^(s) relative to the identity, and operator
norms (the form norm relative to S = identity) of the differences.
"""
import sys, itertools, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from t7_gauss3d import terminal_cov

TOL = 1e-9


def Dsum(q, M):
    q = np.asarray(q, dtype=float)
    out = np.empty(q.shape, dtype=complex)
    small = np.abs(np.exp(-1j*q) - 1) < 1e-13
    out[small] = M
    e = np.exp(-1j*q[~small])
    out[~small] = (1 - e**M) / (1 - e)
    return out


def transverse_P(n):
    a = 2*np.pi*np.arange(n)/n
    P0, P1, P2 = np.meshgrid(a, a, a, indexing='ij')
    r = np.stack([np.exp(1j*P0)-1, np.exp(1j*P1)-1, np.exp(1j*P2)-1], axis=-1)
    r2 = (np.abs(r)**2).sum(-1)
    zero = r2 < 1e-24
    r2s = np.where(zero, 1.0, r2)
    P = np.eye(3)[None, None, None] - np.conj(r)[..., :, None]*r[..., None, :]/r2s[..., None, None]
    P[zero] = 0.0
    return P


def pinv_h(A, rank_tol=1e-9):
    """pseudo-inverse of Hermitian PSD matrices, last two axes."""
    A = (A + np.conj(np.swapaxes(A, -1, -2)))/2
    w, U = np.linalg.eigh(A)
    wi = np.where(w > rank_tol, 1.0/np.where(w > rank_tol, w, 1.0), 0.0)
    return (U*wi[..., None, :]) @ np.conj(np.swapaxes(U, -1, -2))


def step_cov(F, L):
    """one block step on covariance field F (n,n,n,3,3) -> (n/L,)^3."""
    n = F.shape[0]; nc = n//L
    b = 2*np.pi*np.arange(nc)/nc
    B0, B1, B2 = np.meshgrid(b, b, b, indexing='ij')
    out = np.zeros((nc, nc, nc, 3, 3), dtype=complex)
    for m in itertools.product(range(L), repeat=3):
        p = [(Bk + 2*np.pi*mk)/L for Bk, mk in zip((B0, B1, B2), m)]
        Dm = [Dsum(pi, L) for pi in p]
        w = []
        for j in range(3):
            f = Dm[j]/L**3
            for i in range(3):
                if i != j:
                    f = f*Dm[i]**2
            w.append(f)
        W = np.stack(w, axis=-1)                     # (nc,nc,nc,3)
        # fine index a = b + nc*m
        Fm = F[m[0]*nc:(m[0]+1)*nc, m[1]*nc:(m[1]+1)*nc, m[2]*nc:(m[2]+1)*nc]
        out += np.conj(W)[..., :, None]*Fm*W[..., None, :]
    return out/L**4


def basis_B(n):
    """orthonormal basis (n,n,n,3,2) of the transverse space; zero at p=0."""
    P = transverse_P(n)
    w, U = np.linalg.eigh(P)
    return U[..., 1:], np.abs(P).sum((-1, -2)) < 1e-14   # two top eigenvectors, zero-mode mask


def compress(A, U):
    return np.conj(np.swapaxes(U, -1, -2)) @ A @ U


def eigs(A2):
    A2 = (A2 + np.conj(np.swapaxes(A2, -1, -2)))/2
    return np.linalg.eigvalsh(A2)


def sigma_prec(Pi, L):
    return pinv_h(step_cov(pinv_h(Pi), L), 1e-9)


def tangent_step(Pi, dPi, L):
    F = pinv_h(Pi); dF = -F @ dPi @ F
    Fp = step_cov(F, L); dFp = step_cov(dF, L)
    Pip = pinv_h(Fp, 1e-9)
    return Pip, -Pip @ dFp @ Pip


def run(L, n0, N, svals=(0.0, 0.25, 0.5, 0.75, 1.0)):
    n = n0*L**N
    a = 2*np.pi*np.arange(n)/n
    Kg = np.stack(np.meshgrid(a, a, a, indexing='ij'), axis=-1)
    P = transverse_P(n)
    F1 = np.zeros((n, n, n, 3, 3), dtype=complex)
    for ia, ib, ic in itertools.product(range(n), repeat=3):
        if (ia, ib, ic) != (0, 0, 0):
            F1[ia, ib, ic] = terminal_cov(Kg[ia, ib, ic], L)
    Pi1 = pinv_h(F1, 1e-9)
    U, zm = basis_B(n)
    ev = eigs(compress(Pi1 - P, U))[~zm]
    print(f"L={L} n0={n0} N={N}: level-N lattice {n}^3; eig(Pi_1 - P) on B: min {ev.min():.4f}, max {ev.max():.4f}"
          f"  (r = 1 + eig: {1+ev.min():.3f} .. {1+ev.max():.3f})")
    Delta = Pi1 - P
    orbit = {s: (1-s)*P + s*Pi1 for s in svals}
    tang = {s: Delta.copy() for s in svals}
    cur = dict(orbit)
    worst = dict(A1=-1e9, A2=-1e9, A4a=-1e9, A4b=-1e9)
    for j in range(0, N+1):
        nj = n0*L**(N-j)
        Uj, zj = basis_B(nj)
        keep = ~zj
        def E(A):
            return eigs(compress(A, Uj))[keep]
        if j > 0:
            for s in svals:
                cur[s], tang[s] = tangent_step(cur[s], tang[s], L)
        # NB: tangent_step at level j uses cur[s] at level j-1 (before update)
        # (done above in one call: returns updated cur and tangent)
        e = {s: E(cur[s]) for s in svals}
        lo = min(e[s].min() for s in svals); hi = max(e[s].max() for s in svals)
        line = f"  j={j} level {nj}^3: eig(Pi_j^(s)) over s, K in [{lo:.4f}, {hi:.4f}]"
        # A1
        a1 = max((-(E(cur[s] - (1-s)*cur[0.0] - s*cur[1.0])).min()) for s in svals)
        # A2
        a2 = max(E(cur[s] - cur[0.0] - s*tang[0.0]).max() for s in svals)
        # A4
        a4a = max(E(tang[s] - tang[1.0]).min()*-1 for s in svals)
        a4b = max(E(tang[0.0] - tang[s]).min()*-1 for s in svals)
        worst['A1'] = max(worst['A1'], a1); worst['A2'] = max(worst['A2'], a2)
        worst['A4a'] = max(worst['A4a'], a4a); worst['A4b'] = max(worst['A4b'], a4b)
        nT0 = np.abs(E(tang[0.0])).max(); nT1 = np.abs(E(tang[1.0])).max(); nT5 = np.abs(E(tang[0.5])).max()
        nD1 = np.abs(E(cur[1.0] - cur[0.0])).max()
        nDh = np.abs(E(cur[0.5] - cur[0.0])).max()
        print(line)
        print(f"     (A1) max violation {a1:+.2e}   (A2) max violation {a2:+.2e}   (A4) {a4a:+.2e} {a4b:+.2e}")
        print(f"     ||T_j^(0)D|| {nT0:.4f}  ||T_j^(1/2)D|| {nT5:.4f}  ||T_j^(1)D|| {nT1:.4f}   "
              f"||Pi_j^(1)-Pi_j^(0)|| {nD1:.4f}  ||Pi_j^(1/2)-Pi_j^(0)|| {nDh:.4f}  (bound s*max = {0.5*max(nD1, nT0):.4f})")
    # consistency with note 18: Pi_N^(1) = (cov of depth N+1)^+
    nj = n0
    Ks = [np.array(k)*2*np.pi/n0 for k in itertools.product(range(n0), repeat=3) if k != (0, 0, 0)]
    err = 0.0
    for K in Ks:
        ia = tuple(int(round(x*n0/(2*np.pi))) % n0 for x in K)
        Cdirect = terminal_cov(K, L**(N+1))
        Cflow = pinv_h(cur[1.0][ia][None], 1e-9)[0]
        err = max(err, np.abs(Cdirect - Cflow).max())
    print(f"  consistency: max|terminal_cov(K,L^(N+1)) - (Pi_N^(1))^+| = {err:.2e}")
    print(f"  WORST violations: {worst}")
    ok = all(v <= TOL for v in worst.values())
    print(f"  all orderings hold to {TOL}: {ok}")
    return ok


if __name__ == '__main__':
    ok = True
    for L, n0, N in [(2, 4, 1), (2, 4, 2), (2, 4, 3), (3, 4, 1), (3, 4, 2)]:
        ok &= run(L, n0, N)
    print("ALL OK" if ok else "VIOLATION")
