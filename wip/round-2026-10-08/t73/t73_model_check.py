"""T73 step 1: exact finite-lattice check of the free-step covariance in note 48's model.

Scalar toy, fine torus (Z/N)^d, d = 2, box averages Q_s (s^d cells), N = M*L*n0.
Claim (research/50 sec 2.6.1):
  Gamma := H_M C_L H_M^T = G_{Q_LM} - G_{Q_M} = R_M - R_LM,
where H_M = G0 Q_M^T C_M^{-1} is the minimizer map, C_M = Q_M G0 Q_M^T, C_L is the
covariance of the level-M averages B conditioned on Q_L B = 0, and
R_Q = G0 Q^T (Q G0 Q^T)^{-1} Q G0.
Exact linear algebra only (np.linalg.solve / inv / eigvalsh); no pinv.
"""
import itertools
import numpy as np


def boxavg(N, s, d):
    """Q_s: (N/s)^d x N^d matrix of s^d-box averages."""
    n = N // s
    Q = np.zeros((n**d, N**d))
    for jj, j in enumerate(itertools.product(range(n), repeat=d)):
        for off in itertools.product(range(s), repeat=d):
            x = tuple((s * j[i] + off[i]) % N for i in range(d))
            Q[jj, np.ravel_multi_index(x, (N,) * d)] = 1.0 / s**d
    return Q


def G0(N, d, m2):
    """(-Lap + m2)^{-1} on the torus, dense (a mass keeps G0 positive definite; the
    identity tested is pure conditioning algebra and holds for any positive G0)."""
    sites = list(itertools.product(range(N), repeat=d))
    idx = {x: i for i, x in enumerate(sites)}
    A = np.zeros((N**d, N**d))
    for x in sites:
        i = idx[x]
        A[i, i] += 2 * d + m2
        for k in range(d):
            for sgn in (1, -1):
                y = list(x)
                y[k] = (y[k] + sgn) % N
                A[i, idx[tuple(y)]] -= 1.0
    return np.linalg.inv(A)


def run(d, M, L, n0, m2=0.3):
    N = M * L * n0
    G = G0(N, d, m2)
    QM, QLM = boxavg(N, M, d), boxavg(N, M * L, d)
    CM = QM @ G @ QM.T
    H = G @ QM.T @ np.linalg.inv(CM)  # minimizer map
    QL = boxavg(N // M, L, d)  # block average on the level-M lattice
    CL = CM - CM @ QL.T @ np.linalg.solve(QL @ CM @ QL.T, QL @ CM)  # B | Q_L B = 0
    Gam = H @ CL @ H.T

    def R(Q):
        return G @ Q.T @ np.linalg.solve(Q @ G @ Q.T, Q @ G)

    D = (G - R(QLM)) - (G - R(QM))
    err1 = np.abs(Gam - D).max() / np.abs(D).max()
    ev = np.linalg.eigvalsh((D + D.T) / 2)
    rank = int((ev > 1e-10 * ev.max()).sum())
    err2 = np.abs(D - (R(QM) - R(QLM))).max() / np.abs(D).max()
    err3 = np.abs(QLM @ Gam).max() / np.abs(Gam).max()
    return N, err1, err2, err3, rank, (L**d - 1) * n0**d, ev.min()


if __name__ == "__main__":
    for (d, M, L, n0) in [(2, 2, 2, 2), (2, 2, 3, 2), (2, 3, 2, 2), (2, 2, 2, 3)]:
        N, e1, e2, e3, r, rexp, emin = run(d, M, L, n0)
        print(f"d={d} M={M} L={L} n0={n0} N={N}: rel|H C_L H^T - (G_QLM - G_QM)|={e1:.1e}  "
              f"rel|G_QLM - G_QM - (R_M - R_LM)|={e2:.1e}  rel|Q_LM Gamma|={e3:.1e}  "
              f"rank={r} (expected {rexp})  min eig={emin:.1e}")
