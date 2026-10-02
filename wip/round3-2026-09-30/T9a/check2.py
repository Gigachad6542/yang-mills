"""Linearization (3.1)-(3.2) and Proposition 2 (3.4)-(3.7) checks."""
import sys, itertools, numpy as np, scipy.linalg as sla
sys.path.insert(0,'/private/tmp/ym-r3/T9a')
from avg04 import *
rng=np.random.default_rng(2)

def run(d,L,Nc):
    lat=Lat(d,L,Nc); CB=list(lat.coarse_bonds()); FB=all_bonds(lat)
    fi={b:i for i,b in enumerate(FB)}; ci={c:i for i,c in enumerate(CB)}
    TR={c:lat.triples(c) for c in CB}
    # exact linearization: Q_lin A(c) = sum_w A(ell)   (A(ell) signed sum)
    Q=np.zeros((len(CB),len(FB)))
    for c in CB:
        for w,ell in TR[c]:
            for (x,mu,sg) in ell: Q[ci[c],fi[(x,mu)]]+=w*sg
    # finite-difference check of nonlinear map at U=1, abelian direction sigma_z
    eps=1e-6; A=rng.normal(size=len(FB))
    U={b:sla.expm(1j*eps*A[fi[b]]*sz) for b in FB}
    for c in CB[:4]:
        Ub=avg(lat,U,c,TR[c]); lin=np.real(np.trace(speclog(Ub)@sz))/2/eps
        assert abs(lin-Q[ci[c]]@A)<1e-5, (lin,Q[ci[c]]@A)
    # formula (3.1)-(3.2): Lambda_sym(c_-) + S(A)(c) - Lambda_sym(c_+)
    Q2=np.zeros_like(Q)
    for c in CB:
        y,mu=c; cm=lat.cminus(c); cp=lat.add(cm,mu,L)
        for disp in itertools.product(range(-lat.h,lat.h+1),repeat=d):
            x=tuple((cm[i]+disp[i])%lat.n for i in range(d))
            for base,sgn in [(cm,1),(cp,-1)]:
                F=lat.G(base,disp)
                for g in F:
                    for (z,nu,sg) in g: Q2[ci[c],fi[(z,nu)]]+=sgn*sg*L**(-d)/len(F)
            seg,_=lat.straight(x,mu,L)
            for (z,nu,sg) in seg: Q2[ci[c],fi[(z,nu)]]+=sg*L**(-d)
    assert np.allclose(Q,Q2)
    # coarse divergence matrix: (div tau)(y)=sum_{c_-=y} tau - sum_{c_+=y} tau
    ys=list(itertools.product(range(Nc),repeat=d)); yi={y:i for i,y in enumerate(ys)}
    D=np.zeros((len(ys),len(CB)))
    for c in CB:
        y,mu=c; yp=list(y); yp[mu]=(yp[mu]+1)%Nc
        D[yi[y],ci[c]]+=1; D[yi[tuple(yp)],ci[c]]-=1
    # fine divergence
    xs=list(itertools.product(range(lat.n),repeat=d)); xi={x:i for i,x in enumerate(xs)}
    Df=np.zeros((len(xs),len(FB)))
    for (x,mu) in FB:
        Df[xi[x],fi[(x,mu)]]+=1; Df[xi[lat.add(x,mu)],fi[(x,mu)]]-=1
    Ker=sla.null_space(D)
    P=Q.T
    worst=[0,0,0]; divmax=0
    for _ in range(300):
        tau=Ker@rng.normal(size=Ker.shape[1])
        if rng.random()<0.3: tau=Ker@(rng.normal(size=Ker.shape[1])*(rng.random(Ker.shape[1])<0.2))
        Pt=P@tau
        divmax=max(divmax,np.abs(Df@Pt).max())
        worst[0]=max(worst[0],np.abs(Pt).max()/np.abs(tau).max()/L**(1-d))
        worst[1]=max(worst[1],np.abs(Pt).sum()/np.abs(tau).sum()/L)
        worst[2]=max(worst[2],(Pt@Pt)/(tau@tau)/L**(2-d))
    # exact operator norm of P restricted to Ker in l2
    s2=np.linalg.norm(P@Ker,2)**2/L**(2-d)
    # sharpness: constant current along direction 0
    tau=np.array([1.0 if c[1]==0 else 0.0 for c in CB]); Pt=P@tau
    sh=(np.abs(Pt).max()/L**(1-d), np.abs(Pt).sum()/tau.sum()/L, (Pt@Pt)/(tau@tau)/L**(2-d))
    # without div-free: sup-norm ratio of full P
    tau=np.ones(len(CB));
    print(f"d={d} L={L} Nc={Nc}: lin ok; max|div P tau|={divmax:.1e}; random ratios/bound (inf,1,2)={np.round(worst,4)}; exact l2 op-norm^2 on Ker / L^(2-d) = {s2:.4f}; constant-current ratios={np.round(sh,4)}")

for args in [(2,3,3),(2,3,4),(2,5,2),(3,3,2)]:
    run(*args)
