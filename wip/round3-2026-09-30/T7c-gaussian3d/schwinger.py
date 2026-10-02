import numpy as np, itertools, sys, time
sys.path.insert(0,'/private/tmp/ym-r3/T7c-gaussian3d')
from common import PL, PERP, SIG, site
from fourier import sM, kap

def C_schwinger(n, M, h=0.2, chunk=1<<14):
    """exact finite-M terminal flux covariance via 1/|kappa|^2 = int_0^inf e^{-s|kappa|^2} ds.
    returns dict (a,b,Y) -> C[(Y,a),(0,b)], units g^2 eps_0 = 1"""
    m1 = np.arange(-((n*M-1)//2), n*M//2 + 1); p1 = 2*np.pi*m1/n
    s1 = sM(p1, M); k1 = kap(p1, M)
    kmin2 = (2*M*np.sin(np.pi/(n*M)))**2
    u = np.arange(np.log(1e-13/M**2), np.log(45/kmin2), h); sn = np.exp(u)
    xs = sorted(set([y + d for y in range(n) for d in (-0.5, 0.0, 0.5)]))
    combos = [(e,j,x) for e in (2,3,4) for j in (0,1,2) for x in xs]
    cols = np.stack([s1**e * k1**j * np.exp(1j*p1*x) for (e,j,x) in combos], 1)
    W = np.zeros((len(sn), len(combos)), complex)
    for i0 in range(0, len(p1), chunk):
        E = np.exp(-np.outer(sn, k1[i0:i0+chunk]**2))
        W += E @ cols[i0:i0+chunk]
    W0 = cols.sum(0)                          # s = 0 plain sums
    idx = {c:i for i,c in enumerate(combos)}
    out = {}
    for a,(mu,nu) in enumerate(PL):
        for b,(mp,np_) in enumerate(PL):
            pa, pb = PERP[(mu,nu)], PERP[(mp,np_)]
            ca = np.zeros(3); ca[mu]+=.5; ca[nu]+=.5
            cb = np.zeros(3); cb[mp]+=.5; cb[np_]+=.5
            e = [(1 if lam==pa else 2)+(1 if lam==pb else 2) for lam in range(3)]
            j = [(lam==pa)+(lam==pb) for lam in range(3)]
            for Y in itertools.product(range(n), repeat=3):
                x = [Y[l]+ca[l]-cb[l] for l in range(3)]
                ident = 0.0
                if pa == pb:
                    ident = np.prod([W0[idx[(e[l],0,x[l])]] for l in range(3)]) - 1.0
                integrand = np.prod([W[:, idx[(e[l],j[l],x[l])]] for l in range(3)], axis=0)
                proj = h*np.sum(integrand*sn)      # trapezoid in u = log s
                out[(a,b,Y)] = SIG[(mu,nu)]*SIG[(mp,np_)]*np.real(ident - proj)/n**3
    return out

def to_matrix(out, n):
    C = np.zeros((3*n**3,3*n**3))
    for (a,b,Y),v in out.items():
        for Yp in itertools.product(range(n), repeat=3):
            Yd = tuple((np.array(Y)+np.array(Yp))%n)
            C[3*site(Yd,n)+a, 3*site(Yp,n)+b] = v
    return C

if __name__=="__main__":
    from fourier import C_fourier_direct
    for n,M in [(2,2),(2,4),(3,3),(2,8),(2,16),(3,9)]:
        t=time.time(); Cs = to_matrix(C_schwinger(n,M), n); Cd = C_fourier_direct(n,M)
        print(n,M,'max|schwinger-direct|',np.abs(Cs-Cd).max(), 'C00',Cs[0,0], f'{time.time()-t:.1f}s')
