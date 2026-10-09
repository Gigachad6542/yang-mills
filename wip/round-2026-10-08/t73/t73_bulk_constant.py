"""T73: the bulk constant kappa_0 = 1/(24 pi^2), two independent ways.

(a) position space: with Gamma = G0 = 1/(4 pi^2 r^2) the kernel of note 50 sec 2.6.2 is
      F_{01}(r) = 2 [Gamma d_x0 d_y1 Gamma - d_x0 Gamma d_y1 Gamma] = -2 G0 G0_{01} + 2 G0_0 G0_1,
    homogeneous of degree -6, and b_bulk = (int_{S^3} (-n_0 n_1) F_{01}(n) dOmega) * int dr/r.
(b) momentum space: coefficient of P_0 P_1 in (2q+P)_0 (2q+P)_1 / (q^2 (q+P)^2), obtained by a
    4-point finite-difference mixed derivative, angular-averaged on |q| = 1 (degree -4 homogeneity),
    weighted by dOmega/(2 pi)^4.
"""
import numpy as np


def sphere_quadrature(n=24):
    """Gauss-Legendre product rule on S^3: n = (cos a, sin a cos b, sin a sin b cos c, sin a sin b sin c)."""
    x, w = np.polynomial.legendre.leggauss(n)
    a = (x + 1) * np.pi / 2
    wa = w * np.pi / 2
    b = a.copy()
    wb = wa.copy()
    c = (x + 1) * np.pi  # [0, 2 pi]
    wc = w * np.pi
    A, B, C = np.meshgrid(a, b, c, indexing="ij")
    W = wa[:, None, None] * wb[None, :, None] * wc[None, None, :] * np.sin(A) ** 2 * np.sin(B)
    pts = np.stack([np.cos(A), np.sin(A) * np.cos(B), np.sin(A) * np.sin(B) * np.cos(C),
                    np.sin(A) * np.sin(B) * np.sin(C)], -1)
    return pts.reshape(-1, 4), W.reshape(-1)


def main():
    pts, W = sphere_quadrature()
    print(f"area of S^3 = {W.sum():.10f}  (2 pi^2 = {2 * np.pi**2:.10f})")
    # (a) position space, r = 1 (homogeneous of degree -4 after r^2 * r^3 dr measure)
    r2 = 1.0
    n0, n1 = pts[:, 0], pts[:, 1]
    G = 1 / (4 * np.pi**2)  # G0 at |r| = 1
    G_0 = -n0 / (2 * np.pi**2)
    G_1 = -n1 / (2 * np.pi**2)
    G_01 = 2 * n0 * n1 / np.pi**2
    F = -2 * G * G_01 + 2 * G_0 * G_1
    # F_{mu nu}(x,y) = 2 [Gamma d_x d_y Gamma - d_x Gamma d_y Gamma]; for Gamma = G0(x-y):
    #   d_x d_y Gamma = -G_{mu nu}(r), d_x Gamma = G_mu, d_y Gamma = -G_nu  ->  F = -2 G G_{mu nu} + 2 G_mu G_nu
    ka = (W * (-n0 * n1) * F).sum()
    # (b) momentum space
    h = 1e-3

    def f(P0, P1):
        q = pts
        N = (2 * q[:, 0] + P0) * (2 * q[:, 1] + P1)
        qp0, qp1 = q[:, 0] + P0, q[:, 1] + P1
        qp2 = qp0**2 + qp1**2 + q[:, 2] ** 2 + q[:, 3] ** 2
        return N / (1.0 * qp2)

    mixed = (f(h, h) - f(h, -h) - f(-h, h) + f(-h, -h)) / (4 * h * h)
    kb = (W * mixed).sum() / (2 * np.pi) ** 4
    print(f"kappa_0 (a) position space  = {ka:.10f}")
    print(f"kappa_0 (b) momentum space  = {kb:.10f}")
    print(f"1/(24 pi^2)                 = {1 / (24 * np.pi**2):.10f}")


if __name__ == "__main__":
    main()
