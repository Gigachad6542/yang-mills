"""T79 Part A: obstruction to ANY Haar-preserving T with q(T U) = R q(U) on a
single coarse bond of axis 0 or 1 (beta = 0).

If T: Omega_{N+1} -> Omega_{N+1} preserves Haar measure and q(TU)_c = -q(U)_c,
q(TU)_{c'} = q(U)_{c'} (c' != c), then for every coarse plaquette p containing c
once,  E_Haar[ (1/2) tr hol_q(p) ] = E[ (1/2) tr hol_{q(TU)}(p) ] = -E[...] = 0.
So a nonzero Monte-Carlo mean of (1/2) tr hol_q(p) for a plaquette p in the plane
(0,1) refutes such a T (any bond of p, any axis in {0,1}); the planes (0,2), (1,2)
contain a last-axis bond, where T exists (note 64 Lemma 64.5a), so those means
must vanish: they are the control.
d = 3, torus, coarse side 3, L given, links iid Haar, q = CMP 98 (42).

usage: python3 t79_center_obstruction.py L N seed
"""
import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t47_average_jacobian as t  # noqa: E402
import t74_extension_check as t74  # noqa: E402
from t74_extension_check import Torus  # noqa: E402


def e_(mu):
    v = np.zeros(3, dtype=int)
    v[mu] = 1
    return v


def sample(L, n, seed):
    np.random.seed(seed % (2 ** 32))
    s = n * L
    T = Torus(s)
    keys = [(x, mu) for x in itertools.product(range(s), repeat=3)
            for mu in range(3)]
    H = t.haar(len(keys))
    for k, h in zip(keys, H):
        T.U[k] = h
    return T


def plaq_trace(T, L, n, y, mu, nu):
    ym = tuple((np.array(y) + e_(mu)) % n)
    yn = tuple((np.array(y) + e_(nu)) % n)

    def g(yy, m):
        return t74.q_full(T, L, m, tuple(L * c for c in yy))

    P = g(y, mu) @ g(ym, nu) @ g(yn, mu).conj().T @ g(y, nu).conj().T
    return float(np.real(P[0, 0] + P[1, 1]) / 2)


def run(L, N, seed):
    n = 3
    planes = {"(0,1)": (0, 1), "(0,2)": (0, 2), "(1,2)": (1, 2)}
    acc = {k: [] for k in planes}
    for i in range(N):
        T = sample(L, n, seed * 1000003 + i)
        for k, (mu, nu) in planes.items():
            acc[k].append(plaq_trace(T, L, n, (0, 0, 0), mu, nu))
    print(f"L={L}, N={N} samples, coarse side 3, seed {seed} (links iid Haar)")
    for k, v in acc.items():
        v = np.array(v)
        m, se = v.mean(), v.std(ddof=1) / np.sqrt(len(v))
        print(f"  plane {k}: mean (1/2)tr hol_q(p) = {m:+.4f} +- {se:.4f}"
              f"  ({m / se:+.1f} sigma)")


if __name__ == "__main__":
    run(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
