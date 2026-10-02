"""Numerical checks of research/15 (CMP 109 Eq. (0.4) average) on small tori.

Fine torus Z_n^d, n = L*Nc, odd L. Coarse site y <-> fine center L*y.
Block B(y) = {L*y + k, |k_mu| <= (L-1)/2}. Coarse bond c=(y,mu): c_- = L y, c_+ = L(y+e_mu).
Link U[x][mu] for x -> x+e_mu. Path = list of (site, mu, sign).
"""
import itertools, numpy as np, scipy.linalg as sla

sx = np.array([[0,1],[1,0]],complex); sy = np.array([[0,-1j],[1j,0]]); sz = np.array([[1,0],[0,-1]],complex)
PAULI = [sx, sy, sz]

class Lat:
    def __init__(s, d, L, Nc):
        s.d, s.L, s.Nc = d, L, Nc; s.n = L*Nc
        s.h = (L-1)//2
    def add(s, x, mu, k=1):
        y = list(x); y[mu] = (y[mu]+k) % s.n; return tuple(y)
    def straight(s, x, mu, k):
        """path from x moving k steps along mu (k may be negative)"""
        p=[]; cur=x
        for _ in range(abs(k)):
            if k>0: p.append((cur,mu,+1)); cur=s.add(cur,mu,1)
            else:
                cur=s.add(cur,mu,-1); p.append((cur,mu,-1))
        return p, cur
    def G(s, y, disp):
        """family of axis-ordered shortest paths from y with displacement disp"""
        nz=[mu for mu in range(s.d) if disp[mu]!=0]
        fam=[]
        for perm in itertools.permutations(nz):
            p=[]; cur=y
            for mu in perm:
                q,cur=s.straight(cur,mu,disp[mu]); p+=q
            fam.append(p)
        if not nz: fam=[[]]
        return fam
    def coarse_bonds(s):
        for y in itertools.product(range(s.Nc),repeat=s.d):
            for mu in range(s.d): yield (y,mu)
    def cminus(s,c):
        y,mu=c; return tuple(s.L*a for a in y)
    def triples(s, c):
        """list of (weight, ell) with ell = Gamma [x,x'] (-Gamma')"""
        y,mu=c; cm=s.cminus(c); cp=s.add(cm,mu,s.L)
        out=[]
        for disp in itertools.product(range(-s.h,s.h+1),repeat=s.d):
            x=tuple((cm[i]+disp[i])%s.n for i in range(s.d))
            F1=s.G(cm,disp); F2=s.G(cp,disp)
            seg,_=s.straight(x,mu,s.L)
            for g1 in F1:
                for g2 in F2:
                    rev=[(b[0],b[1],-b[2]) for b in reversed(g2)]
                    out.append((s.L**(-s.d)/(len(F1)*len(F2)), g1+seg+rev))
        return out
    def central(s,c):
        y,mu=c; return s.straight(s.cminus(c),mu,s.L)[0]

def hol(U, path):
    M=np.eye(2,dtype=complex)
    for (x,mu,sg) in path:
        M = M @ (U[(x,mu)] if sg>0 else U[(x,mu)].conj().T)
    return M

def speclog(H):
    """(1/i) log H, spectral, args in (-pi,pi]"""
    T,Zs = sla.schur(H, output='complex')
    ev=np.diag(T); ph=np.angle(ev)
    ph=np.where(ph<=-np.pi+1e-15, np.pi, ph)
    return Zs @ np.diag(ph) @ Zs.conj().T

def avg(lat, U, c, trip=None):
    trip = trip or lat.triples(c)
    Uc = hol(U, lat.central(c))
    X = sum(w*speclog(hol(U,ell) @ Uc.conj().T) for w,ell in trip)
    return sla.expm(1j*X) @ Uc

def rand_su2(eps, rng):
    a=rng.normal(size=3); a*=eps/np.linalg.norm(a) if eps is not None else 1
    if eps is None:
        v=rng.normal(size=4); v/=np.linalg.norm(v)
        return np.array([[v[0]+1j*v[3], v[2]+1j*v[1]],[-v[2]+1j*v[1], v[0]-1j*v[3]]])
    return sla.expm(1j*sum(a[i]*PAULI[i] for i in range(3)))

def all_bonds(lat):
    return [(x,mu) for x in itertools.product(range(lat.n),repeat=lat.d) for mu in range(lat.d)]
