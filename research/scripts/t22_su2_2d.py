"""T22: exact 2D SU(2) check of the sup-oscillation depth comparison (H-1 form).
Wilson weight exp(beta*cos(theta)) per fine plaquette (cos theta = tr(U)/2).
Exact holonomy blocking on a disc/plane (axial gauge): a terminal plaquette
holonomy is the product of M^2 = L^(2N) independent fine plaquette holonomies,
so its density is the M^2-fold class-function convolution
   f_M(theta) = sum_n (n+1) c_n(beta)^(M^2) chi_n(theta),
   c_n(beta) = I_{n+1}(beta)/I_1(beta),  chi_n = sin((n+1)theta)/sin(theta).
Continuum scaling: beta_M = M^2 * b (b = 4/(g^2 A0), A0 = terminal plaquette area).
Reports sup_theta |log f_{M L} - log f_M| (the terminal log-density oscillation)."""
import numpy as np
from scipy.special import ive
def logc(n, beta):            # log(I_{n+1}(beta)/I_1(beta)) using exponentially scaled Bessel
    return np.log(ive(n+1, beta)) - np.log(ive(1, beta))
def density(M, b, th, nmax=400):
    beta = M*M*b
    n = np.arange(nmax)
    w = (n+1)*np.exp(M*M*logc(n, beta))
    chi = np.sin(np.outer(n+1, th))/np.sin(th)
    return w @ chi
def heat(t, th, nmax=400):
    n = np.arange(nmax)
    return ((n+1)*np.exp(-t*n*(n+2)/4.0)) @ (np.sin(np.outer(n+1, th))/np.sin(th))
th = np.linspace(1e-3, np.pi-1e-3, 2001)
for b in (2.0, 8.0):
    print(f"b = {b} (heat-kernel time t = 1/b... continuum limit check)")
    for L in (2, 3):
        prev = None; last = None
        for N in range(0, 7 if L == 2 else 5):
            M = L**N; f = density(M, b, th)
            if f.min() <= 0: print("  nonpositive density", M); break
            if prev is not None:
                osc = np.abs(np.log(f) - np.log(prev)).max()
                print(f"  L={L} N={N} M={M:4d}  sup|log f_N - log f_(N-1)| = {osc:.4e}" + (f"  ratio={last/osc:.3f}" if last else ""))
                last = osc
            prev = f
