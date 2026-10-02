# Finite-space check of: log(dnu_1/dnu_0)(W) = int_0^1 (E_s[D|b=W]-E_s[D]) ds
# and dZ_s/ds = Cov_s(G o b, D) for complex G.
import numpy as np
rng=np.random.default_rng(1)
n, nW = 40, 5
mu0 = rng.random(n); mu0/=mu0.sum()
D = rng.normal(size=n)*2; b = rng.integers(0,nW,size=n)
G = np.exp((0.3+0.7j)*rng.normal(size=nW))
def mus(s): w=mu0*np.exp(s*D); return w/w.sum()
def nu(m): return np.bincount(b,weights=m,minlength=nW)
def cond(m,f): return np.bincount(b,weights=m*f,minlength=nW)/nu(m)
ss=np.linspace(0,1,2001)
integrand=np.array([cond(mus(s),D)-(mus(s)*D).sum() for s in ss])
lhs=np.log(nu(mus(1))/nu(mus(0)))
rhs=np.trapezoid(integrand,ss,axis=0)
print("RN identity max err", np.abs(lhs-rhs).max())
Z=lambda s:(mus(s)*G[b]).sum()
h=1e-6; s=0.37
cov=(mus(s)*G[b]*D).sum()-Z(s)*(mus(s)*D).sum()
print("cov identity err", abs((Z(s+h)-Z(s-h))/(2*h)-cov))
