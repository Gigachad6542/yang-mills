"""T15 (fast): vectorized quaternion implementation of the CMP 109 Eq. (0.4)
average and the Ad-invariant sup-norm contraction theta of conserved currents
(see t15_curved_contraction.py for the reference implementation; both agree)."""
import sys, itertools, time, numpy as np
import cvxpy as cp
from t15_avg04 import Lat, all_bonds

# quaternion (a0,a) <-> a0 + i a.sigma ; SU(2)
def qmul(p, q):
    a0, a = p[..., 0], p[..., 1:]; b0, b = q[..., 0], q[..., 1:]
    out = np.empty(np.broadcast(p, q).shape)
    out[..., 0] = a0*b0 - (a*b).sum(-1)
    out[..., 1:] = a0[..., None]*b + b0[..., None]*a - np.cross(a, b)
    return out
def qinv(p): q = p.copy(); q[..., 1:] *= -1; return q
def qlog(p):   # X = x.sigma with p = exp(i X); x = theta * a/|a|
    a0 = np.clip(p[..., 0], -1, 1); a = p[..., 1:]; na = np.linalg.norm(a, axis=-1)
    th = np.arctan2(na, a0); f = np.where(na > 1e-14, th/np.where(na > 1e-14, na, 1), 1.0)
    return a*f[..., None]
def qexp(x):
    nx = np.linalg.norm(x, axis=-1); out = np.empty(x.shape[:-1]+(4,))
    out[..., 0] = np.cos(nx); s = np.where(nx > 1e-14, np.sin(nx)/np.where(nx > 1e-14, nx, 1), 1.0)
    out[..., 1:] = x*s[..., None]; return out

class Avg:
    def __init__(s, lat):
        s.lat = lat; s.FB = all_bonds(lat); s.fidx = {b: i for i, b in enumerate(s.FB)}
        s.CB = list(lat.coarse_bonds()); s.data = []
        for c in s.CB:
            tr = lat.triples(c); m = max(len(ell) for w, ell in tr)
            idx = np.zeros((len(tr), m), int); sg = np.zeros((len(tr), m), int); w = np.zeros(len(tr))
            for k, (wt, ell) in enumerate(tr):
                w[k] = wt
                for j, (x, mu, sgn) in enumerate(ell): idx[k, j] = s.fidx[(x, mu)]; sg[k, j] = sgn
            cen = [(s.fidx[(x, mu)], sgn) for (x, mu, sgn) in lat.central(c)]
            supp = sorted(set(idx[sg != 0].ravel()) | set(i for i, _ in cen))
            s.data.append((idx, sg, w, cen, supp))
    def hol(s, Uq, idx, sg):
        H = np.zeros((idx.shape[0], 4)); H[:, 0] = 1
        for j in range(idx.shape[1]):
            q = Uq[idx[:, j]]; q = np.where((sg[:, j] < 0)[:, None], qinv(q), q)
            q = np.where((sg[:, j] == 0)[:, None], np.array([1., 0, 0, 0]), q)
            H = qmul(H, q)
        return H
    def avg(s, Uq, k):
        idx, sg, w, cen, supp = s.data[k]
        Uc = np.array([1., 0, 0, 0])
        for (i, sgn) in cen: Uc = qmul(Uc, Uq[i] if sgn > 0 else qinv(Uq[i]))
        H = s.hol(Uq, idx, sg)
        X = (w[:, None]*qlog(qmul(H, qinv(Uc)[None, :]))).sum(0)
        return qmul(qexp(X), Uc)
    def jacobian(s, Uq, h=1e-6):
        J = np.zeros((3*len(s.CB), 3*len(s.FB)))
        for k in range(len(s.CB)):
            V0i = qinv(s.avg(Uq, k)); supp = s.data[k][4]
            for b in supp:
                for a in range(3):
                    e = np.zeros(3); e[a] = h
                    Up = Uq.copy(); Up[b] = qmul(Uq[b], qexp(e)); Um = Uq.copy(); Um[b] = qmul(Uq[b], qexp(-e))
                    J[3*k:3*k+3, 3*b+a] = (qlog(qmul(V0i, s.avg(Up, k))) - qlog(qmul(V0i, s.avg(Um, k))))/(2*h)
        return J
    def gauge_dirs(s, V, h=1e-6):
        lat = s.lat; Nc, d = lat.Nc, lat.d
        sites = list(itertools.product(range(Nc), repeat=d))
        G = np.zeros((3*len(s.CB), 3*len(sites)))
        for si, y in enumerate(sites):
            for a in range(3):
                e = np.zeros(3); e[a] = h; wq = qexp(e)
                for k, c in enumerate(s.CB):
                    yc, mu = c; yp = tuple((yc[i] + (i == mu)) % Nc for i in range(d))
                    if yc != y and yp != y: continue
                    Vp = V[k]
                    if yc == y: Vp = qmul(wq, Vp)
                    if yp == y: Vp = qmul(Vp, qinv(wq))
                    G[3*k:3*k+3, 3*si+a] += qlog(qmul(qinv(V[k]), Vp))/h
        return G

