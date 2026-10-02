"""T22 high-precision version (mpmath) for small heat-kernel time (b large),
where the density near theta=pi is exponentially small."""
import mpmath as mp
mp.mp.dps = 60
def coeffs(M, b, nmax):
    beta = mp.mpf(M*M*b); I1 = mp.besseli(1, beta)
    return [(n+1)*mp.power(mp.besseli(n+1, beta)/I1, M*M) for n in range(nmax)]
def dens(cs, th):
    s = mp.sin(th); return sum(c*mp.sin((n+1)*th)/s for n, c in enumerate(cs))
ths = [mp.pi*k/41 for k in range(1, 41)]
for b in (4, 8):
    nmax = int(12*mp.sqrt(b))+30
    print(f"b={b}, nmax={nmax}")
    for L in (2,):
        prev = None; last = None
        for N in range(0, 6):
            M = L**N; cs = coeffs(M, b, nmax); f = [dens(cs, t) for t in ths]
            if min(f) <= 0: print("  nonpositive", M); break
            if prev is not None:
                osc = max(abs(mp.log(a) - mp.log(p)) for a, p in zip(f, prev))
                print(f"  L={L} N={N} M={M:3d}  sup|dlog f| = {mp.nstr(osc,5)}" + (f"  ratio={mp.nstr(last/osc,5)}" if last else ""), flush=True)
                last = osc
            prev = f
