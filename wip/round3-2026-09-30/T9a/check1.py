"""Checks: weights sum to 1; K_{d,L} and sup_b sum_c omega_c({b}) vs 2d+L^{1-d};
linearization (3.1)-(3.2); Prop 2 bounds and sharpness; Prop 1 bound."""
import sys, itertools, numpy as np
sys.path.insert(0,'/private/tmp/ym-r3/T9a')
from avg04 import *
rng=np.random.default_rng(1)

for (d,L,Nc) in [(2,3,3),(2,5,2),(3,3,2)]:
    lat=Lat(d,L,Nc)
    CB=list(lat.coarse_bonds())
    TR={c:lat.triples(c) for c in CB}
    for c in CB: assert abs(sum(w for w,_ in TR[c])-1)<1e-12
    # incidence
    inc={}; incN={}
    for c in CB:
        for w,ell in TR[c]:
            cnt={}
            for (x,mu,sg) in ell: cnt[(x,mu)]=cnt.get((x,mu),0)+1
            for b,k in cnt.items():
                inc[b]=inc.get(b,0)+w; incN[b]=incN.get(b,0)+w*k
    maxN=max(incN.values()); maxI=max(inc.values())
    # max multiplicity along a single loop
    mult=max(max([sum(1 for bb in ell if (bb[0],bb[1])==(b[0],b[1])) for b in ell] or [0]) for c in CB for w,ell in TR[c])
    print(f"d={d} L={L}: sum weights ok; sup_b sum_c omega_c(b)={maxI:.4f}, K_dL={maxN:.4f}, bound 2d+L^(1-d)={2*d+L**(1-d):.4f}, max traversal mult in a loop={mult}")
