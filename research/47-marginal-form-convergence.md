# Depth convergence of the marginal form: the block-flux covariance converges geometrically

Status: **proved** (T41), abelian 4D, Balaban's linear block flux (note 19).
Rate data: `research/scripts/t41_covariance_convergence.py` (output `.out`).

## Statement

Let C^{(M)}(K) be the 6×6 terminal block-flux covariance at coarse momentum
K and block size M (note 19 (2.5), β = 1). Its inverse, restricted to the
exact subspace, is the symbol of the minimal-energy (marginal) quadratic
form S at depth m (M = L^m; notes 36 §3, 46).

**Theorem 1.** There is a continuum symbol C^∞(K) such that, uniformly in
K, in a fixed phase convention,

    ||C^{(M)}(K) - C^∞(K)|| <= C (1 + log M)/M.

Consequently ||C^{(L^m)} - C^{(L^{m+1})}|| <= C' m L^{-m}. The same holds for
the inverses on the exact subspace, since their eigenvalues there are
bounded below uniformly in M (§3). So the marginal form converges
geometrically in the depth.

This is the quadratic-form part of (O2) in note 41, for the free
(marginal) structure, which includes the lattice Laplacian through the
projector P_2. The measured rate (below) is faster, about M^{-2}.

## Proof

1. *Alias sum.* With p_n = (K + 2πn)/M, n ∈ B_M := (-M/2, M/2]^4 ∩ Z^4,
   and K_j ∈ (-π, π]:

       C^{(M)}_{ab}(K) = Σ_{n ∈ B_M} P_{ab}(p_n) ω^{(M)}_{ab}(n),
       ω^{(M)}_{ab} = M^{-4} conj(w_a(p_n)) w_b(p_n),

   with w_a = M^{-4} Π_j D_M(p_j) · D_M(p_μ) D_M(p_ν) for a = (μν).
2. *Dirichlet factors.* Since M p_n = K + 2πn,
   D_M(p) = e^{-iK/2} e^{ip/2} sin(K/2)/sin(p/2). So
   |D_M(p_n)|/M = δ_M(n) := |sin(K/2)|/(M |sin x_n|), with
   x_n = (K + 2πn)/(2M) ∈ (-π/2, π/2]. The only other n-dependence is the
   phase e^{ip/2}.
3. *Continuum weights.* Put δ_∞(n) := |sin(K/2)|/(M|x_n|) = 2|sin(K/2)|/|K + 2πn|,
   which does not depend on M. On |x| <= π/2,
   0 <= 1/sin²x - 1/x² <= 1 - 4/π² < 1, so |δ_M² - δ_∞²| <= sin²(K/2)/M².
   Summing over the M values of n_j gives
   Σ_{n_j ∈ B} |δ_M² - δ_∞²| <= 1/M. The tail obeys
   Σ_{|n_j| > M/2} δ_∞² <= Σ_{|n|>M/2} 4/(π²(2|n|-1)²) <= C/M. The δ⁴ factors
   (tent coordinates) give the better bounds C/M³.
4. *Products.* |ω^{(M)}_{ab}| <= Π_j δ_M(n_j)² × (two extra δ_M factors per
   index), and the weights are products over coordinates. By telescoping one
   coordinate at a time, using Σ_n δ_M² = Σ_n δ_∞² = 1 (Fejér / Parseval)
   for the unchanged coordinates, the total weight error is <= 4C/M.
5. *Projector and phases.* P(p) is built from r(p) = e^{ip} - 1. Write
   r_j = e^{ip_j/2} s_j with s_j = 2 sin(p_j/2) real. Then
   P(p) = Θ(p) P̃(s(p)) Θ(p)*, where Θ is a diagonal phase matrix and
   P̃(s) = R(s)R(s)^T/|s|² is the real projector. The continuum symbol uses
   P̃_∞(q) with q = K + 2πn, and no phases. Now:
   - s(p)/|s(p)| = q/|q| + O(|p|²), so |P̃(s) - P̃_∞(q)| <= C|p_n|²;
   - the phases (from Θ and from e^{ip/2} in D_M) differ from 1 by
     O(|p_n|).

   Weighted by the coordinate weights, Σ_n |p_n| W(n) <= Σ_{|n_j|<=M/2} (|n_j|/M)(1/n_j²) <= C log M/M,
   and Σ_n |p_n|² W(n) <= C/M.
6. *Limit.* C^∞(K) := Σ_{n∈Z^4} P̃_∞(K + 2πn) ω^∞(n), where ω^∞ has the
   δ_∞ weights. The sum converges absolutely, because the weights are
   products of δ_∞² ~ 1/n² over 4 coordinates. Steps 3-5 give the bound. ∎

## 2a. Measured rate

On a coarse 4⁴ momentum grid (K ≠ 0):

| M -> 2M | sup_K ||C^{(M)} - C^{(2M)}|| | ratio to previous |
|---|---|---|
| 2 -> 4 | 1.77e-1 | — |
| 4 -> 8 | 5.88e-2 | 3.00 |
| 8 -> 16 | 1.68e-2 | 3.50 |
| 16 -> 32 | 4.42e-3 | 3.81 |

The ratio per doubling rises towards 4. The true rate is close to M^{-2},
faster than the proved O(log M/M). The first-order errors of step 5 cancel
between the aliases ±n, as the remark on the exact identity
Σδ_M² = Σδ_∞² in step 4 suggests. The proved rate is enough for geometric
convergence in m.

## 3. Lower bound on the exact subspace

On the 3-dimensional range (exact 2-forms at momentum K ≠ 0), the
alias-0 term alone gives ⟨v, C^{(M)} v⟩ >= ω^{(M)}(0)·|P(p_0)v|². By the
alias-0 fraction of note 44 step 4, ω^{(M)}(0) >= c_0 > 0 uniformly in M.
And |P(p_0) v| >= c|v| for v in the exact range at the lowest alias,
uniformly in M, up to O(1/M). So λ_min >= c > 0 on the exact subspace for
large M, and the inverses converge with the same rate.

## Use

- (C) of note 22 needs geometric convergence of the free step operators
  (note 41 (O2)). For the marginal quadratic form (block-flux covariance and
  minimal energy) this is now proved, with rate O(m L^{-m}).
- What remains of (O2) is the one-loop vertex structure of the gluon and
  ghost loop at step j. The same alias-sum technique applies, but it was
  not carried out (the SU(2) vertices of note 23 §7).
