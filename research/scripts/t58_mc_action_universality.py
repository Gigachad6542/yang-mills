"""T58: memory of an irrelevant perturbation of the bare action (4D SU(2)).

Compares the Wilson action with the tree-level Symanzik action
(c0 = 5/3 on plaquettes, c1 = -1/12 on 1x2 rectangles). The two differ by a
dimension-6 (irrelevant) term. At each depth N the configurations are
mapped N times through Balaban's average (t51) to the terminal 4^4
lattice, and beta is matched so that the terminal plaquette agrees.
Memory decay ((D) of note 22, (S1)-(S3) of note 29) predicts that after
matching, the remaining terminal differences (here in W12) between the two
actions decay like L^{-2N} (dimension 6), up to logarithms.

Heat bath plus over-relaxation. With rectangles, mu-links interact at
offsets (0, +-1), (0, +-2) and (+-1, +-1) in the (mu, nu) plane. So the
mu-links are updated in 8 colours (x_mu mod 2, sum_{nu != mu} x_nu mod 4),
which requires the lattice size to be divisible by 4.

Usage: python3 t58_mc_action_universality.py SEED ACTION(wil|sym) D N n0 beta...

In d = 3, beta_N = beta0 L^N is the exact bare scaling for both actions
(tree-level normalization c0 + 8 c1 = 1), so no matching is needed: the
terminal differences between the actions at equal beta_N should decay with N.
"""
import sys
import time
import numpy as np

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import t51_mc_universality_4d as t
import t50_mc_terminal_convergence as q

qmul, qinv, qnormalize = q.qmul, q.qinv, q.qnormalize
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 58)
q.rng = rng
t.rng = rng


def path_from(U, start, steps):
    """Product of links along `steps`, starting at offset `start` from each site."""
    D = U.shape[0]
    out = np.zeros(U.shape[1:]); out[..., 0] = 1.0
    pos = np.array(start, int)
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


def loop_shapes(mu, nu):
    """Remaining steps (after the initial +mu step at x) of every loop that
    contains the link (x, mu) as a forward step. Returns (weight_key, steps)."""
    shapes = []
    for s in (1, -1):
        shapes.append(("p", [(nu, s), (mu, -1), (nu, -s)]))                       # plaquette
        shapes.append(("r", [(nu, s), (nu, s), (mu, -1), (nu, -s), (nu, -s)]))    # 1 x 2
        shapes.append(("r", [(mu, 1), (nu, s), (mu, -1), (mu, -1), (nu, -s)]))    # 2 x 1, link first
        shapes.append(("r", [(nu, s), (mu, -1), (mu, -1), (nu, -s), (mu, 1)]))    # 2 x 1, link second
    return shapes


def staple(U, mu, c0, c1):
    D = U.shape[0]
    e = [0] * D; e[mu] = 1
    S = np.zeros(U.shape[1:])
    for nu in range(D):
        if nu == mu:
            continue
        for key, steps in loop_shapes(mu, nu):
            w = c0 if key == "p" else c1
            if w == 0:
                continue
            S += w * path_from(U, e, steps)
    return S


def masks(D, n, mu):
    x = np.indices((n,) * D)
    a = x[mu] % 2
    b = (x.sum(axis=0) - x[mu]) % 4
    return [(a == i) & (b == j) for i in range(2) for j in range(4)]


def sweep(U, beta, c0, c1, ms):
    D = U.shape[0]
    for mu in range(D):
        for m in ms[mu]:
            S = staple(U, mu, c0, c1)[m]
            k = np.linalg.norm(S, axis=-1)
            Vbar = S / k[:, None]
            a0 = q.sample_a0(beta * k)
            v = rng.normal(size=(len(k), 3)); v /= np.linalg.norm(v, axis=-1, keepdims=True)
            X = np.concatenate([a0[:, None], np.sqrt(np.maximum(1 - a0 ** 2, 0))[:, None] * v], axis=-1)
            U[mu][m] = qnormalize(qmul(X, qinv(Vbar)))
    for mu in range(D):
        for m in ms[mu]:
            S = staple(U, mu, c0, c1)[m]
            Vi = qinv(S / np.linalg.norm(S, axis=-1, keepdims=True))
            U[mu][m] = qnormalize(qmul(qmul(Vi, qinv(U[mu][m])), Vi))


