"""T50: weighted fits of the terminal observables of note 55.

Model: X_N = X_inf + a L^{-N} + b L^{-2N}, compared with the one-term models.
Data are the N >= 1 points (N = 0 has no averaging step), copied from
t50_mc_terminal_convergence.out.
"""
import numpy as np

DATA = {
    # (L, beta0, observable): (N list, values, errors)
    (2, 4.0, "P"): ([1, 2, 3, 4], [0.81827, 0.85039, 0.86271, 0.86809],
                    [0.00058, 0.00073, 0.00071, 0.00155]),
    (2, 4.0, "W12"): ([1, 2, 3, 4], [0.65641, 0.70565, 0.72513, 0.73207],
                      [0.00112, 0.00168, 0.00188, 0.00388]),
}


def fit(L, N, y, e, model):
    N = np.array(N, float); y = np.array(y); e = np.array(e)
    cols = [np.ones_like(N)]
    if "1" in model:
        cols.append(float(L) ** -N)
    if "2" in model:
        cols.append(float(L) ** (-2 * N))
    A = np.stack(cols, 1) / e[:, None]
    c, *_ = np.linalg.lstsq(A, y / e, rcond=None)
    chi2 = float(((A @ c - y / e) ** 2).sum())
    return c, chi2, len(y) - len(c)


if __name__ == "__main__":
    for (L, b0, obs), (N, y, e) in DATA.items():
        for model in ["1+2", "1", "2"]:
            c, chi2, dof = fit(L, N, y, e, model)
            label = {"1+2": "L^-N + L^-2N", "1": "L^-N only", "2": "L^-2N only"}[model]
            print(f"L={L} beta0={b0} {obs:4s} model {label:13s}: "
                  f"params {np.round(c, 4)}, chi2 = {chi2:.2f} (dof {dof})")
