"""T15: sup-norm contraction of the pulled-back conserved current for the
CMP 109 Eq. (0.4) average at curved SU(2) backgrounds (research/12 (3.3)-(3.4)).

theta(U) = sup { ||P tau||_inf : tau covariantly conserved at V=Q(U), ||tau||_inf <= 1 },
P = DQ(U)^T in right-trivialized coordinates (components along Pauli matrices),
||.||_inf = max over bonds and the 3 Lie-algebra components (box norm).
Computed exactly (up to finite differences) by one LP per fine bond component."""
import sys, itertools, numpy as np, scipy.linalg as sla
from scipy.optimize import linprog
from t15_avg04 import Lat, avg, hol, speclog, PAULI, all_bonds, rand_su2

def comps(X):          # X Hermitian 2x2 -> 3 real comps with X = sum x_a sigma_a
    return np.array([np.trace(X @ s).real/2 for s in PAULI])

def coarse_map(lat, U, TR, CB):
    return {c: avg(lat, U, c, TR[c]) for c in CB}

def support(lat, TR, c):
    S = set((b[0], b[1]) for w, ell in TR[c] for b in ell)
    S |= set((b[0], b[1]) for b in lat.central(c))
    return S

def jacobian(lat, U, TR, CB, FB, h=1e-6):
    fidx = {b: i for i, b in enumerate(FB)}; cidx = {c: i for i, c in enumerate(CB)}
    J = np.zeros((3*len(CB), 3*len(FB)))
    for c in CB:
        V0 = avg(lat, U, c, TR[c]); V0i = V0.conj().T
        for b in support(lat, TR, c):
            for a in range(3):
                Up = dict(U); Up[b] = U[b] @ sla.expm(1j*h*PAULI[a])
                Um = dict(U); Um[b] = U[b] @ sla.expm(-1j*h*PAULI[a])
                dp = comps(speclog(V0i @ avg(lat, Up, c, TR[c])))
                dm = comps(speclog(V0i @ avg(lat, Um, c, TR[c])))
                J[3*cidx[c]:3*cidx[c]+3, 3*fidx[b]+a] = (dp - dm)/(2*h)
    return J

def gauge_dirs(lat_c_bonds, V, Nc, d, h=1e-6):
    """columns: right-trivialized coarse link variations under infinitesimal gauge at each coarse site"""
    sites = list(itertools.product(range(Nc), repeat=d)); cidx = {c: i for i, c in enumerate(lat_c_bonds)}
    G = np.zeros((3*len(lat_c_bonds), 3*len(sites)))
    for si, y in enumerate(sites):
        for a in range(3):
            w = sla.expm(1j*h*PAULI[a])
            for c in lat_c_bonds:
                yc, mu = c; yp = tuple((yc[i] + (i == mu)) % Nc for i in range(d))
                L_ = w if yc == y else np.eye(2); R_ = w.conj().T if yp == y else np.eye(2)
                if yc != y and yp != y: continue
                Vp = L_ @ V[c] @ R_
                G[3*cidx[c]:3*cidx[c]+3, 3*si+a] += comps(speclog(V[c].conj().T @ Vp))/h
    return G

def theta(J, G):
    """sup-norm operator norm of J^T on {tau : G^T tau = 0}"""
    n = J.shape[0]; best = 0.0; arg = None
    A_eq = G.T; b_eq = np.zeros(G.shape[1])
    # orthonormal-ish cleanup of equality constraints
    Q_, R_ = np.linalg.qr(A_eq.T); rank = int((np.abs(np.diag(R_)) > 1e-8).sum())
    A_eq = Q_[:, :rank].T; b_eq = np.zeros(rank)
    for i in range(J.shape[1]):
        col = J[:, i]
        if np.abs(col).max() < 1e-12: continue
        r = linprog(-col, A_eq=A_eq, b_eq=b_eq, bounds=[(-1, 1)]*n, method='highs')
        if r.status == 0 and -r.fun > best: best, arg = -r.fun, i
    return best, arg

