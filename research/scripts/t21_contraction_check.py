"""T21: worst-case check of note 29 Theorem 1 (shooting-form contraction).
delta_{k+1} = theta*delta_k + b*|Delta_k|,  Delta_{k+1} = Delta_k - c*delta_k - e*Delta_k (Delta decreasing to 0),
Delta_K = 0 fixed by shooting Delta_0 (bisection). Compare with delta_k <= 2*theta1^k*delta_0."""
import numpy as np
def run(D0, theta, b, c, e, K):
    d, D = 1.0, D0; ds = [d]; Ds = [D]
    for k in range(K):
        d, D = theta*d + b*abs(D), D - c*d - e*D
        ds.append(d); Ds.append(D)
    return np.array(ds), np.array(Ds)
for (theta, b, c, e) in [(0.3, 0.05, 0.05, 0.002), (0.5, 0.1, 0.05, 0.01), (0.3, 0.2, 0.2, 0.01)]:
    th1 = (1 + theta)/2
    cond = b*c <= 0.5*(th1 - theta)*(1 - th1 - e)
    for K in (10, 50, 200):
        lo, hi = 0.0, 10.0
        for _ in range(200):
            mid = (lo+hi)/2; ds, Ds = run(mid, theta, b, c, e, K)
            (lo, hi) = (mid, hi) if Ds[-1] < 0 else (lo, mid)
        ds, Ds = run(lo, theta, b, c, e, K)
        ratio = (ds/(2*th1**np.arange(K+1))).max()
        print(f"theta={theta} b={b} c={c} e={e} K={K:3d}  (2.1) holds={cond}  max delta_k/(2 theta1^k) = {ratio:.4f}  Delta_0={lo:.4f}")