def theta_hs(J, G, starts=2, iters=5, seed=0, bonds=None):
    rng = np.random.default_rng(seed); nC = J.shape[0]//3
    U_, S_, Vt = np.linalg.svd(G, full_matrices=True); rank = int((S_ > 1e-8*S_.max()).sum())
    N = U_[:, rank:]
    sv = cp.Variable(N.shape[1]); v = cp.Parameter(N.shape[1]); tau = N @ sv
    prob = cp.Problem(cp.Maximize(v @ sv), [cp.norm(tau[3*k:3*k+3], 2) <= 1 for k in range(nC)])
    best, arg = 0.0, None
    nb = J.shape[1]//3
    for b in (range(nb) if bonds is None else bonds):
        Jb = J[:, 3*b:3*b+3]
        if np.abs(Jb).max() < 1e-12: continue
        # start from top singular direction of the projected block, plus random
        M = N.T @ Jb; _, _, vt = np.linalg.svd(M)
        us = [vt[0]] + [rng.normal(size=3) for _ in range(starts-1)]
        for u in us:
            u = u/np.linalg.norm(u); val = 0
            for it in range(iters):
                v.value = N.T @ (Jb @ u)
                try: prob.solve(solver='CLARABEL')
                except Exception: break
                if sv.value is None: break
                w_ = Jb.T @ (N @ sv.value); val = np.linalg.norm(w_)
                if val < 1e-14: break
                u = w_/val
            if val > best: best, arg = val, b
    return best, arg

def background(lat, FB, kind, eps, rng):
    n, d = lat.n, lat.d; Uq = np.zeros((len(FB), 4))
    if kind == 'flat': Uq[:, 0] = 1
    elif kind == 'puregauge':
        sites = list(itertools.product(range(n), repeat=d))
        g = {x: (lambda v: v/np.linalg.norm(v))(rng.normal(size=4)) for x in sites}
        for i, (x, mu) in enumerate(FB): Uq[i] = qmul(g[x], qinv(g[lat.add(x, mu)]))
    elif kind == 'rough':
        x = rng.normal(size=(len(FB), 3)); x *= eps/np.linalg.norm(x, axis=1, keepdims=True); Uq = qexp(x)
    elif kind == 'smooth':
        ph = rng.uniform(0, 2*np.pi, size=(d, 3, d)); amp = rng.normal(size=(d, 3))
        for i, (x, mu) in enumerate(FB):
            X = np.array([eps*amp[mu, a]*np.cos(sum(2*np.pi*x[k]/n + ph[mu, a, k] for k in range(d))) for a in range(3)])
            Uq[i] = qexp(X)
    return Uq

def max_curv(lat, FB, Uq):
    fidx = {b: i for i, b in enumerate(FB)}; m = 0
    for x in itertools.product(range(lat.n), repeat=lat.d):
        for mu in range(lat.d):
            for nu in range(mu+1, lat.d):
                H = qmul(qmul(Uq[fidx[(x, mu)]], Uq[fidx[(lat.add(x, mu), nu)]]),
                         qmul(qinv(Uq[fidx[(lat.add(x, nu), mu)]]), qinv(Uq[fidx[(x, nu)]])))
                m = max(m, np.linalg.norm(qlog(H)))
    return m

if __name__ == '__main__':
    d, L, Nc = (int(a) for a in sys.argv[1:4])
    kinds = sys.argv[4].split(',') if len(sys.argv) > 4 else ['flat', 'puregauge', 'smooth:0.02', 'smooth:0.05', 'rough:0.02', 'rough:0.05', 'rough:0.1']
    lat = Lat(d, L, Nc); A = Avg(lat); rng = np.random.default_rng(11)
    print(f"d={d} L={L} Nc={Nc}: fine bonds {len(A.FB)}, coarse bonds {len(A.CB)}, contours/coarse bond {A.data[0][0].shape[0]}; flat L^(1-d)={L**(1-d):.5f}", flush=True)
    for kd in kinds:
        kind, eps = (kd.split(':') + ['0'])[:2]; eps = float(eps)
        t0 = time.time(); Uq = background(lat, A.FB, kind, eps, rng)
        J = A.jacobian(Uq); V = [A.avg(Uq, k) for k in range(len(A.CB))]; G = A.gauge_dirs(V)
        th, b = theta_hs(J, G); kap = max_curv(lat, A.FB, Uq)
        print(f"  {kind:9s} eps={eps:5.3f} kappa={kap:.4f} theta={th:.6f} theta/L^(1-d)={th/L**(1-d):.4f} "
              f"(theta-L^(1-d))/kappa={(th-L**(1-d))/kap if kap>1e-9 else float('nan'):.4f} bond={A.FB[b] if b is not None else None} [{time.time()-t0:.0f}s]", flush=True)
