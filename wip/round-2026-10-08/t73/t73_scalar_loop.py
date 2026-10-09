"""T73: the P_0 P_1 coefficient of the exact one-loop step increment of the scalar loop,
in the k -> infinity (continuum) limit of note 48's model.  research/50 sec 2.6.

Model (sec 2.6.2).  M -> infinity limit of the free step, field momentum q in R^4, cube side 1
(scale-k block) and L (scale-(k+1) block):
    Gamma_L = R_1 - R_L,    G_1 = G0 - R_1,     G0(q) = 1/q^2,
    R_s = G0 Q_s^* (Q_s G0 Q_s^*)^{-1} Q_s G0,  what_s(q) = prod_j (1 - exp(-i s q_j)) / (i s q_j).
On the L-sector K (q = (K + 2 pi n)/L) the unit sectors a in (Z/L)^4 (kappa_a = (K + 2 pi a)/L,
q = kappa_a + 2 pi m) give
    Gamma(K) = sum_a u_a u_a^* / C_a - v v^* / C_v,
    G_1(K)   = diag(1/q^2) - sum_a u_a u_a^* / C_a,
    u(q) = what_1(q)/q^2 (q in class a), C_a = sum_{q in a} |what_1|^2/q^2,
    v(q) = what_L(q)/q^2 (all q in the L-sector), C_v = sum_q |what_L|^2/q^2.
Exact second variation of the step increment  log det C_{LM}(A) - log det C_M(A)
(sec 2.6.1, checked on a lattice by t73_increment_check.py), P_0 P_1 part, no seagull for mu != nu:
    I_{01}(P) = Tr[Gamma V_0 Gamma' V_1^*] + Tr[Gamma V_0 G_1' V_1^*] + Tr[Gamma' V_1^* G_1 V_0]
              = BUB + X1 + X2,
with V_mu = diag (2q+P)_mu, primes = sector K' = K + L P (q -> q + P).
b_L := coefficient of P_0 P_1 in  (1/L^4) int_{(-pi,pi]^4} dK/(2 pi)^4 I_{01}(P)
      [= (1/L^4) mean over K, midpoint rule on an offset periodic grid];
the claim of sec 2.6 is b_L = kappa_0 log L exactly, kappa_0 = 1/(24 pi^2).
Alias sums are truncated at |m_j| <= NM.

The engine `increment_terms` is generic: it takes, per coordinate j, the 1D arrays of the
momenta, the Laplacian symbol, the unit-cube and L-cube symbols and the vertex factor.  The
lattice front-end t73_lattice_limit.py reuses it with lattice symbols.

usage: python3 t73_scalar_loop.py L NK NM h [h ...]
"""
import sys
import numpy as np

TWO_PI = 2 * np.pi
KAPPA0 = 1 / (24 * np.pi**2)


def increment_terms(coord):
    """(BUB, X1, X2) for one sector from per-coordinate data.

    `coord` is a list of 4 dicts with 1D-per-axis arrays of shape (L, n) (class, alias):
        s2, s2p   Laplacian symbol at q and at q + P
        w1, wL, w1p, wLp   unit-cube / L-cube averaging symbols (what_s) at q and q + P
        vert      vertex factor (2q+P)_j at q (used for j = 0, 1)
    """
    L, n = coord[0]["s2"].shape

    def bc(arr, j):  # arr (L, n) -> broadcast shape with class axis j and alias axis 4+j
        shp = [1] * 8
        shp[j], shp[4 + j] = L, n
        return arr.reshape(shp)

    q2 = sum(bc(c["s2"], j) for j, c in enumerate(coord))
    qp2 = sum(bc(c["s2p"], j) for j, c in enumerate(coord))
    wu = bc(coord[0]["w1"], 0) * bc(coord[1]["w1"], 1) * bc(coord[2]["w1"], 2) * bc(coord[3]["w1"], 3)
    wv = bc(coord[0]["wL"], 0) * bc(coord[1]["wL"], 1) * bc(coord[2]["wL"], 2) * bc(coord[3]["wL"], 3)
    wup = bc(coord[0]["w1p"], 0) * bc(coord[1]["w1p"], 1) * bc(coord[2]["w1p"], 2) * bc(coord[3]["w1p"], 3)
    wvp = bc(coord[0]["wLp"], 0) * bc(coord[1]["wLp"], 1) * bc(coord[2]["wLp"], 2) * bc(coord[3]["wLp"], 3)
    u, v, up, vp = wu / q2, wv / q2, wup / qp2, wvp / qp2
    ax = (4, 5, 6, 7)
    Cu = (np.abs(wu) ** 2 / q2).sum(ax)
    Cup = (np.abs(wup) ** 2 / qp2).sum(ax)
    Cv = (np.abs(wv) ** 2 / q2).sum()
    Cvp = (np.abs(wvp) ** 2 / qp2).sum()
    V0 = bc(coord[0]["vert"], 0)
    V1 = bc(coord[1]["vert"], 1)

    def ov(x, y, V):
        return (np.conj(x) * V * y).sum(ax)

    Ouu0, Ouu1 = ov(u, up, V0), ov(u, up, V1)
    Ouv0, Ouv1 = ov(u, vp, V0), ov(u, vp, V1)
    Ovu0, Ovu1 = ov(v, up, V0), ov(v, up, V1)
    Ovv0, Ovv1 = ov(v, vp, V0).sum(), ov(v, vp, V1).sum()
    # bubble Tr[Gamma V_0 Gamma' V_1^*]
    B = (Ouu0 * np.conj(Ouu1) / (Cu * Cup)).sum()
    B -= (Ouv0 * np.conj(Ouv1) / (Cu * Cvp)).sum()
    B -= (Ovu0 * np.conj(Ovu1) / (Cv * Cup)).sum()
    B += Ovv0 * np.conj(Ovv1) / (Cv * Cvp)
    # cross terms with the unit-cell propagator G_1 = diag(1/q^2) - R_1
    Gdiag = np.abs(u) ** 2 / Cu.reshape(Cu.shape + (1,) * 4) - np.abs(v) ** 2 / Cv
    Gdiagp = np.abs(up) ** 2 / Cup.reshape(Cup.shape + (1,) * 4) - np.abs(vp) ** 2 / Cvp
    D1 = (Gdiag * (V0 * V1) / qp2).sum()
    D2 = (Gdiagp * (V0 * V1) / q2).sum()
    X1 = D1 - (((Ouu0 * np.conj(Ouu1)) / Cu - (Ovu0 * np.conj(Ovu1)) / Cv) / Cup).sum()
    X2 = D2 - (((Ouu1 * np.conj(Ouu0)) / Cup - (Ouv1 * np.conj(Ouv0)) / Cvp) / Cu).sum()
    return B, X1, X2


