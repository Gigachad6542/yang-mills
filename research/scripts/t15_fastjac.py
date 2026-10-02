"""Faster Jacobian for t15_fast: only contours through the perturbed bond are recomputed
(incremental update of the convex-log sum). Validated against Avg.jacobian."""
import sys, time, numpy as np
from t15_fast import Avg, background, theta_hs, max_curv, qmul, qinv, qlog, qexp
from t15_avg04 import Lat

def jacobian_fast(A, Uq, h=1e-6):
    J = np.zeros((3*len(A.CB), 3*len(A.FB)))
    for k in range(len(A.CB)):
        idx, sg, w, cen, supp = A.data[k]
        cen_set = set(i for i, _ in cen)
        Uc = np.array([1., 0, 0, 0])
        for (i, s_) in cen: Uc = qmul(Uc, Uq[i] if s_ > 0 else qinv(Uq[i]))
        H = A.hol(Uq, idx, sg); Z = qlog(qmul(H, qinv(Uc)[None, :])); X = (w[:, None]*Z).sum(0)
        V0i = qinv(qmul(qexp(X), Uc))
        through = {}
        rr, cc = np.nonzero(sg)
        for r, j in zip(rr, cc): through.setdefault(idx[r, j], set()).add(r)
        for b in supp:
            rows = np.array(sorted(through.get(b, ())), dtype=int)
            for a in range(3):
                e = np.zeros(3); e[a] = h; res = []
                for sgn in (+1, -1):
                    Up = Uq.copy(); Up[b] = qmul(Uq[b], qexp(sgn*e))
                    if b in cen_set:
                        V = A.avg(Up, k)
                    else:
                        Xp = X
                        if len(rows):
                            Hp = A.hol(Up, idx[rows], sg[rows])
                            Zp = qlog(qmul(Hp, qinv(Uc)[None, :]))
                            Xp = X + (w[rows, None]*(Zp - Z[rows])).sum(0)
                        V = qmul(qexp(Xp), Uc)
                    res.append(qlog(qmul(V0i, V)))
                J[3*k:3*k+3, 3*b+a] = (res[0] - res[1])/(2*h)
    return J

if __name__ == '__main__':
    if sys.argv[1] == 'check':
        lat = Lat(2, 3, 3); A = Avg(lat); Uq = background(lat, A.FB, 'rough', 0.1, np.random.default_rng(1))
        t = time.time(); J1 = A.jacobian(Uq); t1 = time.time()-t
        t = time.time(); J2 = jacobian_fast(A, Uq); t2 = time.time()-t
        print('max diff', np.abs(J1-J2).max(), 'times', round(t1, 2), round(t2, 2)); sys.exit()
    d, L, Nc = (int(a) for a in sys.argv[1:4]); kinds = sys.argv[4].split(',')
    lat = Lat(d, L, Nc); A = Avg(lat); rng = np.random.default_rng(11)
    print(f"d={d} L={L} Nc={Nc}: fine bonds {len(A.FB)}, coarse bonds {len(A.CB)}; flat L^(1-d)={L**(1-d):.5f}", flush=True)
    for kd in kinds:
        kind, eps = (kd.split(':') + ['0'])[:2]; eps = float(eps)
        t0 = time.time(); Uq = background(lat, A.FB, kind, eps, rng)
        J = jacobian_fast(A, Uq); tJ = time.time()-t0
        V = [A.avg(Uq, k) for k in range(len(A.CB))]; G = A.gauge_dirs(V)
        th, b = theta_hs(J, G, starts=1, iters=4); kap = max_curv(lat, A.FB, Uq)
        print(f"  {kind:9s} eps={eps:5.3f} kappa={kap:.4f} theta={th:.6f} theta/L^(1-d)={th/L**(1-d):.4f} "
              f"(theta-L^(1-d))/kappa={(th-L**(1-d))/kap if kap>1e-9 else float('nan'):.4f} [J {tJ:.0f}s, total {time.time()-t0:.0f}s]", flush=True)
