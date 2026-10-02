"""T13 scalar fallback: exact O(N) sigma-model one-loop window sums.

Primary calculation: one terminal cell, so the composite M-box constraint is
the removal of the global fluctuation zero mode.  A constant total twist gives
the complete one-loop stiffness decrement, including its bounded longitudinal
edge term.

Secondary calculation: the transverse trace for a genuine multi-cell M-box
constraint.  It uses the alias-space Schur complement and a stable exact
formula for the Dirichlet kernel at alias momenta.
"""

from __future__ import annotations

import numpy as np


def inverse_laplacian_sum(M: int) -> float:
    """Sum 1/hat{k}^2 on the M by M torus with the zero mode removed."""
    momenta = 2.0 * np.pi * np.arange(M) / M
    k0, k1 = np.meshgrid(momenta, momenta, indexing="ij")
    laplacian = 4.0 * np.sin(0.5 * k0) ** 2 + 4.0 * np.sin(0.5 * k1) ** 2
    inverse = np.zeros_like(laplacian)
    nonzero = laplacian > 1.0e-24
    inverse[nonzero] = 1.0 / laplacian[nonzero]
    return float(np.sum(inverse))


def sigma_window_shift(M: int, components: int = 3) -> float:
    """Positive one-loop decrement of the inverse O(N) sigma coupling."""
    longitudinal_edge = 0.25 * (1.0 - M**-2)
    transverse = (components - 2) * inverse_laplacian_sum(M) / M**2
    return longitudinal_edge + transverse


def alias_dirichlet(K: float, M: int) -> np.ndarray:
    """D_M((K+2*pi*l)/M) for K in [0, 2*pi), preserving alias zeros."""
    aliases = np.arange(M)
    p = (K + 2.0 * np.pi * aliases) / M
    result = np.zeros(M, dtype=complex)
    if abs(np.sin(0.5 * K)) < 1.0e-14:
        if abs(K) < 1.0e-14:
            result[0] = M
        return result
    result = (
        np.exp(-0.5j * p * (M - 1))
        * (-1.0) ** aliases
        * np.sin(0.5 * K)
        / np.sin(0.5 * p)
    )
    return result


def constrained_transverse_trace(n0: int, M: int) -> float:
    """Return |Lambda_f|^-1 Tr C_M for Q_M phi=0 on n0^2 coarse cells."""
    coarse_momenta = 2.0 * np.pi * np.arange(n0) / n0
    aliases = np.arange(M)
    total_trace = 0.0
    for K0 in coarse_momenta:
        p0 = (K0 + 2.0 * np.pi * aliases) / M
        d0 = alias_dirichlet(K0, M)
        for K1 in coarse_momenta:
            p1 = (K1 + 2.0 * np.pi * aliases) / M
            d1 = alias_dirichlet(K1, M)
            p0_grid, p1_grid = np.meshgrid(p0, p1, indexing="ij")
            laplacian = (
                4.0 * np.sin(0.5 * p0_grid) ** 2
                + 4.0 * np.sin(0.5 * p1_grid) ** 2
            )
            propagator = np.zeros_like(laplacian)
            nonzero = laplacian > 1.0e-24
            propagator[nonzero] = 1.0 / laplacian[nonzero]
            q_squared = (
                np.abs(d0)[:, None] ** 2 * np.abs(d1)[None, :] ** 2 / M**4
            )
            denominator = np.sum(q_squared * propagator)
            group_trace = np.sum(propagator)
            if denominator > 1.0e-30:
                group_trace -= np.sum(q_squared * propagator**2) / denominator
            total_trace += group_trace
    return float(total_trace / (n0 * M) ** 2)


def real_space_check(n0=4, M=2):
    """Dense null-space check of the multi-cell Schur formula."""
    side = n0 * M
    volume = side**2
    laplacian = np.zeros((volume, volume))

    def site(x0, x1):
        return (x0 % side) + side * (x1 % side)

    for x0 in range(side):
        for x1 in range(side):
            row = site(x0, x1)
            laplacian[row, row] = 4.0
            laplacian[row, site(x0 + 1, x1)] = -1.0
            laplacian[row, site(x0 - 1, x1)] = -1.0
            laplacian[row, site(x0, x1 + 1)] = -1.0
            laplacian[row, site(x0, x1 - 1)] = -1.0

    average = np.zeros((n0**2, volume))
    for y0 in range(n0):
        for y1 in range(n0):
            row = y0 + n0 * y1
            for u0 in range(M):
                for u1 in range(M):
                    average[row, site(M * y0 + u0, M * y1 + u1)] = M**-2

    _, singular_values, vh = np.linalg.svd(average, full_matrices=True)
    rank = int(np.sum(singular_values > 1.0e-12))
    null_basis = vh[rank:].T
    restricted = null_basis.T @ laplacian @ null_basis
    eigenvalues = np.linalg.eigvalsh(restricted)
    real_value = float(np.sum(1.0 / eigenvalues) / volume)
    fourier_value = constrained_transverse_trace(n0, M)
    return real_value, fourier_value, null_basis.shape[1], float(eigenvalues.min())


def run_table(components=3):
    print(f"O({components}) sigma model; exact one-terminal-cell twist determinant")
    for L in (2, 3):
        target = (components - 2) * np.log(L) / (2.0 * np.pi)
        rows = []
        previous = None
        print(f"L={L}, universal slope per step={target:.12f}")
        print("n     M       beta_window       edge=beta-n*slope     increment")
        for depth in range(1, 7):
            M = L**depth
            shift = sigma_window_shift(M, components=components)
            edge = shift - depth * target
            increment = np.nan if previous is None else shift - previous
            rows.append((depth, shift, edge))
            increment_text = "" if previous is None else f"{increment: .12f}"
            print(
                f"{depth:d}  {M:4d}  {shift: .12f}  "
                f"{edge: .12f}  {increment_text}"
            )
            previous = shift
        tail_depths = np.array([row[0] for row in rows[3:]], dtype=float)
        tail_values = np.array([row[1] for row in rows[3:]])
        fitted_slope, fitted_edge = np.polyfit(tail_depths, tail_values, 1)
        print(
            f"n=4..6 fit slope={fitted_slope:.12f}, "
            f"relative error={fitted_slope/target-1:+.3e}, "
            f"last edge={rows[-1][2]:.12f}"
        )

    print("multi-cell box-constraint transverse trace, n0=4")
    for L in (2, 3):
        target = np.log(L) / (2.0 * np.pi)
        values = [constrained_transverse_trace(4, L**depth) for depth in range(1, 7)]
        edges = [value - depth * target for depth, value in enumerate(values, 1)]
        print(
            f"L={L}: n=1..6 values="
            + ", ".join(f"{value:.12f}" for value in values)
        )
        print(f"     last bounded edge={edges[-1]:.12f}")

    real, fourier, dimension, minimum = real_space_check()
    print(
        "real-space check n0=4,M=2: "
        f"real={real:.15f}, Fourier={fourier:.15f}, "
        f"error={abs(real-fourier):.3e}, dim={dimension}, min_ev={minimum:.6f}"
    )


if __name__ == "__main__":
    run_table()
