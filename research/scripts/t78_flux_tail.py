"""T78: tail of the zero-extended FLUX-form kernel (contrast with the potential-form kernel).

The form Pi_j^(s)(K) on the transverse space, extended by zero off it, contains the
projector P(K) = 1 - conj(r) r^T/|r|^2, whose real-space kernel is the (nonlocal) lattice
Riesz-type kernel.  Local exponents of |k(x)| along an axis and along the diagonal,
n = 64 coarse torus.
"""
import sys, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from t78_kernel_decay import symbols, to_real, P_of, r_of

n = 64
idx = [1, 2, 4, 8, 16, 24, 30]


def report(name, fr):
    ax = [np.abs(fr[i, 0, 0]).max() for i in idx]
    dg = [np.abs(fr[i, i, i]).max() for i in idx]
    ex = lambda v, sc: [round(float(np.log(v[i]/v[i+1])/np.log(sc[i+1]/sc[i])), 2) for i in range(len(idx)-1)]
    print(name)
    print("  axis  x=" + str(idx) + " |k|=" + str(['%.2e' % a for a in ax]))
    print("        local power-law exponents " + str(ex(ax, idx)))
    print("  diag  |k|=" + str(['%.2e' % a for a in dg]))
    print("        local power-law exponents " + str(ex(dg, idx)))


for (L, j, s) in [(2, 1, 0.0), (2, 2, 0.0)]:
    Kg, sym, zero = symbols(j, s, L, n)
    report(f"L={L} j={j} s={s}: zero-extended flux form Pi(K)", to_real(sym))

a = 2*np.pi*np.arange(n)/n
Kg = np.stack(np.meshgrid(a, a, a, indexing='ij'), axis=-1)
Pk = P_of(Kg)
Pk[(np.abs(r_of(Kg)).sum(-1) < 1e-12)] = 0
report("Wilson form P(K) alone (j = 0)", to_real(Pk))
