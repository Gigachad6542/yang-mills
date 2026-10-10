"""T54: matching analysis for the 4D universality test, depths N = 0..3 (note 56).

Same method as t51_matching.py (quadratic interpolation in beta at each depth,
Gaussian resampling of the errors), applied to the T54 runs, which use the
checkpointed driver t54_mc_checkpointed.py and add the terminal 2x2 loop W22.
The N = 0, 1, 2 points are independent re-runs (fresh seeds) of note 56's; the
N = 3 points (32^4) are new.  Data are read from the t54_n{N}_b{beta}.out files.

At fixed terminal plaquette P the script prints beta_N(P), W12 and W22 at the
matched beta, the differences between consecutive depths, and the beta step
beta_N - beta_{N-1}, to be compared with the one-loop step 8 b_0 log 2.
"""
import glob
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
PAT = re.compile(r"N=(\d+) n=\d+ beta=([\d.]+): P=([\d.]+)\(([\d.]+)\) "
                 r"W12=([\d.]+)\(([\d.]+)\) W22=([\d.]+)\(([\d.]+)\)")


def load():
    data = {}
    for f in sorted(glob.glob(os.path.join(HERE, "t54_n*_b*.out"))):
        for line in open(f):
            m = PAT.search(line)
            if m:
                N = int(m.group(1))
                data.setdefault(N, []).append(tuple(float(x) for x in m.groups()[1:]))
    for N in data:
        data[N].sort()
    return data


DATA = load()
OBS = {"P": 1, "W12": 3, "W22": 5}           # column of the value; error in the next column
TARGETS = [0.62, 0.64, 0.66]
rng = np.random.default_rng(54)


def fit(N, sample):
    rows = DATA[N]
    b = np.array([r[0] for r in rows])
    deg = min(2, len(b) - 1)
    out = {}
    for name, k in OBS.items():
        y = np.array([r[k] + (rng.normal() * r[k + 1] if sample else 0.0) for r in rows])
        out[name] = np.polyfit(b, y, deg)
    return out, b


def analyse(sample):
    res = {}
    for N in DATA:
        c, b = fit(N, sample)
        grid = np.linspace(b.min(), b.max(), 4001)
        Pv = np.polyval(c["P"], grid)
        if np.any(np.diff(Pv) <= 0):
            continue
        for Pt in TARGETS:
            if Pv[0] <= Pt <= Pv[-1]:
                bt = np.interp(Pt, Pv, grid)
                res[(N, Pt)] = (bt, np.polyval(c["W12"], bt), np.polyval(c["W22"], bt))
    return res


def main():
    print("Data (t54_n*.out): N: (beta, P, W12, W22)")
    for N, rows in sorted(DATA.items()):
        print(f"  N={N}: " + "; ".join(f"({r[0]:.2f}, {r[1]:.5f}, {r[3]:.5f}, {r[5]:.5f})" for r in rows))
    base = analyse(False)
    samples = [analyse(True) for _ in range(2000)]

    print("\nP_target | N | beta_N(P) | W12 at matched beta | W22 at matched beta")
    for key in sorted(base, key=lambda k: (k[1], k[0])):
        vals = np.array([s[key] for s in samples if key in s])
        sd = vals.std(axis=0)
        bt, w12, w22 = base[key]
        print(f"{key[1]:.2f} | {key[0]} | {bt:.4f}({sd[0]:.4f}) | {w12:.5f}({sd[1]:.5f}) | {w22:.5f}({sd[2]:.5f})")

    print("\nDifferences between consecutive depths at fixed P (value(error)):")
    for Pt in TARGETS:
        for N in sorted(DATA):
            if N == 0 or (N, Pt) not in base or (N - 1, Pt) not in base:
                continue
            a, p = (N, Pt), (N - 1, Pt)
            ok = [s for s in samples if a in s and p in s]
            d = np.array([[s[a][i] - s[p][i] for i in range(3)] for s in ok])
            b0 = [base[a][i] - base[p][i] for i in range(3)]
            sd = d.std(axis=0)
            print(f"P={Pt:.2f}, N={N-1}->{N}: beta step {b0[0]:.4f}({sd[0]:.4f}); "
                  f"dW12 {b0[1]:+.5f}({sd[1]:.5f}); dW22 {b0[2]:+.5f}({sd[2]:.5f})")
    print(f"\none-loop step 8 b0 log 2 = {8 * 11 / (24 * np.pi**2) * np.log(2):.4f}")


if __name__ == "__main__":
    main()
