# Gaussian check: terminal block-averaged covariance of a 3D lattice field at
# depth N vs N+1 on the unit torus. Terminal lattice n0^3 (eps0=1/n0), block L.
# Action: (1/2) sum_x eps^3 [ sum_mu (grad_mu phi)^2 + m^2 phi^2 ].
import numpy as np, sys
n0, L, m2 = 4, 2, 1.0
def terminal_cov(N):
    n = n0 * L**N; eps = 1.0/n; b = L**N
    k = np.arange(n); p = 2*np.pi*k           # physical momenta (unit torus)
    lam1 = (4/eps**2)*np.sin(p*eps/2)**2       # 1D lattice Laplacian symbol
    # |average over b consecutive sites|^2 symbol (per direction)
    with np.errstate(invalid='ignore', divide='ignore'):
        num = np.sin(p*eps*b/2)**2; den = (b*np.sin(p*eps/2))**2
        chi2 = np.where(den > 1e-30, num/np.where(den>1e-30,den,1), 1.0)
    # covariance G(p) = 1/(eps^3 * n^3) ... use continuum-normalized: E|phihat|^2 = 1/(lam+m2)
    C = np.zeros((n0,n0,n0))
    K = k % n0
    for i in range(n):
        lam = lam1[i] + lam1[:,None] + lam1[None,:] + m2
        w = chi2[i]*chi2[:,None]*chi2[None,:]/lam
        # accumulate by terminal momentum class
        np.add.at(C, (K[i], K[:,None].repeat(n,1), K[None,:].repeat(n,0)), w)
    return C
prev = None
for N in range(0, int(sys.argv[1]) if len(sys.argv)>1 else 6):
    C = terminal_cov(N)
    if prev is not None:
        r = C/prev - 1
        print(N, "eps=%g"%(1/(n0*L**N)), "max|r|=%.4e"%np.abs(r).max(),
              "HS=%.4e"%np.sqrt((r**2).sum()), flush=True)
    prev = C
