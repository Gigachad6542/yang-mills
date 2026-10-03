"""T37: sharp constant in ||grad_nu F_min||_2 <= C_M M^{-1} ||F_min||_2 (abelian, note 44).

F_min = d Delta^{-1} J, with J_rho(p_l) = A_rho(p_l) c_rho(K) and
A_rho(p) = prod_j D_M(p_j) * D_M(p_rho), p_l = (K + 2 pi l)/M. For each coarse
momentum K and component rho, the energy ratio is N_rho/D_rho with
    N_rho = sum_l |e^{i p_nu}-1|^2 |A_rho|^2 / |r|^2,   D_rho = sum_l |A_rho|^2 / |r|^2.
The sharp constant is C_M = M * sup_K max_{rho, nu} sqrt(N/D) (an upper bound,
since the c_rho are further constrained). Also checks the alias-0 fraction
against the proven c_0 = 1024/pi^10.
"""
import itertools
import numpy as np


def D(p, M):
    p = np.asarray(p, float)
    den = 1 - np.exp(-1j * p)
    out = np.where(np.abs(den) < 1e-13, M + 0j, (1 - np.exp(-1j * M * p)) / np.where(np.abs(den) < 1e-13, 1, den))
    return out


def run(M, nK=6):
    ells = np.array(list(itertools.product(range(M), repeat=4))).T
    worst, frac_min = 0.0, 1.0
    ks = [2 * np.pi * (k + 0.5) / nK - np.pi for k in range(nK)]  # avoid K = 0 exactly
    for K in itertools.product(ks, repeat=4):
        K = np.array(K)
        p = (K[:, None] + 2 * np.pi * ells) / M
        Dp = D(p, M)
        base = np.abs(np.prod(Dp, axis=0)) ** 2
        r2 = np.sum(4 * np.sin(p / 2) ** 2, axis=0)
        i0 = np.argmin(r2)
        for rho in range(4):
            A2 = base * np.abs(Dp[rho]) ** 2
            frac_min = min(frac_min, A2[i0] / A2.sum())
            Dn = np.sum(A2 / r2)
            for nu in range(4):
                N = np.sum(4 * np.sin(p[nu] / 2) ** 2 * A2 / r2)
                worst = max(worst, np.sqrt(N / Dn))
    return M * worst, frac_min


if __name__ == "__main__":
    print("proven c0 = 1024/pi^10 =", 1024 / np.pi**10, " -> proven constant 2 pi/sqrt(c0) =", 2 * np.pi / np.sqrt(1024 / np.pi**10))
    for M in (2, 3, 4, 6, 8, 12, 16):
        C, f = run(M)
        print(f"M={M}: sharp C_M = M*sup ratio = {C:.3f}; min alias-0 fraction = {f:.4f}", flush=True)


def run2(M, nK=6):
    """Sharp ratio for second differences: sup sqrt(N2/D) with N2 = sum |r_mu|^2|r_nu|^2 |A|^2/|r|^2."""
    ells = np.array(list(itertools.product(range(M), repeat=4))).T
    worst = 0.0
    ks = [2 * np.pi * (k + 0.5) / nK - np.pi for k in range(nK)]
    for K in itertools.product(ks, repeat=4):
        K = np.array(K)
        p = (K[:, None] + 2 * np.pi * ells) / M
        Dp = D(p, M)
        base = np.abs(np.prod(Dp, axis=0)) ** 2
        s2 = 4 * np.sin(p / 2) ** 2
        r2 = s2.sum(0)
        for rho in range(4):
            A2 = base * np.abs(Dp[rho]) ** 2
            Dn = np.sum(A2 / r2)
            for mu in range(4):
                for nu in range(4):
                    N = np.sum(s2[mu] * s2[nu] * A2 / r2)
                    worst = max(worst, np.sqrt(N / Dn))
    return worst


if __name__ == "__main__":
    print("\nSecond differences: sup ||grad_mu grad_nu F|| / ||F||")
    for M in (2, 3, 4, 6, 8, 12, 16):
        w = run2(M)
        print(f"M={M}: ratio {w:.4f}  M*ratio {M*w:.3f}  M^1.5*ratio {M**1.5*w:.3f}  M^2*ratio {M*M*w:.3f}", flush=True)


def run_potential(M, nK=6):
    """Sharp M * sup ||grad A_min|| / ||A_min|| for the Landau-gauge potential (|A|^2 = |J|^2/|r|^4)."""
    ells = np.array(list(itertools.product(range(M), repeat=4))).T
    worst = 0.0
    ks = [2 * np.pi * (k + 0.5) / nK - np.pi for k in range(nK)]
    for K in itertools.product(ks, repeat=4):
        K = np.array(K)
        p = (K[:, None] + 2 * np.pi * ells) / M
        Dp = D(p, M)
        base = np.abs(np.prod(Dp, axis=0)) ** 2
        s2 = 4 * np.sin(p / 2) ** 2
        r4 = s2.sum(0) ** 2
        for rho in range(4):
            A2 = base * np.abs(Dp[rho]) ** 2
            Dn = np.sum(A2 / r4)
            for nu in range(4):
                worst = max(worst, np.sqrt(np.sum(s2[nu] * A2 / r4) / Dn))
    return M * worst
