"""T7 check 1: for Balaban's linear block average Q (research/10 (7.1)-(7.2)),
the coarse plaquette flux d_c(Q^N A) equals the fine flux dA smeared by
w_j = (L^N-box average) * (L^N x L^N square perpendicular to j).
Brute force on small tori; verifies the kernel used in t7_gauss3d.py."""
import itertools, numpy as np
from gauge3d_common import dmat, Qmat, site, PL, PERP
rng = np.random.default_rng(0)

def flux_kernel_apply(B, s, M):
    """B: plaquette fluxes on (Z/s)^3 indexed [3*site+o]; returns smeared
    fluxes on coarse lattice (Z/(s/M))^3 using the box*square kernel."""
    sc = s // M; out = np.zeros(3*sc**3)
    for y in itertools.product(range(sc), repeat=3):
        for o, (mu, nu) in enumerate(PL):
            tot = 0.0
            for u in itertools.product(range(M), repeat=3):
                for a in range(M):
                    for b in range(M):
                        x = [M*y[i] + u[i] for i in range(3)]
                        x[mu] += a; x[nu] += b
                        tot += B[3*site(x, s) + o]
            out[3*site(y, sc) + o] = tot / M**3
    return out

for (s, L, N) in [(4, 2, 1), (6, 3, 1), (8, 2, 2)]:
    A = rng.normal(size=3*s**3)
    V = A.copy(); cur = s
    for k in range(N):
        V = Qmat(cur, L) @ V; cur //= L
    lhs = dmat(cur) @ V
    rhs = flux_kernel_apply(dmat(s) @ A, s, L**N)
    print(f"s={s} L={L} N={N}: max|d_c Q^N A - w*dA| = {np.abs(lhs-rhs).max():.2e}")
