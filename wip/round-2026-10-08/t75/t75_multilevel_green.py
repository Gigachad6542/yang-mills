"""T75: multi-level penalty of Balaban's free step operator (note 41 section 5a).

What the script prints (every number quoted in note 41 section 5a):

 0. the weights a_j of CMP 96 (2.14) / CMP 99 (3.24): recursion = closed form (exact
    rational arithmetic), a_j - a_inf <= a L^{-2j}, coarse-unit strengths beta = a_i L^{2(j-i)};
 1. the Bloch real-space model of one coarse cell equals the alias model of note 41 section 5
    (t68_two_scale_green.pairings_dense), to rounding;
 2. the literal "all levels at every point" operator K_all = Lambda + sum_i beta_i E_i:
    K_all >= a M^2 (finest level), so its induced coarse kernels are O(M^-2);
 3. the faithful translation-invariant (bulk) operator Lambda + a_j w w^* : the rate of
    Theorem 2 (note 41 section 5.2) with the true weight a_M = a_j;
 4. Lemma 5a.1 (K >= c_0) and Lemma 5a.2 (Combes-Thomas, explicit delta_0) on random and
    shell-type nested tilings, d = 1, 2, 4;
 5. entry decay of the induced coarse kernel in a nested shell geometry (Cor. 5a.3) and the
    agreement with the bulk operator away from the shells (computation only, not a theorem).

Conventions (coarse units of step j, M = L^j fine cells per coarse cell, L = 2):
  K_T = M^2 * (graph Laplacian of the fine lattice) + sum_{B in T} beta_B v_B v_B^T,
  v_B = |B|^{-1/2} 1_B, B a cube of side L^i (0 <= i <= j), beta_B = a_i L^{2(j-i)},
  T a tiling of the fine lattice by such cubes.  (CMP 96 (2.14) with eta = 1/M:
  a_i (L^i eta)^{d-2} sum_y |Q_i lambda(y)|^2 = a_i L^{-2i} <lambda, E_i lambda> per fine unit,
  times M^2.)  All linear algebra is dense numpy (eigvalsh / svd / solve); no pseudoinverse.
"""
import itertools
import math
import sys
from fractions import Fraction

import numpy as np

from t68_two_scale_green import pairings_dense, pairings_schur

L = 2
A0 = 1.0  # the constant a of CMP 96 / CMP 99


# ---------------------------------------------------------------- weights
def a_seq(i, a=A0):
    """a_0 = a_1 = a, a_{i+1} = a a_i / (a L^-2 + a_i)  (CMP 96 (2.14); CMP 99 (3.24))."""
    x = a
    for _ in range(1, i):
        x = a * x / (a / L ** 2 + x)
    return x


def a_exact(i, a=Fraction(1)):
    x = a
    for _ in range(1, i):
        x = a * x / (a / L ** 2 + x)
    return x


def a_closed(i, a=Fraction(1)):
    return a * (1 - Fraction(1, L ** 2)) / (1 - Fraction(1, L ** (2 * i)))


A_INF = A0 * (1 - L ** -2)
C0 = min(4.0, A_INF)  # Lemma 5a.1


def eps_ct(delta, d, a=A0):
    """Combes-Thomas error of Lemma 5a.2: eps(delta) = 1.0862 d delta^2 + 3 a (e^delta - 1)^2."""
    return 2 * d * (math.cosh(1.0) - 1.0) * delta ** 2 + 3 * a * (math.exp(delta) - 1.0) ** 2


def delta0(d, a=A0, c0=None):
    """largest delta in (0,1] with eps(delta) <= c0/4 (bisection)."""
    c0 = C0 if c0 is None else c0
    lo, hi = 0.0, 1.0
    if eps_ct(hi, d, a) <= c0 / 4:
        return 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if eps_ct(mid, d, a) <= c0 / 4:
            lo = mid
        else:
            hi = mid
    return lo


