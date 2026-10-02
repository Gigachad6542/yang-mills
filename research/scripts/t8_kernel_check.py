"""T8: direct check of the exact block-flux kernel in four dimensions."""

from __future__ import annotations

import itertools
import numpy as np

from t8_brute_check import PLAQ, dmat, link, qmat, site


def plaquette_flux(field, x, mu, nu, side):
    emu = [0] * 4
    enu = [0] * 4
    emu[mu] = 1
    enu[nu] = 1
    xmu = [x[j] + emu[j] for j in range(4)]
    xnu = [x[j] + enu[j] for j in range(4)]
    return (
        field[link(x, mu, side)]
        + field[link(xmu, nu, side)]
        - field[link(xnu, mu, side)]
        - field[link(x, nu, side)]
    )


def flux_kernel_apply(field, side, M):
    coarse = side // M
    result = np.zeros(6 * coarse**4)
    offsets = tuple(itertools.product(range(M), repeat=4))
    for y in itertools.product(range(coarse), repeat=4):
        origin = [M * coordinate for coordinate in y]
        for orientation, (mu, nu) in enumerate(PLAQ):
            total = 0.0
            for offset in offsets:
                for a in range(M):
                    for b in range(M):
                        x = [origin[j] + offset[j] for j in range(4)]
                        x[mu] += a
                        x[nu] += b
                        total += plaquette_flux(field, x, mu, nu, side)
            result[6 * site(y, coarse) + orientation] = total / M**4
    return result


if __name__ == "__main__":
    rng = np.random.default_rng(20261002)
    for side, L in ((4, 2), (6, 3)):
        field = rng.normal(size=4 * side**4)
        coarse = side // L
        for reverse in (False, True):
            lhs = dmat(coarse) @ (qmat(side, L, reverse=reverse) @ field)
            rhs = flux_kernel_apply(field, side, L)
            print(
                f"side={side} L={L} reverse={reverse}: "
                f"max|d_c Q A-kernel*dA|={np.max(np.abs(lhs-rhs)):.3e}"
            )
