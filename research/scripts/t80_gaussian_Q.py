"""T80 part 2: the decisive test of (R) in the abelian Gaussian fibre model.

In the non-compact abelian model of t80_abelian_fibre.py the fibre integral is
exactly Gaussian, so (with the V-independent fluctuation determinant and the
V-independent Jacobian of the linear map q dropped)

    D_N(V) = beta_N * Q(V) + const,   Q(V) = A_N(V) - L * A_min(V),

    A_N(V)   = (1/2) V^T Dc V,         Dc = dc^T dc   (coarse plaquette matrix dc)
    A_min(V) = min_{qA = V} (1/2)|C A|^2 = (1/2) V^T M V,
    Q(V)     = (1/2) V^T Qm V,         Qm = Dc - L M.

(R) with no log term, for a set Z of coarse bonds, is the statement that
Dd := Qm - P^T Qm P (P = identity with the Z entries zeroed, i.e. V -> V^Z)
satisfies  Dd + C * Dz  >= 0  for some finite C, where
A_Z(V) = (1/2) V^T Dz V, Dz = sum over the coarse plaquettes touching Z.

(a) Is Q <= 0?   (b) Is Dd >= 0 on ker(Dz)?   (c) the optimal C.
eigh only.  Everything is computed from the fine-lattice matrices of
t80_abelian_fibre.py (no Fourier shortcut).
"""
import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t80_abelian_fibre as ab  # noqa: E402


def e_(mu):
    v = np.zeros(3, dtype=int)
    v[mu] = 1
    return v


def coarse_d(T):
    """Coarse plaquette matrix dc: rows (y, mu<nu), columns coarse bonds."""
    n = T.n
    nb = 3 * n ** 3
    rows, labels = [], []
    for y in itertools.product(range(n), repeat=3):
        for mu, nu in ((0, 1), (0, 2), (1, 2)):
            bonds = ab.coarse_plaq_bonds(n, y, mu, nu)
            r = np.zeros(nb)
            for sgn, b in zip((1, 1, -1, -1), bonds):
                r[T.bond_index[b]] += sgn
            rows.append(r)
            labels.append((y, mu, nu, bonds))
    return np.array(rows), labels


def build_M(L, n):
    """The fine-lattice Schur complement M: A_min(V) = (1/2) V^T M V."""
    T, C, Q = ab.build(L, n)
    FS = ab.FibreSolver(T, C, Q)
    nc = Q.shape[0]
    QQt_inv_Q = np.linalg.solve(FS.QQt, Q)           # (QQ^T)^-1 Q   (nc x nl)
    Ap = QQt_inv_Q.T                                  # Q^T (QQ^T)^-1 (nl x nc)
    rhs = -FS.K.T @ (FS.H @ Ap)
    assert np.abs(FS.Zm.T @ rhs).max() < 1e-9
    z = FS.Wp @ ((FS.Wp.T @ rhs) / FS.lam[:, None])
    S = Ap + FS.K @ z
    assert np.abs(Q @ S - np.eye(nc)).max() < 1e-9
    CS = C @ S
    M = CS.T @ CS
    M = 0.5 * (M + M.T)
    return T, C, Q, FS, M


def dist_plaq_bond(n, labels, zbonds):
    """Torus distance (in coarse lattice units, max-norm of the offset of
    the plaquette centre from the bond midpoint, doubled) -- only used to
    label supports."""
    out = []
    for (y, mu, nu, bonds) in labels:
        cx = np.array(y, float) + 0.5 * (e_(mu) + e_(nu))
        best = 1e9
        for (yb, mb) in zbonds:
            bx = np.array(yb, float) + 0.5 * e_(mb)
            d = np.abs(((cx - bx) + n / 2) % n - n / 2)
            best = min(best, d.max())
        out.append(best)
    return np.array(out)


def nullspace_eigh(A, tol=1e-9):
    w, U = np.linalg.eigh(A)
    return U[:, w < tol], w