def section0():
    print("== 0. weights a_j of CMP 96 (2.14) / CMP 99 (3.24) ==")
    ok = all(a_exact(i) == a_closed(i) for i in range(1, 25))
    print("   exact recursion a_{i+1} = a a_i/(a L^-2 + a_i), a_1 = a, equals a(1-L^-2)/(1-L^-2i), i = 1..24:", ok)
    print("   a_0..a_6 =", [round(a_seq(i), 6) for i in range(7)], " a_inf = a(1-L^-2) =", A_INF)
    sup = max(float((a_closed(i) - Fraction(3, 4)) * L ** (2 * i)) for i in range(1, 40))
    print(f"   sup_(i>=1) (a_i - a_inf) L^(2i) / a = {sup:.6f}   (so C_a = a in |a_M - a_inf| <= C_a M^-2)")
    print("   monotone decreasing, a_i >= a_inf:", all(a_seq(i + 1) <= a_seq(i) + 1e-15 and a_seq(i) >= A_INF - 1e-15 for i in range(1, 30)))
    j = 6
    print(f"   coarse-unit strength beta_i = a_i L^(2(j-i)) of level i at step j = {j}:")
    print("     i   :", " ".join(f"{i:9d}" for i in range(j + 1)))
    print("     beta:", " ".join(f"{a_seq(i) * L ** (2 * (j - i)):9.3f}" for i in range(j + 1)))


# ------------------------------------------------- Bloch real-space model of one cell
def kron_all(mats):
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


def bloch_lap(K, M):
    d = len(K)
    I = np.eye(M)
    out = 0
    for mu in range(d):
        T = np.eye(M, k=1, dtype=complex)
        T[M - 1, 0] = np.exp(1j * K[mu])
        D1 = M ** 2 * (2 * I - T - T.conj().T)
        mats = [I.astype(complex)] * d
        mats[mu] = D1
        out = out + kron_all(mats)
    return out


