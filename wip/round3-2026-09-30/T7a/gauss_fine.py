# Fine-level vs terminal-level defect in the 3D Gaussian model.
# On the common eps-lattice (n^3 sites): once-blocked finer covariance Ct(p)
# vs coarse lattice covariance G_eps(p).  Report per-mode relative defect.
import numpy as np
n0, L, m2 = 4, 2, 1.0
def lam1(n):
    eps=1.0/n; k=np.arange(n); p=2*np.pi*k
    return (4/eps**2)*np.sin(p*eps/2)**2, p, eps
def chi2_1(p, eps, b):
    num=np.sin(p*eps*b/2)**2; den=(b*np.sin(p*eps/2))**2
    return np.where(den>1e-30, num/np.where(den>1e-30,den,1), 1.0)
for N in range(0,5):
    n = n0*L**N; nf = n*L
    lf, pf, ef = lam1(nf); c2 = chi2_1(pf, ef, L)
    lc, pc, ec = lam1(n)
    Kf = np.arange(nf) % n
    Ct = np.zeros((n,n,n))
    for i in range(nf):
        w = c2[i]*c2[:,None]*c2[None,:]/(lf[i]+lf[:,None]+lf[None,:]+m2)
        np.add.at(Ct,(Kf[i],Kf[:,None].repeat(nf,1),Kf[None,:].repeat(nf,0)),w)
    G = 1/(lc[:,None,None]+lc[None,:,None]+lc[None,None,:]+m2)
    r = Ct/G - 1
    print(N, "sites=%d"%n**3, "max|r|=%.3f"%np.abs(r).max(),
          "HS^2/sites=%.4f"%((r**2).sum()/n**3), "HS=%.2f"%np.sqrt((r**2).sum()), flush=True)
