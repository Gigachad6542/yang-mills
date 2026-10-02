"""T17: abelian check of the persistent-curvature action lemma (PA).
4D torus (Z/n)^4. Level-j block-flux functional w_j (orientation (0,1)):
(M_j-box average) * (M_j x M_j square), M_j = L^j, all with corner at the origin
(nested blocks). Minimal 1/2|dA|^2 subject to <w_j, dA> = eps (j=1..t) equals
1/2 eps^2 * 1^T G^{-1} 1, with G_ij = <w_i, P w_j> and P the projection onto exact 2-forms.
(PA) in the abelian case <=> 1^T G^{-1} 1 grows linearly in t."""
import sys, numpy as np
L = int(sys.argv[1]) if len(sys.argv) > 1 else 2
n = int(sys.argv[2]) if len(sys.argv) > 2 else 32
tmax = int(sys.argv[3]) if len(sys.argv) > 3 else 4
k = 2*np.pi*np.fft.fftfreq(n)
K = np.meshgrid(k, k, k, k, indexing='ij')
r = [np.exp(1j*Ki) - 1 for Ki in K]
r2 = sum(np.abs(x)**2 for x in r); r2[0,0,0,0] = 1.0
mu, nu = 0, 1
# P_aa for a=(mu,nu) with R_{(mu nu),j} = r_mu delta_{nu j} - r_nu delta_{mu j}: P_aa = (|r_mu|^2+|r_nu|^2)/|r|^2
Paa = (np.abs(r[mu])**2 + np.abs(r[nu])**2)/r2; Paa[0,0,0,0] = 0.0
def D(q, M): return np.where(np.abs(np.exp(-1j*q)-1) < 1e-12, M, (1-np.exp(-1j*q*M))/(1-np.exp(-1j*q)))
def what(M):
    w = np.ones_like(K[0], dtype=complex)
    for i in range(4): w = w*D(K[i], M)/M
    return w*D(K[mu], M)*D(K[nu], M)
W = [what(L**j) for j in range(1, tmax+1)]
G = np.array([[np.real(np.sum(np.conj(W[i])*Paa*W[j]))/n**4 for j in range(tmax)] for i in range(tmax)])
print(f"L={L} n={n}: Gram diagonal (variance of level-j flux, scale-invariant ~ const):", np.round(np.diag(G), 5))
print("correlation matrix:\n", np.round(G/np.sqrt(np.outer(np.diag(G), np.diag(G))), 4))
for t in range(1, tmax+1):
    g = G[:t, :t]; val = np.ones(t) @ np.linalg.solve(g, np.ones(t))
    print(f"  t={t}: 1^T G^-1 1 = {val:.4f}   per level = {val/t:.4f}")
