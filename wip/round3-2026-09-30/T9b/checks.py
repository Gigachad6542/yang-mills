import numpy as np
rng=np.random.default_rng(1)
# 1. Prop 1 (note 13) on random finite measures with disjoint parts of support, plus unequal-mass generalization
n=12
P=rng.random(n)*(rng.random(n)<.6); R=rng.random(n)*(rng.random(n)<.6)
F=rng.normal(size=n)+1j*rng.normal(size=n)
S=P+R; m=S>0
h=np.zeros(n); h[m]=(R[m]-P[m])/S[m]
aP,aR=P.sum(),R.sum()
mu=S/(aP+aR)
lhs=(F*(R-P)).sum()
EF=(mu*F).sum(); Eh=(mu*h).sum()
cov=(mu*F*h).sum()-EF*Eh
print("general identity err", abs(lhs-((aP+aR)*cov+(aR-aP)*EF)))
R2=R*aP/aR; S2=P+R2; h2=np.zeros(n); m2=S2>0; h2[m2]=(R2[m2]-P[m2])/S2[m2]; mu2=S2/(2*aP)
EF2=(mu2*F).sum(); cov2=(mu2*F*h2).sum()-EF2*(mu2*h2).sum()
print("equal-mass Prop1 err", abs((F*(R2-P)).sum()/aP-2*cov2), "E h", (mu2*h2).sum())
# TV-sharpened (2.4): |1/a int F d(R-P)| <= ||F-c|| * TV/a
Fr=F.real; c=(Fr.max()+Fr.min())/2
print("TV bound", abs((Fr*(R2-P)).sum())/aP, "<=", np.abs(Fr-c).max()*np.abs(R2-P).sum()/aP, "<=", 2*np.abs(Fr-c).max())
# 2. SU(2) Haar: int (tr U)^2 = 1, int trU = 0 ; smooth counterexample
q=rng.normal(size=(400000,4)); q/=np.linalg.norm(q,axis=1)[:,None]
tr=2*q[:,0]; Fh=tr/2
print("E trU", tr.mean(), "E (trU)^2", (tr**2).mean())
t=1.0
print("smooth cex: int F d(R-P) = 2t E F^2 =", 2*t*(Fh**2).mean(), "(exact 1/2)")
# two-point example
print("two-point: ", 1-(-1))
# 3. note 16 examples
eps=1e-3
Q=eps; Pm=1.0; r_b=Pm/Q*eps; print("(2.6) r(E)=",r_b)
alpha={'a':eps,'b':1-eps}; varpi={'a':1,'b':1-eps}
print("(3.5) exact avg", alpha['a']*1, "majorant avg", varpi['a']*1)
# 4. note 14 tail exponent with H_L>1
L=2;H=1.5;N=6;eps0=1.0
for e in [1e-3,1e-4,1e-5]:
    K=np.log(eps0/e)/np.log(L)
    tail=(H*L**(3-N))**K
    print(e, tail, "exponent", np.log(tail)/np.log(e), "N-3-log_L H =", N-3-np.log(H)/np.log(L))
