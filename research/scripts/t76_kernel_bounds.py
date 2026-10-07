"""T76 check (note 61 section 6c, Lemma 6c.2 and constants).

(1) Kernel facts used in the Cauchy-Schwarz proof of Sigma(S) >= S:
    real-space kernel w_j = b(x_j) * prod_{i != j} (b*s)(x_i), b = (1/L) 1_[0,L),
    s = 1_[0,L); w >= 0, mass L^2, periodization over (L Z)^3 equal to 1/L at
    every site, and its Fourier transform equals the w_j(p) of t7_gauss3d.
(2) r(K) = eigenvalues of Pi_1(K) = (C_L(K))^+ on the transverse space, sampled
    at random continuum K: r_min >= 1 (Sigma(S) >= S), r_max.
(3) Wilson orbit W_n = Sigma^n(S) at the terminal momentum K:
    eigenvalues of (C_{L^n}(K))^+ on the transverse space; W_n increasing in n,
    and sup_K lambda_max(W_n) for sampled K.
"""
import sys, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from t7_gauss3d import terminal_cov, D as Dsum_t7


def kernel_checks():
    print("(1) kernel facts")
    rng = np.random.default_rng(0)
    for L in (2, 3, 4, 5):
        b = np.ones(L)/L; s = np.ones(L)
        bs = np.convolve(b, s)                      # support 0..2L-2
        # 1D periodization over L Z of b and of b*s at every residue
        def period(f):
            out = np.zeros(L)
            for t, v in enumerate(f):
                out[t % L] += v
            return out
        pb, pbs = period(b), period(bs)
        ok = (np.allclose(pb, 1.0/L) and np.allclose(pbs, 1.0) and (bs >= 0).all()
              and abs(b.sum()-1) < 1e-14 and abs(bs.sum()-L) < 1e-12)
        # Fourier transform check: sum_t f(t) e^{-i q t} vs formula
        q = rng.uniform(0, 2*np.pi, 5)
        ft_b = np.array([(b*np.exp(-1j*qq*np.arange(L))).sum() for qq in q])
        ft_bs = np.array([(bs*np.exp(-1j*qq*np.arange(len(bs)))).sum() for qq in q])
        Dq = Dsum_t7(q, L)
        ok &= np.allclose(ft_b, Dq/L) and np.allclose(ft_bs, Dq*Dq/L)
        print(f"  L={L}: mass(w_j)=1*{bs.sum():.0f}*{bs.sum():.0f}={bs.sum()**2:.0f} (=L^2={L*L}), "
              f"periodization along j = {pb[0]:.4f} (1/L), perpendicular = {pbs[0]:.4f} (1) -> "
              f"sum_Y w(x-Y) = {pb[0]*pbs[0]**2:.4f} (1/L={1/L:.4f}); all checks {ok}")


def basisB(K):
    r = np.exp(1j*np.asarray(K)) - 1
    r2 = (abs(r)**2).sum()
    P = np.eye(3) - np.outer(np.conj(r), r)/r2
    w, U = np.linalg.eigh(P)
    return U[:, 1:]


def Pi_eigs(C, U):
    Cb = U.conj().T @ ((C + C.conj().T)/2) @ U
    lam = np.linalg.eigvalsh(Cb)
    return 1.0/lam


def sampled_K(n, rng):
    Ks = []
    for _ in range(n):
        mag = 10**rng.uniform(-2, 0)               # include small momenta
        K = rng.uniform(-np.pi, np.pi, 3)
        K = np.where(rng.random(3) < 0.5, K*mag, K)
        Ks.append(K)
    Ks += [np.array(k) for k in [(np.pi, np.pi, np.pi), (np.pi, 0, 0), (np.pi, np.pi, 0),
                                 (np.pi/2, 0, 0), (np.pi/2, np.pi/2, np.pi/2), (0, 0, np.pi/2)]]
    return Ks


def r_range():
    print("(2) r = eig(Pi_1) on transverse space, random continuum K (1500 points + special points)")
    rng = np.random.default_rng(1)
    Ks = sampled_K(1500, rng)
    for L in (2, 3, 4, 5):
        rs = []
        for K in Ks:
            if np.abs(np.exp(1j*K) - 1).max() < 1e-9:
                continue
            rs.extend(Pi_eigs(terminal_cov(K, L), basisB(K)))
        rs = np.array(rs)
        print(f"  L={L}: min r = {rs.min():.6f}, max r = {rs.max():.4f}, r>=1 for all samples: {bool((rs >= 1-1e-9).all())}")


def wilson_orbit():
    print("(3) Wilson orbit W_n = Sigma^n(S): lambda_min, lambda_max over sampled K (300 points + special)")
    rng = np.random.default_rng(2)
    Ks = sampled_K(300, rng)
    for L, nmax in ((2, 5), (3, 3), (4, 2)):
        prev = None
        for n in range(1, nmax+1):
            lo, hi, mono = 1e9, 0.0, True
            cur = []
            for K in Ks:
                if np.abs(np.exp(1j*K) - 1).max() < 1e-9:
                    continue
                U = basisB(K)
                ev = Pi_eigs(terminal_cov(K, L**n), U)
                cur.append(ev)
                lo = min(lo, ev.min()); hi = max(hi, ev.max())
            cur = np.array(cur)
            inc = "" if prev is None else f"  min over K of (lam_max_n - lam_max_(n-1)) = {(cur.max(1)-prev.max(1)).min():+.4f}"
            print(f"  L={L} n={n}: min eig {lo:.6f}, max eig {hi:.4f}{inc}")
            prev = cur


if __name__ == '__main__':
    kernel_checks(); r_range(); wilson_orbit()
