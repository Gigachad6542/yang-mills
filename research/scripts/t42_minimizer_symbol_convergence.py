"""T42: depth convergence of the minimizer's induced child symbol B^(m)_{l'}(K).

B^(m)_{l'}(K) maps level-m coarse fluxes at momentum K to the level-(m-1)
image fluxes at child momentum (K + 2 pi l')/L (note 35's kernel, before the
inverse FFT). We print sup_{K, l'} ||B^(m) - B^(m+1)|| for L = 2.
"""
import itertools
import numpy as np
import t27_minimizer_regularity as t


def symbols(L, m, Ks):
    M = L**m
    M1 = M // L
    ells = np.array(list(itertools.product(range(M), repeat=4))).T
    child = ells % L
    cid = ((child[0] * L + child[1]) * L + child[2]) * L + child[3]
    out = []
    for K in Ks:
        p = (K[:, None] + 2 * np.pi * ells) / M
        wM = t.what(p, M)
        wM1 = t.what(p, M1) if M1 > 1 else np.ones((6, p.shape[1]), dtype=complex)
        P = t.projector(p)
        cov = np.einsum("aN,abN,bN->ab", wM.conj(), P, wM) / M**8
        cinv = t.pinv_h(cov)
        cross = np.einsum("aN,abN,bN->abN", wM1.conj(), P, wM) / (M1**4 * M**4)
        B = np.zeros((L**4, 6, 6), dtype=complex)
        np.add.at(B, cid, np.moveaxis(cross, 2, 0))
        out.append(B @ cinv)
    return out


if __name__ == "__main__":
    L, n0 = 2, 4
    Ks = [2 * np.pi * np.array(k) / n0 for k in itertools.product(range(n0), repeat=4)]
    Ks = [K for K in Ks if np.any(K != 0)]
    prev, pd = None, None
    for m in (1, 2, 3, 4):
        S = symbols(L, m, Ks)
        if prev is not None:
            d = max(np.abs(a - b).max() for a, b in zip(S, prev))
            msg = f"m={m-1}->{m}: sup |B^(m) - B^(m+1)| = {d:.3e}"
            if pd:
                msg += f"  ratio {pd/d:.2f}"
            print(msg, flush=True)
            pd = d
        prev = S
