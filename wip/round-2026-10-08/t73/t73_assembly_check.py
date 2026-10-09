"""T73: check the rank-one assembly in t73_scalar_loop.bubble against dense linear algebra.

For L = 2, 3 and one sector K, build the dense alias matrices Gamma(K), Gamma(K') on the
truncated alias lattice (all classes a and m in [-NM,NM]^4), the diagonal vertices V_0, V_1,
and compare Tr[Gamma V_0 Gamma' V_1^*] with the closed rank-one formula.  Also check
Gamma >= 0 with rank L^4 - 1, and Q_L-annihilation: what_L^* Gamma = 0 (exactly, up to rounding).
"""
import itertools
import numpy as np
from t73_scalar_loop import bubble, what, TWO_PI


def dense(L, K, P, NM):
    m = np.array(list(itertools.product(range(-NM, NM + 1), repeat=4)), dtype=float)
    a = np.array(list(itertools.product(range(L), repeat=4)), dtype=float)
    kap = (K[None, :] + TWO_PI * a) / L
    kap = kap - TWO_PI * np.round(kap / TWO_PI)
    q = (kap[:, None, :] + TWO_PI * m[None, :, :] + P).reshape(-1, 4)  # shifted by P
    nal = len(m)
    cls = np.repeat(np.arange(len(a)), nal)
    q2 = (q * q).sum(-1)
    wu, wv = what(q, 1.0), what(q, float(L))
    Gam = np.zeros((len(q), len(q)), dtype=complex)
    for c in range(len(a)):
        idx = np.where(cls == c)[0]
        u = wu[idx] / q2[idx]
        Cc = (np.abs(wu[idx]) ** 2 / q2[idx]).sum()
        Gam[np.ix_(idx, idx)] += np.outer(u, np.conj(u)) / Cc
    v = wv / q2
    Cv = (np.abs(wv) ** 2 / q2).sum()
    Gam -= np.outer(v, np.conj(v)) / Cv
    return Gam, q, v, wv


if __name__ == "__main__":
    rng = np.random.default_rng(1)
    for L, NM in ((2, 1), (3, 0)):
        K = rng.uniform(-3, 3, 4)
        P = np.array([0.07, 0.05, 0.0, 0.0])
        G1, q1, v1, wv1 = dense(L, K, 0 * P, NM)
        G2s, qs, v2s, _ = dense(L, K, P, NM)  # sector K' = K + L P: the q's shifted by P
        V0 = np.diag(2 * q1[:, 0] + P[0])
        V1 = np.diag(2 * q1[:, 1] + P[1])
        tr_dense = np.trace(G1 @ V0 @ G2s @ V1.conj().T)
        tr_fast = bubble(L, K, P, NM)
        ev = np.linalg.eigvalsh((G1 + G1.conj().T) / 2)
        rk = int((ev > 1e-10 * ev.max()).sum())
        print(f"L={L}: dense trace = {tr_dense:.10e}  rank-one formula = {tr_fast:.10e}  "
              f"rel diff = {abs(tr_dense - tr_fast) / abs(tr_dense):.1e};  "
              f"Gamma eig range [{ev.min():.1e},{ev.max():.2e}], rank {rk} (expected {L**4 - 1}); "
              f"|what_L^* Gamma| = {np.abs(wv1.conj() @ G1).max():.1e} (|Gamma| max {np.abs(G1).max():.1e})")
