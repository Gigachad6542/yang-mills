"""T12: sensitivity J_K = d x_K / d x_0 of a discrete coupling flow
x_{k+1} = x_k - a - r(x_k),  x = 1/g^2, k = 0 (finest) .. K (terminal).
Asymptotic freedom: x decreases toward the terminal scale.
(i)  two-loop-type r = b/x      : dr/dx = -b/x^2  = O(g^4)  -> J_K bounded.
(ii) non-autonomous O(g^2)-sensitive correction -> J_K ~ K^(-c/a).
SU(2): a = 2*beta0*log L, beta0 = 22/(3*16 pi^2), b = 2*beta1/beta0... (illustrative)."""
import numpy as np
L = 3.0
beta0 = 22/(3*16*np.pi**2); beta1 = 136/(3*(16*np.pi**2)**2)
a = 2*beta0*np.log(L); b = 2*beta1*np.log(L)/ (1.0)   # two-loop term coefficient (scheme-free order of magnitude)
def run(xK, K, r, dr):
    # shoot backwards from terminal x_K to get x_0, then compute J = prod (1 - dr(x_k)) forward
    xs = [xK]
    for _ in range(K):            # invert x_{k+1} = x_k - a - r(x_k) approximately by fixed point
        y = xs[-1]; x = y + a
        for _ in range(50): x = y + a + r(x)
        xs.append(x)
    xs = xs[::-1]                 # xs[0] = x_0 (fine), xs[K] = x_K
    J = 1.0
    for k in range(K): J *= (1 - dr(xs[k]))
    return xs[0], J
gamma2 = 0.5                      # terminal g^2
print("(i) autonomous two-loop correction r = b/x (dr/dx = O(g^4))")
for K in [10, 100, 1000, 10000, 100000]:
    x0, J = run(1/gamma2, K, lambda x: b/x, lambda x: -b/x**2)
    print(f"   K={K:6d}  x_0={x0:10.3f}  J_K = {J:.6f}")
print("(ii) non-autonomous correction r_{k+1}(x) = c (x - xbar_k)/xbar_k, which vanishes on the")
print("     reference trajectory xbar (so the flow is unchanged) but has dr/dx = c/xbar_k = O(g^2)")
for c in (+0.05, -0.05):
    for K in [10, 100, 1000, 10000, 100000]:
        xbar, _ = None, None
        xs = [1/gamma2]
        for _ in range(K):
            y = xs[-1]; x = y + a
            for _ in range(50): x = y + a + b/x
            xs.append(x)
        xs = np.array(xs[::-1])
        J = np.prod(1 + b/xs[:-1]**2 - c/xs[:-1])
        print(f"   c={c:+.2f} K={K:6d}  J_K = {J:.4f}   K^(-c/a) = {K**(-c/a):.4f}")
print("(i) with autonomous bounded r: sum_k r'(x_k) ~ (1/a) int r' dx is bounded, so J_K is bounded;")
print("    an O(g^2) derivative destroys uniformity only through scale dependence (memory, lattice effects).")
