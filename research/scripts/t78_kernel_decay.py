"""T78 computation (note 61 section 6d): decay of the real-space kernels of the
interpolated Schur complements Pi_j^(s) in the 3D abelian Fourier model of t76.

Model (t76_convexity.py): at every level the Wilson flux precision on the
transverse space B(p) = {B : sum_a r_a(p) B_a = 0}, r_a = e^{i p_a} - 1, is the
projector P(p).  One block step on precisions is Sigma(Pi) = (G Pi^+)^+,
(GF)(K) = L^-4 sum_{m in [0,L)^3} conj(W) F(p_m) W,  p_m = (K + 2 pi m)/L.
Level-N data of the orbit:  Pi_N^(s) = (1-s) P + s Sigma(P);
Pi_j^(s) = Sigma^j Pi_N^(s)  (t76 / note 61 (6c.1), with the factor L per step
absorbed in G).

For a coarse momentum grid K in (2 pi/n)Z^3 we evaluate Pi_j^(s)(K) exactly by
recursion over the L^(3j) aliases (no fine grid is built).

Two symbols are Fourier transformed to real space on the n^3 coarse torus:

  kappa(K) = C(K)^* Pi(K) C(K),  C(K) a = r(K) x a  (the form on coarse
             POTENTIALS: a -> Pi(curl a); 3x3, gauge invariant, kappa r = 0),
  Pi(K)    = the form on coarse FLUXES extended by zero off the transverse
             space (pinv convention; contains the projector P(K)).

Output per case: decay rate per coarse unit, fitted on  max_{ab}|kernel_ab(x)|
against |x|_1 (and the maximum over the shell), on the window where the kernel
is above floating-point noise and the torus wrap-around (|x|_inf <= n/2) is
negligible.
"""
import sys, time, itertools, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from t76_convexity import Dsum, pinv_h


def r_of(p):
    return np.exp(1j*p) - 1


def P_of(p):
    """transverse projector, p (...,3) -> (...,3,3); zero at p = 0."""
    r = r_of(p)
    r2 = (np.abs(r)**2).sum(-1)
    zero = r2 < 1e-24
    r2s = np.where(zero, 1.0, r2)
    P = np.eye(3)[None]*np.ones(p.shape[:-1] + (1, 1)) - np.conj(r)[..., :, None]*r[..., None, :]/r2s[..., None, None]
    P[zero] = 0.0
    return P


def W_of(p, L):
    """one-step kernel vector w_a(p), p (...,3) -> (...,3)."""
    D = [Dsum(p[..., i].copy(), L) for i in range(3)]
    out = []
    for a in range(3):
        f = D[a]/L**3
        for i in range(3):
            if i != a:
                f = f*D[i]**2
        out.append(f)
    return np.stack(out, axis=-1)


ALIAS = {}


def aliases(L):
    if L not in ALIAS:
        ALIAS[L] = np.array(list(itertools.product(range(L), repeat=3)), dtype=float)
    return ALIAS[L]


def G_batch(Ffun, K, L):
    """(GF)(K) for K (B,3): returns (B,3,3)."""
    m = aliases(L)                                       # (L^3,3)
    p = (K[:, None, :] + 2*np.pi*m[None])/L              # (B,L^3,3)
    Bn = K.shape[0]
    F = Ffun(p.reshape(-1, 3)).reshape(Bn, m.shape[0], 3, 3)
    W = W_of(p, L)                                       # (B,L^3,3)
    out = np.einsum('bmj,bmjk,bmk->bjk', np.conj(W), F, W) if False else \
        (np.conj(W)[..., :, None]*F*W[..., None, :]).sum(1)
    return out/L**4


def Pi1_of(p, L):
    return pinv_h(G_batch(lambda q: P_of(q), p, L), 1e-9)


def Pi(j, s, K, L):
    """Pi_j^(s)(K), K (B,3)."""
    if j == 0:
        Pp = P_of(K)
        if s == 0.0:
            return Pp
        return (1-s)*Pp + s*Pi1_of(K, L)
    F = lambda q: pinv_h(Pi(j-1, s, q, L), 1e-9)
    return pinv_h(G_batch(F, K, L), 1e-9)


