"""T8: exact 4D Gaussian gauge-field power counting.

The fine lattice is (Z/(n0*M))^4, M=L^m, with action

    (beta/2) * ||dA||_2^2.

For Balaban's linear block average, the terminal plaquette flux has Fourier
kernel

    w_{mu,nu}(p) = M^-4 prod_j D_M(p_j) D_M(p_mu) D_M(p_nu),
    D_M(q) = sum_{a=0}^{M-1} exp(-i q a).

The fine flux covariance is beta^-1 times the orthogonal projector onto
exact two-forms.  This file evaluates the resulting alias sum and the
connected response of a terminal small loop to one local quadratic defect.
"""

from __future__ import annotations

import itertools
import numpy as np


PLAQ = tuple((mu, nu) for mu in range(4) for nu in range(mu + 1, 4))


def dirichlet(q: np.ndarray, M: int) -> np.ndarray:
    """D_M(q), evaluated without the removable 0/0 singularity."""
    q = np.asarray(q, dtype=float)
    den = 1.0 - np.exp(-1j * q)
    out = np.empty(q.shape, dtype=complex)
    regular = np.abs(den) >= 1.0e-13
    out[~regular] = M
    out[regular] = (1.0 - np.exp(-1j * M * q[regular])) / den[regular]
    return out


def _alias_data(K: np.ndarray, M: int):
    aliases = np.arange(M)
    momenta = [(K[j] + 2.0 * np.pi * aliases) / M for j in range(4)]
    dm = [dirichlet(p, M) for p in momenta]
    pgrid = np.meshgrid(*momenta, indexing="ij", sparse=True)
    dgrid = np.meshgrid(*dm, indexing="ij", sparse=True)
    r = [np.exp(1j * p) - 1.0 for p in pgrid]
    r2 = sum(np.abs(x) ** 2 for x in r)
    nonzero = r2 > 1.0e-24
    return dgrid, r, r2, nonzero


def _projector_entry(a, b, r, r2, nonzero):
    """Entry of E E*/|r|^2 on two-forms, E_{mu nu,a}=r_mu delta_nu,a-..."""
    mu, nu = a
    rho, sigma = b
    ha = [r[mu] * (nu == j) - r[nu] * (mu == j) for j in range(4)]
    hb = [r[rho] * (sigma == j) - r[sigma] * (rho == j) for j in range(4)]
    safe = np.where(nonzero, r2, 1.0)
    value = sum(ha[j] * np.conj(hb[j]) for j in range(4)) / safe
    return np.where(nonzero, value, 0.0)


def terminal_covariance(K, M: int, beta: float = 1.0) -> np.ndarray:
    """Six-by-six covariance at one terminal momentum K.

    The orientation order is (01,02,03,12,13,23).  Fourier transforms on
    both lattices are unnormalized; the aliasing prefactor is 1/(beta*M^4).
    """
    K = np.asarray(K, dtype=float)
    dgrid, r, r2, nonzero = _alias_data(K, M)
    base = np.ones((M,) * 4, dtype=complex) / M**4
    for factor in dgrid:
        base *= factor
    kernels = []
    for mu, nu in PLAQ:
        kernels.append(base * dgrid[mu] * dgrid[nu])

    cov = np.empty((6, 6), dtype=complex)
    for ia, a in enumerate(PLAQ):
        for ib, b in enumerate(PLAQ):
            projector = _projector_entry(a, b, r, r2, nonzero)
            cov[ia, ib] = np.sum(
                projector * np.conj(kernels[ia]) * kernels[ib]
            ) / (beta * M**4)
    return cov


def terminal_entry(K, M: int, orientation=(0, 1), beta: float = 1.0) -> float:
    """Diagonal terminal covariance entry, without constructing all 36 entries."""
    K = np.asarray(K, dtype=float)
    dgrid, r, r2, nonzero = _alias_data(K, M)
    kernel = np.ones((M,) * 4, dtype=complex) / M**4
    for factor in dgrid:
        kernel *= factor
    for direction in orientation:
        kernel *= dgrid[direction]
    mu, nu = orientation
    safe = np.where(nonzero, r2, 1.0)
    projector = (np.abs(r[mu]) ** 2 + np.abs(r[nu]) ** 2) / safe
    projector = np.where(nonzero, projector, 0.0)
    return float(np.sum(projector * np.abs(kernel) ** 2).real / (beta * M**4))


def terminal_local_variance(n0: int, M: int, beta: float = 1.0) -> float:
    """Variance of the 01 terminal plaquette flux at one terminal site."""
    coarse_momenta = 2.0 * np.pi * np.arange(n0) / n0
    total = sum(
        terminal_entry(K, M, beta=beta)
        for K in itertools.product(coarse_momenta, repeat=4)
    )
    return total / n0**4


