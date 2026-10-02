# Memory decay from single-step Lipschitz bounds

Status:

- **Proved here.** Theorem 1 is an abstract contraction lemma for two RG
  flows shot to the same terminal coupling. Their irrelevant data differ by
  δ_k and their couplings by Δ_k. The lemma is a forward/backward
  bootstrap in a weighted norm and needs only sup-bounds on the Lipschitz
  constants.
- **Conditional.** Corollary 2: the memory-decay hypotheses used by the
  master reduction follow from three **single-step** Lipschitz properties
  (S1)-(S3) of Balaban's RG step and small γ. These are (D) of note 22,
  (T-b) and (B-b) of note 27, and, in 3D, H3D-1 of note 18.
- **Heuristic.** Why (S2) and (S3) carry O(g_k²) is explained in §3. It is
  not proved.
- **Effect.** The "one remaining kind of theorem" of the README is reduced
  from a multi-scale statement to single-step statements about one
  fluctuation integral.

## 1. Two flows

Consider two RG flows on the same sequence of lattices, k = 0, 1, ..., K. At
scale k each carries:

- an inverse coupling x_k = g_k^{-2};
- irrelevant (small-field) effective-action data E_k, in Balaban's
  polymer representation, measured in a norm ||·||_k in which CMP 109 (0.29)
  reads ||E_k||_k <= E_0;
- large-field data R_k, measured in an analogous norm.

Write δ_k = ||E_k - E'_k||_k (and similarly for R) and Δ_k = x_k - x'_k.

## 2. Abstract contraction in shooting form (proved)

**Theorem 1.** Suppose that for 0 <= k < K:

- (i) δ_{k+1} <= θ δ_k + b_k |Δ_k|;
- (ii) |Δ_{k+1} - Δ_k| <= c_k δ_k + e_k |Δ_k|;
- (iii) Δ_K = 0 (both flows shot to the same terminal coupling).

Let b_k <= b̄, c_k <= c̄, e_k <= ē, and fix θ_1 with θ < θ_1 < 1 such that

    ē < 1 - θ_1,   b̄ c̄ <= ½ (θ_1 - θ)(1 - θ_1 - ē).   (2.1)

Then, for all k <= K,

    δ_k <= 2 θ_1^k δ_0,   |Δ_k| <= (2c̄/(1 - θ_1 - ē)) θ_1^k δ_0.   (2.2)

The constants do not depend on K. No summability of b_k, c_k or e_k is
needed. This matters in 4D, where g_k² ~ 1/k.

*Proof.* Put ||δ|| := max_k δ_k θ_1^{-k} and ||Δ|| := max_k |Δ_k| θ_1^{-k};
both are finite for a finite chain.

1. *Forward.* Iterating (i),
   δ_k <= θ^k δ_0 + Σ_{i<k} θ^{k-1-i} b_i |Δ_i|
   <= θ_1^k [δ_0 + b̄ ||Δ|| Σ_{i<k} θ^{k-1-i} θ_1^{i-k}]
   <= θ_1^k [δ_0 + b̄ ||Δ||/(θ_1 - θ)].
   So ||δ|| <= δ_0 + b̄||Δ||/(θ_1 - θ).
2. *Backward.* By (iii), Δ_k = -Σ_{i=k}^{K-1}(Δ_{i+1} - Δ_i), so by (ii)
   |Δ_k| <= Σ_{i>=k} (c̄||δ|| + ē||Δ||) θ_1^i <= (c̄||δ|| + ē||Δ||) θ_1^k/(1 - θ_1).
   Hence ||Δ|| <= c̄||δ||/(1 - θ_1 - ē).
3. *Combine.* ||δ|| <= δ_0 + [b̄c̄/((θ_1 - θ)(1 - θ_1 - ē))] ||δ|| <= δ_0 + ½||δ||
   by (2.1). So ||δ|| <= 2δ_0, and the bound on ||Δ|| follows. ∎

