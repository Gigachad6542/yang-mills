"""T51: d-dimensional SU(2) Monte Carlo with Balaban's iterated average.

Generalizes t50 (d = 3) to any d. Used in d = 4 for a universality test of
the coupling flow (H0):

- at depth N, on the lattice (Z/(n0 2^N))^4, run Wilson SU(2) at several
  beta;
- map each configuration N times through Balaban's average to the terminal
  lattice (Z/n0)^4, and measure the terminal plaquette P and 1x2 loop W12;
- interpolate in beta to the beta_N(*) at which the terminal P equals a
  fixed target (matching). Universality predicts that W12 at beta_N(*)
  converges as N grows, and that beta_N(*) - beta_{N-1}(*) approaches the
  asymptotic-freedom step 4 * 2 b_0 log 2 + O(g^2) (SU(2): b_0 = 11/(24 pi^2)).

Usage: python3 t51_mc_universality_4d.py SEED D N n0 beta1 [beta2 ...]
"""
import sys
import time
import itertools
import numpy as np

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import t50_mc_terminal_convergence as q   # quaternion algebra

qmul, qinv, qlog, qexp, qnormalize = q.qmul, q.qinv, q.qlog, q.qexp, q.qnormalize
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 51)
q.rng = rng


def shift(a, mu, k):
    return np.roll(a, -k, axis=mu)


def cold(D, n):
    U = np.zeros((D,) + (n,) * D + (4,))
    U[..., 0] = 1.0
    return U


def staple_sum(U, mu):
    D = U.shape[0]
    S = np.zeros(U.shape[1:])
    for nu in range(D):
        if nu == mu:
            continue
        f = qmul(qmul(shift(U[nu], mu, 1), qinv(shift(U[mu], nu, 1))), qinv(U[nu]))
        Unm = shift(U[nu], nu, -1)
        b = qmul(qmul(qinv(shift(Unm, mu, 1)), qinv(shift(U[mu], nu, -1))), Unm)
        S += f + b
    return S


def parity_mask(D, n):
    x = np.indices((n,) * D).sum(axis=0)
    return (x % 2 == 0), (x % 2 == 1)


def heatbath(U, beta, masks):
    for mu in range(U.shape[0]):
        for m in masks:
            S = staple_sum(U, mu)[m]
            k = np.linalg.norm(S, axis=-1)
            Vbar = S / k[:, None]
            a0 = q.sample_a0(beta * k)
            v = rng.normal(size=(len(k), 3))
            v /= np.linalg.norm(v, axis=-1, keepdims=True)
            X = np.concatenate([a0[:, None],
                                np.sqrt(np.maximum(1 - a0 ** 2, 0))[:, None] * v], axis=-1)
            U[mu][m] = qnormalize(qmul(X, qinv(Vbar)))


def overrelax(U, masks):
    for mu in range(U.shape[0]):
        for m in masks:
            S = staple_sum(U, mu)[m]
            Vi = qinv(S / np.linalg.norm(S, axis=-1, keepdims=True))
            U[mu][m] = qnormalize(qmul(qmul(Vi, qinv(U[mu][m])), Vi))


def plaq(U):
    D = U.shape[0]
    tot, cnt = 0.0, 0
    for mu in range(D):
        for nu in range(mu + 1, D):
            p = qmul(qmul(U[mu], shift(U[nu], mu, 1)),
                     qmul(qinv(shift(U[mu], nu, 1)), qinv(U[nu])))
            tot += p[..., 0].mean(); cnt += 1
    return tot / cnt


def path_product(U, steps):
    D = U.shape[0]
    out = np.zeros(U.shape[1:]); out[..., 0] = 1.0
    pos = np.zeros(D, int)
    for mu, s in steps:
        off = pos.copy()
        if s == 1:
            link = U[mu]
        else:
            off[mu] -= 1
            link = qinv(U[mu])
        l = link
        for ax in range(D):
            if off[ax]:
                l = np.roll(l, -off[ax], axis=ax)
        out = qmul(out, l)
        pos[mu] += s
    return out


def gamma_steps(src, dst):
    steps, cur = [], list(src)
    for mu in range(len(src)):
        while cur[mu] != dst[mu]:
            s = 1 if dst[mu] > cur[mu] else -1
            steps.append((mu, s)); cur[mu] += s
    return steps


def average(U, L):
    D, n = U.shape[0], U.shape[1]
    nc = n // L
    V = np.zeros((D,) + (nc,) * D + (4,))
    offs = list(itertools.product(range(L), repeat=D))
    sl = (slice(None, None, L),) * D
    for mu in range(D):
        e = [0] * D; e[mu] = L
        X = path_product(U, [(mu, 1)] * L)
        Xi = qinv(X)
        acc = np.zeros(U.shape[1:-1] + (3,))
        for x in offs:
            xc = tuple(x[i] + e[i] for i in range(D))
            steps = gamma_steps((0,) * D, x) + [(mu, 1)] * L + gamma_steps(xc, tuple(e))
            acc += qlog(qmul(path_product(U, steps), Xi))
        V[mu] = qmul(qexp(acc / L ** D), X)[sl]
    return V


def w12(V):
    D = V.shape[0]
    W, cnt = 0.0, 0
    for mu in range(D):
        for nu in range(D):
            if mu == nu:
                continue
            a = qmul(V[mu], shift(V[mu], mu, 1))
            b = qmul(shift(V[nu], mu, 2), qinv(shift(shift(V[mu], nu, 1), mu, 1)))
            c = qmul(qinv(shift(V[mu], nu, 1)), qinv(V[nu]))
            W += qmul(qmul(a, b), c)[..., 0].mean(); cnt += 1
    return W / cnt


def run(D, N, n0, beta, L=2, ntherm=150, nmeas=200, every=2):
    n = n0 * L ** N
    U = cold(D, n)
    masks = parity_mask(D, n)
    t0 = time.time()
    for _ in range(ntherm):
        heatbath(U, beta, masks); overrelax(U, masks)
    data = []
    for _ in range(nmeas):
        for _ in range(every):
            heatbath(U, beta, masks); overrelax(U, masks)
        V = U
        for _ in range(N):
            V = average(V, L)
        data.append((plaq(V), w12(V), plaq(U)))
    data = np.array(data)
    nb = 10
    bl = data[: (len(data) // nb) * nb].reshape(nb, -1, 3).mean(axis=1)
    m, e = bl.mean(0), bl.std(0, ddof=1) / np.sqrt(nb)
    print(f"D={D} N={N} n={n} beta={beta:.4f}: P={m[0]:.5f}({e[0]:.5f}) "
          f"W12={m[1]:.5f}({e[1]:.5f}) fine plaq={m[2]:.5f} [{time.time()-t0:.0f}s]",
          flush=True)
    return m, e


if __name__ == "__main__":
    D, N, n0 = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    for b in sys.argv[5:]:
        run(D, N, n0, float(b))
