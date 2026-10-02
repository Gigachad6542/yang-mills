import numpy as np, itertools, sys
sys.path.insert(0,'/private/tmp/ym-r3/T7c-gaussian3d')
from common import *
def brute(n, L, N, contour='axis'):
    M = L**N; s = n*M
    D = dmat(s); G = np.linalg.pinv(D.T@D, rcond=1e-9, hermitian=True)
    Qt = np.eye(3*s**3); ss = s
    for j in range(N):
        Qt = Qmat(ss, L, contour)@Qt; ss//=L
    T = dmat(n)@Qt                       # terminal fluxes as functional of fine A
    g0sq = 1.0/M                         # g^2 eps_0 = 1
    C = g0sq * T@G@T.T
    # check gauge covariance: T annihilates gradients & constants
    grad = D  # not used
    return C, T, D
if __name__=="__main__":
    for (n,L,N) in [(2,2,1),(2,3,1),(3,2,1),(2,2,2)]:
        C,T,D = brute(n,L,N)
        # T kills ker d? test on gradient fields and constant fields
        s=n*L**N
        # gradient of random lambda
        lam = np.random.randn(s**3); A=np.zeros(3*s**3)
        for x in itertools.product(range(s),repeat=3):
            for mu in range(3):
                e=[0,0,0]; e[mu]=1
                A[link(x,mu,s)] = lam[site([x[i]+e[i] for i in range(3)],s)]-lam[site(x,s)]
        const = np.zeros(3*s**3); const[0::3]=1.0
        C2,_,_ = brute(n,L,N,'rev') if s<=9 else (None,None,None)
        np.save(f'/private/tmp/ym-r3/T7c-gaussian3d/brute_n{n}_L{L}_N{N}.npy', C)
        print(n,L,N, 'max|T grad|',np.abs(T@A).max(),'max|T const|',np.abs(T@const).max(),
              'C[0,0..2]',C[0,:3], 'contour-indep', None if C2 is None else np.abs(C-C2).max())
