# T82 (audit 2026-10-09, item 4). Run: python3 research/scripts/t82_kernel_check67.py research/scripts
# Does d_c q = W C hold for note 67's q (t80_abelian_fibre.build) with W >= 0,
# row sums L^2 and column sums <= 1/L (the Schur-test facts of note 61 Lemma 6c.2)?
import sys, itertools, numpy as np
sys.path.insert(0, sys.argv[1])
import t80_abelian_fibre as t80
from scipy.optimize import nnls
for L, n in ((2, 3), (3, 2)):
    T, C, Q = t80.build(L, n)
    rows, sums, resid = [], [], 0.0
    Wfull = np.zeros((0, C.shape[0]))
    for y in itertools.product(range(n), repeat=3):
        for mu, nu in ((0, 1), (0, 2), (1, 2)):
            b = t80.coarse_plaq_bonds(n, y, mu, nu)
            sg = [1, 1, -1, -1]
            m = sum(s * Q[T.bond_index[bb]] for s, bb in zip(sg, b))   # (d_c q) row
            # restrict to fine plaquettes of the same orientation
            cols = [i for (x, a, c), i in T.plaq_index.items() if (a, c) == (mu, nu)]
            w, r = nnls(C[cols].T, m, maxiter=50 * len(cols))
            wf = np.zeros(C.shape[0]); wf[cols] = w
            resid = max(resid, np.abs(wf @ C - m).max())
            sums.append(w.sum()); Wfull = np.vstack([Wfull, wf])
    colmax = Wfull.sum(axis=0).max()
    lam = np.linalg.norm(Wfull, 2)
    print(f"L={L} n={n}: max residual {resid:.2e}; row sums in [{min(sums):.6f}, {max(sums):.6f}] (L^2 = {L*L}); "
          f"max column sum {colmax:.6f} (1/L = {1/L:.6f}); ||W||_2^2 = {lam**2:.6f} (L = {L})")
