"""T66 check (note 61 §6b.5): zero-free s-disc of the Gaussian s-flow.

3D noncompact U(1), units g^2 eps0 = 1. At terminal momentum K the Wilson
terminal flux covariance is C_1(K) = P(K) (M = 1), a projection onto a 2-dim
transverse space. The once-blocked covariance is C_L(K) (M = L), from
t7_gauss3d.terminal_cov. On range P(K) the once-blocked precision has
eigenvalues r = 1/lambda, lambda the eigenvalues of P C_L P there. The
s-deformed precision is 1 + s(r - 1), so Xi(s) is zero-free on
|s| < 1/(r_max - 1), independently of N and of the volume.
"""
import sys, itertools, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from t7_gauss3d import terminal_cov

def rvals(K, L):
    P = terminal_cov(K, 1)
    w, U = np.linalg.eigh((P + P.conj().T) / 2)
    B = U[:, w > 0.5]                       # transverse eigenspace of C_1
    CL = terminal_cov(K, L)
    lam = np.linalg.eigvalsh(B.conj().T @ ((CL + CL.conj().T) / 2) @ B)
    return 1.0 / lam

print("| L | grid n_0 | min r | max r | 1/(max r - 1) |")
print("|---|---|---|---|---|")
for L, n0 in [(2, 16), (3, 12), (4, 8)]:
    rs = []
    for m in itertools.product(range(n0), repeat=3):
        if m == (0, 0, 0):
            continue
        K = 2*np.pi*np.array(m)/n0
        K = np.where(K > np.pi, K - 2*np.pi, K)
        rs.extend(rvals(K, L))
    rs = np.array(rs)
    print(f"| {L} | {n0} | {rs.min():.3f} | {rs.max():.3f} | {1/(rs.max()-1):.3f} |")
