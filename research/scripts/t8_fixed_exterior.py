"""T8: exact one-fiber Gaussian calculation at fixed exterior data.

The local fiber coordinate Y has conditional law N(h,sigma^2).  The same
quadratic defect used in t8_gauss4d.py tilts it by exp(-lambda*Y^2/2).
The terminal loop sees x+a_M Y, with a_M=M^-2, the scale of a central
plaquette coefficient in the exact 4D block-flux kernel.
"""

from __future__ import annotations

import numpy as np


def loop_expectation(a, exterior_phase, h, variance):
    return np.exp(-0.5 * a * a * variance) * np.cos(exterior_phase + a * h)


def fixed_exterior_shift(M, h, lam=1.0, variance=1.0, exterior_phase=0.7):
    a = M**-2
    tilted_variance = variance / (1.0 + lam * variance)
    tilted_mean = h / (1.0 + lam * variance)
    before = loop_expectation(a, exterior_phase, h, variance)
    after = loop_expectation(a, exterior_phase, tilted_mean, tilted_variance)
    return after - before


if __name__ == "__main__":
    print("lambda=1, sigma^2=1, terminal coefficient a_M=M^-2")
    local_mean_shift = 0.5 - 1.0
    local_loop_shift = np.exp(-0.25) * np.cos(0.5) - np.exp(-0.5) * np.cos(1.0)
    print(
        "at h=1 the normalized local fiber shifts are independent of M: "
        f"Delta E[Y]={local_mean_shift:.6f}, Delta E[cos Y]={local_loop_shift:.9f}"
    )
    print("M    h=0 shift       h=1 shift       h=M^2 shift")
    for M in (2, 4, 8, 16, 32, 64):
        symmetric = fixed_exterior_shift(M, 0.0)
        bounded = fixed_exterior_shift(M, 1.0)
        uniform_counterexample = fixed_exterior_shift(M, float(M * M))
        print(
            f"{M:2d}  {symmetric: .8e}  {bounded: .8e}  "
            f"{uniform_counterexample: .8e}"
        )