def registered_cross_covariance(M: int, n0: int = 2, beta: float = 1.0) -> float:
    """Cov(Phi_01(0), F_01(z_M)) at a registered local placement.

    z_M=(M-1,M-1,M/2,M/2) for even M.  This placement attains the maximum
    absolute covariance for M=2,4,8,16 (up to reflected/translated ties).
    The p0 loop keeps the M=32 computation small in memory.
    """
    if M % 2:
        raise ValueError("the registered placement is defined for even M")
    n = n0 * M
    p = 2.0 * np.pi * np.arange(n) / n
    dm = dirichlet(p, M)
    z = np.array((M - 1, M - 1, M // 2, M // 2))

    p1, p2, p3 = np.meshgrid(p, p, p, indexing="ij")
    one = np.ones_like(p1)
    phase123 = np.exp(-1j * (p1 * z[1] + p2 * z[2] + p3 * z[3]))
    total = 0.0j
    for q0, p0 in enumerate(p):
        pgrid = (p0 * one, p1, p2, p3)
        dgrid = (
            dm[q0] * one,
            dm[:, None, None] * one,
            dm[None, :, None] * one,
            dm[None, None, :] * one,
        )
        r = [np.exp(1j * q) - 1.0 for q in pgrid]
        r2 = sum(np.abs(x) ** 2 for x in r)
        nonzero = r2 > 1.0e-24
        safe = np.where(nonzero, r2, 1.0)
        projector = (np.abs(r[0]) ** 2 + np.abs(r[1]) ** 2) / safe
        projector = np.where(nonzero, projector, 0.0)

        kernel = one.astype(complex) / M**4
        for factor in dgrid:
            kernel *= factor
        kernel *= dgrid[0] * dgrid[1]
        phase = np.exp(-1j * p0 * z[0]) * phase123
        total += np.sum(phase * np.conj(kernel) * projector)
    return float((total / (beta * n**4)).real)


def maximum_cross_covariance(M: int, n0: int = 2, beta: float = 1.0):
    """Maximum |Cov(Phi_01(0),F_01(z))| over z, for small verification runs."""
    n = n0 * M
    p = 2.0 * np.pi * np.arange(n) / n
    dm = dirichlet(p, M)
    pgrid = np.meshgrid(p, p, p, p, indexing="ij", sparse=True)
    dgrid = np.meshgrid(dm, dm, dm, dm, indexing="ij", sparse=True)
    r = [np.exp(1j * q) - 1.0 for q in pgrid]
    r2 = sum(np.abs(x) ** 2 for x in r)
    nonzero = r2 > 1.0e-24
    safe = np.where(nonzero, r2, 1.0)
    projector = (np.abs(r[0]) ** 2 + np.abs(r[1]) ** 2) / safe
    projector = np.where(nonzero, projector, 0.0)

    kernel = np.ones((n,) * 4, dtype=complex) / M**4
    for factor in dgrid:
        kernel *= factor
    kernel *= dgrid[0] * dgrid[1]
    field = np.fft.fftn(np.conj(kernel) * projector).real / (beta * n**4)
    location = np.unravel_index(np.argmax(np.abs(field)), field.shape)
    return float(field[location]), location


def run_table():
    rows = []
    previous = None
    for M in (2, 4, 8, 16, 32):
        cross = registered_cross_covariance(M)
        var_terminal = terminal_local_variance(2, M)
        # For W=cos(Phi) and H=F_01(z)^2, Wick's formula gives
        # Cov(W,H)=-exp(-Var(Phi)/2)*cross^2.
        response = np.exp(-0.5 * var_terminal) * cross**2
        ratio = None if previous is None else previous / response
        rows.append((M, cross, M * M * cross, var_terminal, response, ratio))
        previous = response

    fit_rows = rows[1:]  # M >= 4
    exponent = -np.polyfit(
        np.log([row[0] for row in fit_rows]),
        np.log([row[4] for row in fit_rows]),
        1,
    )[0]

    print("n0=2, beta=1, a=b=(0,1), z_M=(M-1,M-1,M/2,M/2)")
    print("M       c_M          M^2 c_M      Var(Phi)      |Cov(cos Phi,F^2)|   ratio")
    for M, cross, scaled, variance, response, ratio in rows:
        tail = "" if ratio is None else f"  {ratio:8.4f}"
        print(
            f"{M:2d}  {cross: .9e}  {scaled: .9f}  {variance: .9f}  "
            f"{response: .9e}{tail}"
        )
    print(f"log-log fitted exponent on M=4,8,16,32: {exponent:.6f}")
    print("registered-placement maximum check")
    for M in (2, 4, 8, 16):
        registered = registered_cross_covariance(M)
        maximum, location = maximum_cross_covariance(M)
        print(
            f"  M={M:2d}: |registered|/max={abs(registered/maximum):.12f}, "
            f"one maximizing z={location}"
        )


if __name__ == "__main__":
    run_table()
