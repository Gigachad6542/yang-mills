"""T32: single-step Lipschitz structure of the 4D SU(2) Migdal-Kadanoff RG.

Plaquette weight f (class function on SU(2)) with character coefficients
c_m = a_m / (d_m a_0), m = 2j, d_m = m + 1, Casimir C2(m) = m(m+2)/4.
One MK step with L = 2 in d = 4:
    B (bond moving):  f -> f^(L^(d-2)) = f^4   (pointwise),
    D (decimation):   c_m -> c_m^(L^2) = c_m^4.
Coordinates: t from c_1 = exp(-t C2(1)); x = 1/t (inverse coupling, ~ 1/g^2);
u from a fit l_m = -log c_m = t C2 + u C2^2 over the visible range; the
dimensionless irrelevant coordinate is w = u / t^2.
We follow the flow from a heat-kernel start and compute the Jacobian of one
step in (x, w) by finite differences, and report
    e = |dx'/dx - 1|, c = |dx'/dw|, b = |dw'/dx|, theta = |dw'/dw|,
against t, to test note 29's assumptions: theta < 1, b, c = O(g^2) and
e = O(g^4) in suitable units.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 60
MMAX = 160
NQ = 6000


def setup():
    # Gauss-Legendre on [0, pi] for the Haar measure (2/pi) sin^2 phi dphi
    xs, ws = np.polynomial.legendre.leggauss(NQ)
    phi = (xs + 1) * np.pi / 2
    w = ws * np.pi / 2 * (2 / np.pi) * np.sin(phi) ** 2
    m = np.arange(MMAX + 1)
    chi = np.sin(np.outer(m + 1, phi)) / np.sin(phi)  # (M, Q)
    return phi, w, m, chi


PHI, WQ, MS, CHI = setup()
C2 = MS * (MS + 2) / 4.0


def logf_from_l(l):
    """log f on the grid from log-coefficients l_m = -log c_m (c_0 = 1)."""
    # f = sum d_m c_m chi_m ; use scaling to avoid underflow
    terms = (MS + 1)[:, None] * np.exp(-l)[:, None] * CHI
    f = terms.sum(0)
    return np.log(np.maximum(f, 1e-300))


def l_from_logf(logf):
    """log-coefficients of f (normalized so c_0 = 1), computed stably."""
    s = logf.max()
    f = np.exp(logf - s)
    a = (CHI * f[None, :] * WQ[None, :]).sum(1)  # a_m
    c = a / ((MS + 1) * a[0])
    c = np.maximum(c, 1e-300)
    return -np.log(c)


def step(l):
    logf = logf_from_l(l)
    l1 = l_from_logf(4.0 * logf)  # bond moving, f^4
    return 4.0 * l1               # decimation, c^4


def coords(l):
    t = l[1] / C2[1]
    vis = (t * C2 <= 8.0) & (MS >= 1)
    A = np.vstack([C2[vis], C2[vis] ** 2]).T
    (tt, u), *_ = np.linalg.lstsq(A, l[vis], rcond=None)
    return 1.0 / t, u / t**2


def from_coords(x, w):
    t = 1.0 / x
    u = w * t**2
    return t * C2 + u * C2**2


def jacobian(x, w, hx=1e-4, hw=1e-4):
    def F(x, w):
        return np.array(coords(step(from_coords(x, w))))
    f0 = F(x, w)
    dx = (F(x + hx * x, w) - F(x - hx * x, w)) / (2 * hx * x)
    dw = (F(x, w + hw) - F(x, w - hw)) / (2 * hw)
    return f0, np.array([dx, dw]).T  # J[i, j] = d out_i / d in_j


if __name__ == "__main__":
    print("t = 1/x | x' - x | e = |dx'/dx - 1| | c = |dx'/dw| | b = |dw'/dx| | theta = |dw'/dw| | w'")
    for t0 in [0.4, 0.2, 0.1, 0.05, 0.025]:
        x, w = 1.0 / t0, 0.0
        (x1, w1), J = jacobian(x, w)
        print(f"{t0:6.3f} | {x1 - x:+.5f} | {abs(J[0,0]-1):.3e} | {abs(J[0,1]):.3e} | "
              f"{abs(J[1,0]):.3e} | {abs(J[1,1]):.4f} | {w1:+.4f}", flush=True)


def off_shape_table():
    print("\nAway from the heat-kernel shape (w != 0):")
    print("t | w | e | c | b | theta | b*c")
    for t0 in [0.2, 0.05]:
        for w0 in [0.01, 0.02, 0.05]:  # w < 0 gives growing c_m: not a positive weight
            (x1, w1), J = jacobian(1.0 / t0, w0)
            e, c, b, th = abs(J[0, 0] - 1), abs(J[0, 1]), abs(J[1, 0]), abs(J[1, 1])
            print(f"{t0:5.3f} | {w0:+.2f} | {e:.3e} | {c:.3e} | {b:.3e} | {th:.4f} | {b*c:.3e}",
                  flush=True)


if __name__ == "__main__":
    off_shape_table()
