"""T28: abelian 4D fiber-convexity constant for (D1) of note 34.

For the Gaussian action (1/2)||F||^2, S_j(W) - S_{j+1}(CW) = (1/2) phi^T
Cov(Phi_j | Phi_{j+1})^{-1} phi >= |phi|_inf^2 / (2 Lambda_j), where
Lambda_j = sup_K lambda_max of the block-flux covariance multiplier
(note 19 (2.5), beta = 1) at block size M = L^j. This prints Lambda and
c_1 = 1/(2 Lambda).
"""
import itertools
import numpy as np
import t8_gauss4d as g

if __name__ == "__main__":
    n0 = 6
    for L, ms in ((2, (1, 2, 3)), (3, (1, 2))):
        for m in ms:
            M = L**m
            lam, arg = 0.0, None
            for k in itertools.product(range(n0), repeat=4):
                K = 2 * np.pi * np.array(k) / n0
                v = np.linalg.eigvalsh(g.terminal_covariance(K, M)).max()
                if v > lam:
                    lam, arg = v, k
            print(f"L={L} M={M}: sup_K lambda_max = {lam:.4f} at K-index {arg}"
                  f"  => c1 >= {1/(2*lam):.3f}", flush=True)
