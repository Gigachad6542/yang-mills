"""T81: numerical check of (I-LF)(b') in union form in the abelian Gaussian model
(note 61 §6e.2 (LF-b'), note 67 §4-§5).  For a set Z of coarse bonds, with
D_d = Q_m - P_Z^T Q_m P_Z (note 67 §3.1), D_z the near-energy form of Z and
T_m the summed tail form  sum_{x not near Z} (sum_{c in Z} e^{-m d(x,c)}) A_x,
prints the least C_T with  D_d + C D_z + C_T T_m >= 0  (inf: no finite C_T at
this C).  Usage: python3 t81_union_check.py L n   (L = 2, n = 8: about 80 s).
Written by the T81 worker; committed by the lead.
"""
import sys, os, time, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t80_abelian_fibre as ab
import t80_bloch_kernel as bk
import t80_gaussian_Q as gq

def e_(mu):
    v = np.zeros(3, dtype=int); v[mu] = 1; return v

L, n = int(sys.argv[1]), int(sys.argv[2])
t0 = time.time()
T, dc, labels = bk.coarse_plaq_matrix(n)
M, gap = bk.M_from_bloch(L, n)
Dc = dc.T @ dc
Qm = Dc - L * M
nb = Dc.shape[0]
print("setup", time.time() - t0, "max eig Qm", np.linalg.eigvalsh(Qm)[-1], flush=True)

def bond_mid(b):
    (yb, mb) = b
    return np.array(yb, float) + 0.5 * e_(mb)

def plaq_centre(lab):
    y, mu, nu, bonds = lab
    return np.array(y, float) + 0.5 * (e_(mu) + e_(nu))

def cheb(a, b):
    d = np.abs(((a - b) + n / 2) % n - n / 2)
    return d.max()

CS = (2.9, 3.0, 6.0, 20.0) if L == 2 else (4.4, 5.0, 8.0, 20.0)
def analyse(Z, ms=(1.0, 2.0), Cs=CS):
    Z = set(Z)
    P = np.eye(nb)
    for b in Z:
        P[T.bond_index[b], T.bond_index[b]] = 0.0
    Dd = Qm - P.T @ Qm @ P
    Dd = 0.5 * (Dd + Dd.T)
    near = np.array([any(b in Z for b in lab[3]) for lab in labels])
    dZ = dc[near]
    Dz = dZ.T @ dZ
    cent = [plaq_centre(lab) for lab in labels]
    mids = [bond_mid(b) for b in Z]
    res = {}
    for m in ms:
        w = np.zeros(len(labels))
        for i, c in enumerate(cent):
            if near[i]:
                continue
            w[i] = sum(np.exp(-m * cheb(c, bm)) for bm in mids)
        Tm = dc.T @ (w[:, None] * dc)
        for C in Cs:
            kap = gq.min_ratio(Dd + C * Dz, Tm)
            res[(m, C)] = -kap if np.isfinite(kap) else np.inf
    return res

y0 = (0, 0, 0)
def plaq_bonds(y, mu, nu):
    return set(ab.coarse_plaq_bonds(n, tuple(y), mu, nu))

configs = {}
configs["1 bond"] = {(y0, 2)}
configs["Z(1 plaquette)"] = plaq_bonds((0,0,0), 0, 1)
for r in (2, 3, 4):
    configs[f"2 bonds, separation {r} along axis 0"] = {(y0, 2), ((r,0,0), 2)}
for r in (3, 4):
    configs[f"2 plaquette loops, separation {r}"] = plaq_bonds((0,0,0),0,1) | plaq_bonds((r,0,0),0,1)
configs["Z(2x2 patch, 4 plaquettes)"] = set().union(*[plaq_bonds((i,j,0),0,1) for i in (0,1) for j in (0,1)])
configs["Z(cube faces: 12 plaquettes)"] = set().union(*[plaq_bonds((i,j,k),mu,nu) for i in (0,1) for j in (0,1) for k in (0,1) for (mu,nu) in ((0,1),(0,2),(1,2))])
configs["Z(4x4 patch, 16 plaquettes)"] = set().union(*[plaq_bonds((i,j,0),0,1) for i in range(4) for j in range(4)])
configs["Z(3x3x3 solid: all plaquettes in box)"] = set().union(*[plaq_bonds((i,j,k),mu,nu) for i in range(3) for j in range(3) for k in range(3) for (mu,nu) in ((0,1),(0,2),(1,2))])
configs["Z(plane slab 6x6, 36 plaquettes)"] = set().union(*[plaq_bonds((i,j,0),0,1) for i in range(6) for j in range(6)])
for name, Z in configs.items():
    t1 = time.time()
    res = analyse(Z)
    print(f"L={L} n={n} {name} (|Z|={len(Z)}): " + "; ".join(f"m={m},C={C}: C_T={v:.3f}" for (m, C), v in res.items()) + f"   [{time.time()-t1:.1f}s]", flush=True)