def background(lat, kind, eps, rng):
    FB = all_bonds(lat); U = {}
    if kind == 'flat':
        for b in FB: U[b] = np.eye(2, dtype=complex)
    elif kind == 'puregauge':
        g = {x: rand_su2(None, rng) for x in itertools.product(range(lat.n), repeat=lat.d)}
        for (x, mu) in FB: U[(x, mu)] = g[x] @ g[lat.add(x, mu)].conj().T
    elif kind == 'rough':      # iid small links: curvature ~ eps per plaquette
        for b in FB: U[b] = rand_su2(eps, rng)
    elif kind == 'smooth':     # smooth non-abelian field: A_mu(x) = eps * sum_a f_a,mu(x) sigma_a, f slowly varying
        ph = rng.uniform(0, 2*np.pi, size=(lat.d, 3, lat.d)); amp = rng.normal(size=(lat.d, 3))
        for (x, mu) in FB:
            X = sum(eps*amp[mu, a]*np.cos(sum(2*np.pi*x[k]/lat.n + ph[mu, a, k] for k in range(lat.d)))*PAULI[a] for a in range(3))
            U[(x, mu)] = sla.expm(1j*X)
    return U

def max_plaq_curv(lat, U):
    m = 0
    for x in itertools.product(range(lat.n), repeat=lat.d):
        for mu in range(lat.d):
            for nu in range(mu+1, lat.d):
                P = [(x, mu, 1), (lat.add(x, mu), nu, 1), (lat.add(x, nu), mu, -1), (x, nu, -1)]
                # proper path: x ->x+mu ->x+mu+nu <- x+nu <- x
                H = U[(x, mu)] @ U[(lat.add(x, mu), nu)] @ U[(lat.add(x, nu), mu)].conj().T @ U[(x, nu)].conj().T
                m = max(m, np.linalg.norm(speclog(H), 2))
    return m

def main():
    d, L, Nc = (int(a) for a in sys.argv[1:4]); norm = sys.argv[4] if len(sys.argv) > 4 else 'hs'
    rng = np.random.default_rng(7)
    lat = Lat(d, L, Nc); CB = list(lat.coarse_bonds()); FB = all_bonds(lat)
    TR = {c: lat.triples(c) for c in CB}
    print(f"d={d} L={L} Nc={Nc}: flat value L^(1-d) = {L**(1-d):.4f}")
    runs = [('flat', 0), ('puregauge', 0)] + [(k, e) for k in ('smooth', 'rough') for e in (0.02, 0.05, 0.1, 0.2, 0.4)]
    for kind, eps in runs:
        U = background(lat, kind, eps, rng)
        J = jacobian(lat, U, TR, CB, FB)
        V = {c: avg(lat, U, c, TR[c]) for c in CB}
        G = gauge_dirs(CB, V, Nc, d)
        th, i = theta_hs(J, G) if norm == 'hs' else theta(J, G)
        if norm == 'hs' and i is not None: i = 3*i
        kap = max_plaq_curv(lat, U)
        bond = FB[i//3] if i is not None else None
        print(f"  {kind:9s} eps={eps:4.2f}  max plaquette curvature={kap:.4f}  theta={th:.5f}  theta/L^(1-d)={th/L**(1-d):.3f}  argmax bond={bond}", flush=True)

# ---- Ad-invariant version: per-bond Hilbert-Schmidt (Euclidean) norm -------------
import cvxpy as cp
def theta_hs(J, G, starts=3, iters=6, rng=np.random.default_rng(0)):
    """sup over tau in ker(G^T), max_c |tau_c|_2 <= 1, of max_b |(J^T tau)_b|_2.
    For each fine bond: alternating maximization over unit u in R^3 (lower bound, local max)."""
    nC = J.shape[0]//3
    Q_, R_ = np.linalg.qr(G); rank = int((np.abs(np.diag(R_)) > 1e-8).sum())
    # nullspace of G^T: complement of range(G)
    U_, S_, Vt = np.linalg.svd(G, full_matrices=True)
    N = U_[:, rank:]                       # basis of ker G^T
    s = cp.Variable(N.shape[1]); v = cp.Parameter(N.shape[1])
    tau = N @ s
    cons = [cp.norm(tau[3*k:3*k+3], 2) <= 1 for k in range(nC)]
    prob = cp.Problem(cp.Maximize(v @ s), cons)
    best = 0.0; arg = None
    nb = J.shape[1]//3
    for b in range(nb):
        Jb = J[:, 3*b:3*b+3]               # coarse x 3
        if np.abs(Jb).max() < 1e-12: continue
        for st in range(starts):
            u = rng.normal(size=3); u /= np.linalg.norm(u)
            val = 0
            for it in range(iters):
                v.value = N.T @ (Jb @ u)
                prob.solve(solver='CLARABEL')
                t = N @ s.value; w = Jb.T @ t; val = np.linalg.norm(w)
                if val < 1e-14: break
                u = w/val
            if val > best: best, arg = val, b
    return best, arg

if __name__ == '__main__':
    main()
