"""T72 (note 66): d-dependence of the conditions in CMP 122 II (1.76)-(1.99), and
the exact 3D coupling flow facts used for R = identity.

Pure standard library; no linear algebra is involved. Every number quoted in
research/66-cmp122ii-d3-reading.md is printed here (output: t72_d_dependence.out).

Part A  exponent conditions between the large-field exponent p_0 and the domain
        exponent r (R_j ~ (log g_j^-2)^r, p_0(g) = (log g^-2)^p_0), as functions of d.
        Each is a strict inequality between exponents that must hold as g -> 0.
Part B  L-conditions of the printed geometry.
Part C  the 3D flow g_j^2 = g^2 L^(j-K) (CMP 109 p. 259), x_j = ln g_j^-2, with
        R_j the smallest power of L with R_j >= x_j^r (CMP 119 (2.5)); checks
        (B1) K - j < R_j, (B2) R_{j+1} in {R_j, R_j/L},
        (B3) every window of w >= 2 steps contains at most w/2 steps with
             R_{j+1} = R_j/L (the 'no gain' steps of CMP 122 II p. 385).
"""
import math
from fractions import Fraction


def minimal_int_above(x):
    """smallest integer strictly greater than the Fraction x"""
    return math.floor(x) + 1


# ---------------------------------------------------------------- Part A
print("PART A. exponent conditions (strict, as g -> 0); minimal integer p_0")
print("  (a) R on, CMP 122 II p. 383 : 2 p_1 - (d+5) r > p_0 with p_1 < p_0  <=>  p_0 > (d+5) r")
print("  (b) R on, (1.88) merge step : p_0 > (d+2) r   [linear p_0(g_{j+1}) against R^(d+2)]")
print("  (c) R on, (1.82) base case  : 2 p_0 > (d+2) r [quadratic p_0^2 against R^(d+2)]")
print("  (d) R on, (1.95)            : p_0 > d r       [2 kappa (100 R_k)^d <= p_0(g_k)/4 - 1]")
print("  (e) R = id, d = 3 (Prop. 2) : p_0 > (d+1) r   [merge], 2 p_0 > (d+1) r + 1 [base, tail <= x/ln L steps]")
print("  (f) note 49 s5 (superseded) : 2 p_0 > (d+1) r")
print()
hdr = "| d | r | (a) p_0 > (d+5)r | (b) p_0 > (d+2)r | (c) 2p_0 > (d+2)r | (d) p_0 > d r | (e) merge p_0 > (d+1)r | (e) base 2p_0 > (d+1)r+1 | (f) 2p_0 > (d+1)r |"
print(hdr)
print("|" + "---|" * 9)
for d in (3, 4):
    for r in (2, 3):
        a = minimal_int_above(Fraction((d + 5) * r))
        b = minimal_int_above(Fraction((d + 2) * r))
        c = minimal_int_above(Fraction((d + 2) * r, 2))
        dd = minimal_int_above(Fraction(d * r))
        e1 = minimal_int_above(Fraction((d + 1) * r))
        e2 = minimal_int_above(Fraction((d + 1) * r + 1, 2))
        f = minimal_int_above(Fraction((d + 1) * r, 2))
        print(f"| {d} | {r} | {a} | {b} | {c} | {dd} | {e1} | {e2} | {f} |")
print()
print("Binding exponent, R on:   p_0 > (d+5) r :  d = 4 -> 9 r,  d = 3 -> 8 r (if R were kept at d = 3)")
print("Binding exponent, R = id: p_0 > (d+1) r :  d = 3 -> 4 r")
print()

# ---------------------------------------------------------------- Part B
print("PART B. L-conditions of the printed geometry (CMP 122 II p. 384-385, CMP 122 I p. 193-194)")
print("| L | 42 L/(L-1) | < 63 ? | L^(-1/2) | <= 1/2 ? | exists integer L_0 >= 2 with L_0^2 <= L/3 ? |")
print("|---|---|---|---|---|---|")
for L in (2, 3, 4, 5, 6, 12):
    sup42 = Fraction(42 * L, L - 1)
    ok63 = sup42 <= 63  # sup is not attained for finite n-j, so '< 63' holds when sup <= 63
    inv_sqrt = L ** -0.5
    okhalf = L >= 4
    ok_L0 = (4 <= Fraction(L, 3))
    print(f"| {L} | {float(sup42):.2f} | {'yes' if ok63 else 'NO'} | {inv_sqrt:.4f} | {'yes' if okhalf else 'NO'} | {'yes' if ok_L0 else 'NO'} |")
print("  (sup over n-j of 42(1-L^-(n-j))/(1-1/L) = 42L/(L-1) is never attained, so the strict '< 63' needs 42L/(L-1) <= 63, i.e. L >= 3)")
print()

