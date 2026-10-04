"""T51: matching analysis for the 4D universality test (note 56).

For each depth N, the terminal observables (P, W12) are measured at several
beta. Universality predicts that the curve W12 as a function of P (with beta
as the parameter) is the same at every depth, up to corrections that vanish
as N grows. The curves are compared on the common P range, by quadratic
interpolation in beta and Gaussian resampling of the errors. The matched
beta_N(P) also gives the step beta_2 - beta_1 at fixed terminal P, to be
compared with the one-loop step 8 b_0 log 2 = 0.2575 (SU(2), beta = 4/g^2).
"""
import numpy as np

DATA = {  # N: list of (beta, P, dP, W12, dW12), from t51_universality.out
    0: [(2.4, 0.63354, 0.00134, 0.43330, 0.00222), (2.5, 0.65449, 0.00084, 0.46183, 0.00124),
        (2.6, 0.67200, 0.00063, 0.48633, 0.00108)],
    1: [(2.6, 0.57820, 0.00111, 0.35265, 0.00160), (2.7, 0.61253, 0.00114, 0.39336, 0.00173),
        (2.8, 0.64183, 0.00056, 0.43027, 0.00089), (2.9, 0.66466, 0.00076, 0.45913, 0.00108)],
    2: [(2.85, 0.55016, 0.00133, 0.32397, 0.00191), (3.0, 0.61058, 0.00084, 0.39189, 0.00121),
        (3.15, 0.65528, 0.00087, 0.44630, 0.00146), (3.3, 0.68649, 0.00074, 0.48540, 0.00118)],
}
rng = np.random.default_rng(56)


def curves(sample):
    out = {}
    for N, rows in DATA.items():
        b = np.array([r[0] for r in rows])
        P = np.array([r[1] + (rng.normal() * r[2] if sample else 0) for r in rows])
        W = np.array([r[3] + (rng.normal() * r[4] if sample else 0) for r in rows])
        deg = min(2, len(b) - 1)
        out[N] = (np.polyfit(b, P, deg), np.polyfit(b, W, deg), b)
    return out


def beta_at(cP, b, Pt):
    grid = np.linspace(b.min(), b.max(), 4001)
    Pv = np.polyval(cP, grid)
    return np.interp(Pt, Pv, grid)


def analyse(sample):
    c = curves(sample)
    res = {}
    for Pt in [0.62, 0.64, 0.66]:
        for N in (1, 2):
            cP, cW, b = c[N]
            bt = beta_at(cP, b, Pt)
            res[(N, Pt)] = (bt, np.polyval(cW, bt))
        cP, cW, b = c[0]
        if 0.634 <= Pt <= 0.672:
            bt = beta_at(cP, b, Pt)
            res[(0, Pt)] = (bt, np.polyval(cW, bt))
    return res


if __name__ == "__main__":
    base = analyse(False)
    samples = [analyse(True) for _ in range(2000)]
    print("P_target | N | beta_N(P) | W12 at matched beta")
    for key in sorted(base, key=lambda k: (k[1], k[0])):
        N, Pt = key
        bs = np.array([s[key][0] for s in samples]); ws = np.array([s[key][1] for s in samples])
        print(f"{Pt:.2f} | {N} | {base[key][0]:.4f}({bs.std():.4f}) | {base[key][1]:.5f}({ws.std():.5f})")
    print("\nW12 differences at fixed P, and the beta step:")
    for Pt in [0.62, 0.64, 0.66]:
        d = np.array([s[(2, Pt)][1] - s[(1, Pt)][1] for s in samples])
        db = np.array([s[(2, Pt)][0] - s[(1, Pt)][0] for s in samples])
        line = (f"P={Pt:.2f}: W12(N=2)-W12(N=1) = {base[(2, Pt)][1]-base[(1, Pt)][1]:+.5f}({d.std():.5f}); "
                f"beta_2-beta_1 = {base[(2, Pt)][0]-base[(1, Pt)][0]:.4f}({db.std():.4f})")
        if (0, Pt) in base:
            d0 = np.array([s[(1, Pt)][1] - s[(0, Pt)][1] for s in samples])
            db0 = np.array([s[(1, Pt)][0] - s[(0, Pt)][0] for s in samples])
            line += (f"; W12(N=1)-W12(N=0) = {base[(1, Pt)][1]-base[(0, Pt)][1]:+.5f}({d0.std():.5f}), "
                     f"beta_1-beta_0 = {base[(1, Pt)][0]-base[(0, Pt)][0]:.4f}({db0.std():.4f})")
        print(line)
    print(f"\none-loop step 8 b0 log 2 = {8 * 11 / (24 * np.pi**2) * np.log(2):.4f}")
