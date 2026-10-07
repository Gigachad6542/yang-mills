"""T69: numerical check of the growth exponents of ghost / gauge-fixing
alias symbols (note 58 section 6).

Part A (d = 4, one alias variable).  Rescaled alias sums
    S_M = sum_{n in B_M^4} prod_j delta_M(n_j)^2 * f_M(n),
    f_M(n) = M^k v_k(p_n) / (M^2 |r(p_n)|^2)^2,
with v_0 = cos p_1 (k = 0, seagull type) and v_1 = sin p_1 (k = 1, one lattice
difference), plus the scalar ghost coarse covariance
    C_M(K) = sum_n prod_j delta_M(n_j)^2 / (M^2 |r(p_n)|^2)   (s = -2).
Claim (Lemma A, s <= 0): |S_M - S_inf| <= C (1 + log M)/M.  We print
|S_M - S_2M| and the successive ratios.

Part B (d = 2, two coupled alias variables n and m, background momentum P != 0).
    T_M = sum_{n,m} W(n) W(n-m) W_b(m) * M v(p_n, p_{n-m}) /
          ((M^2|r(p_n)|^2)(M^2|r(p_{n-m})|^2)),
v = sin((p_n+p_{n-m})_1/2) (symmetric first-order ghost vertex, k = 1),
W = prod delta_M^2 with coarse momenta K and K-P, W_b = prod delta_M^2 with
coarse momentum P.  This is the structure of Lemma A2 with r = 2.
Part C (d = 2, the true minimizer-field weights).  Each minimizer-type line
carries ONE power of the Dirichlet product (not two), so the coupled sum is
    U_M = sum_{n,m} W1(n) W1(n-m) W1_b(m) * M v(p_n, p_{n-m}) /
          ((M^2|r(p_n)|^2)(M^2|r(p_{n-m})|^2)(M^2|r(p^b_m)|^2)),
W1 = prod_j delta_M (exponent 1).  Lemma A3 predicts rate M^{-1+eps}.
Run:  python3 -I research/scripts/t69_vertex_exponents.py
"""
import numpy as np


def grid(M, d):
    n1 = np.arange(-(M // 2) + 1, M // 2 + 1)
    return np.meshgrid(*([n1] * d), indexing="ij")


def delta(M, Kj, nj):
    # delta_M(n_j) = |sin(K/2)| / (M |sin(q/(2M))|), q = K + 2 pi n
    return np.abs(np.sin(Kj / 2)) / (M * np.abs(np.sin((Kj + 2 * np.pi * nj) / (2 * M))))


def partA(K, Ms):
    d = len(K)
    out = {0: [], 1: [], "C": []}
    for M in Ms:
        ns = grid(M, d)
        p = [(K[j] + 2 * np.pi * ns[j]) / M for j in range(d)]
        r2 = sum(4 * np.sin(pj / 2) ** 2 for pj in p) * M ** 2  # M^2 |r|^2
        W = np.ones_like(r2)
        for j in range(d):
            W = W * delta(M, K[j], ns[j]) ** 2
        out[0].append(np.sum(W * np.cos(p[0]) / r2 ** 2))
        out[1].append(np.sum(W * M * np.sin(p[0]) / r2 ** 2))
        out["C"].append(np.sum(W / r2))
    return out


def partB(K, P, Ms):
    res = []
    for M in Ms:
        ns = grid(M, 2)
        m = [x.reshape(-1) for x in ns]
        n = [x.reshape(-1) for x in ns]
        tot = 0.0
        # loop over m to keep memory small
        Kp = [K[j] - P[j] for j in range(2)]
        for m0 in range(-(M // 2) + 1, M // 2 + 1):
            for m1 in range(-(M // 2) + 1, M // 2 + 1):
                mm = (m0, m1)
                n0, n1 = ns[0], ns[1]
                pn = [(K[j] + 2 * np.pi * ns[j]) / M for j in range(2)]
                l = [ns[j] - mm[j] for j in range(2)]
                pl = [(Kp[j] + 2 * np.pi * l[j]) / M for j in range(2)]
                rn = sum(4 * np.sin(x / 2) ** 2 for x in pn) * M ** 2
                rl = sum(4 * np.sin(x / 2) ** 2 for x in pl) * M ** 2
                Wn = np.ones_like(rn)
                Wl = np.ones_like(rn)
                for j in range(2):
                    Wn = Wn * delta(M, K[j], ns[j]) ** 2
                    Wl = Wl * delta(M, Kp[j], l[j]) ** 2
                Wb = 1.0
                for j in range(2):
                    Wb *= delta(M, P[j], np.array(mm[j])) ** 2
                v = M * np.sin((pn[0] + pl[0]) / 2)
                tot += Wb * np.sum(Wn * Wl * v / (rn * rl))
        res.append(tot)
    return res


def partC(K, P, Ms):
    res = []
    for M in Ms:
        ns = grid(M, 2)
        Kp = [K[j] - P[j] for j in range(2)]
        pn = [(K[j] + 2 * np.pi * ns[j]) / M for j in range(2)]
        rn = sum(4 * np.sin(x / 2) ** 2 for x in pn) * M ** 2
        Wn = delta(M, K[0], ns[0]) * delta(M, K[1], ns[1])
        tot = 0.0
        for m0 in range(-(M // 2) + 1, M // 2 + 1):
            for m1 in range(-(M // 2) + 1, M // 2 + 1):
                mm = (m0, m1)
                l = [ns[j] - mm[j] for j in range(2)]
                pl = [(Kp[j] + 2 * np.pi * l[j]) / M for j in range(2)]
                pb = [(P[j] + 2 * np.pi * mm[j]) / M for j in range(2)]
                rl = sum(4 * np.sin(x / 2) ** 2 for x in pl) * M ** 2
                rb = sum(4 * np.sin(x / 2) ** 2 for x in pb) * M ** 2
                Wl = delta(M, Kp[0], l[0]) * delta(M, Kp[1], l[1])
                Wb = delta(M, P[0], np.array(mm[0])) * delta(M, P[1], np.array(mm[1]))
                v = M * np.sin((pn[0] + pl[0]) / 2)
                tot += Wb / rb * np.sum(Wn * Wl * v / (rn * rl))
        res.append(tot)
    return res


def report(name, vals, Ms):
    print(name)
    prev = None
    for i in range(len(Ms) - 1):
        diff = abs(vals[i] - vals[i + 1])
        ratio = "" if prev is None else "  ratio %.2f" % (prev / diff)
        print("  M=%3d -> %3d  S_M=% .8f  |S_M-S_2M|=%.3e%s" % (Ms[i], Ms[i + 1], vals[i], diff, ratio))
        prev = diff


if __name__ == "__main__":
    K = np.array([1.0, 0.5, -0.7, 0.3])
    Ms = [2, 4, 8, 16, 32]
    A = partA(K, Ms)
    report("A: k=0 (seagull type, s=-4), d=4", A[0], Ms)
    report("A: k=1 (one difference,  s=-3), d=4", A[1], Ms)
    report("A: scalar ghost coarse covariance C_M(K) (s=-2), d=4", A["C"], Ms)
    K2 = np.array([1.0, -0.6])
    P2 = np.array([0.6, -0.4])
    Ms2 = [4, 8, 16, 32]
    B = partB(K2, P2, Ms2)
    report("B: coupled (n,m), k=1, d=2, P != 0, squared weights", B, Ms2)
    C = partC(K2, P2, [4, 8, 16, 32, 64])
    report("C: coupled (n,m), k=1, d=2, P != 0, exponent-1 weights", C, [4, 8, 16, 32, 64])
