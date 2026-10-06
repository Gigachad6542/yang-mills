"""T50: Monte Carlo test of M1-3D: convergence of terminal block observables.

SU(2) Wilson action in d = 3 on the periodic lattice (Z/(n0 L^N))^3 with
beta_N = beta0 * L^N (CMP 102 (1): beta_N = 1/(g^2 eps_N), so g^2 eps_0 is
fixed). Each configuration is mapped N times through Balaban's one-step
average (CMP 98 (42), corner blocks, CMP 95 (1.7) contours) down to the
terminal lattice (Z/n0)^3. The terminal observables are:

- P   = <(1/2) tr V(dp)>, the averaged-field plaquette, per terminal plaquette;
- W12 = <(1/2) tr V(1x2 loop)>;
- PL2 = <|(1/2) tr Polyakov loop|^2>.

M1-3D predicts that these converge as N -> infinity, with increments
decaying geometrically (note 18 Theorem 1).

Updates: checkerboard heat bath (Creutz algorithm) plus over-relaxation.
SU(2) elements are stored as unit quaternions (a0, a1, a2, a3), meaning
a0 + i a.sigma.
"""
import sys
import time
import os
import numpy as np

HOT = os.environ.get("HOT") == "1"   # random (hot) start instead of cold

rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 50)


# ---------- quaternion algebra ----------
def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    # (a0 + i a.s)(b0 + i b.s) = a0b0 - a.b + i(a0 b + b0 a - a x b)
    return np.stack([
        a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
        a0 * b1 + b0 * a1 - (a2 * b3 - a3 * b2),
        a0 * b2 + b0 * a2 - (a3 * b1 - a1 * b3),
        a0 * b3 + b0 * a3 - (a1 * b2 - a2 * b1)], axis=-1)


def qinv(a):
    out = -a.copy()
    out[..., 0] = a[..., 0]
    return out


def qlog(a):
    # a = exp(i h.sigma), |h| <= pi; returns h (principal branch)
    a0 = np.clip(a[..., 0], -1.0, 1.0)
    t = np.arccos(a0)
    s = np.sqrt(np.maximum(1 - a0 ** 2, 0.0))
    g = np.where(s > 1e-12, t / np.where(s > 0, s, 1.0), 1.0)
    return g[..., None] * a[..., 1:]


def qexp(h):
    t = np.linalg.norm(h, axis=-1)
    s = np.where(t > 1e-14, np.sin(t) / np.where(t > 0, t, 1.0), 1.0)
    return np.concatenate([np.cos(t)[..., None], s[..., None] * h], axis=-1)


def qnormalize(a):
    return a / np.linalg.norm(a, axis=-1, keepdims=True)


def shift(a, mu, k):
    # value at x + k e_mu
    return np.roll(a, -k, axis=mu)


# ---------- lattice ----------
def cold(n):
    U = np.zeros((3, n, n, n, 4))
    U[..., 0] = 1.0
    return U


def staple_sum(U, mu):
    S = np.zeros(U.shape[1:])
    for nu in range(3):
        if nu == mu:
            continue
        # forward: U_nu(x+mu) U_mu(x+nu)^-1 U_nu(x)^-1
        f = qmul(qmul(shift(U[nu], mu, 1), qinv(shift(U[mu], nu, 1))),
                 qinv(U[nu]))
        # backward: U_nu(x+mu-nu)^-1 U_mu(x-nu)^-1 U_nu(x-nu)
        Unm = shift(U[nu], nu, -1)
        b = qmul(qmul(qinv(shift(Unm, mu, 1)), qinv(shift(U[mu], nu, -1))), Unm)
        S += f + b
    return S


def parity_mask(n):
    x = np.indices((n, n, n)).sum(axis=0)
    return (x % 2 == 0), (x % 2 == 1)


def sample_a0(bk):
    # Creutz: density sqrt(1 - a0^2) exp(bk a0) on [-1, 1]
    out = np.empty_like(bk)
    todo = np.ones(bk.shape, bool)
    while todo.any():
        b = bk[todo]
        r = rng.uniform(np.exp(-2 * b), 1.0)
        a0 = 1 + np.log(r) / b
        acc = rng.uniform(size=b.shape) ** 2 <= 1 - a0 ** 2
        idx = np.flatnonzero(todo)
        out.flat[idx[acc]] = a0[acc]
        todo.flat[idx[acc]] = False
    return out


def heatbath(U, beta, masks):
    for mu in range(3):
        for m in masks:
            S = staple_sum(U, mu)[m]          # (k,4); action -(beta/2) tr(U S)
            k = np.linalg.norm(S, axis=-1)
            Vbar = S / k[:, None]             # in SU(2) (sum of SU(2) elements)
            a0 = sample_a0(beta * k)
            v = rng.normal(size=(len(k), 3))
            v /= np.linalg.norm(v, axis=-1, keepdims=True)
            X = np.concatenate([a0[:, None],
                                np.sqrt(np.maximum(1 - a0 ** 2, 0))[:, None] * v],
                               axis=-1)
            # want U with tr(U S) distributed: U = X Vbar^-1
            U[mu][m] = qnormalize(qmul(X, qinv(Vbar)))


