# H7 absorbed: rough-then-contract and large-field persistence

Status, item by item:

- **Proved here.**
  - Lemma 1: a relative gauge lemma.
  - Lemma 2: a rough-then-contract oscillation bound valid for **every**
    fiber configuration. It needs no branch-gap or fine-level regular event.
  - Prop. 3: an exact decomposition of each R'-label's terminal bias into
    (i) squared terms and (ii) first-order mean shifts, both evaluated at
    the coarse level where the true configuration's image first becomes
    small-field.
- **Conditional.** Cor. 4: the squared part is summable under a
  large-field persistence bound (P) on Balaban's unnormalized history masses.
- **Consequence.** H7_Σ is no longer a separate obligation. The complete
  R-bias reduces to (P), the component counting of note 11 (3.11), and a
  generalized H8_Σ (first-order mean shifts, now indexed also by the
  persistence length).
- **Open.** (P) and generalized H8_Σ.

Inputs: note 15 Prop. 1 (the rough step, valid for arbitrary fields);
note 24 Thm. 1 (curved contraction θ <= L^{1-d} + c_{d,L}κ); note 20 Thm. 2
(the actual R'-template has equal fixed-exterior fiber mass, and by CMP 122 I
(1.101) it is supported on small fields, ϑ(plaquettes) <= ε_k on Λ_i).

## 1. Setting

Fix an R'-label λ at fine level m (depth m below the terminal scale) with
fiber variables W on Λ and fixed exterior V_c. The true and template
conditional laws are p̂ and q̂, with equal fiber mass C_λ(V_c) (note 20).
For a fiber configuration W, write U_j(W) for its image at level j, where
j = m, ..., 0 counts the remaining block steps (U_m = (W, V_c), U_0 =
terminal field). S_j(W, W') is the set of level-j bonds where U_j(W) and
U_j(W') differ. It lies within C_d L of the image of Λ (block locality of
(0.4)).

**Small-field at level j near a set.** Every plaquette within distance R of
the set has ϑ <= κ_1. Exterior hypothesis (from Balaban's localization:
components X_i are separated by small-field buffers): V_c is small-field on
a neighborhood of Λ at every level of the history up to the scale of λ.

## 2. Two lemmas

**Lemma 1 (relative gauge).** Let U, U' be configurations at one level that
agree outside a set S, both small-field (plaquette ϑ <= κ_1) on the box N of
side R ⊃ S, with S at distance >= 1 from ∂N. Then there is a gauge
transformation u, equal to 1 outside N, such that
max_b ϑ(U^u_b{}^{-1} U'_b) <= 2(d-1)R²κ_1.

*Proof.*

1. Take complete axial gauges g, g' on N for U, U', with the same tree
   rooted at a corner x_0 of N outside S. By note 24 Lemma B, all links of
   U^g and U'^{g'} on N have ϑ <= (d-1)Rκ_1.
2. Put u = g g'^{-1} on N and u = 1 outside. For b ⊂ N, U^u_b and U'_b are
   simultaneous conjugates of U^g_b and U'^{g'}_b, so their distance is at
   most 2(d-1)Rκ_1.
