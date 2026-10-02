"""Check of note 24 Lemma E: ||P_U - P_1||_{inf->inf} <= 2(2d+3)(7d+16) L r, r = max link angle."""
import numpy as np
from t15_fast import Avg, background, qlog
from t15_fastjac import jacobian_fast
from t15_avg04 import Lat
for d, L, Nc in [(2,3,3), (3,3,2)]:
    lat = Lat(d, L, Nc); A = Avg(lat); rng = np.random.default_rng(5)
    J1 = jacobian_fast(A, background(lat, A.FB, 'flat', 0, rng))
    for eps in (0.01, 0.03, 0.1):
        Uq = background(lat, A.FB, 'rough', eps, rng)
        r = max(np.linalg.norm(qlog(u)) for u in Uq)
        dJ = jacobian_fast(A, Uq) - J1
        nC, nF = len(A.CB), len(A.FB)
        norm = max(sum(np.linalg.norm(dJ[3*c:3*c+3, 3*b:3*b+3], 2) for c in range(nC)) for b in range(nF))
        bound = 2*(2*d+3)*(7*d+16)*L*r
        print(f"d={d} L={L} eps={eps}: r={r:.4f}  ||P_U-P_1|| = {norm:.4f}   Lemma E bound = {bound:.2f}   ratio/(L r) = {norm/(L*r):.3f}")