def symbols(j, s, L, n, chunk=None):
    a = 2*np.pi*np.arange(n)/n
    Kg = np.stack(np.meshgrid(a, a, a, indexing='ij'), axis=-1).reshape(-1, 3)
    if chunk is None:
        chunk = max(1, int(2e6 // (L**(3*(j+1)))))
    out = np.zeros((Kg.shape[0], 3, 3), dtype=complex)
    for i in range(0, Kg.shape[0], chunk):
        out[i:i+chunk] = Pi(j, s, Kg[i:i+chunk], L)
    zero = (np.abs(r_of(Kg)) .sum(-1) < 1e-12)
    out[zero] = 0.0
    return Kg, out.reshape(n, n, n, 3, 3), zero.reshape(n, n, n)


def cross_matrix(r):
    """C(K) with C a = r x a, r (...,3) -> (...,3,3)."""
    z = np.zeros(r.shape[:-1], dtype=complex)
    return np.stack([np.stack([z, -r[..., 2], r[..., 1]], -1),
                     np.stack([r[..., 2], z, -r[..., 0]], -1),
                     np.stack([-r[..., 1], r[..., 0], z], -1)], -2)


def potential_symbol(Pisym, n):
    a = 2*np.pi*np.arange(n)/n
    Kg = np.stack(np.meshgrid(a, a, a, indexing='ij'), axis=-1)
    C = cross_matrix(r_of(Kg))
    return np.conj(np.swapaxes(C, -1, -2)) @ Pisym @ C


def to_real(sym):
    """kernel k(x)_{ab} = n^-3 sum_K sym(K)_{ab} e^{iKx}; returns array (n,n,n,3,3)."""
    n = sym.shape[0]
    return np.fft.ifftn(sym, axes=(0, 1, 2))      # = n^-3 sum_K e^{+iKx} sym(K)


def shell_profile(ker, n, norm='l1'):
    """max_{ab,x: |x|=d} |ker_ab(x)| for d = 0,1,..., using the periodic distance."""
    idx = np.arange(n); idx = np.minimum(idx, n-idx)
    X, Y, Z = np.meshgrid(idx, idx, idx, indexing='ij')
    if norm == 'l1':
        d = X + Y + Z
    elif norm == 'linf':
        d = np.maximum(np.maximum(X, Y), Z)
    else:
        d = np.sqrt(X**2 + Y**2 + Z**2)
    mag = np.abs(ker).max((-1, -2))
    prof = {}
    for dv in np.unique(d.round(6)):
        prof[float(dv)] = mag[np.isclose(d, dv)].max()
    return prof


def fit_rate(prof, n, noise=1e-13, dmin=2.0, dmax=None, rel=1e-9):
    """fit log prof ~ a - mu d on the window d in [dmin, dmax] where prof > noise
    (relative to the profile maximum) and d <= dmax (default: n/2 for l1... caller)."""
    ds = np.array(sorted(prof)); vs = np.array([prof[d] for d in ds])
    vmax = vs.max()
    ok = (ds >= dmin) & (vs > max(noise, rel*vmax))
    if dmax is not None:
        ok &= ds <= dmax
    if ok.sum() < 3:
        return np.nan, np.nan, int(ok.sum())
    A = np.vstack([np.ones(ok.sum()), -ds[ok]]).T
    coef, *_ = np.linalg.lstsq(A, np.log(vs[ok]), rcond=None)
    # also the local slope between the last two usable shells
    return coef[1], coef[0], int(ok.sum())


def run_case(L, j, s, n, verbose=True):
    t0 = time.time()
    Kg, sym, zero = symbols(j, s, L, n)
    kap = potential_symbol(sym, n)
    kap[zero] = 0.0
    kr = to_real(kap)
    pr = shell_profile(kr, n, 'l1')
    # power-law check on the flux symbol (extended by zero): kernel of Pi(K)
    fr = to_real(sym)
    pf = shell_profile(fr, n, 'l1')
    mu, c, npt = fit_rate(pr, n, dmax=n//2)
    # tail rate: fit on the last 5 usable shells (d <= n/2, kernel above 1e-8 x its maximum)
    dtop = max(d for d in pr if d <= n//2 and pr[d] > 1e-8*pr[0.0])
    mu_tail, _c2, _n2 = fit_rate(pr, n, dmin=dtop-4, dmax=dtop)
    # local slopes of the potential kernel
    ds = np.array(sorted(pr))
    sl = [(ds[i], np.log(pr[ds[i]]/pr[ds[i+1]])/(ds[i+1]-ds[i])) for i in range(len(ds)-1)
          if ds[i+1] <= n//2 and pr[ds[i+1]] > 1e-13 and ds[i] >= 1]
    # flux kernel: apparent decay between d = 2 and d = n/4
    d1, d2 = 2.0, float(n//4)
    fl = np.log(pf[d1]/pf[d2])/(d2-d1) if pf[d2] > 0 else np.nan
    pw = np.log(pf[d1]/pf[d2])/np.log(d2/d1) if pf[d2] > 0 else np.nan
    if verbose:
        print(f"L={L} j={j} s={s:<4} n={n}: potential-form kernel rate mu = {mu:.3f} per coarse unit "
              f"(l1 fit, {npt} shells, prefactor e^{c:.2f}), tail rate (d in [{dtop-4:.0f},{dtop:.0f}]) {mu_tail:.3f}; kernel(0) = {pr[0.0]:.3e}; "
              f"flux-form (zero-extended) kernel: |k|(2)={pf[2.0]:.2e}, |k|({int(d2)})={pf[d2]:.2e}, "
              f"apparent power-law exponent {pw:.2f} [{time.time()-t0:.0f}s]")
        sys.stdout.flush()
    return mu, mu_tail, pr, pf, sl


if __name__ == '__main__':
    cases = []
    for L, jmax, nn in [(2, 3, {1: 32, 2: 32, 3: 32}), (3, 3, {1: 16, 2: 16, 3: 16})]:
        for j in range(1, jmax+1):
            for s in (0.0, 0.5, 1.0):
                cases.append((L, j, s, nn[j]))
    only = sys.argv[1:]
    res = {}
    for L, j, s, n in cases:
        if only and f"{L},{j}" not in only:
            continue
        res[(L, j, s)] = run_case(L, j, s, n)
    print("\nSUMMARY (potential-form kernel decay rate mu per coarse unit, l1 distance)")
    for (L, j, s), (mu, mu_tail, *_r) in res.items():
        print(f"  L={L} j={j} s={s}: mu(fit) = {mu:.3f}  mu(tail) = {mu_tail:.3f}")
