"""T36: l2 (energy) norms of the minimizer-image kernel restricted to exact
coarse fluxes, compared with the sup-norm constants of note 35.

For a row g of G (level-m fluxes -> one level-(m-1) image flux), the norm of
Phi -> <g, Phi> on exact Phi in the l2 norm is ||P_ex g||_2, where P_ex is the
orthogonal projection onto exact coarse 2-forms. P_ex is the coarse version of
the projector P_2 of note 19 (1.3). It is computed in Fourier space on the
coarse torus.
"""
import itertools
import numpy as np
import t27_minimizer_regularity as t

PLAQ = t.PLAQ


def coarse_projector_fft(n0):
    k = 2 * np.pi * np.arange(n0) / n0
    K = np.array(np.meshgrid(k, k, k, k, indexing="ij")).reshape(4, -1)
    return t.projector(K).reshape(6, 6, n0, n0, n0, n0)


def l2_rows(L, m, n0, s=1):
    G = t.kernel(L, m, n0, s).real  # (u, D..., a, b)
    P = coarse_projector_fft(n0)
    out = []
    for u in range(G.shape[0]):
        for a in range(6):
            g = np.moveaxis(G[u, :, :, :, :, a, :], -1, 0)  # (b, D)
            gh = np.fft.fftn(g, axes=(1, 2, 3, 4))
            ph = np.einsum("bcK,cK->bK", P.reshape(6, 6, -1), gh.reshape(6, -1))
            # projection is orthogonal and Hermitian; Parseval
            out.append((u, a, np.sqrt(np.sum(np.abs(ph) ** 2) / n0**4), np.sqrt(np.sum(g**2))))
    return out


if __name__ == "__main__":
    n0 = 8
    print("L m n0 | max_rows ||P_ex g||_2 | L^2 * that | mean over rows | (unprojected max)")
    for L, m in [(2, 1), (3, 1), (4, 1), (5, 1), (2, 2), (2, 3)]:
        r = l2_rows(L, m, n0)
        mx = max(x[2] for x in r); mean = np.mean([x[2] for x in r]); un = max(x[3] for x in r)
        print(f"{L} {m} {n0} | {mx:.4f} | {L**2*mx:.4f} | {mean:.4f} | {un:.4f}", flush=True)


def diff_rows(L, m, n0):
    """l2 norms on exact Phi of differences of neighbouring child rows (same block)."""
    G = t.kernel(L, m, n0).real
    P = coarse_projector_fft(n0).reshape(6, 6, -1)
    offs = list(itertools.product(range(L), repeat=4))
    idx = {o: i for i, o in enumerate(offs)}

    def pnorm(g):
        gh = np.fft.fftn(g, axes=(1, 2, 3, 4)).reshape(6, -1)
        ph = np.einsum("bcK,cK->bK", P, gh)
        return np.sqrt(np.sum(np.abs(ph) ** 2) / n0**4)

    best, ratio_mean = 0.0, []
    for o in offs:
        for nu in range(4):
            o2 = list(o); o2[nu] += 1
            if o2[nu] >= L:
                continue
            for a in range(6):
                g1 = np.moveaxis(G[idx[o], :, :, :, :, a, :], -1, 0)
                g2 = np.moveaxis(G[idx[tuple(o2)], :, :, :, :, a, :], -1, 0)
                d = pnorm(g1 - g2); base = pnorm(g1)
                best = max(best, d); ratio_mean.append(d / base)
    return best, float(np.mean(ratio_mean))


if __name__ == "__main__":
    print("\nNeighbouring-child differences (dimension-5 structure):")
    print("L | max ||P(g_u - g_{u+e})||_2 | mean ratio to ||P g_u||_2")
    for L in (2, 3, 4, 5):
        b, r = diff_rows(L, 1, 8)
        print(f"{L} | {b:.4f} | {r:.3f}", flush=True)


def cross_face_rows(L, m, n0):
    """Pairs u (u_nu = L-1, block Y) and u' (u'_nu = 0, block Y + e_nu)."""
    G = t.kernel(L, m, n0).real
    P = coarse_projector_fft(n0).reshape(6, 6, -1)
    offs = list(itertools.product(range(L), repeat=4))
    idx = {o: i for i, o in enumerate(offs)}

    def pnorm(g):
        gh = np.fft.fftn(g, axes=(1, 2, 3, 4)).reshape(6, -1)
        ph = np.einsum("bcK,cK->bK", P, gh)
        return np.sqrt(np.sum(np.abs(ph) ** 2) / n0**4)

    ratios = []
    for o in offs:
        for nu in range(4):
            if o[nu] != L - 1:
                continue
            o2 = list(o); o2[nu] = 0
            for a in range(6):
                g1 = np.moveaxis(G[idx[o], :, :, :, :, a, :], -1, 0)          # block Y0, Phi(Y0 - D)
                g2 = np.moveaxis(G[idx[tuple(o2)], :, :, :, :, a, :], -1, 0)  # block Y0 + e_nu
                # express g2 against Phi(Y0 - D): Phi((Y0+e) - D') with D' = D + e
                g2 = np.roll(g2, -1, axis=1 + nu)  # coefficient of Phi(Y0 - D) is G[u2, D + e]
                ratios.append(pnorm(g1 - g2) / pnorm(g1))
    return float(np.mean(ratios)), float(np.max(ratios))


if __name__ == "__main__":
    print("\nCross-face neighbouring children (u_nu = L-1 -> next block u_nu = 0):")
    print("L | mean ratio | max ratio | L*mean | sqrt(L)*mean")
    for L in (2, 3, 4, 5):
        mr, xr = cross_face_rows(L, 1, 8)
        print(f"{L} | {mr:.3f} | {xr:.3f} | {L*mr:.2f} | {np.sqrt(L)*mr:.2f}", flush=True)