def min_ratio(X, A, tol=1e-9):
    """inf_V  V^T X V / V^T A V  over V with V^T A V > 0, for symmetric X, A
    with A >= 0.  Split R^m = ker A + range A.  If X is not >= 0 on ker A the
    infimum is -inf.  Otherwise take the Schur complement of X over ker A
    (X restricted to ker A may be singular; its range must contain the
    coupling) and return the least generalised eigenvalue.  eigh only."""
    X = 0.5 * (X + X.T)
    A = 0.5 * (A + A.T)
    wA, UA = np.linalg.eigh(A)
    g = wA < tol
    F = UA[:, ~g] / np.sqrt(wA[~g])
    G = UA[:, g]
    if F.shape[1] == 0:
        return 0.0
    if G.shape[1] == 0:
        return np.linalg.eigvalsh(F.T @ X @ F)[0]
    XGG = G.T @ X @ G
    wg, Ug = np.linalg.eigh(0.5 * (XGG + XGG.T))
    if wg[0] < -1e-8:
        return -np.inf
    XFG = F.T @ X @ G
    pg = wg > 1e-8
    Sch = F.T @ X @ F
    if pg.any():
        c = XFG @ Ug[:, pg]
        Sch = Sch - (c / wg[pg]) @ c.T
    # coupling into the null part of XGG must vanish, else -inf
    c0 = XFG @ Ug[:, ~pg]
    if c0.size and np.abs(c0).max() > 1e-7:
        return -np.inf
    return np.linalg.eigvalsh(0.5 * (Sch + Sch.T))[0]


def analyse(L, n, T, Dc, labels, M, Z, name, verbose=True):
    nb = Dc.shape[0]
    Qm = Dc - L * M
    ev = np.linalg.eigvalsh(Qm)
    pZ = [i for i, lab in enumerate(labels) if any(b in Z for b in lab[3])]
    dcmat = coarse_d_cache[(L, n)]
    dZ = dcmat[pZ]
    Dz = dZ.T @ dZ
    P = np.eye(nb)
    for b in Z:
        P[T.bond_index[b], T.bond_index[b]] = 0.0
    Dd = Qm - P.T @ Qm @ P
    Dd = 0.5 * (Dd + Dd.T)
    N, wz = nullspace_eigh(Dz)
    DN = N.T @ Dd @ N
    wD = np.linalg.eigvalsh(0.5 * (DN + DN.T))
    res = dict(name=name, Qmax=ev[-1], Qmin=ev[0], nkerAZ=N.shape[1],
               lamDN=wD[0], pZ=len(pZ))
    # smallest eigenvalue of Dd + C Dz for a range of C
    def mineig(Cc):
        return np.linalg.eigvalsh(Dd + Cc * Dz)[0]
    kapZ = min_ratio(Dd, Dz)       # inf Dd / A_Z-form; -inf iff no finite C
    res["Cfin"] = None if not np.isfinite(kapZ) else max(0.0, -kapZ)
    res["mineig"] = {C_: mineig(C_) for C_ in (1.0, 10.0, 100.0, 1e4)}
    return res, Qm, Dz, Dd, N, DN



def comb_tree(T, cut_axis_bond):
    """Spanning tree of the coarse torus graph (n^3 - 1 bonds) that avoids the
    bond cut_axis_bond = (y, ax): a 'comb' (axial gauge): lines along the axis
    ax starting just after the cut, joined along the next axis at the
    starting level, joined along the third axis at the starting corner.
    The cut bond is not in the tree."""
    n = T.n
    (yc, ax) = cut_axis_bond
    others = [a for a in (2, 1, 0) if a != ax]
    a1, a2 = others            # a1: second line direction, a2: third
    start = np.array(yc) + e_(ax)       # first vertex after the cut
    tree = set()
    # lines along ax: from level start+0 ... n-2 steps, for every (a1,a2) offset
    for i1 in range(n):
        for i2 in range(n):
            base = start + i1 * e_(a1) + i2 * e_(a2)
            for t in range(n - 1):
                y = tuple(int(c) % n for c in base + t * e_(ax))
                tree.add((y, ax))
    # join along a1 at the starting a2-level, level ax = start
    for i1 in range(n - 1):
        for i2 in range(0, 1):
            y = tuple(int(c) % n for c in start + i1 * e_(a1))
            tree.add((y, a1))
    # join along a2 at i1 = 0
    for i2 in range(n - 1):
        y = tuple(int(c) % n for c in start + i2 * e_(a2))
        tree.add((y, a2))
    return tree


