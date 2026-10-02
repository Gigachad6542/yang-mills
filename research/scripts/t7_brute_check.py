"""T7 check 2: the aliasing formula of t7_gauss3d.py against a brute-force
real-space covariance Cov(d_c Q^N A) = beta^{-1} (d_c Q^N)(d^T d)^+ (d_c Q^N)^T."""
import itertools, numpy as np
from gauge3d_common import dmat, Qmat, site, PL, PERP, SIG
from t7_gauss3d import terminal_cov, all_K
for (n0, L, N) in [(2, 2, 2), (2, 3, 1), (3, 2, 1)]:
    M = L**N; s = n0*M; beta = M        # units g^2 eps0 = 1
    d = dmat(s); W = np.eye(3*s**3); cur = s
    for k in range(N):
        W = Qmat(cur, L) @ W; cur //= L
    W = dmat(n0) @ W
    ev, U = np.linalg.eigh(d.T @ d); keep = ev > 1e-9 * ev.max()
    Cb = (W @ U[:, keep]) @ np.diag(1/ev[keep]) @ (W @ U[:, keep]).T / beta
    Ks = all_K(n0); Ch = {tuple(K): terminal_cov(K, M) for K in Ks}
    err = 0
    for D in itertools.product(range(n0), repeat=3):
        for o in range(3):
            for o2 in range(3):
                j, k = PERP[PL[o]], PERP[PL[o2]]          # plaquette orientation -> normal
                sg = SIG[PL[o]]*SIG[PL[o2]]               # F_{mu nu} = SIG * B_normal
                v = sum(np.exp(-1j*np.dot(K, D))*Ch[tuple(K)][j, k] for K in Ks) / n0**3
                err = max(err, abs(sg*v - Cb[o, 3*site(D, n0)+o2]))
    print(f"n0={n0} L={L} N={N}: max |Fourier - brute| = {err:.2e}  (max|C|={np.abs(Cb).max():.3f})")
