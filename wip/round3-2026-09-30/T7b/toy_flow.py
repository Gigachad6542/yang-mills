# Toy version of Dimock I sec.5 boundary-value flow (259)-(260), scalar caricature.
# mu_k = L^-2 (mu_{k+1} - c*E_k - mustar(lam_k, mu_k, E_k)),  E_{k+1} = L^-1 E_k + Estar(lam_k, mu_k, E_k)
# lam_k = L^{-(N-k)} lam; boundary mu_N = 0, E_0 = 0. Solve by fixed-point iteration (the contraction of Lemma 23).
# Compare N and N+1 at equal distance j = N-k from the coarse end.
import math
L, lam, c = 3.0, 0.5, 0.1
def mustar(l, mu, E): return 0.5*l**0.75 + 0.3*l**0.25*mu + 0.2*E*E
def Estar(l, mu, E):  return 0.4*l**0.25*(1+mu) + 0.1*E*E
def solve(N, iters=400):
    lamk=[L**(-(N-k))*lam for k in range(N+1)]
    mu=[0.0]*(N+1); E=[0.0]*(N+1)
    for _ in range(iters):
        mu2=mu[:]; E2=E[:]
        for k in range(N-1,-1,-1): mu2[k]=L**-2*(mu[k+1]-c*E[k]-mustar(lamk[k],mu[k],E[k]))
        mu2[N]=0.0
        E2[0]=0.0
        for k in range(1,N+1): E2[k]=E[k-1]/L+Estar(lamk[k-1],mu[k-1],E[k-1])
        mu,E=mu2,E2
    return mu,E
print(" N   max_j<=5 |E^{N+1}_j-E^N_j|   max_j<=5 |mu^{N+1}_j-mu^N_j|   ratio")
prev=None
for N in range(6,22,2):
    m1,e1=solve(N); m2,e2=solve(N+1)
    dE=max(abs(e2[N+1-j]-e1[N-j]) for j in range(6))
    dm=max(abs(m2[N+1-j]-m1[N-j]) for j in range(6))
    print(f"{N:3d}   {dE:.3e}                 {dm:.3e}      {'' if prev is None else f'{prev/dE:.2f}'}")
    prev=dE
# a_k shift (Dimock I (32)): a_k = a(1-L^-2)/(1-L^-2k)
a=1.0
ak=lambda k: a*(1-L**-2)/(1-L**(-2*k))
print("a_{k+1}-a_k:", [f"{ak(k+1)-ak(k):.2e}" for k in range(1,8)], " L^-2k:", [f"{L**(-2*k):.2e}" for k in range(1,8)])
