"""T72 (note 66): scalar checks for CMP 122 II (1.79)-(1.99) at d = 3 with R = identity.

Pure standard library; no linear algebra. Every number quoted in
research/66-cmp122ii-d3-reading.md is printed here (output: t72_cmp122ii_d3_checks.out).
This script re-creates and extends the salvaged wip/round-2026-10-08/t72 script
(its .out was kept; the .py was not in the repository).

The 3D flow is exact (CMP 109 p. 259): g_j^2 = g^2 L^(j-K), j = 0..K, g_K = g, so
    x_j := log g_j^{-2} = x_K + (K - j) ln L,
and R_j is the smallest power of L with R_j >= x_j^r (CMP 119 (2.5)).
Balaban's constants (A_0, A_1, gamma_0, kappa, M, ...) are not specified in the
papers, so only exponents of x and the d-dependent inequalities are tested.

Part A  exponent conditions between p_0 and r as functions of d.
Part B  L-conditions of the printed geometry (CMP 122 II pp. 384-385).
Part C  3D flow facts used by the induction (1.80)-(1.88) with R = identity:
        (C0) R_n <= R_j and R_n <= L R_j for n > j;
        (C1) K - j < R_j for every j (the remaining number of steps is below the
             R_j that CMP 122 II uses as the bound K <= n_0 - j + R_j);
        (C2) R_{j+1} in {R_j, R_j / L};
        (C3) every window of w >= 2 steps contains at most w/2 steps with
             R_{m+1} = R_m / L (the 'no gain' steps behind d'_n <= L^{-(n-j)/2} d'_j).
Part D  accumulated entropy of a domain carried from creation scale i to the unit
        lattice, against the creation weight p_0^2(g_i) (exponents only).
Part E  exp(-2 p_0(g)) <= g^q thresholds.
"""
import math
from fractions import Fraction


def minimal_int_above(x):
    """smallest integer strictly greater than the Fraction x"""
    return math.floor(x) + 1


# ---------------------------------------------------------------- Part A
print("PART A. exponent conditions (strict, as g -> 0); minimal integer p_0.")
print("  p_0(g) = (log g^-2)^p_0, R_j ~ (log g_j^-2)^r (r = r_0 of II p. 383).")
print("  (a) R on, II p. 383 prose after (1.78): 2 p_1 - (d+5) r > p_0; if p_1 <= p_0 this gives p_0 > (d+5) r")
print("  (b) R on, (1.88): p_0 > (d+2) r        [linear 2(1+b0)^-1 p_0(g_{j+1}) against R^(d+2)]")
print("  (c) (1.82) base case, R on or R = id (verbatim): 2 p_0 > (d+2) r   [p_0^2 against R^(d+2)]")
print("  (d) R on, (1.95): p_0 > d r             [2 kappa (100 R_k)^d <= p_0(g_k)/4 - 1]")
print("  (e) R = id, merge (1.87) (no extra steps): p_0 > (d+1) r        [linear p_0 against R^(d+1)]")
print("  (f) R = id, base with tail <= x/ln L steps (refined): 2 p_0 > (d+1) r + 1")
print("  CMP 119 (1.1), p. 246: p_0 >= 5 r.   note 49 s5 / note 61 s6a quote 2 p_0 > (d+1) r  [(1.82) has R^(d+2)].")
print()
print("| d | r | (a) p_0 > (d+5)r | (b) p_0 > (d+2)r | (c) 2p_0 > (d+2)r | (d) p_0 > d r | (e) p_0 > (d+1)r | (f) 2p_0 > (d+1)r+1 | p_0 >= 5r ok for (b)? (c)? (e)? |")
print("|" + "---|" * 9)
for d in (3, 4):
    for r in (2, 3):
        a = minimal_int_above(Fraction((d + 5) * r))
        b = minimal_int_above(Fraction((d + 2) * r))
        c = minimal_int_above(Fraction((d + 2) * r, 2))
        dd = minimal_int_above(Fraction(d * r))
        e = minimal_int_above(Fraction((d + 1) * r))
        f = minimal_int_above(Fraction((d + 1) * r + 1, 2))
        p0 = 5 * r                       # the CMP 119 (1.1) value p_0 = 5r
        ok = lambda cond: "yes" if cond else "NO"
        print(f"| {d} | {r} | {a} | {b} | {c} | {dd} | {e} | {f} | "
              f"{ok(p0 >= b)} / {ok(p0 >= c)} / {ok(p0 >= e)} (p_0 = {p0}) |")
