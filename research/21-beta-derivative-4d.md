# The β-derivative bound H4D-3 in four dimensions

Status, item by item:

- **Proved here.**
  - Prop. 1, the exact identity: ∂_β of a normalized physical terminal
    expectation is a terminal covariance with the transported tangent. This
    holds in any dimension, for the physical law, with no R.
  - Lemma 2, uniform flow sensitivity: 1/2 <= ∂x_K/∂x_0 <= 2 for Balaban's
    coupling recursion, under explicit derivative hypotheses.
  - Prop. 3: the derivative hypothesis cannot be weakened to O(g²) without
    autonomy. There is an explicit counterexample with power-law growth.
  - Prop. 4, the conditional H4D-3 for Balaban's R-modified densities.
  - Prop. 5, the exact place where R enters: one extra term, ∂_β log h,
    which an analytic-in-β version of the R-bias bound controls.
- **Computation.** `research/scripts/t12_flow_sensitivity.py`.
- **Open.** Hypotheses F3, E-β and Rβ are not published. Balaban's Theorem 2
  (CMP 109, the coupling-flow bound (0.31)) is unpublished. **H4D-3 is not
  proved.**

Context (see the correction in research/18 §9a: in 4D the split must be done at fixed terminal coupling, where ∂_βΦ enters multiplied by an O(1) compensating rate c'(s), so a uniform bound on it is still exactly what is needed): research/18 Thm. 5 splits the 4D adjacent-depth comparison into:

- H4D-3, the uniform β-derivative bound (this note);
- H4D-0, summable coupling matching;
- tangent decay of the irrelevant part together with the R-bias.

## 1. Exact identity (proved)

At depth N, let μ_{N,β} be the Wilson measure on Λ_N with dimensionless
inverse coupling β, b_N the exact N-fold block map, ν_{N,β} = (b_N)_*μ_{N,β}
the **physical** terminal law, and Φ_N(z;β) = ν_{N,β}(e^{z·F}) for bounded
terminal tests.

**Proposition 1.** With τ_N := E_{μ_{N,β}}[-A_N | b_N] (the transported
tangent),

    ∂_β Φ_N = -Cov_{μ_N}(e^{z·F}∘b_N, A_N) = Cov_{ν_N}(e^{z·F}, τ_N),
    |∂_β Φ_N| <= 2 e^{S_ρ} inf_c ν_N|τ_N - c| <= e^{S_ρ} osc τ_N.

*Proof.* Differentiate the normalized integral; A_N is bounded at fixed N.
Then apply the tower property. The bounds follow from
|Cov(f, τ)| = |E[(f - Ef)(τ - c)]| <= 2 sup|f| E|τ - c|. ∎

This uses only exact T-transport of a fine-scale function (research/14
Prop. 1). In 3D that is the whole story. In 4D, Balaban's estimates are not
for ν_N but for R-modified densities (research/09 §1). That gap is
Proposition 5.

## 2. Flow sensitivity (proved, conditional on the recursion's structure)

CMP 109 (0.18), (0.20) defines the effective couplings by

    x_{k+1} = x_k + β_{k+1}(g_0, ..., g_k),   x_k = 1/g_k²,   k = 0 (finest), ..., K (terminal).

CMP 109 p. 267 says the β_j can be taken analytic in the effective couplings.
Write β_{k+1} = -a - r_{k+1}(x_0, ..., x_k), with a > 0 the one-loop constant
(∝ b_0 log L; it is coupling-independent).

**Hypotheses.**

- **(F2)** |r_{k+1}| <= a/2.
- **(F3)** |∂r_{k+1}/∂x_j| <= C θ^{k-j}/(x_j x_k) for j <= k, with θ < 1.

(F3) says two things. The coupling-derivative of the β-function is
O(g_j² g_k²), which is two-loop order. The memory of earlier scales decays
geometrically.

**Lemma 2.** Under (F2)-(F3), set c_* = C/(1-θ) and
S = c_*(x_K^{-2} + 2/(a x_K)). Then

    |∂x_K/∂x_0 - 1| <= e^S - 1.

In particular 1/2 <= ∂x_K/∂x_0 <= 2 once S <= 0.4. This holds when the
terminal coupling g_K² = 1/x_K is small, which is Balaban's regime g_k <= γ.
The bound is uniform in K, i.e. in the cutoff.

*Proof.* By (F2), x_k - x_{k+1} = a + r_{k+1} >= a/2, so x is decreasing in
k and x_k >= x_K + (a/2)(K-k). Let J_k = ∂x_k/∂x_0. Then J_0 = 1 and

    J_{k+1} = J_k - Σ_{j<=k} (∂r_{k+1}/∂x_j) J_j.

Set J*_k = max_{j<=k}|J_j|. Since x_j >= x_k for j <= k, (F3) gives
|J_{k+1} - J_k| <= c_k J*_k with c_k = c_* x_k^{-2}. Hence
J*_K <= Π_k (1 + c_k) and

    |J_K - 1| <= Σ_k c_k Π_{i<k}(1 + c_i) = Π_k(1 + c_k) - 1 <= e^{Σ c_k} - 1.

Finally, Σ_k x_k^{-2} <= Σ_{m>=0} (x_K + a m/2)^{-2}
<= x_K^{-2} + ∫_0^∞ (x_K + a t/2)^{-2} dt = x_K^{-2} + 2/(a x_K). ∎

*Source of (F3).* Suppose r_{k+1} = Σ_{j<=k} s_{k+1,j}, where s_{k+1,j} is
analytic in x_j on |x'_j - x_j| <= x_j/2 and bounded there by
(C/2)θ^{k-j}/x_k. Then Cauchy's estimate gives (F3). This is the natural
analytic form of "the step-j contribution to the β-function is O(g_k²) and
decays like θ^{k-j}". CMP 109 states analyticity of β_j and defers the
perturbative bounds, including (0.31), to an unpublished paper. So (F3) is a
**hypothesis** here.

## 3. Necessity of the two-loop structure (counterexample; proved)

**Proposition 3.** Lemma 2 fails if (F3) is weakened to |∂r_{k+1}/∂x_k| =
O(1/x_k), i.e. O(g²), for a scale-dependent r. Let x̄ be any reference
trajectory with x̄_k - x̄_{k+1} ∈ [a/2, 2a], and set
r_{k+1}(x) = r̄_{k+1} + c(x - x̄_k)/x̄_k. Then r_{k+1} agrees with r̄_{k+1}
on x̄, so the flow is unchanged and (F2) holds near x̄. But
∂x_K/∂x_0 = Π_k(1 - c/x̄_k + O(x̄_k^{-2})). This behaves like K^{-c/(2a)}
or faster, so it tends to 0 for c > 0 and to ∞ for c < 0.

*Proof.* x̄_k <= x̄_K + 2a(K-k), so Σ_k 1/x̄_k >= (1/2a) log(1 + 2aK/x̄_K).
Exponentiate. ∎

For an **autonomous** bounded correction r(x), the sum Σ r'(x_k) is close to
(1/a)∫r' dx, which is bounded, so even an O(1/x) derivative does no harm.
Uniformity can fail only through scale dependence of the correction: memory
of earlier steps, or finite-lattice effects. That is exactly what the θ^{k-j}
factor in (F3) controls.

**Computation** (`t12_flow_sensitivity.py`, SU(2) one- and two-loop
coefficients, L = 3, g_K² = 0.5):

- With the autonomous two-loop correction, J_K = 1.0063, 1.0158, 1.0187,
  1.0190, 1.0191 for K = 10 to 10^5. It converges.
- With the non-autonomous O(g²) correction (c = ∓0.05), J_K grows or decays
  by a factor ≈ 3.08 per decade of K, matching 10^{|c|/a} = 3.09.

## 4. Conditional H4D-3 for Balaban's R-modified densities

Balaban's terminal density (CMP 109 (0.22)-(0.28), CMP 119 (2.23)-(2.31)) has
the form

    ρ_K^R(V) = exp(-x_K A(U_K(V)) - Σ_X E_K(X; V) - Σ_X R_K(X; V) - Σ_X B_K(X; V)) × (large-field factors).

The terms depend on the couplings x_0, ..., x_K. CMP 119 p. 392 bounds the
marginal terms produced at step j by O(1)(L^jη)^4 g_j^{n} e^{-κd(X)}, where
η = L^{-K} at the terminal scale. They therefore decay like L^{-4(K-j)}.

**Hypothesis E-β.** Each step-j contribution to E_K, R_K, B_K is analytic in
x_j on |x'_j - x_j| <= x_j/2 and obeys the published bound there. On the
terminal lattice that bound is C L^{-δ(K-j)} e^{-κd(X)} per localization
domain, with δ > 0.

**Proposition 4.** Assume (F2), (F3), E-β, and the terminal small-field set
S (note 17). Then, uniformly in K,

    sup_{V∈S} |∂_{x_0} log ρ_K^R(V) + J_K A(U_K(V))| <= C n0^4 Σ_j J*_j L^{-δ(K-j)}/x_j <= C'/x_K,

and on S the terminal tangent is -J_K A(U_K(V)) + O(1/x_K), with
1/2 <= J_K <= 2.

*Proof.* Use the chain rule through x_j = x_j(x_0). The step-j term's
derivative in x_j is at most its bound divided by x_j/2 (Cauchy). Multiply by
|∂x_j/∂x_0| <= J*_j <= 2 (Lemma 2) and sum the geometric series in K-j over
the O(n0^4) terminal localization domains. ∎

**Consequence.** For the R-modified terminal law ν^R_N ∝ ρ_K^R dλ,
∂_β ν^R(e^{z·F}) = Cov_{ν^R}(e^{z·F}, ∂_{x_0} log ρ_K^R). On S this is
bounded by Prop. 4. Off S it is bounded by the large-field suppression,
provided the β-derivative of the large-field factors is controlled by the
same Cauchy argument. That proviso is part of E-β. So **H4D-3 holds for ν^R
under (F2), (F3) and E-β.**

## 5. Where the R-operation enters (exact; proved)

Let h_β = dν_{N,β}/dν^R_{N,β} be the R-bias density. This is the object that
notes 11-13 and 16 bound through H6-H8.

**Proposition 5.** With unnormalized densities,

    ∂_β Φ_N = Cov_{ν_N}(e^{z·F}, ∂_β log ρ_K^R + ∂_β log h_β).

The R-operation therefore enters H4D-3 **only** through ∂_β log h_β. If the
R-bias bound holds analytically in β, then Cauchy gives
osc ∂_β log h <= 2η/(c β) and

    |∂_β Φ_N - Cov_{ν_N}(e^{z·F}, ∂_β log ρ_K^R)| <= 2 e^{S_ρ} η/(c β),

which is even small, since β ~ b_0 log ε^{-1}. The analytic R-bias bound
needed is:

**Hypothesis Rβ.** |log h_{β'}| <= η uniformly for complex β' with
|β' - β| <= cβ.

*Proof.* log(dν/dλ) = log ρ_K^R + log h - log Z. Differentiate the normalized
integral, then apply Cauchy on the disc of radius cβ. ∎

What this shows:

- A real-β bound on the R-bias (H6-H8) is **not enough** for H4D-3. Its
  β-derivative is needed too. An analytic-in-coupling version of H6-H8 gives
  that for free.
- This matches how Balaban builds R (CMP 109 p. 267 already prefers the
  χ-convention that makes everything analytic in the couplings).

## 6. Summary for the 4D programme

    H4D-3  <=  (F2) + (F3) [two-loop-order, memory-decaying β-function derivatives]
             + E-β [analyticity of each step's effective-action terms in its coupling]
             + Rβ  [R-bias bound analytic in β].

None of the four inputs is published. (F2) is a consequence of the unpublished
CMP 109 Theorem 2. The others are natural analytic strengthenings of bounds
that Balaban states for real couplings. The new information is:

- the uniformity mechanism: the one-loop coefficient is coupling-independent,
  and the remainder's coupling-derivative is O(g⁴) with scale-memory decay;
- that mechanism's sharpness (Prop. 3);
- the exact single term through which R enters (Prop. 5).

**Next concrete step.** Verify (F3) at one loop for the actual CMP 109
β-function: compute the one-step β_{k+1} of the Gaussian-plus-one-loop
approximation with Balaban's block average, and its dependence on the
earlier x_j through the background minimizer. This is a finite lattice
computation, the 4D analogue of research/18 §8(c). After T8 (research/19)
it is the natural next computation.