def bloch_block_projector(M, b, d):
    """projector onto functions constant on cubes of side b (b | M) inside the cell."""
    P1 = np.kron(np.eye(M // b), np.ones((b, b)) / b)
    return kron_all([P1] * d)


def bloch_K(K, M, d, levels, j, a=A0):
    """Lambda + sum_{i in levels} a_i L^(2(j-i)) E_i, in the Bloch cell."""
    Km = bloch_lap(K, M)
    for i in levels:
        Km = Km + a_seq(i, a) * L ** (2 * (j - i)) * bloch_block_projector(M, L ** i, d)
    return Km


def box_pairing(Km, M, d):
    u = np.ones(M ** d) / math.sqrt(M ** d)
    x = np.linalg.solve(Km, u)
    return np.vdot(u, x).real


def section1():
    print("== 1. Bloch real-space cell = alias model of note 41 section 5 (top level only, weight a_j) ==")
    for d, M in ((2, 8), (4, 4)):
        K = np.array([0.7, 2.9, -1.3, 0.2][:d])
        j = int(round(math.log(M, L)))
        Km = bloch_K(K, M, d, [j], j)
        mu = np.linalg.eigvalsh(Km)
        al = pairings_dense(K, M, a_seq(j), (1,) * d, (2,) * d)[0].real
        rs = box_pairing(Km, M, d)
        print(f"   d={d} M={M}: <w,Gw> alias = {al:.14f}, real-space = {rs:.14f}, |diff| = {abs(al - rs):.2e}")


# ------------------------------------------------------ all levels at every point
def section2():
    print("== 2. literal 'all levels at every point' K_all = Lambda + sum_(i=0..j) a_i L^(2(j-i)) E_i ==")
    print("   finest level i = 0: E_0 = I, strength a_0 M^2, so K_all >= a M^2 (proved in 5a.4).")
    for d, js in ((2, (1, 2, 3, 4, 5)), (4, (1, 2, 3))):
        for j in js:
            M = L ** j
            K = np.array([0.9, 2.2, -1.4, 0.4][:d]) if not (d == 4 and j == 3) else np.zeros(d)
            Kall = bloch_K(K, M, d, range(j + 1), j)
            Ktop = bloch_K(K, M, d, [j], j)
            mu = np.linalg.eigvalsh(Kall)[0]
            xa = box_pairing(Kall, M, d)
            xt = box_pairing(Ktop, M, d)
            tag = " (K = 0)" if (d == 4 and j == 3) else ""
            print(f"   d={d} j={j} M={M:2d}: min eig K_all = {mu:10.3f}, a M^2 = {A0 * M * M:8.1f}, ratio = {mu / (A0 * M * M):.3f};"
                  f"  M^2 <w,K_all^-1 w> = {M * M * xa:.4f};  <w,K_top^-1 w> = {xt:.4f}{tag}", flush=True)


# ------------------------------------------- faithful bulk: top level with weight a_j
def section3():
    print("== 3. faithful bulk operator Lambda + a_j w w^*, true weights a_M = a_j (rate of Theorem 2) ==")
    for d, js, vals in ((2, (1, 2, 3, 4, 5, 6), np.linspace(-np.pi, np.pi, 5)),
                        (4, (1, 2, 3, 4), np.array([0.9, 2.2, -1.4]))):
        print(f"   d={d}: sup_K |Xi_M - Xi_2M|, Xi = (<w1,G w1>, <w1,G w2> mixed exponents, G_00), a = a_j")
        Ks = [np.array(k) for k in itertools.product(vals, repeat=d)]
        prev, pd = None, None
        for j in js:
            M = L ** j
            cur = [pairings_schur(K, M, a_seq(j), (1,) * d, (2,) * d) for K in Ks]
            if prev is not None:
                dd = np.max([np.abs(x - y) for x, y in zip(cur, prev)], axis=0)
                msg = f"     M={M // 2:3d}->{M:3d}: " + "  ".join(f"{v:.3e}" for v in dd)
                if pd is not None:
                    msg += "   ratios " + " ".join(f"{p / v:.2f}" for p, v in zip(pd, dd))
                print(msg, flush=True)
                pd = dd
            prev = cur


# ------------------------------------------------------------- nested tilings
def lap_grid(S, d):
    """dense graph Laplacian of the free-boundary S^d grid."""
    n = S ** d
    A = np.zeros((n, n))
    idx = np.arange(n).reshape((S,) * d)
    for mu in range(d):
        a = np.take(idx, range(S - 1), axis=mu).ravel()
        b = np.take(idx, range(1, S), axis=mu).ravel()
        A[a, a] += 1
        A[b, b] += 1
        A[a, b] -= 1
        A[b, a] -= 1
    return A


def cube_indices(S, d, origin, side):
    rng = [np.arange(o, o + side) for o in origin]
    grids = np.meshgrid(*rng, indexing="ij")
    return np.ravel_multi_index([g.ravel() for g in grids], (S,) * d)


def random_tiling(S, j, d, rng, p):
    tiles = []

    def rec(o, i):
        if i > 0 and rng.random() < p:
            for off in itertools.product(range(L), repeat=d):
                rec(tuple(o[m] + off[m] * L ** (i - 1) for m in range(d)), i - 1)
        else:
            tiles.append((o, i))

    M = L ** j
    for o in itertools.product(range(0, S, M), repeat=d):
        rec(o, j)
    return tiles


def shell_offsets(j, w=2):
    c = [0]
    for i in range(1, j + 1):
        c.append(L ** i * math.ceil((c[i - 1] + w * L ** (i - 1)) / L ** i))
    return c


def shell_tiling(S, j, d, w=2):
    """Omega_i = [c_i, S-c_i)^d, Lambda_i = Omega_i \\ Omega_{i+1} tiled by level-i cubes, Lambda_j = Omega_j
    (CMP 96 (2.1)-(2.4), k = j, widths >= w L^i)."""
    c = shell_offsets(j, w)
    assert S - 2 * c[j] >= L ** j and (S - 2 * c[j]) % L ** j == 0
    tiles = []
    for i in range(j + 1):
        side = L ** i
        for o in itertools.product(range(0, S, side), repeat=d):
            def inside(ci):
                return all(ci <= x and x + side <= S - ci for x in o)
            if inside(c[i]) and (i == j or not inside(c[i + 1])):
                tiles.append((o, i))
    return tiles, c


def check_partition(tiles, S, d):
    cov = np.zeros(S ** d, int)
    for o, i in tiles:
        cov[cube_indices(S, d, o, L ** i)] += 1
    assert np.all(cov == 1), "tiles do not partition the lattice"


def build_K(S, j, d, tiles):
    M = L ** j
    K = M ** 2 * lap_grid(S, d)
    for o, i in tiles:
        idx = cube_indices(S, d, o, L ** i)
        K[np.ix_(idx, idx)] += a_seq(i) * L ** (2 * (j - i)) / len(idx)
    return K


def bulk_tiling(S, j, d):
    M = L ** j
    return [(o, j) for o in itertools.product(range(0, S, M), repeat=d)]


def section4():
    print("== 4. nested tilings (CMP 96 (2.1)-(2.4)): Lemma 5a.1 (K >= c_0) and Lemma 5a.2 (Combes-Thomas) ==")
    print(f"   a = {A0}, L = {L}: c_0 = min(4, a(1-L^-2)) = {C0};  delta_0(d) with eps(delta_0) = c_0/4:",
          {d: round(delta0(d), 4) for d in (1, 2, 4)})
    rng = np.random.default_rng(75)
    cases = [(1, j, 2 * L ** j, 6) for j in range(1, 7)] + [(2, 1, 8, 6), (2, 2, 16, 5), (2, 3, 16, 3), (2, 4, 32, 2), (4, 2, 8, 1)]
    print("   Lemma 5a.1: min eig of K_T over random quadtree tilings T and the shell tiling, ratio to c_0")
    worst = 1e9
    for d, j, S, nsamp in cases:
        M = L ** j
        vals = []
        for p in ([0.5] if d == 4 else [0.0, 0.3, 0.6, 0.9]):
            for _ in range(max(1, nsamp // 4 if d < 4 else 1)):
                T = random_tiling(S, j, d, rng, p)
                check_partition(T, S, d)
                vals.append(np.linalg.eigvalsh(build_K(S, j, d, T))[0])
        if d < 4 and S - 2 * shell_offsets(j)[j] >= M:
            Sb = 2 * shell_offsets(j)[j] + M * max(1, (S - 2 * shell_offsets(j)[j]) // M)
            if Sb == S:
                T, _ = shell_tiling(S, j, d)
                check_partition(T, S, d)
                vals.append(np.linalg.eigvalsh(build_K(S, j, d, T))[0])
        Tb = bulk_tiling(S, j, d)
        vb = np.linalg.eigvalsh(build_K(S, j, d, Tb))[0]
        worst = min(worst, min(vals) / C0)
        print(f"     d={d} j={j} S={S:3d} (n={S ** d:5d}): min over {len(vals):2d} tilings = {min(vals):.4f} (ratio {min(vals) / C0:.3f}); "
              f"single-level bulk tiling: {vb:.4f} (= a_j = {a_seq(j):.4f})", flush=True)
    print(f"   worst ratio min eig / c_0 over all cases: {worst:.4f} (>= 1 as proved)")

    print("   Lemma 5a.2: Re K_phi >= c_0/2 - eps(delta), phi = x_1/M (1-Lipschitz in coarse sup metric), K_phi = e^(delta phi) K e^(-delta phi)")
    print("     columns: lambda_min(Re K_phi), sigma_min(K_phi), lemma bound c_0/2 - eps(delta)")
    for d, j, S in ((1, 3, 16), (1, 6, 128), (2, 2, 16), (2, 3, 16), (2, 4, 32)):
        M = L ** j
        n = S ** d
        coords = np.indices((S,) * d).reshape(d, -1)
        for p in (0.0, 0.5):
            T = random_tiling(S, j, d, rng, p)
            K = build_K(S, j, d, T)
            for delta in sorted({round(delta0(d), 4), 0.5, 1.0}):
                Ph = np.exp(delta * coords[0] / M)
                Kp = (Ph[:, None] * K) / Ph[None, :]
                lre = np.linalg.eigvalsh((Kp + Kp.T) / 2)[0]
                smin = np.linalg.svd(Kp, compute_uv=False)[-1]
                bound = C0 / 2 - eps_ct(delta, d)
                flag = "" if bound <= 0 else ("  ok" if lre >= bound - 1e-12 else "  VIOLATED")
                print(f"     d={d} j={j} S={S:3d} p={p}: delta={delta:.4f}: lam_min Re = {lre:9.4f}, sigma_min = {smin:9.4f}, bound = {bound:9.4f}{flag}", flush=True)


# ---------------------------------------- entry decay and bulk dominance (computation)
def cell_vectors(S, d, M):
    """box vectors u_X on the coarse cells of the S^d box, columns, and the cell grid."""
    nc = S // M
    cols = []
    for X in itertools.product(range(nc), repeat=d):
        u = np.zeros(S ** d)
        u[cube_indices(S, d, tuple(x * M for x in X), M)] = M ** (-d / 2)
        cols.append(u)
    return np.array(cols).T, nc


def section5():
    print("== 5. nested shell geometry (k = j, widths 2 L^i): induced coarse kernel Xi(X,Y) = <u_X, K^-1 u_Y> ==")
    for d in (1, 2, 4):
        d0 = delta0(d)
        c1 = 4 / C0 * math.exp(2 * d0)
        dp = d0 / (2 * d)
        print(f"   d={d}: delta_0 = {d0:.4f}, C_1 = (4/c_0) e^(2 delta_0) = {c1:.4f}, delta' = delta_0/(2d) = {dp:.4f}, "
              f"weighted-norm bound C_1 coth(delta_0/4d)^d = {c1 * (1 / math.tanh(d0 / (4 * d))) ** d:.4e}")
    conv = {}
    for d, js, nb in ((1, (1, 2, 3, 4, 5, 6, 7), 14), (2, (1, 2, 3), 6)):
        for j in js:
            M = L ** j
            c = shell_offsets(j)
            S = 2 * c[j] + nb * M
            Tn, _ = shell_tiling(S, j, d)
            check_partition(Tn, S, d)
            Kn = build_K(S, j, d, Tn)
            Kb = build_K(S, j, d, bulk_tiling(S, j, d))
            U, nc = cell_vectors(S, d, M)
            Gn = np.linalg.solve(Kn, U)
            Gb = np.linalg.solve(Kb, U)
            Xn = U.T @ Gn
            Xb = U.T @ Gb
            cells = list(itertools.product(range(nc), repeat=d))
            cm = np.array(cells)
            dd = np.max(np.abs(cm[:, None, :] - cm[None, :, :]), axis=2)
            d0 = delta0(d)
            pref = 4 / C0 * math.exp(2 * d0)
            ratio = np.max(np.abs(Xn) * np.exp(d0 * dd) / pref)
            prof = [np.max(np.abs(Xn)[dd == D]) for D in range(0, nc)]
            slope = [math.log(prof[D] / prof[D + 1]) for D in range(1, min(6, nc - 1)) if prof[D + 1] > 0]
            fr = c[j] // M
            print(f" d={d} j={j} S={S} cells={nc}^{d} frame={fr} cells; max |Xi| e^(delta_0 D)/[(4/c_0)e^(2 delta_0)] = {ratio:.3e} (<= 1 as proved);"
                  f" decay rate per cell of max_D|Xi|: " + " ".join(f"{s_:.2f}" for s_ in slope))
            rows = []
            for r in range(fr, nc // 2 + 1):
                X = tuple(r if m == 0 else nc // 2 for m in range(d))
                ix = cells.index(X)
                rows.append((r - fr, abs(Xn[ix, ix] - Xb[ix, ix]), Xb[ix, ix], Xn[ix, ix]))
            if j == js[-1] or (d == 1 and j in (1, 4)):
                print("     |Xi^nested(X,X) - Xi^bulk(X,X)| versus distance D (cells) of X from the frame edge:")
                print("       D        diff           Xi_bulk(X,X)    ratio to previous")
                pv = None
                for D, df, xb, _ in rows:
                    print(f"       {D:2d}  {df:.4e}   {xb:.6e}   " + ("" if pv is None or df == 0 else f"{pv / df:8.2f}"), flush=True)
                    pv = df
            conv[(d, j)] = (rows[0][3], rows[-1][3])
        print(f"   d={d}: nested Xi_j(X,X) at fixed coarse positions (first bulk cell D=0, central cell) and its change with j:")
        print("      j   Xi(D=0)         Xi(center)      |Xi_j - Xi_(j-1)| at D=0, center")
        pv = None
        for j in js:
            a0, a1 = conv[(d, j)]
            print(f"      {j}   {a0:.8e}   {a1:.8e}" + ("" if pv is None else f"   {abs(a0 - pv[0]):.3e}  {abs(a1 - pv[1]):.3e}"), flush=True)
            pv = (a0, a1)


if __name__ == "__main__":
    which = sys.argv[1:] or ["0", "1", "2", "3", "4", "5"]
    for w in which:
        {"0": section0, "1": section1, "2": section2, "3": section3, "4": section4, "5": section5}[w]()
