import numpy as np, itertools, sys
sys.path.insert(0,'/private/tmp/ym-r3/T7c-gaussian3d')
from common import PL, PERP, SIG, site

def sM(t, M):
    """s_M(t) = sin(t/2)/(M sin(t/(2M))), M=inf -> sinc"""
    t = np.asarray(t, float)
    out = np.ones_like(t)
    nz = np.abs(t) > 1e-14
    if M == np.inf:
        out[nz] = np.sin(t[nz]/2)/(t[nz]/2)
    else:
        out[nz] = np.sin(t[nz]/2)/(M*np.sin(t[nz]/(2*M)))
    return out

def kap(t, M):
    return t if M == np.inf else 2*M*np.sin(t/(2*M))

def C_fourier_direct(n, M, R=None):
    """terminal flux covariance, units g^2 eps_0 = 1, rows ordered 3*site(Y)+o.
    M finite: sum over fine BZ D_M. M=inf: sum over |m_i|<=R (truncated)."""
    if M == np.inf:
        m1 = np.arange(-R, R+1)
    else:
        m1 = np.arange(-(n*M)//2 + 1 if (n*M)%2==0 else -(n*M)//2, (n*M)//2 + 1)
        # ensure exactly nM reps in (-nM/2, nM/2]
        m1 = np.arange(-((n*M-1)//2), n*M//2 + 1)
        assert len(m1) == n*M
    p1 = 2*np.pi*m1/n
    P = np.stack(np.meshgrid(p1,p1,p1, indexing='ij'), -1).reshape(-1,3)
    P = P[np.any(P != 0, axis=1)]
    s = sM(P, M); k = kap(P, M); k2 = (k**2).sum(1)
    S = {}
    for (mu,nu) in PL:
        pe = PERP[(mu,nu)]
        S[(mu,nu)] = s[:,pe]*s[:,mu]**2*s[:,nu]**2
    C = np.zeros((3*n**3, 3*n**3))
    Ys = list(itertools.product(range(n), repeat=3))
    for a,(mu,nu) in enumerate(PL):
        for b,(mp,np_) in enumerate(PL):
            pa, pb = PERP[(mu,nu)], PERP[(mp,np_)]
            proj = (1.0 if pa==pb else 0.0) - k[:,pa]*k[:,pb]/k2
            w = SIG[(mu,nu)]*SIG[(mp,np_)]*S[(mu,nu)]*S[(mp,np_)]*proj
            ca = np.zeros(3); ca[mu]+=.5; ca[nu]+=.5
            cb = np.zeros(3); cb[mp]+=.5; cb[np_]+=.5
            for Y in Ys:
                dZ = np.array(Y) + ca - cb     # Z - Z' with Y' = 0
                val = (w*np.cos(P@dZ)).sum()/n**3
                for Yp in Ys:
                    Yd = tuple((np.array(Y)+np.array(Yp)) % n)
                    C[3*site(Yd,n)+a, 3*site(Yp,n)+b] = val
    return C

if __name__ == "__main__":
    for (n,L,N) in [(2,2,1),(2,3,1),(3,2,1),(2,2,2)]:
        Cb = np.load(f'/private/tmp/ym-r3/T7c-gaussian3d/brute_n{n}_L{L}_N{N}.npy')
        Cf = C_fourier_direct(n, L**N)
        print(n,L,N,'max|brute-fourier| =', np.abs(Cb-Cf).max(), ' max|C| =', np.abs(Cb).max())