def bfs_tree(T, avoid, seed=0):
    """A random spanning tree (random-order union-find) avoiding `avoid`."""
    import random
    rnd = random.Random(seed)
    n = T.n
    parent = {y: y for y in itertools.product(range(n), repeat=3)}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    bonds = [(y, m) for y in itertools.product(range(n), repeat=3)
             for m in range(3) if (y, m) not in avoid]
    rnd.shuffle(bonds)
    tree = set()
    for (y, m) in bonds:
        y2 = tuple((np.array(y) + e_(m)) % n)
        ra, rb = find(y), find(y2)
        if ra != rb:
            parent[ra] = rb
            tree.add((y, m))
    assert len(tree) == n ** 3 - 1
    return tree


def gauge_fixed(T, dc, Dc, Dd, Dz, tree, Z, labels):
    """Restrict to V with V_b = 0 on the tree bonds.  Returns (A_Z-kernel
    dimension in the gauge slice, inf of Dd/A_N over ker(A_Z) in the slice,
    min eigenvalue of Dd on the kernel, and C_opt if finite)."""
    nb = Dc.shape[0]
    keep = [i for i in range(nb)
            if not any(T.bond_index[b] == i for b in tree)]
    B = np.zeros((nb, len(keep)))
    for j, i in enumerate(keep):
        B[i, j] = 1.0
    Dd_ = B.T @ Dd @ B
    Dz_ = B.T @ Dz @ B
    Dc_ = B.T @ Dc @ B
    Nz, _ = nullspace_eigh(Dz_)
    wD = np.linalg.eigvalsh(0.5 * (Nz.T @ Dd_ @ Nz + (Nz.T @ Dd_ @ Nz).T))
    # inf ratio of Dd / A_N(V) over ker(A_Z) in the slice (A_N positive there
    # except on the holonomy directions)
    kap = min_ratio(Nz.T @ Dd_ @ Nz, Nz.T @ Dc_ @ Nz)
    kapZ = min_ratio(Dd_, Dz_)
    Cfin = None if not np.isfinite(kapZ) else max(0.0, -kapZ)
    return Nz.shape[1], len(keep), wD[0], kap, Cfin


coarse_d_cache = {}


def zlists(n):
    y0 = (0, 0, 0)
    out = {}
    for ax in (2, 1, 0):
        out[f"1 bond, axis {ax}"] = {(y0, ax)}
    out["2 bonds, collinear last axis"] = {(y0, 2), ((0, 0, 1), 2)}
    out["2 bonds sharing a vertex (axes 2,1)"] = {(y0, 2), (y0, 1)}
    return out


