"""T76 check (note 61 section 6c, Proposition 6c.4): N-independent complex
neighbourhood of the real s-orbit for the quadratic (Schur) sector.

For s = sigma + i varsigma, Pi_N^(s) = S + s Delta on the level-N lattice, flowed
down j steps by the holomorphic continuation of the Schur step
(Sigma(Pi) = (G Pi^{-1})^{-1} on the transverse space).  Claim: with
    eps := max_p || Pi_N^(sigma)^{-1/2} (i varsigma Delta) Pi_N^(sigma)^{-1/2} ||
         = max_p |varsigma| rho(p)/(1+sigma rho(p)),   rho = eig(Delta) (S = 1),
and eps < 1, for every j and every transverse vector Phi at level j,
    | Phi^dag (Pi_j^(s) - Pi_j^(sigma)) Phi | <= eps/(1-eps) Phi^dag Pi_j^(sigma) Phi.
Reported: the largest ratio |.| / (eps/(1-eps) Phi^dag Pi Phi) over K, j (numerical
radius of the whitened difference), which must be <= 1.
"""
import sys, itertools, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from t7_gauss3d import terminal_cov
from t76_convexity import transverse_P, step_cov, basis_B, pinv_h


def inv_on_B(A, U):
    """inverse of A restricted to B (basis U), expanded back to 3x3; zero off B."""
    Ab = np.conj(np.swapaxes(U, -1, -2)) @ A @ U
    return U @ np.linalg.inv(Ab) @ np.conj(np.swapaxes(U, -1, -2))


def whitened_numrad(Diff, Pi, U, keep):
    """numerical radius of Pi^{-1/2} Diff Pi^{-1/2} on B (2x2 blocks)."""
    Db = np.conj(np.swapaxes(U, -1, -2)) @ Diff @ U
    Pb = np.conj(np.swapaxes(U, -1, -2)) @ Pi @ U
    Pb = (Pb + np.conj(np.swapaxes(Pb, -1, -2)))/2
    w, V = np.linalg.eigh(Pb)
    Ph = (V/np.sqrt(w)[..., None, :]) @ np.conj(np.swapaxes(V, -1, -2))
    M = (Ph @ Db @ Ph)[keep]
    H = (M + np.conj(np.swapaxes(M, -1, -2)))/2
    # numerical radius of 2x2 M: max over theta of lambda_max(Re(e^{i theta} M))
    best = 0.0
    for th in np.linspace(0, 2*np.pi, 361):
        Hh = (np.exp(1j*th)*M + np.conj(np.swapaxes(np.exp(1j*th)*M, -1, -2)))/2
        best = max(best, np.linalg.eigvalsh(Hh).max())
    return best


def flow_complex(Pi, L, N, n0):
    """list of level-j precisions (j = 0..N) from level-N precision Pi (complex ok)."""
    out = [Pi]
    n = Pi.shape[0]
    for j in range(1, N+1):
        U, z = basis_B(n)
        F = np.zeros_like(Pi)
        F[~z] = inv_on_B(Pi[~z], U[~z])
        Fc = step_cov(F, L)
        n //= L
        Uc, zc = basis_B(n)
        Pi = np.zeros_like(Fc)
        keep = ~zc
        Pi[keep] = inv_on_B(Fc[keep], Uc[keep])
        out.append(Pi)
    return out


def run(L, n0, N, cases):
    n = n0*L**N
    a = 2*np.pi*np.arange(n)/n
    Kg = np.stack(np.meshgrid(a, a, a, indexing='ij'), axis=-1)
    P = transverse_P(n)
    F1 = np.zeros((n, n, n, 3, 3), dtype=complex)
    for ia, ib, ic in itertools.product(range(n), repeat=3):
        if (ia, ib, ic) != (0, 0, 0):
            F1[ia, ib, ic] = terminal_cov(Kg[ia, ib, ic], L)
    Pi1 = pinv_h(F1, 1e-9)
    Delta = Pi1 - P
    U, zm = basis_B(n)
    rho = np.linalg.eigvalsh(np.conj(np.swapaxes(U, -1, -2)) @ Delta @ U)[~zm].max()
    print(f"L={L} n0={n0} N={N}: rho = max eig Delta = {rho:.4f}, 1/rho = {1/rho:.4f}")
    allok = True
    for sig, vs in cases:
        s = sig + 1j*vs
        eps = vs*rho/(1+sig*rho)
        if eps >= 1:
            print(f"  s={sig}+{vs}i: eps={eps:.3f} >= 1, skipped"); continue
        ref = flow_complex(P + sig*Delta, L, N, n0)
        cpx = flow_complex(P + s*Delta, L, N, n0)
        worst = 0.0
        for j in range(N+1):
            nj = n0*L**(N-j)
            Uj, zj = basis_B(nj)
            nr = whitened_numrad(cpx[j] - ref[j], ref[j], Uj, ~zj)
            worst = max(worst, nr/(eps/(1-eps)))
        ok = worst <= 1+1e-9
        allok &= ok
        print(f"  s={sig}+{vs}i: eps={eps:.3f}, bound eps/(1-eps)={eps/(1-eps):.3f}, "
              f"max_j,K ratio (numerical radius)/(bound) = {worst:.4f}  {'OK' if ok else 'VIOLATION'}")
    return allok


if __name__ == '__main__':
    ok = True
    ok &= run(2, 4, 2, [(0.0, 0.1), (0.0, 0.2), (0.0, 0.3), (0.5, 0.2), (0.5, 0.4), (1.0, 0.3), (1.0, 0.6)])
    ok &= run(2, 4, 3, [(0.0, 0.2), (0.5, 0.4), (1.0, 0.6)])
    ok &= run(3, 4, 2, [(0.0, 0.1), (0.0, 0.15), (0.5, 0.2), (1.0, 0.3)])
    print("ALL OK" if ok else "VIOLATION")
