"""T41: depth convergence of the block-flux covariance C^(M)(K) (note 19 (2.5)).

Prints sup_K ||C^(M)(K) - C^(2M)(K)|| (operator norm) on a coarse momentum
grid, for M = 2, 4, 8, 16, and the ratio of successive differences.
"""
import itertools
import numpy as np
import t8_gauss4d as g

if __name__ == "__main__":
    n0 = 4
    Ks = [2 * np.pi * np.array(k) / n0 for k in itertools.product(range(n0), repeat=4)]
    Ks = [K for K in Ks if np.any(K != 0)]
    prev, prevdiff = None, None
    for M in (2, 4, 8, 16, 32):
        Cs = [g.terminal_covariance(K, M) for K in Ks]
        if prev is not None:
            d = max(np.linalg.norm(a - b, 2) for a, b in zip(Cs, prev))
            msg = f"M={M//2}->{M}: sup_K ||C^(M) - C^(2M)|| = {d:.3e}"
            if prevdiff:
                msg += f"   ratio prev/this = {prevdiff/d:.2f}"
            print(msg, flush=True)
            prevdiff = d
        prev = Cs
