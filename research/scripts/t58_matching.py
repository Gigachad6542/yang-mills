"""T58 (4D): Wilson vs tree-level Symanzik at matched terminal plaquette.

For each depth N, compare the curves W12(P) of the two actions (beta as the
parameter) at common P values. Memory decay predicts that the gap
W12_sym - W12_wil at fixed terminal P shrinks with N (dimension 6: a factor
of about L^2 = 4 per step, up to logarithms).
"""
import numpy as np

WIL = {  # from t51_universality.out
    1: [(2.6, 0.57820, 0.00111, 0.35265, 0.00160), (2.7, 0.61253, 0.00114, 0.39336, 0.00173),
        (2.8, 0.64183, 0.00056, 0.43027, 0.00089), (2.9, 0.66466, 0.00076, 0.45913, 0.00108)],
    2: [(2.85, 0.55016, 0.00133, 0.32397, 0.00191), (3.0, 0.61058, 0.00084, 0.39189, 0.00121),
        (3.15, 0.65528, 0.00087, 0.44630, 0.00146), (3.3, 0.68649, 0.00074, 0.48540, 0.00118)],
}
SYM = {  # from t58_4d.out
    1: [(1.9, 0.56582, 0.00103, 0.32870, 0.00138), (2.1, 0.64377, 0.00103, 0.42479, 0.00128),
        (2.3, 0.69545, 0.00076, 0.49266, 0.00096), (2.5, 0.73333, 0.00044, 0.54560, 0.00078)],
    2: [(2.3, 0.60263, 0.00084, 0.37642, 0.00107), (2.45, 0.65188, 0.00086, 0.43599, 0.00139),
        (2.6, 0.68949, 0.00052, 0.48450, 0.00103)],
}
rng = np.random.default_rng(58)


def w_at(rows, Pt, sample):
    b = np.array([r[0] for r in rows])
    P = np.array([r[1] + (rng.normal() * r[2] if sample else 0) for r in rows])
    W = np.array([r[3] + (rng.normal() * r[4] if sample else 0) for r in rows])
    deg = min(2, len(b) - 1)
    cP, cW = np.polyfit(b, P, deg), np.polyfit(b, W, deg)
    grid = np.linspace(b.min(), b.max(), 4001)
    bt = np.interp(Pt, np.polyval(cP, grid), grid)
    return bt, np.polyval(cW, bt)


if __name__ == "__main__":
    for N in (1, 2):
        if not SYM[N]:
            continue
        lo = max(min(r[1] for r in WIL[N]), min(r[1] for r in SYM[N]))
        hi = min(max(r[1] for r in WIL[N]), max(r[1] for r in SYM[N]))
        for Pt in np.round(np.linspace(lo + 0.005, hi - 0.005, 3), 3):
            base = w_at(SYM[N], Pt, False)[1] - w_at(WIL[N], Pt, False)[1]
            ds = [w_at(SYM[N], Pt, True)[1] - w_at(WIL[N], Pt, True)[1] for _ in range(2000)]
            bs, bw = w_at(SYM[N], Pt, False)[0], w_at(WIL[N], Pt, False)[0]
            print(f"N={N} P={Pt:.3f}: beta_sym={bs:.4f} beta_wil={bw:.4f} "
                  f"W12_sym - W12_wil = {base:+.5f} ({np.std(ds):.5f})")