def run(action, D, N, n0, beta, L=2, ntherm=150, nmeas=200, every=2):
    c0, c1 = (1.0, 0.0) if action == "wil" else (5.0 / 3.0, -1.0 / 12.0)
    n = n0 * L ** N
    U = t.cold(D, n)
    ms = [masks(D, n, mu) for mu in range(D)]
    t0 = time.time()
    for _ in range(ntherm):
        sweep_fast(U, beta, c0, c1, ms)
    data = []
    for _ in range(nmeas):
        for _ in range(every):
            sweep_fast(U, beta, c0, c1, ms)
        V = U
        for _ in range(N):
            V = t.average(V, L)
        data.append((t.plaq(V), t.w12(V), t.plaq(U)))
    data = np.array(data)
    nb = 10
    bl = data[: (len(data) // nb) * nb].reshape(nb, -1, 3).mean(axis=1)
    m, e = bl.mean(0), bl.std(0, ddof=1) / np.sqrt(nb)
    print(f"{action} D={D} N={N} n={n} beta={beta:.4f}: P={m[0]:.5f}({e[0]:.5f}) "
          f"W12={m[1]:.5f}({e[1]:.5f}) fine plaq={m[2]:.5f} [{time.time()-t0:.0f}s]", flush=True)


# ---------- faster masked staples (gather only the sites being updated) ----------
def _flat(coords, n):
    idx = np.zeros(coords.shape[0], dtype=np.int64)
    for ax in range(coords.shape[1]):
        idx = idx * n + (coords[:, ax] % n)
    return idx


def staple_masked(Uflat, n, D, coords, mu, c0, c1):
    """Staple sum at the sites `coords` (m x D) only. Uflat[mu] is U[mu]
    reshaped to (n^D, 4)."""
    S = np.zeros((coords.shape[0], 4))
    e = np.zeros(D, int); e[mu] = 1
    for nu in range(D):
        if nu == mu:
            continue
        for key, steps in loop_shapes(mu, nu):
            w = c0 if key == "p" else c1
            if w == 0:
                continue
            out = np.zeros((coords.shape[0], 4)); out[:, 0] = 1.0
            pos = e.copy()
            for a, sgn in steps:
                off = pos.copy()
                if sgn == -1:
                    off[a] -= 1
                link = Uflat[a][_flat(coords + off, n)]
                out = qmul(out, link if sgn == 1 else qinv(link))
                pos[a] += sgn
            S += w * out
    return S


def sweep_fast(U, beta, c0, c1, ms):
    D, n = U.shape[0], U.shape[1]
    coords_all = [[np.argwhere(m) for m in ms[mu]] for mu in range(D)]
    Uflat = [U[a].reshape(-1, 4) for a in range(D)]   # views into U
    for over in (False, True):
        for mu in range(D):
            for ci, m in enumerate(ms[mu]):
                coords = coords_all[mu][ci]
                S = staple_masked(Uflat, n, D, coords, mu, c0, c1)
                k = np.linalg.norm(S, axis=-1)
                Vbar = S / k[:, None]
                fl = _flat(coords, n)
                if not over:
                    a0 = q.sample_a0(beta * k)
                    v = rng.normal(size=(len(k), 3)); v /= np.linalg.norm(v, axis=-1, keepdims=True)
                    X = np.concatenate([a0[:, None], np.sqrt(np.maximum(1 - a0 ** 2, 0))[:, None] * v], axis=-1)
                    Uflat[mu][fl] = qnormalize(qmul(X, qinv(Vbar)))
                else:
                    Vi = qinv(Vbar)
                    Uflat[mu][fl] = qnormalize(qmul(qmul(Vi, qinv(Uflat[mu][fl])), Vi))


if __name__ == "__main__":
    # usage: SEED ACTION D N n0 beta...
    action, D, N, n0 = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    for b in sys.argv[6:]:
        run(action, D, N, n0, float(b))