print()
print("Binding condition, R on (d = 4): (a) p_0 > 9 r (if p_1 <= p_0), against p_0 >= 5 r of CMP 119 (1.1).")
print("Binding condition, R = id (d = 3): (b)-form p_0 > 5 r verbatim, p_0 > 4 r refined; p_0 >= 5 r meets the refined one.")
print()

# ---------------------------------------------------------------- Part B
print("PART B. L-conditions of the printed geometry (II p. 384-385). L is odd and > 11 in CMP 109 (note 65).")
print("  L_{n-j} <= 42 (1 - L^-(n-j))/(1 - 1/L) < 63 needs 42 L/(L-1) <= 63, i.e. L >= 3;")
print("  L^(-1/2 (n-j)) <= 2^(-(n-j)) needs L >= 4.")
print("| L | 42 L/(L-1) | <= 63 ? | L^(-1/2) | <= 1/2 ? |")
print("|---|---|---|---|---|")
for L in (2, 3, 4, 5, 13, 15):
    s = Fraction(42 * L, L - 1)
    print(f"| {L} | {float(s):.2f} | {'yes' if s <= 63 else 'NO'} | {L ** -0.5:.4f} | {'yes' if L >= 4 else 'NO'} |")
print()


# ---------------------------------------------------------------- Part C
def R_exponents(L, r, xK, K):
    """e_j with R_j = L^e_j, j = 0..K (R_j smallest power of L >= x_j^r)."""
    ell = math.log(L)
    out = []
    for j in range(K + 1):
        x = xK + (K - j) * ell
        e = max(math.ceil(r * math.log(x) / ell - 1e-12), 0)
        out.append(e)
    return out


def flow_checks(L, r, xK, K):
    ell = math.log(L)
    e = R_exponents(L, r, xK, K)
    R = [L ** v for v in e]
    c0 = all(e[n] <= e[j] for j in range(K + 1) for n in range(j, K + 1, 1)) if K <= 400 else \
        all(e[j + 1] <= e[j] for j in range(K))
    c0b = all(R[n] <= L * R[j] for j in range(K + 1) for n in range(j, K + 1)) if K <= 400 else c0
    c1 = all((K - j) < R[j] for j in range(K + 1))
    c2 = all(e[j] - e[j + 1] in (0, 1) for j in range(K))
    dec = [1 if e[j + 1] < e[j] else 0 for j in range(K)]
    c3 = True
    prev = None
    for dv in dec:
        t = 2 * dv - 1
        if prev is not None and t + prev > 0:
            c3 = False
            break
        prev = t + max(0, prev) if prev is not None else t
    return c0, c0b, c1, c2, c3, R


print("PART C. 3D flow, x_j = x_K + (K-j) ln L; K = 300 steps (all j = 0..K), g^2 = exp(-x_K).")
print("  analytic: (C1) holds once x_j >= 1 (K - j = (x_j - x_K)/ln L < x_j/ln L <= x_j <= x_j^r for L >= 3).")
print("            (C2) needs (x/(x - ln L))^r <= L, i.e. x >= x_b = ln L/(1 - L^(-1/r)).")
print("            (C3) is guaranteed once drops are >= 3 steps apart: x >= x_c = ln L/(1 - L^(-1/(3r))).")
print("| L | r | x_b | x_c | g^2 = e^-x_c |")
print("|---|---|---|---|---|")
for L in (3, 4, 5, 13):
    for r in (2, 3):
        lnL = math.log(L)
        xb = lnL / (1 - L ** (-1.0 / r))
        xc = lnL / (1 - L ** (-1.0 / (3 * r)))
        print(f"| {L} | {r} | {xb:.3f} | {xc:.3f} | {math.exp(-xc):.2e} |")
