"""T73: numerical value of the Lemma R majorants (research/50 sec 2.6.3).

C_ab := int_{(-pi,pi]^4} dk/(2 pi)^4  S_a(k) S_b(k) / C(k),
  S_a(k) = sum_m |q_m|^a |what_1(q_m)| / q_m^2,   C(k) = sum_m |what_1(q_m)|^2 / q_m^2,  q_m = k + 2 pi m,
so that |d_x^a d_y^b R_1(x,y)| <= C_ab for all x, y.  The integrand ~ |k|^{a+b-2} at k -> 0
(integrable in 4D); an offset grid is used and the N-dependence printed (error ~ N^-2).
"""
import itertools
import numpy as np

TWO_PI = 2 * np.pi


def integrand_grid(N, NM):
    g = (np.arange(N) + 0.5) * TWO_PI / N - np.pi
    m1 = np.arange(-NM, NM + 1, dtype=float)
    # per-coordinate tables: q (N, n), |what_j| = 2|sin(k/2)|/|q|
    q = g[:, None] + TWO_PI * m1[None, :]
    wj = 2 * np.abs(np.sin(g[:, None] / 2)) / np.abs(q)
    q2 = q**2
    n = len(m1)
    return g, q, wj, q2


def compute(N, NM):
    g, q, wj, q2 = integrand_grid(N, NM)
    n = q.shape[1]
    tot = {"00": 0.0, "01": 0.0, "11": 0.0}
    # loop over k0, k1 (N^2), vectorize over (k2,k3,m0..m3)
    for i0 in range(N):
        for i1 in range(i0, N):
            wgt = 1 if i0 == i1 else 2
            # shape (k2, k3, m0, m1, m2, m3)
            qq2 = (q2[i0][None, None, :, None, None, None]
                   + q2[i1][None, None, None, :, None, None]
                   + q2[:, None, None, None, :, None]
                   + q2[None, :, None, None, None, :])
            # m2 axis pairs with k2 -> shape trick: q2[:,None,...,:,None] has axes (k2, ., ., ., m2, .)
            ww = (wj[i0][None, None, :, None, None, None]
                  * wj[i1][None, None, None, :, None, None]
                  * wj[:, None, None, None, :, None]
                  * wj[None, :, None, None, None, :])
            qa = np.sqrt(qq2)
            base = ww / qq2
            S0 = base.sum((2, 3, 4, 5))
            S1 = (base * qa).sum((2, 3, 4, 5))
            Cc = (ww**2 / qq2).sum((2, 3, 4, 5))
            tot["00"] += wgt * (S0 * S0 / Cc).sum()
            tot["01"] += wgt * (S0 * S1 / Cc).sum()
            tot["11"] += wgt * (S1 * S1 / Cc).sum()
    return {k: v / N**4 for k, v in tot.items()}


if __name__ == "__main__":
    for N in (4, 6, 8, 12):
        r = compute(N, 2)
        print(f"N={N:3d} NM=2: C_00 = {r['00']:.5f}  C_01 = {r['01']:.5f}  C_11 = {r['11']:.5f}", flush=True)