def overrelax(U, masks):
    for mu in range(3):
        for m in masks:
            S = staple_sum(U, mu)[m]
            Vbar = S / np.linalg.norm(S, axis=-1, keepdims=True)
            Vi = qinv(Vbar)
            # reflection keeping tr(U S) fixed: U -> Vi U^-1 Vi
            U[mu][m] = qnormalize(qmul(qmul(Vi, qinv(U[mu][m])), Vi))


def plaq(U):
    tot = 0.0
    for mu in range(3):
        for nu in range(mu + 1, 3):
            p = qmul(qmul(U[mu], shift(U[nu], mu, 1)),
                     qmul(qinv(shift(U[mu], nu, 1)), qinv(U[nu])))
            tot += p[..., 0].mean()
    return tot / 3


# ---------- Balaban one-step average, CMP 98 (42) ----------
def path_product(U, start, steps):
    """U(Gamma) for the path from site array `start` (offsets) following
    `steps` (list of (mu, +1/-1)); returns array over coarse sites y of the
    product, where start is an offset relative to y (block corner)."""
    n = U.shape[1]
    out = np.zeros(U.shape[1:])
    out[..., 0] = 1.0
    pos = np.array(start)
    for mu, s in steps:
        if s == +1:
            link = U[mu]
            off = pos.copy()
        else:
            off = pos.copy()
            off[mu] -= 1
            link = qinv(U[mu])
        # link at site y + off for all y: roll by -off
        l = link
        for ax in range(3):
            if off[ax]:
                l = np.roll(l, -off[ax], axis=ax)
        out = qmul(out, l)
        pos[mu] += s
    return out


def gamma_steps(src, dst):
    steps = []
    cur = list(src)
    for mu in range(3):
        while cur[mu] != dst[mu]:
            s = 1 if dst[mu] > cur[mu] else -1
            steps.append((mu, s))
            cur[mu] += s
    return steps


def average(U, L):
    n = U.shape[1]
    nc = n // L
    V = np.zeros((3, nc, nc, nc, 4))
    offs = [(a, b, c) for a in range(L) for b in range(L) for c in range(L)]
    for mu in range(3):
        e = [0, 0, 0]; e[mu] = L
        Xfull = path_product(U, (0, 0, 0), [(mu, 1)] * L)
        acc = np.zeros(U.shape[1:-1] + (3,))
        Xinv = qinv(Xfull)
        for x in offs:
            xc = (x[0] + e[0], x[1] + e[1], x[2] + e[2])
            steps = (gamma_steps((0, 0, 0), x) + [(mu, 1)] * L
                     + gamma_steps(xc, tuple(e)))
            Y = path_product(U, (0, 0, 0), steps)
            acc += qlog(qmul(Y, Xinv))
        Vfull = qmul(qexp(acc / L ** 3), Xfull)
        V[mu] = Vfull[::L, ::L, ::L]
    return V


def terminal_obs(V):
    P = plaq(V)
    W = 0.0
    for mu in range(3):
        for nu in range(3):
            if mu == nu:
                continue
            a = qmul(V[mu], shift(V[mu], mu, 1))           # 2 along mu
            b = qmul(shift(V[nu], mu, 2), qinv(shift(shift(V[mu], nu, 1), mu, 1)))
            c = qmul(qinv(shift(V[mu], nu, 1)), qinv(V[nu]))
            W += qmul(qmul(a, b), c)[..., 0].mean()
    W /= 6
    n = V.shape[1]
    PL = 0.0
    for mu in range(3):
        p = V[mu].copy()
        for k in range(1, n):
            p = qmul(p, shift(V[mu], mu, k))
        PL += (p[..., 0] ** 2).mean()
    return P, W, PL / 3


def run(N, n0, L, beta0, ntherm, nmeas, every):
    n = n0 * L ** N
    beta = beta0 * L ** N
    U = cold(n)
    if HOT:
        U = qnormalize(rng.normal(size=U.shape))
    masks = parity_mask(n)
    t0 = time.time()
    for it in range(ntherm):
        heatbath(U, beta, masks)
        overrelax(U, masks)
        overrelax(U, masks)
    data = []
    for it in range(nmeas):
        for _ in range(every):
            heatbath(U, beta, masks)
            overrelax(U, masks)
            overrelax(U, masks)
        V = U
        for _ in range(N):
            V = average(V, L)
        data.append(terminal_obs(V) + (plaq(U),))
    data = np.array(data)
    nb = 10
    bl = data[: (len(data) // nb) * nb].reshape(nb, -1, data.shape[1]).mean(axis=1)
    mean = bl.mean(axis=0)
    err = bl.std(axis=0, ddof=1) / np.sqrt(nb)
    print(f"N={N} n={n} beta={beta:g}: P={mean[0]:.5f}({err[0]:.5f}) "
          f"W12={mean[1]:.5f}({err[1]:.5f}) PL2={mean[2]:.4f}({err[2]:.4f}) "
          f"fine plaq={mean[3]:.5f}  [{time.time() - t0:.0f}s]", flush=True)
    return mean, err


if __name__ == "__main__":
    beta0 = float(sys.argv[2]) if len(sys.argv) > 2 else 4.0
    n0 = int(sys.argv[6]) if len(sys.argv) > 6 else 4
    L = int(sys.argv[5]) if len(sys.argv) > 5 else 2
    Nmax = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    Nmin = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    print(f"n0={n0}, L={L}, beta0={beta0}")
    for N in range(Nmin, Nmax + 1):
        run(N, n0, L, beta0, ntherm=200, nmeas=400, every=2)
