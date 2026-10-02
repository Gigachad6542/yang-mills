"""Prop 1 (2.2),(2.4); Lemma 3 constant; Prop 4 (4.4)-(4.7); branch-cut example."""
import sys, itertools, numpy as np, scipy.linalg as sla
sys.path.insert(0,'/private/tmp/ym-r3/T9a')
from avg04 import *
rng=np.random.default_rng(3)
d,L,Nc=2,3,3
lat=Lat(d,L,Nc); CB=list(lat.coarse_bonds()); FB=all_bonds(lat)
TR={c:lat.triples(c) for c in CB}
CEN={c:set((b[0],b[1]) for b in lat.central(c)) for c in CB}
def omega(c,S):
    return sum(w for w,ell in TR[c] if any((b[0],b[1]) in S for b in ell))

# ---- Prop 1, rough fields (Haar-random background, arbitrary change on S)
worst=0; worst_sum=0
for trial in range(40):
    U={b:rand_su2(None,rng) for b in FB}
    k=rng.integers(1,4); S=set(FB[i] for i in rng.choice(len(FB),k,replace=False))
    U2=dict(U);
    for b in S: U2[b]=rand_su2(None,rng)
    tot=0
    for c in CB:
        diff=np.linalg.norm(avg(lat,U,c,TR[c])-avg(lat,U2,c,TR[c]),2)
        if CEN[c]&S: bnd=2
        else: bnd=min(2,2*np.pi*omega(c,S))
        worst=max(worst,diff/bnd if bnd>0 else (0 if diff<1e-12 else np.inf))
        tot+=diff
    worst_sum=max(worst_sum,tot/((2+2*np.pi*(2*d+L**(1-d)))*len(S)))
print("Prop1 max ratio diff/bound:",round(worst,4)," (2.4) max ratio:",round(worst_sum,4))

# ---- Lemma 3 constant: sup over directions of ||Zdot||/||Hdot H^-1|| at angle theta equals theta/sin(theta)
for th in [0.5,2.0,3.0]:
    Z=th*sz; best=0
    for _ in range(2000):
        a=rng.normal(size=3); Zd=sum(a[i]*PAULI[i] for i in range(3)); h=1e-6
        H0=sla.expm(1j*Z); H1=sla.expm(1j*(Z+h*Zd))
        v=(H1-H0)/h@H0.conj().T/1j
        best=max(best,np.linalg.norm(Zd)/np.linalg.norm(v))
    print(f"Lemma3 theta={th}: max ratio {best:.5f} vs theta/sin theta {th/np.sin(th):.5f}")

# ---- Prop 4: path length on Reg_delta
def Qall(U): return {c:avg(lat,U,c,TR[c]) for c in CB}
Kdl=2*d+L**(1-d)
worstP=0; worstP_sharp=0; nreg=0
for trial in range(25):
    k=rng.integers(1,4); S=[FB[i] for i in rng.choice(len(FB),k,replace=False)]
    Hs={}
    for b in S:
        a=rng.normal(size=3); a*=rng.uniform(0.2,2.5)/np.linalg.norm(a); Hs[b]=sum(a[i]*PAULI[i] for i in range(3))
    def W(t):
        U={b:np.eye(2,dtype=complex) for b in FB}
        for b in S: U[b]=sla.expm(1j*t*Hs[b])
        return U
    ts=np.linspace(0,1,121); vals=[]; mintheta_gap=np.inf
    for t in ts:
        U=W(t); vals.append(Qall(U))
        for c in CB:
            Uc=hol(U,lat.central(c))
            for w,ell in TR[c]:
                th=np.abs(np.linalg.eigvalsh(speclog(hol(U,ell)@Uc.conj().T))).max()
                mintheta_gap=min(mintheta_gap,np.pi-th)
    delta=mintheta_gap
    if delta<=1e-3: continue
    nreg+=1
    length=0
    for i in range(len(ts)-1):
        dt=ts[i+1]-ts[i]
        for c in CB:
            A=vals[i][c]; B=vals[i+1][c]
            X=speclog(B@A.conj().T)   # right-trivialized increment
            length+=np.linalg.norm(X)  # HS
    Cd=(np.pi-delta)/np.sin(delta)
    C0=np.pi*np.sqrt(2)*(Cd*(2*d+1+L**(1-d))+1)
    sharp=(Cd*(Kdl+1)+1)*sum(np.linalg.norm(Hs[b]) for b in S)
    worstP=max(worstP,length/(C0*len(S))); worstP_sharp=max(worstP_sharp,length/sharp)
print(f"Prop4: {nreg} regular trials; max length/(C0 s)={worstP:.4f}; max length/((C_d(K+1)+1)sum||H_b||_HS)={worstP_sharp:.4f}")

# ---- branch-cut example: bond in direction nu != mu at c_-
c=CB[0]; y,mu=c; nu=1-mu; cm=lat.cminus(c); b=(cm,nu)
om=sum(w for w,ell in TR[c] if any((z,n)==b for (z,n,sg) in ell))
U={bb:np.eye(2,dtype=complex) for bb in FB}; U[b]=-np.eye(2)
Ub=avg(lat,U,c,TR[c]); print("branch example: omega=",round(om,4)," det at endpoint=",np.round(np.linalg.det(Ub),6)," expected e^{2 pi i omega}=",np.round(np.exp(2j*np.pi*om),6))
for eps in [1e-2,1e-4]:
    U[b]=sla.expm(1j*(np.pi-eps)*sx); Ue=avg(lat,U,c,TR[c])
    print("  approach eps=",eps," det=",np.round(np.linalg.det(Ue),6)," ||Q(eps)-Q(end)||=",round(np.linalg.norm(Ue-Ub,2),4))
