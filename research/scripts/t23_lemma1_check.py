"""Check of note 31 Lemma 1: E[f(U e^{igB})] - f(U) = O(g^2) for f = Re tr of a 4-link loop holonomy."""
import numpy as np
from t15_fast import qmul, qexp
rng = np.random.default_rng(0)
U = qexp(rng.normal(size=(4,3))*0.3)            # background links on a plaquette-like loop
def f(V):                                        # Re tr(V1 V2 V3 V4)/2 = scalar part of the quaternion product
    H = V[...,0,:]
    for i in range(1,4): H = qmul(H, V[...,i,:])
    return H[...,0]
f0 = f(U); S = 400000
B = rng.normal(size=(S,4,3))
for g in (0.4, 0.2, 0.1, 0.05):
    V = qmul(U[None], qexp(g*B))
    d = f(V).mean() - f0
    print(f"g={g:5.2f}  E f(Ue^(igB)) - f(U) = {d:+.6e}   /g^2 = {d/g**2:+.5f}")
