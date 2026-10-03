"""T47: conditional Jacobian of Balaban's one-step average (CMP 98 (42)).

For a coarse bond c = (y, y + L e_0) in d = 3, the fine configuration is
sampled from product Haar measure on the links of B(y) u B(y + L e_0) and the
crossing links. U(c) is the straight product along the central line; its last
link b* is the central crossing link. With U_rest fixed,

    Q(U)(c) = Phi_Y(X) = exp(L^-d sum_{x in S} Log(Y_x X^-1)) X,
    X = W u,  u = U_{b*},

where S is the set of off-central points of B(y). The script checks:

1. the central terms vanish identically (U(Gamma_{c,x}) = U(c) on the line);
2. no Y_x depends on u;
3. F := det dPhi/du (left trivialisations) equals L^{3(1-d)} at U = 1;
4. under Haar, min F >= c_L := eps^3 (sin(eps pi)/((1-eps) pi))^2, with
   eps = L^{1-d} (note 53, Theorem 2), and in fact min F ~ eps^3;
5. operator concavity of S(h) = P_h + |h|cot|h| (1 - P_h) on |h| < pi
   (note 53, Lemma 3), by random midpoint tests;
6. the number of solutions X of Phi_Y(X) = V, by vectorised Newton from
   many starts, for random Y and V (note 53 Remark 6: 0 or 1 observed).
"""
import itertools
import numpy as np

rng = np.random.default_rng(47)
sig = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])


def haar(n):
    a = rng.normal(size=(n, 4))
    a /= np.linalg.norm(a, axis=1, keepdims=True)
    return su2(a)


def su2(a):
    # a0 + i a.sigma
    return (a[:, 0, None, None] * np.eye(2)
            + 1j * np.einsum("na,aij->nij", a[:, 1:], sig))


def expm(h):
    # h: (n,3), returns exp(i h.sigma)
    t = np.linalg.norm(h, axis=1)
    s = np.where(t > 1e-14, np.sin(t) / np.where(t > 0, t, 1), 1.0)
    a = np.concatenate([np.cos(t)[:, None], s[:, None] * h], axis=1)
    return su2(a)


def logm(z):
    # principal log: z = exp(i h.sigma), |h| <= pi; returns h
    a0 = np.clip(np.real(z[:, 0, 0] + z[:, 1, 1]) / 2, -1, 1)
    av = np.stack([np.imag(z[:, 0, 1] + z[:, 1, 0]) / 2,
                   np.real(z[:, 0, 1] - z[:, 1, 0]) / 2,
                   np.imag(z[:, 0, 0] - z[:, 1, 1]) / 2], axis=1)
    t = np.arccos(a0)
    st = np.sqrt(np.maximum(1 - a0 ** 2, 0))
    g = np.where(st > 1e-12, t / np.where(st > 0, st, 1), 1.0)
    return g[:, None] * av


def mul(a, b):
    return np.einsum("nij,njk->nik", a, b)


def inv(a):
    return np.conj(np.transpose(a, (0, 2, 1)))


class Config:
    def __init__(self, L, n, ident=False):
        self.L, self.n = L, n
        self.links = {}
        self.ident = ident

    def link(self, site, mu):
        key = (tuple(site), mu)
        if key not in self.links:
            if self.ident:
                self.links[key] = np.broadcast_to(np.eye(2, dtype=complex),
                                                  (self.n, 2, 2)).copy()
            else:
                self.links[key] = haar(self.n)
        return self.links[key]

    def path(self, sites):
        out = np.broadcast_to(np.eye(2, dtype=complex), (self.n, 2, 2)).copy()
        for p, q in zip(sites[:-1], sites[1:]):
            d = np.array(q) - np.array(p)
            mu = int(np.nonzero(d)[0][0])
            if d[mu] == 1:
                out = mul(out, self.link(p, mu))
            else:
                out = mul(out, inv(self.link(q, mu)))
        return out


def gamma(y, x):
    # CMP 95 (1.7): from y to x, coordinate 0 first, then 1, then 2
    pts = [list(y)]
    cur = list(y)
    for mu in range(3):
        step = 1 if x[mu] >= cur[mu] else -1
        while cur[mu] != x[mu]:
            cur[mu] += step
            pts.append(list(cur))
    return pts


def contour(L, x):
    y = (0, 0, 0)
    yp = (L, 0, 0)
    xc = (x[0] + L, x[1], x[2])
    p1 = gamma(y, x)
    seg = [[x[0] + t, x[1], x[2]] for t in range(1, L + 1)]
    p3 = gamma(yp, xc)[::-1][1:]
    return p1 + seg + p3


def setup(L, n, ident=False):
    cfg = Config(L, n, ident)
    pts = list(itertools.product(range(L), repeat=3))
    straight = [[t, 0, 0] for t in range(L + 1)]
    X = cfg.path(straight)
    central = [x for x in pts if x[1] == 0 and x[2] == 0]
    S = [x for x in pts if not (x[1] == 0 and x[2] == 0)]
    Yc = [cfg.path(contour(L, x)) for x in central]
    bstar = ((L - 1, 0, 0), 0)
    # contours of S must not contain b*; record the keys they use
    before = set(cfg.links)
    Ys = [cfg.path(contour(L, x)) for x in S]
    return cfg, X, Yc, Ys, bstar, pts


def phi(Ys, X, L):
    w = sum(logm(mul(Y, inv(X))) for Y in Ys) / L ** 3
    return mul(expm(w), X)


