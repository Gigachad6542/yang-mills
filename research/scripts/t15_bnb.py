"""T15 d=4 driver: exact sup via branch-and-bound over fine bonds.
UB_b = sum_c ||J_{c,b}||_op (drops the conservation constraint) >= true per-bond value;
bonds processed in decreasing UB; stop when UB_b <= best found (then best is the exact max
of the alternating-maximization values)."""
import sys, time, numpy as np, cvxpy as cp
from t15_fast import Avg, background, max_curv
from t15_fastjac import jacobian_fast
from t15_avg04 import Lat

def theta_bnb(J, G, iters=5, tlimit=3000):
    nC = J.shape[0]//3; nb = J.shape[1]//3
    U_, S_, Vt = np.linalg.svd(G, full_matrices=True); rank = int((S_ > 1e-8*S_.max()).sum())
    N = U_[:, rank:]
    sv = cp.Variable(N.shape[1]); v = cp.Parameter(N.shape[1]); tau = N @ sv
    prob = cp.Problem(cp.Maximize(v @ sv), [cp.norm(tau[3*k:3*k+3], 2) <= 1 for k in range(nC)])
    UB = np.array([sum(np.linalg.norm(J[3*c:3*c+3, 3*b:3*b+3], 2) for c in range(nC)) for b in range(nb)])
    order = np.argsort(-UB); best, arg, done = 0.0, None, 0; t0 = time.time()
    for b in order:
        if UB[b] <= best or time.time()-t0 > tlimit: break
        Jb = J[:, 3*b:3*b+3]; M = N.T @ Jb; _, _, vt = np.linalg.svd(M); u = vt[0]; val = 0
        for it in range(iters):
            v.value = M @ u
            try: prob.solve(solver='CLARABEL')
            except Exception: break
            if sv.value is None: break
            w_ = Jb.T @ (N @ sv.value); val = np.linalg.norm(w_)
            if val < 1e-14: break
            u = w_/val
        done += 1
        if val > best: best, arg = val, b
    exact = (done == nb) or (UB[order[min(done, nb-1)]] <= best)
    return best, arg, done, exact, UB.max()

if __name__ == '__main__':
    d, L, Nc = (int(a) for a in sys.argv[1:4]); kinds = sys.argv[4].split(',')
    lat = Lat(d, L, Nc); A = Avg(lat); rng = np.random.default_rng(11)
    print(f"d={d} L={L} Nc={Nc}: fine bonds {len(A.FB)}, coarse bonds {len(A.CB)}; flat L^(1-d)={L**(1-d):.5f}", flush=True)
    for kd in kinds:
        kind, eps = (kd.split(':') + ['0'])[:2]; eps = float(eps)
        t0 = time.time(); Uq = background(lat, A.FB, kind, eps, rng)
        J = jacobian_fast(A, Uq); tJ = time.time()-t0
        print(f"  [{kind} eps={eps}] Jacobian done in {tJ:.0f}s", flush=True)
        V = [A.avg(Uq, k) for k in range(len(A.CB))]; G = A.gauge_dirs(V)
        th, b, done, exact, ubmax = theta_bnb(J, G); kap = max_curv(lat, A.FB, Uq)
        print(f"  {kind:9s} eps={eps:5.3f} kappa={kap:.4f} theta={th:.6f} theta/L^(1-d)={th/L**(1-d):.4f} "
              f"(theta-L^(1-d))/kappa={(th-L**(1-d))/kap if kap>1e-9 else float('nan'):.4f} "
              f"[SOCPs on {done} bonds, exact={exact}, max UB={ubmax:.3f}, total {time.time()-t0:.0f}s]", flush=True)