def run(L, n, report_tree=True):
    print(f"\n=== L = {L}, coarse side n = {n} (fine side {L*n}) ===")
    T, C, Q, FS, M = build_M(L, n)
    dc, labels = coarse_d(T)
    coarse_d_cache[(L, n)] = dc
    Dc = dc.T @ dc
    nb = dc.shape[1]
    # sanity: M annihilates the ker of dc (coarse gauge + constants)
    N0, w0 = nullspace_eigh(Dc)
    print(f"  ker(dc) dim {N0.shape[1]} (expected n^3 + 2 = {n**3+2}); "
          f"|M N0| = {np.abs(M @ N0).max():.2e}; "
          f"M symmetric PSD: min eig {np.linalg.eigvalsh(M)[0]:.2e}")
    # classical check against the script's solver
    Vp = np.zeros(nb)
    Vp[T.bond_index[((0, 0, 0), 0)]] = 1.0
    Acl = FS.solve(Vp)
    print(f"  A_min(single-bond flux 1): direct {0.5*np.sum((C@Acl)**2):.8f} "
          f"vs (1/2)V^T M V {0.5*Vp@M@Vp:.8f}; A_N = {0.5*Vp@Dc@Vp:.4f}")
    Qm = Dc - L * M
    evQ = np.linalg.eigvalsh(Qm)
    # sup of -Q/A_N  (generalised eigenvalue on the non-gauge space)
    Wc, Uc = np.linalg.eigh(Dc)
    pos = Wc > 1e-9
    Dh = Uc[:, pos] / np.sqrt(Wc[pos])
    gen = np.linalg.eigvalsh(Dh.T @ Qm @ Dh)
    print(f"  (a) Q = A_N - L A_min: eigenvalues of Qm in [{evQ[0]:.5f}, "
          f"{evQ[-1]:.5f}] (Q <= 0 iff max <= 0); Q/A_N in "
          f"[{gen[0]:.5f}, {gen[-1]:.5f}]  (Thm 64.1: >= -(L^2-1) = {-(L*L-1)})")
    results = []
    for name, Z in zlists(n).items():
        res, Qm_, Dz, Dd, N, DN = analyse(L, n, T, Dc, labels, M, Z, name)
        results.append(res)
        status = (f"C_opt = {res['Cfin']:.5f}" if res["Cfin"] is not None
                  else "NO finite C")
        print(f"  Z = {name:38s} ker(A_Z) dim {res['nkerAZ']:3d}  "
              f"min eig of Dd on ker(A_Z) = {res['lamDN']:+.3e}  -> {status}")
        if res["Cfin"] is None:
            # the most negative direction: describe it
            w, U = np.linalg.eigh(0.5 * (DN + DN.T))
            V = N @ U[:, 0]
            t_ = sum(V[T.bond_index[b]] for b in Z)
            th = dc @ V
            dist = dist_plaq_bond(n, labels, Z)
            AZ = 0.5 * np.sum(th[dist < 0.51] ** 2)
            far = th.copy()
            far[dist < 0.51] = 0
            print(f"      worst V (|V|=1): max|theta| = {np.abs(th).max():.4f}, V_Z = {t_:+.4f}, near-plaquette flux energy "
                  f"A_Z(V) = {0.5*V@Dz@V:.2e}, far flux energy "
                  f"{0.5*far@far:.4f}, Dd(V) = {0.5*V@Dd@V:+.4e}")
            # decay of the violation with the distance of the flux
            nbmax = int(dist.max() * 2)
            for rr in sorted(set(np.round(dist, 3))):
                if rr < 0.9:
                    continue
                mask = dist < rr - 1e-9     # plaquettes forced flat
                rows = dc[mask]
                Nr, _ = nullspace_eigh(rows.T @ rows)
                # also keep A_Z = 0 (these plaquettes are within the mask
                # because they have the smallest distance)
                Ddr = Nr.T @ Dd @ Nr
                Afar = Nr.T @ (dc.T @ dc) @ Nr
                kap = min_ratio(Ddr, Afar)
                print(f"      flux confined to distance >= {rr:.1f}: "
                      f"inf Dd/A_flux = {kap:+.4e}")

    # ---- gauge-fixed versions (V^Z defined in a fixed gauge) -------------
    for name in ("1 bond, axis 2", "1 bond, axis 0", "2 bonds, collinear last axis"):
        Z = zlists(n)[name]
        res, Qm_, Dz, Dd, N, DN = analyse(L, n, T, Dc, labels, M, Z, name)
        zb = sorted(Z)[0]
        trees = {"comb tree (cut at Z)": comb_tree(T, zb)}
        for sd in range(3):
            trees[f"random spanning tree #{sd}"] = bfs_tree(T, Z, sd)
        if len(Z) == 2:
            trees = {k: v for k, v in trees.items() if k.startswith("random")}
        for tn, tr in trees.items():
            assert not (tr & Z)
            kd, dim, lam, kap, Cf = gauge_fixed(T, dc, Dc, Dd, Dz, tr, Z, labels)
            st = f"C_opt = {Cf:.4f}" if Cf is not None else "NO finite C"
            print(f"  gauge-fixed, Z = {name:28s} {tn:24s} slice dim {dim:3d}, "
                  f"ker(A_Z) dim {kd:3d}: min eig Dd {lam:+.3e}, inf Dd/A_N {kap:+.3e} -> {st}")
    return T, dc, labels, M, Dc, Qm, results


if __name__ == "__main__":
    for (L, n) in ((2, 3), (2, 4), (3, 3), (3, 4)):
        run(L, n)
