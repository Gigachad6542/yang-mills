"""T8: dense real-space checks of the 4D Fourier aliasing formula.

The nontrivial case diagonalizes d^T d on the fine 4^4 torus.  This uses an
eigendecomposition with an explicit spectral cutoff, not numpy.linalg.pinv.
"""

from __future__ import annotations

import itertools
import numpy as np

from t8_gauss4d import PLAQ, terminal_covariance


def site(x, side):
    value = 0
    stride = 1
    for coordinate in x:
        value += (coordinate % side) * stride
        stride *= side
    return value


def link(x, mu, side):
    return 4 * site(x, side) + mu


def dmat(side):
    matrix = np.zeros((6 * side**4, 4 * side**4))
    for x in itertools.product(range(side), repeat=4):
        for orientation, (mu, nu) in enumerate(PLAQ):
            row = 6 * site(x, side) + orientation
            emu = [0] * 4
            enu = [0] * 4
            emu[mu] = 1
            enu[nu] = 1
            xmu = [x[j] + emu[j] for j in range(4)]
            xnu = [x[j] + enu[j] for j in range(4)]
            matrix[row, link(x, mu, side)] += 1.0
            matrix[row, link(xmu, nu, side)] += 1.0
            matrix[row, link(xnu, mu, side)] -= 1.0
            matrix[row, link(x, nu, side)] -= 1.0
    return matrix


def path_row(origin, displacement, side, reverse=False):
    row = np.zeros(4 * side**4)
    x = list(origin)
    axes = range(3, -1, -1) if reverse else range(4)
    for axis in axes:
        for _ in range(displacement[axis]):
            row[link(x, axis, side)] += 1.0
            x[axis] += 1
    return row


def qmat(side, L, reverse=False):
    coarse = side // L
    matrix = np.zeros((4 * coarse**4, 4 * side**4))
    offsets = tuple(itertools.product(range(L), repeat=4))

    def radial_average(y):
        origin = [L * coordinate for coordinate in y]
        return sum(
            (path_row(origin, offset, side, reverse=reverse) for offset in offsets),
            start=np.zeros(4 * side**4),
        ) / L**4

    radial = {
        y: radial_average(y) for y in itertools.product(range(coarse), repeat=4)
    }
    for y in itertools.product(range(coarse), repeat=4):
        origin = [L * coordinate for coordinate in y]
        for mu in range(4):
            row = 4 * site(y, coarse) + mu
            straight = np.zeros(4 * side**4)
            for offset in offsets:
                for step in range(L):
                    x = [origin[j] + offset[j] for j in range(4)]
                    x[mu] += step
                    straight[link(x, mu, side)] += 1.0
            yp = list(y)
            yp[mu] = (yp[mu] + 1) % coarse
            matrix[row] = radial[y] + straight / L**4 - radial[tuple(yp)]
    return matrix


def all_momenta(side):
    values = 2.0 * np.pi * np.arange(side) / side
    return tuple(np.asarray(K) for K in itertools.product(values, repeat=4))


def check(n0, L=1, beta=1.0, reverse=False):
    fine = n0 * L
    derivative = dmat(fine)
    if L == 1:
        blocked_flux = derivative
    else:
        blocked_flux = dmat(n0) @ qmat(fine, L, reverse=reverse)

    hessian = derivative.T @ derivative
    eigenvalues, eigenvectors = np.linalg.eigh(hessian)
    threshold = 1.0e-10 * eigenvalues.max()
    keep = eigenvalues > threshold
    factors = (blocked_flux @ eigenvectors[:, keep]) / np.sqrt(eigenvalues[keep])
    real_covariance = factors @ factors.T / beta

    momenta = all_momenta(n0)
    fourier_covariance = {
        tuple(K): terminal_covariance(K, L, beta=beta) for K in momenta
    }
    error = 0.0
    for displacement in itertools.product(range(n0), repeat=4):
        for a in range(6):
            for b in range(6):
                predicted = sum(
                    np.exp(-1j * np.dot(K, displacement))
                    * fourier_covariance[tuple(K)][a, b]
                    for K in momenta
                ) / n0**4
                actual = real_covariance[a, 6 * site(displacement, n0) + b]
                error = max(error, abs(predicted - actual))
    expected_rank = 3 * (fine**4 - 1)
    return error, int(keep.sum()), expected_rank, float(np.abs(real_covariance).max())


if __name__ == "__main__":
    cases = (
        (3, 1, False),
        (2, 2, False),
        (2, 2, True),
    )
    for n0, L, reverse in cases:
        error, rank, expected, scale = check(n0, L=L, reverse=reverse)
        print(
            f"n0={n0} L={L} reverse={reverse}: rank={rank}/{expected}, "
            f"max|Fourier-real|={error:.3e}, max|C|={scale:.6f}"
        )