print()
print("  exact check on the grid x_K in {1.0, 1.25, ..., 40.0}: smallest x_K from which the check holds for every larger grid value")
print("| L | r | (C0) | (C1) | (C2) | (C3) |")
print("|---|---|---|---|---|---|")
K = 300
grid = [1.0 + 0.25 * i for i in range(0, 157)]
for L in (3, 4, 5, 13):
    for r in (2, 3):
        res = {}
        for xK in grid:
            c0, c0b, c1, c2, c3, _ = flow_checks(L, r, xK, K)
            res[xK] = (c0 and c0b, c1, c2, c3)
        out = []
        for idx in range(4):
            ok_from = None
            for xK in reversed(grid):
                if res[xK][idx]:
                    ok_from = xK
                else:
                    break
            out.append("none" if ok_from is None else f"{ok_from:.2f}")
        print(f"| {L} | {r} | {out[0]} | {out[1]} | {out[2]} | {out[3]} |")
print()

# ---------------------------------------------------------------- Part D
print("PART D. a domain created at scale i with weight ~ x_i^(2 p_0) (the p_0^2 term of (1.82), (1.85)) and carried unprocessed to the unit lattice K:")
print("  accumulated entropy E_i = sum_{n=i+1}^{K} R_n^(d+1) (one MR-cube per step; constants (64)^d M^d omitted).")
print("  (1.81) second line: E_i <= L^(d+1) R_i^(d+1) (K - i) <= L^(d+1) R_i^(d+2); ratios printed below.")
print("| d | L | r | p_0 | x_K | max_i E_i / R_i^(d+2) | max_i E_i / x_i^((d+1) r + 1) | min_i x_i^(2 p_0) / E_i |")
print("|---|---|---|---|---|---|---|---|")
for d in (3,):
    for L in (4, 13):
        for r in (2, 3):
            for p0 in (5 * r,):
                for xK in (8.0, 20.0, 60.0):
                    Kd = 300
                    ell = math.log(L)
                    e = R_exponents(L, r, xK, Kd)
                    R = [L ** v for v in e]
                    x = [xK + (Kd - j) * ell for j in range(Kd + 1)]
                    m1 = m2 = 0.0
                    m3 = float("inf")
                    for i in range(Kd):
                        E = sum(R[n] ** (d + 1) for n in range(i + 1, Kd + 1))
                        m1 = max(m1, E / R[i] ** (d + 2))
                        m2 = max(m2, E / x[i] ** ((d + 1) * r + 1))
                        m3 = min(m3, x[i] ** (2 * p0) / E)
                    print(f"| {d} | {L} | {r} | {p0} | {xK:.0f} | {m1:.3f} | {m2:.3f} | {m3:.3e} |")
print("  (L^(d+1) R_i^(d+1) (K-i) <= L^(d+1) R_i^(d+2) is the paper's bound; first ratio stays below L^(d+1).)")
print()

# ---------------------------------------------------------------- Part E
print("PART E. exp(-2 p_0(g)) <= g^q with p_0(g) = (log g^-2)^p_0 (A_0 = 1): need 2 x^p_0 >= q x/2, i.e. x >= (q/4)^(1/(p_0-1)).")
print("| p_0 | q | threshold x_* | g^2 <= e^-x_* |")
print("|---|---|---|---|")
for p0 in (10,):
    for q in (5, 10, 100, 1000):
        xs = (q / 4.0) ** (1.0 / (p0 - 1))
        xs = max(xs, 0.0)
        print(f"| {p0} | {q} | {xs:.3f} | {math.exp(-xs):.3f} |")
print()
print("(2.7) first line on the 3D flow: p_0(g_m) >= p_0(g_n) for m <= n because x_m = x_n + (n-m) ln L >= x_n (beta_0 = 0 suffices).")
