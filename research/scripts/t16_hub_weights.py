"""T16: geometric hub weights of the CMP 109 (0.4) average.
For each fine bond b: max_c omega_c({b}) (weight of contour triples of coarse bond c
through b, excluding the central path) and sum_c omega_c({b})."""
import sys, itertools, numpy as np
from t15_avg04 import Lat, all_bonds
for d, L in [(2,3),(2,5),(3,3),(3,5),(4,3)]:
    lat = Lat(d, L, 3 if d < 4 else 2); CB = list(lat.coarse_bonds())
    om = {}
    for c in CB:
        cen = set((b[0], b[1]) for b in lat.central(c))
        acc = {}
        for w, ell in lat.triples(c):
            for b in set((x[0], x[1]) for x in ell):
                acc[b] = acc.get(b, 0) + w
        for b, v in acc.items():
            if b in cen: continue
            om.setdefault(b, []).append(v)
    mx = max(max(v) for v in om.values()); sm = max(sum(v) for v in om.values())
    print(f"d={d} L={L}: max_b max_c omega_c(b) = {mx:.4f} (2*pi*max = {2*np.pi*mx:.3f}),  max_b sum_c omega_c(b) = {sm:.4f}", flush=True)