# ---------------------------------------------------------------- Part C
def R_sequence(L, r, xK, K):
    """R_j for j = 1..K, x_j = xK + (K-j) ln L, R_j = smallest power of L with R_j >= x_j^r."""
    lnL = math.log(L)
    R = {}
    for j in range(1, K + 1):
        x = xK + (K - j) * lnL
        i = math.ceil(r * math.log(x) / lnL - 1e-12)
        R[j] = L ** max(i, 0)
    return R


def checks(L, r, xK, K):
    R = R_sequence(L, r, xK, K)
    b1 = all((K - j) < R[j] for j in range(1, K + 1))
    b2 = all(R[j + 1] in (R[j], R[j] // L) and (R[j + 1] == R[j] or R[j] % L == 0)
             for j in range(1, K))
    dec = [1 if R[j + 1] < R[j] else 0 for j in range(1, K)]       # step j -> j+1 (no gain)
    # B3: for every window of w >= 2 consecutive steps, #dec <= w/2.  t = 2 dec - 1.
    b3 = True
    gm1 = None
    for m, dv in enumerate(dec):
        t = 2 * dv - 1
        if gm1 is not None and t + gm1 > 0:
            b3 = False
            break
        gm1 = t + max(0, gm1) if gm1 is not None else t
    worst = max((K - j) / R[j] for j in range(1, K + 1))
    return b1, b2, b3, worst, R


print("PART C. 3D flow g_j^2 = g^2 L^(j-K), x_j = ln g_j^-2 = x_K + (K-j) ln L")
print("  analytic thresholds on x_K (g^2 = exp(-x_K)):")
print("    (B1) K-j < R_j  holds as soon as x_j >= 1 (since (x_j - x_K)/ln L < x_j/ln L <= x_j <= x_j^r)")
print("    (B2) R_{j+1}/R_j in {1, 1/L}  needs (x/(x - ln L))^r <= L,  i.e.  x >= x_b := ln L/(1 - L^(-1/r))")
print("    (B3) drops of R separated by >= 3 steps  needs  x >= x_c := ln L/(1 - L^(-1/(3 r)))")
print("| L | r | x_b | x_c | g^2 = e^-x_c |")
print("|---|---|---|---|---|")
for L in (3, 4, 5, 6):
    for r in (2, 3):
        lnL = math.log(L)
        xb = lnL / (1 - L ** (-1.0 / r))
        xc = lnL / (1 - L ** (-1.0 / (3 * r)))
        print(f"| {L} | {r} | {xb:.3f} | {xc:.3f} | {math.exp(-xc):.2e} |")
print()
print("  exact check on the grid x_K in {1.0, 1.25, ..., 40.0}, K = 600 steps (K = 1 .. 600, all j):")
print("  smallest x_K from which (B1),(B2),(B3) all hold for every larger grid value; max_j (K-j)/R_j there")
print("| L | r | x_K,min (B1) | x_K,min (B2) | x_K,min (B3) | max_j (K-j)/R_j at x_K,min(B3) |")
print("|---|---|---|---|---|---|")
K = 600
grid = [1.0 + 0.25 * i for i in range(0, 157)]   # 1.0 .. 40.0
for L in (3, 4, 5, 6):
    for r in (2, 3):
        res = {}
        for xK in grid:
            b1, b2, b3, worst, _ = checks(L, r, xK, K)
            res[xK] = (b1, b2, b3, worst)
        out = []
        for idx in range(3):
            # smallest grid value such that all grid values >= it satisfy check idx
            ok_from = None
            for xK in reversed(grid):
                if res[xK][idx]:
                    ok_from = xK
                else:
                    break
            out.append(ok_from)
        w = res[out[2]][3] if out[2] is not None else float('nan')
        fmt = lambda v: "none" if v is None else f"{v:.2f}"
        print(f"| {L} | {r} | {fmt(out[0])} | {fmt(out[1])} | {fmt(out[2])} | {w:.3f} |")
print()

print("PART D. terminal-lattice R_K = smallest power of L >= (ln g^-2)^r, g = g_K the terminal coupling (r = 2)")
print("| g^2 | x_K = ln g^-2 | x_K^2 | R_K for L = 3 | L = 4 | L = 5 | L = 6 |")
print("|---|---|---|---|---|---|---|")
for g2 in (1e-2, 1e-3, 1e-4):
    x = math.log(1 / g2)
    vals = []
    for L in (3, 4, 5, 6):
        i = math.ceil(2 * math.log(x) / math.log(L) - 1e-12)
        vals.append(L ** i)
    print(f"| {g2:.0e} | {x:.3f} | {x*x:.2f} | {vals[0]} | {vals[1]} | {vals[2]} | {vals[3]} |")