3. For x ∈ N, u(x) = hol_U(τ_x) hol_{U'}(τ_x)^{-1}, where τ_x is the tree
   path. Pick a path σ_x from x_0 to x that avoids S. Since U and U' agree
   off S, this equals a conjugate of hol_U(ℓ) hol_{U'}(ℓ)^{-1}, with
   ℓ = σ_x^{-1}τ_x a loop in N of area <= (d-1)R². Each loop holonomy has
   ϑ <= (d-1)R²κ_1 by the lasso argument.
4. So ϑ(u(x)) <= 2(d-1)R²κ_1. On bonds crossing ∂N (u = 1 outside, and U, U'
   agree there) the distance is ϑ(u(x)) <= 2(d-1)R²κ_1. Inside N it is at
   most 2(d-1)Rκ_1 by step 2. (The earlier draft bound 4(d-1)Rκ_1 assumed
   boundary loops of area O(R); a minimal surface between the tree path and
   a boundary path can have area of order R², so the safe bound is used.) ∎

**Lemma 2 (rough-then-contract).** Let F be a gauge-invariant terminal test
whose differential is bounded by C_F in the dual sup norm. For two fiber
configurations W, W', suppose there is a level j such that:

- U_j(W) and U_j(W') are both small-field with κ_1 near S_j (box side R_j);
- every later level j' < j is small-field with curvature <= κ_* on the
  transport neighborhoods along the interpolation below;
- κ_1(1 + 8(d-1)R_j²) <= κ_*.

Then

    |F(Φ(W)) - F(Φ(W'))| <= C_F θ^{j} · 2(d-1)R_j² κ_1 |N_j|,   θ := L^{1-d} + c_{d,L}κ_*.   (2.1)

*Proof.* Apply Lemma 1 at level j. F∘Φ is gauge invariant, and gauge
transformations at level j act on coarser levels by the restricted gauge
(note 24 Lemma A). Join U_j(W)^u to U_j(W') by the bondwise geodesic. Its
ℓ¹ length is <= 2(d-1)R_j²κ_1|N_j|. Along it plaquette angles change by at
most 4 times the link change, so they stay <= κ_*. Pull back the terminal
differential through the remaining j levels with note 24 Thm. 1 and note 12
Lemma 2, then use ℓ^∞-ℓ¹ duality. ∎

Lemma 2 needs **no** regularity at levels m, ..., j+1. Large fields at the
fine level and at the first few coarser levels are allowed. Only the first
small-field level matters, and every level's rough step is note 15 Prop. 1,
which holds for arbitrary fields.

## 3. Decomposition of one label's bias

For W in the fiber, let the **persistence** t(W) ∈ {0, ..., m} be the
smallest t such that U_{m-t}(W) is small-field (κ_1) near S_{m-t}(W, W_ref),
with W_ref a fixed template reference such as the template minimizer. The
template is small-field at the fine level (CMP 122 I (1.101)) and so at every
coarser level, since averages of small fields are small with κ_1 <= C ε_k.
Hence t = 0 q̂-almost surely.

**Proposition 3.** Write j = m - t(W), let δU_j(W) be the gauge-fixed
level-j difference from Lemma 1, and let J_j be the pulled-back terminal
current at level j (conserved, ||J_j||_∞ <= C_F θ^{j}). Then

    E_q̂F - E_p̂F = Σ_{t=0}^{m} [ E_q̂(⟨J_{m-t}, δU_{m-t}⟩; t) - E_p̂(⟨J_{m-t}, δU_{m-t}⟩; t) ] + R_λ,
    |R_λ| <= C_F Σ_t θ^{2(m-t)} [E_q̂(|δU|_1²; t) + E_p̂(|δU|_1²; t)].   (3.1)

The first sum consists of **first-order mean shifts at the persistence
level** (generalized H8). R_λ is quadratic (H6-type). Each quantity has
||δU_{m-t}||_∞ <= 2(d-1)R²κ_1.

*Proof.* For each W, Taylor-expand F∘Φ along the interpolation of Lemma 2
from the reference image, at the level j(W). The first-order term is
⟨J_j, δU_j⟩, up to a pure-gauge part annihilated by conservation, whose
second-order error is included in the remainder. The remainder is
quadratic in the level-j displacement, with the contracted second
differential bounded through note 24 Thm. 1. Integrate against p̂ and q̂,
splitting by t. ∎

## 4. Summability of the quadratic part under persistence

**Hypothesis (P) (marked large-field persistence; open).** For the
unnormalized label masses, M_{m,t} := Σ over placements per terminal block
of ∫ν(dV_c) C_λ(V_c) p̂(t(W) = t | V_c) satisfies

    M_{m,t} <= C w_m L^{4m} e^{-a t},   with e^{-a} L^{4} <= L^{-δ_1}, δ_1 > 0.   (4.1)

That is, a large field whose image persists through t more levels costs
e^{-a} per level. The condition L^4 e^{-a} < 1 says this cost beats the loss
L^{4+2δ} per level in the squared contraction relative to L^{2δ}. Balaban's
history expansion assigns exp(-c p(g_{k'})²) to each large-field region at
every scale k' (CMP 122 I (0.1); CMP 122 II), so the natural rate is
a ≈ c p(γ)², and (4.1) asks c p(γ)² > 4 log L. That is a smallness
condition on γ, which is Balaban's regime. What is not published is the
**marked** form: the bound for the sequential telescope's labels, with
persistence recorded.

**Corollary 4.** Under (P) and the component counting of note 11 (3.11),

    Σ_m Σ_λ ∫ν C_λ |R_λ| <= C Σ_m w_m Σ_t L^{4m} e^{-a t} L^{-(4+2δ)(m-t)} (R² κ_1|N|)² < ∞.

*Proof.* Insert θ^{2(m-t)} <= L^{-(4+2δ)(m-t)} (note 24 Cor. 2) and (4.1).
The t-sum equals Σ_t L^{-2δ(m-t)} (L^4 e^{-a})^t
<= Σ_t L^{-2δ(m-t)} L^{-δ_1 t} <= C', uniformly in m. Finally Σ_m w_m < ∞. ∎

## 5. What changed

| Item | Before | After |
|---|---|---|
| H7_Σ (normalized irregular tail) | separate open obligation (notes 11, 16) | absorbed: irregular fibers contribute through first-order terms at the persistence level plus summable squares |
| fine-level branch-gap event | needed for H6 path bound (note 15 Prop. 4) | not needed (Lemma 2) |
| R-bias obligations | H6 + H7 + H8 | (P) + counting + generalized H8 |

Generalized H8_Σ is the remaining core:

    Σ_m Σ_t | Σ_λ ∫ν C_λ [E_q̂(⟨J_{m-t}, δU_{m-t}⟩; t) - E_p̂(⟨J_{m-t}, δU_{m-t}⟩; t)] | < ∞,

with the λ-sum inside the absolute value. Crude bounds give
M_{m,t} θ^{m-t} <= C w_m L^{4m} e^{-at} L^{-(2+δ)(m-t)}. At t = 0 this is
w_m L^{(2-δ)m}, which is not summable.
A gain of L^{-(1+δ')(m-t)} from cancellation is required. Note 11 §6
(color invariance at flat exterior), note 13 (the covariance form) and T8
(Gaussian power counting for local even defects) are the inputs aimed at it.

**Gaussian evidence (research/19, T8).** In the 4D Gaussian model, the
exterior-averaged response of a terminal loop to a rooted even defect at
depth m is exactly of order L^{-4m}. The fixed bounded-exterior response is
L^{-2m}. Since (19 (3.8)) the L^{4m} placements of a rooted F² defect sum to
O(1) per scale, the **exterior-averaged** first-order term costs O(w_m) per
scale. With Σ_m w_m < ∞ it is summable. So in the Gaussian model the
generalized H8_Σ holds in its averaged (λ-sum inside, exterior-averaged)
form and fails in pointwise form. This is consistent with note 13's
covariance formulation. The interacting version needs the averaged
covariance bound with Balaban's activities. That is the precise remaining
target.