def jac(Ys, X, L, h=1e-6):
    V0 = phi(Ys, X, L)
    cols = []
    for a in range(3):
        e = np.zeros((X.shape[0], 3))
        e[:, a] = h
        Xp = mul(X, expm(e))   # X = W u, perturb u -> u e^{ih}
        Xm = mul(X, expm(-e))
        dp = logm(mul(inv(V0), phi(Ys, Xp, L)))
        dm = logm(mul(inv(V0), phi(Ys, Xm, L)))
        cols.append((dp - dm) / (2 * h))
    return np.linalg.det(np.stack(cols, axis=2))


def check_structure(L):
    cfg, X, Yc, Ys, bstar, pts = setup(L, 4)
    dev = max(np.abs(Y - X).max() for Y in Yc)
    # recompute Ys with b* changed: they must not move
    old = cfg.links[bstar].copy()
    cfg.links[bstar] = haar(4)
    S = [x for x in pts if not (x[1] == 0 and x[2] == 0)]
    Ys2 = [cfg.path(contour(L, x)) for x in S]
    mv = max(np.abs(a - b).max() for a, b in zip(Ys, Ys2))
    cfg.links[bstar] = old
    print(f"L={L}: central terms |Y_x - X| max = {dev:.1e}; "
          f"Y_x change when b* resampled = {mv:.1e}")


def run(L, n):
    cfg, X, Yc, Ys, bstar, pts = setup(L, n)
    F = jac(Ys, X, L)
    eps0 = L ** (3 * (1 - 3))
    r = np.abs(F) / eps0
    print(f"L={L}, n={n}: |F|/L^-6 quantiles "
          f"{np.quantile(r, [0.001, 0.01, 0.1, 0.5, 0.9]).round(4)}")
    eps = L ** (1 - 3)
    cL = eps ** 3 * (np.sin(eps * np.pi) / ((1 - eps) * np.pi)) ** 2
    print(f"  fraction F<0: {np.mean(F < 0):.4f}; min F/L^-6 = {r.min():.4f}; "
          f"proved bound c_L/L^-6 = {cL / eps0:.4f}")
    return r


def concavity(n=200000):
    def S(h):
        th = np.linalg.norm(h)
        if th < 1e-12:
            return np.eye(3)
        P = np.outer(h, h) / th ** 2
        return P + th / np.tan(th) * (np.eye(3) - P)
    worst = np.inf
    for _ in range(n):
        h1 = rng.normal(size=3); h1 *= rng.uniform(0, np.pi) / np.linalg.norm(h1)
        h2 = rng.normal(size=3); h2 *= rng.uniform(0, np.pi) / np.linalg.norm(h2)
        s = rng.uniform()
        D = S(s * h1 + (1 - s) * h2) - s * S(h1) - (1 - s) * S(h2)
        worst = min(worst, np.linalg.eigvalsh(D).min())
    print(f"concavity of S: min eigenvalue of S(mix) - mix(S) over {n} tests "
          f"= {worst:.2e}")


def fibres(nS, N, trials=30, n0=120):
    counts = []
    agree = 0
    for _ in range(trials):
        Ys = [np.broadcast_to(haar(1), (n0, 2, 2)) for _ in range(nS)]
        V = np.broadcast_to(haar(1), (n0, 2, 2))

        def ph(X):
            w = sum(logm(mul(Y, inv(X))) for Y in Ys) / N
            return mul(expm(w), X)
        X = haar(n0)
        for _ in range(80):
            r = logm(mul(ph(X), inv(V)))
            J = np.zeros((n0, 3, 3))
            for a in range(3):
                e = np.zeros((n0, 3)); e[:, a] = 1e-6
                J[:, :, a] = (logm(mul(ph(mul(expm(e), X)), inv(V))) - r) / 1e-6
            st = np.linalg.solve(J, -r[:, :, None])[:, :, 0]
            nr = np.linalg.norm(st, axis=1, keepdims=True)
            st = np.where(nr > 0.3, st * 0.3 / np.maximum(nr, 1e-300), st)
            X = mul(expm(st), X)
        res = np.linalg.norm(logm(mul(ph(X), inv(V))), axis=1)
        sols = []
        for k in np.nonzero(res < 1e-9)[0]:
            if not any(np.abs(X[k] - s).max() < 1e-6 for s in sols):
                sols.append(X[k])
        # note 53 Theorem 4: count = 1 - #{j : |xi_j - c_j| < p_j pi}
        Y1 = [Y[:1] for Y in Ys]
        V1 = V[:1]
        inside = 0
        for j in range(nS):
            xi = logm(-mul(V1, inv(Y1[j])))
            c = sum(logm(-mul(Y1[k], inv(Y1[j]))) for k in range(nS)
                    if k != j) / N
            inside += np.linalg.norm(xi - c) < np.pi / N
        counts.append(len(sols))
        agree += (len(sols) == 1 - inside)
    print(f"|S|={nS}, N={N}: distinct solutions per (Y,V) over {trials} "
          f"trials: {dict(zip(*np.unique(counts, return_counts=True)))}; "
          f"count formula agrees in {agree}/{trials}")


if __name__ == "__main__":
    for L in [2, 3]:
        check_structure(L)
    for L in [2, 3]:
        cfg, X, Yc, Ys, bstar, pts = setup(L, 1, ident=True)
        print(f"L={L}: F at U=1 times L^6 = {jac(Ys, X, L)[0] * L ** 6:.6f}")
    run(2, 200000)
    run(3, 40000)
    concavity()
    for nS, N in [(6, 8), (24, 27), (2, 3), (1, 2), (3, 4)]:
        fibres(nS, N)
