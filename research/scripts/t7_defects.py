"""T7 computation 3: (a) one-step defect structure; (b) fine-scale defect insertions.
Units g^2 eps0 = 1 (see t7_gauss3d.py)."""
import numpy as np
from t7_gauss3d import terminal_cov, all_K

print("(a) once-blocked finer theory vs Wilson theory on the same lattice, small momentum")
print("    ratio C_blocked/C_Wilson - 1 for the transverse flux B_1 at K=(kappa,0,0)")
for L in (2, 3):
    for kap in (0.4, 0.2, 0.1, 0.05):
        K = np.array([kap, 0, 0])
        r = (terminal_cov(K, L)[1, 1] / terminal_cov(K, 1)[1, 1]).real - 1
        print(f"    L={L} kappa={kap:5.2f}  ratio-1 = {r:+.6e}   /kappa^2 = {r/kap**2:+.5f}")

print("(b) fine-scale defect inserted at depth N, effect on terminal covariance (n0=4)")
Ks = all_K(4)
for kind, gam in (("dim4q", 1.0), ("dim6", 1.0)):
    print(f"  defect {kind}, gamma={gam}")
    last = None
    for N in range(1, 7):
        M = 2**N
        e = max(np.abs(terminal_cov(K, M, gamma=gam, kind=kind) - terminal_cov(K, M)).max() for K in Ks)
        print(f"    L=2 N={N} M={M:3d}  sup|dC| = {e:.4e}" + (f"  ratio={last/e:.3f}" if last else ""))
        last = e
