"""Real-space check of interior vs cross-face fine differences of the minimizer image (m = 1)."""
import numpy as np
import t27_minimizer_regularity as t

def fine_field(L, n0, Phi):
    G = t.kernel(L, 1, n0).real   # (u, D, a, b)
    out = np.zeros((L**4, 6) + (n0,) * 4)
    for D in np.ndindex(*(n0,) * 4):
        sh = np.roll(Phi, shift=D, axis=(1, 2, 3, 4))
        out += np.einsum('uab,bY->uaY', G[(slice(None),) + D], sh.reshape(6, -1)).reshape(out.shape)
    # assemble fine lattice F[a, x], x = L*Y + u
    F = np.zeros((6,) + (n0 * L,) * 4)
    for ui, u in enumerate(np.ndindex(*(L,) * 4)):
        sl = tuple(slice(u[j], None, L) for j in range(4))
        F[(slice(None),) + sl] = out[ui]
    return F

def exact_random(n0, rng):
    A = rng.standard_normal((4,) + (n0,) * 4)
    d = lambda f, mu: np.roll(f, -1, axis=mu) - f
    return np.stack([d(A[nu], mu) - d(A[mu], nu) for mu, nu in t.PLAQ])

if __name__ == "__main__":
    rng = np.random.default_rng(1)
    n0 = 6
    for L in (2, 3, 4):
        Phi = exact_random(n0, rng)
        F = fine_field(L, n0, Phi)
        N = n0 * L
        x = np.arange(N)
        res = []
        for nu in range(4):
            dF = np.roll(F, -1, axis=1 + nu) - F
            face = (x % L) == L - 1
            sel = [slice(None)] * 5
            sel[1 + nu] = face
            sel_i = [slice(None)] * 5
            sel_i[1 + nu] = ~face
            res.append((np.sqrt(np.mean(dF[tuple(sel)] ** 2)), np.sqrt(np.mean(dF[tuple(sel_i)] ** 2))))
        rms = np.sqrt(np.mean(F ** 2))
        cf = np.mean([r[0] for r in res]) / rms; it = np.mean([r[1] for r in res]) / rms
        print(f"L={L}: rms|F|={rms:.4f}  cross-face rms|dF|/rms|F|={cf:.3f}  interior={it:.3f}", flush=True)


def sanity(L, n0, seed=2):
    rng = np.random.default_rng(seed)
    Phi = exact_random(n0, rng)
    F = fine_field(L, n0, Phi)
    d = lambda f, mu: np.roll(f, -1, axis=mu) - f
    db = lambda f, mu: f - np.roll(f, 1, axis=mu)
    pl = {a: i for i, a in enumerate(t.PLAQ)}
    def comp(mu, nu):
        if mu < nu: return F[pl[(mu, nu)]]
        return -F[pl[(nu, mu)]]
    # dF (Bianchi) on each triple
    bian = []
    for (l, mu, nu) in [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]:
        bian.append(d(comp(mu, nu), l) - d(comp(l, nu), mu) + d(comp(l, mu), nu))
    divF = [sum(db(comp(nu, rho), nu) for nu in range(4) if nu != rho) for rho in range(4)]
    rms = np.sqrt(np.mean(F**2))
    return np.sqrt(np.mean(np.array(bian)**2)) / rms, np.sqrt(np.mean(np.array(divF)**2)) / rms