**Application.** The two flows are depth N+1 (started after its first step)
and depth N, on the same lattices, both shot to terminal coupling g. Then
δ_0 = O(E_0) is the irrelevant part of the one-step defect (Balaban's step-1
output, so admissible), and (2.2) gives δ_K <= 2θ_1^K δ_0: geometric memory
decay (T-b) of note 27 at rate θ_1. The same bound gives |Δ_k| = O(θ_1^k),
i.e. the coupling histories of the two depths agree up to O(θ_1^k), which is
the input used in note 27 (T-b) and the content of (D) in note 22.

## 3. The single-step hypotheses

- **(S1) Transport contraction.** Re-expressing the scale-k irrelevant data
  at scale k+1 (pull-back by the minimal configuration, with no new
  integration) is linear and contracts the irrelevant norm by θ_0 = L^{-α}.
  This is the structure behind the factor (L^jη)^{4+α} in CMP 109 (0.29):
  per scale-(k+1) cell, the bound improves by L^{-α}. For differences of
  data the statement is the same, since the map is linear.
- **(S2) Generation Lipschitz.** The new irrelevant terms produced by the
  (k+1)-st fluctuation integral depend on the input data with Lipschitz
  constant a_k <= C g_k² in the irrelevant norm, and on the input coupling
  with constant b_k <= C g_k².
  *Heuristic.* An input term E(X, U_k) enters the fluctuation integral as
  E(X, U_k(V) e^{i g_k B}). The B-independent part is pure transport (S1).
  The B-dependent part has derivatives in B carrying a factor g_k (chain
  rule on the analytic domain of CMP 109 (1.18)), and after integration it
  produces terms of order g_k² times second derivatives.
- **(S3) β-function Lipschitz.** The coupling increment depends on the input
  irrelevant data with constant c_k <= C g_k² and on the input coupling with
  e_k <= C g_k⁴. The second is the two-loop structure of note 21 (F3).

For SU(2) in 4D under H0, g_k² <= γ², so b̄, c̄ <= Cγ² and ē <= Cγ⁴, while
θ = L^{-α} + Cγ². Condition (2.1) holds for small γ: b̄c̄ = O(γ⁴) against
(θ_1 - θ)(1 - θ_1 - ē) of order one, for example θ_1 = (1 + L^{-α})/2.

**Corollary 2.** Assume H0 with shooting, (S1)-(S3), and γ small enough
that θ := L^{-α} + Cγ² < θ_1 < 1 and (2.1) holds. Then:

- (T-b) of note 27 holds with rate θ_1;
- (D) of note 22 holds;
- in 3D, where every coupling g_k² = g² L^k ε is explicit and identical
  across depths (Δ_k = 0) and g_k -> 0 at fine scales, H3D-2 and hence
  P4-3D hold via note 18 Thm. 1, with σ = α minus logarithmic losses.

The large-field analogues (B-b), with R-data in place of E-data, follow
under the same single-step hypotheses for the R-operation step. The extra
factor g_k^{κ_0} on R-terms (CMP 119 (2.31)) only helps.

## 4. What this changes

The programme's remaining core was stated as a multi-scale theorem: "the
flow contracts fine-scale defects in irrelevant directions". Theorem 1
reduces it to (S1)-(S3). Each is a property of a **single** fluctuation
integral at weak coupling: transport of existing irrelevant terms, and the
O(g²) dependence of newly generated terms and of the β-function on the input
data. These are the natural Lipschitz (difference) versions of the bounds
Balaban already proves for each step (CMP 109 Thm. 3, CMP 119, CMP 122). Of
the three, (S2) is the substantive one. A route: Cauchy estimates in an
auxiliary complex parameter s multiplying the input data's B-dependent
part, applied inside Balaban's convergent cluster expansion of one step.
That needs a margin in his admissibility constants, so that s ranges over a
fixed complex disc.
