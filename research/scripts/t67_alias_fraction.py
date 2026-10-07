"""T67: alias-fraction structure of the IR edge E = -g g^T / C (scalar toy, 4D).

Scalar field, linear box average Q over M^4 fine cells, fine propagator
G0(p) = 1/sum_j 4 sin^2(p_j/2).  For coarse momentum K, aliases n in B_M^4,
p_n = (K + 2 pi n)/M.  Block covariance C(K) = sum_n |w_n|^2 G0(p_n), with
|w_n| = prod_j delta_M(n_j), delta_M = |sin(K_j/2)| / (M |sin(p_j/2)|).
Constrained propagator on the alias sector: G_Q = G0 - g g^T / C, g_n = w_n G0(p_n).
Diagonal: G_Q(n,n)/G0(p_n) = 1 - f_n, f_n = |w_n|^2 G0(p_n)/C, sum_n f_n = 1.
"""
import numpy as np


def run(M, K):
    n1 = np.arange(-M // 2 + 1, M // 2 + 1)
    grids = np.meshgrid(*([n1] * 4), indexing="ij")
    q = [K[j] + 2 * np.pi * grids[j] for j in range(4)]
    p = [qj / M for qj in q]
    delta2 = np.ones_like(p[0])
    for j in range(4):
        delta2 = delta2 * (np.sin(K[j] / 2) / (M * np.sin(p[j] / 2))) ** 2
    G0 = 1.0 / sum(4 * np.sin(pj / 2) ** 2 for pj in p)
    num = delta2 * G0
    C = num.sum()
    f = num / C
    i0 = tuple(M // 2 - 1 for _ in range(4))  # index of n = 0
    f0 = f[i0]
    fo = f.copy()
    fo[i0] = 0
    return f0, fo.max(), C


if __name__ == "__main__":
    for M in (4, 8):
        print(f"M = {M}")
        for k in (0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 3.0):
            K = (k, k, k, k)
            f0, fmax, C = run(M, K)
            print(f"  |K|={2*k:5.2f}  f_0 = {f0:.6f}  1-f_0 = {1-f0:.3e}  "
                  f"(1-f_0)/|K|^2 = {(1-f0)/(4*k*k):.4f}  "
                  f"max_(n!=0) f_n = {fmax:.3e}")