def what(q, s):
    """Fourier transform of the indicator of the cube [0,s)^4 divided by s^4 (conjugate convention of the note)."""
    x = s * q
    return ((1 - np.exp(-1j * x)) / (1j * x)).prod(-1)


def coord_continuum(L, K, P, NM):
    n_al = np.arange(-NM, NM + 1, dtype=float)
    aa = np.arange(L, dtype=float)
    out = []
    for j in range(4):
        kap = (K[j] + TWO_PI * aa) / L
        kap = kap - TWO_PI * np.round(kap / TWO_PI)  # re-centre the alias window
        q = kap[:, None] + TWO_PI * n_al[None, :]
        qp = q + P[j]
        out.append(dict(
            s2=q**2, s2p=qp**2,
            w1=(1 - np.exp(-1j * q)) / (1j * q), wL=(1 - np.exp(-1j * L * q)) / (1j * L * q),
            w1p=(1 - np.exp(-1j * qp)) / (1j * qp), wLp=(1 - np.exp(-1j * L * qp)) / (1j * L * qp),
            vert=2 * q + P[j]))
    return out


def terms(L, K, P, NM):
    """(BUB, X1, X2) for the single sector K (complex numbers), continuum model."""
    return increment_terms(coord_continuum(L, K, P, NM))


def kpoints(NK):
    g = (np.arange(NK) + 0.5) * TWO_PI / NK - np.pi
    half = g[g > 0]
    pts = []
    for i2, k2 in enumerate(half):  # K2,K3 -> -K2,-K3 and K2<->K3 symmetry (P_2 = P_3 = 0)
        for i3, k3 in enumerate(half):
            if i3 < i2:
                continue
            pts.append((k2, k3, 4 * (1 if i2 == i3 else 2)))
    return g, pts


def kmean(fun, NK):
    """mean over the offset periodic K grid of fun(K) -> array of 3 complex numbers (symmetry reduced)."""
    g, pts = kpoints(NK)
    tot = np.zeros(3, dtype=complex)
    wsum = 0.0
    for k0 in g:
        for k1 in g:
            for (k2, k3, w) in pts:
                tot += w * np.array(fun(np.array([k0, k1, k2, k3])))
                wsum += w
    return tot / wsum


def integral(L, P, NK, NM):
    """(BUB, X1, X2) integrated:  (1/L^4) mean_K."""
    return kmean(lambda K: terms(L, K, P, NM), NK) / L**4


if __name__ == "__main__":
    L, NK, NM = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    hs = [float(x) for x in sys.argv[4:]] or [0.05]
    for h in hs:
        B, X1, X2 = (z.real / h**2 for z in integral(L, np.array([h, h, 0.0, 0.0]), NK, NM))
        tot = B + X1 + X2
        print(f"L={L} NK={NK} NM={NM} h={h}: BUB/h^2 = {B:+.7f}  (X1+X2)/h^2 = {X1 + X2:+.7f}  "
              f"total b_L = {tot:+.7f}   kappa0*log L = {KAPPA0 * np.log(L):+.7f}   "
              f"(b_L - kappa0 log L)/kappa0 = {(tot - KAPPA0 * np.log(L)) / KAPPA0:+.4f}", flush=True)
