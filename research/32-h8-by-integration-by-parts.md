# Generalized averaged H8 as a decorrelation estimate (integration by parts)

Status:

- **Proved here.**
  - Prop. 1: an integration-by-parts identity on the exterior configuration
    space.
  - Lemma 2: a bounded local right inverse of the linearized block map on
    exterior bonds.
  - Theorem 3: each first-order R-bias term of note 25, Prop. 3, equals
    minus the label mass times a **covariance** between the terminal test,
    evaluated with the reference fiber, and an explicit local function h_λ
    of the exterior field.
  - Corollary 4: only the gauge-averaged part of h_λ contributes.
- **Reduction.** Generalized averaged H8_Σ (note 25 §5) is implied by a
  rooted decorrelation bound (H-dec) for local gauge-invariant functions.
  That is the same kind of estimate as the irrelevant-part decay in P4, and
  it holds at the Gaussian level with the rate L^{-4m} (note 19).
- **Open.** (H-dec) for Balaban's label measures.

## 1. Setting

Fix an R'-label λ at fine level k (depth m), with fiber variables W on Λ
and exterior variables V_c. Note 20 gives the label's exterior measure

    π_λ(dV_c) = C_λ(V_c) ν_λ(dV_c) = p_λ(V_c) dV_c   (Haar on exterior links),

with p_λ smooth and positive on its support (the small-field part of a
Balaban density, analytic in the fields). Write m_λ = π_λ(1) and
π̂_λ = π_λ/m_λ.

From note 25 Prop. 3, the first-order term at persistence level j = m - t is

    T_λ = ∫ π_λ(dV_c) ⟨J_j(V_c), Δm(V_c)⟩,   J_j = ∇_{U_j} G(U_j^{ref}(V_c)),
    Δm(V_c) = E_q̂[δU_j | V_c] - E_p̂[δU_j | V_c].

Here G = F∘Φ_{j->0} is the terminal test as a function of the level-j
configuration, and U_j^{ref}(V_c) = Q^{(m-j)}(W_ref, V_c) is the level-j
image of the reference fiber and the exterior.

## 2. Two lemmas

**Proposition 1 (integration by parts).** Let ξ = Σ_b c_b(V) X_b be a
smooth vector field on the exterior configuration space, where X_b are the
right-invariant generators on link b and c_b are smooth functions supported
in a fixed finite set of links. For smooth Ψ and smooth positive density p,

    ∫ (L_ξ Ψ) p dV = -∫ Ψ (div ξ + L_ξ log p) p dV,   div ξ = Σ_b X_b c_b,

and ∫ (div ξ + L_ξ log p) p dV = 0.

*Proof.* Each X_b is divergence-free with respect to Haar measure (it
generates a measure-preserving flow on the compact group). Integrate
L_ξ(Ψ p) = (L_ξ Ψ)p + Ψ(L_ξ p) and use ∫ X_b(c_b Ψ p) dV = 0. The second
statement is the case Ψ = 1. ∎

**Lemma 2 (local right inverse).** Let D := D_{V_c}U_j^{ref} be the
derivative of the level-j image with respect to the exterior links. It acts
on exterior links within distance C L^{m-j} of Λ, and maps onto the level-j
coarse bonds within distance 1 of the image of Λ. Assume Λ leaves in each
relevant block an exterior set containing a full translated segment family
(true when Λ is small relative to the level-(k+1) blocks), and assume the
background curvature is <= κ_* (note 24). Then D is surjective onto those
coarse bonds, and it has a right inverse R with ||R||_{∞->∞} <= C_R^{m-j}.

*Proof.*

1. *Flat, one level.* The segment part S of note 15 (3.2) restricted to
   exterior segment bonds is onto each coarse bond. Moving every exterior
   bond of the L^d translated segments of c by the same Lie-algebra vector
   moves Q_lin(c) by a fixed positive fraction of it. The radial parts shift
   neighboring coarse bonds by bounded amounts. Solve the resulting finite,
   block-local linear system by least norm; its norm depends only on (d, L)
   and the finitely many local geometries.
2. *Curved background.* Perturb the flat case using note 24 Lemma E: ||D - D_1|| = O(Lr).
3. *Several levels.* Compose the m - j one-level right inverses. ∎

## 3. The identity

**Theorem 3.** Under Lemma 2 put ξ_λ := R Δm, so that D ξ_λ = Δm, and

    h_λ := div ξ_λ + L_{ξ_λ} log p_λ.

Then

    T_λ = -m_λ Cov_{π̂_λ}(G∘U_j^{ref}, h_λ).   (3.1)

*Proof.* By the chain rule,
⟨J_j, Δm⟩ = ⟨∇G(U_j^{ref}), D ξ_λ⟩ = L_{ξ_λ}(G∘U_j^{ref}). Apply Prop. 1
with Ψ = G∘U_j^{ref} and p = p_λ. Since ∫ h_λ dπ_λ = 0, the result is a
covariance. ∎

**Corollary 4 (gauge averaging).** G∘U_j^{ref} is gauge invariant under
exterior gauge transformations that fix the fiber reference. So in (3.1)
h_λ may be replaced by its average over those gauge transformations, which
is a gauge-invariant local function of the exterior near Λ.

*Proof.* Cov(Ψ, h) = Cov(Ψ, E_gauge h) when Ψ is gauge invariant and π̂_λ
is gauge invariant (Balaban's densities are, CMP 109 (1.19)). ∎

**Sizes.**

- ξ_λ is supported within C L^{m-j} of Λ, with |ξ_λ|_∞ <= C_R^t |Δm|_∞,
  where |Δm|_∞ = O(1) (fiber means of the first regular image).
- On small fields log p_λ = -g_k^{-2}A + (analytic terms), so
  |L_ξ log p_λ| <= C|ξ| (|∇A|/g_k² + C), and |∇A| ~ g_k on typical fields.
- So ||h_λ|| = O(C_R^t |Λ|_{eff}/g_k) on the label's support.

## 4. Reduction of generalized averaged H8

**Hypothesis (H-dec), rooted decorrelation.** For gauge-invariant local
functions h of the scale-k exterior, supported near a placement at depth m,
and the terminal tests G above,

    |Cov_{π̂_λ}(G∘U^{ref}, h)| <= C_G L^{-4m} ||h||,

uniformly in labels λ. This is the T8 mechanism: a rooted even
(dimension-4) defect gives L^{-4m}, and the gauge-invariant local functions
of lowest nontrivial dimension in 4D are dimension 4.

**Corollary 5.** Under (H-dec), (P) of note 26 and component counting,

    Σ_λ |T_λ| <= C_G Σ_m Σ_t L^{4m} · (w_m e^{-at}) · L^{-4(m-t)} · C_R^t/g_{k(m)}
              <= C Σ_m (w_m/g_m) Σ_t (L^4 C_R e^{-a})^t < ∞

for small γ (L⁴C_R e^{-a} < 1, and w_m/g_m is still summable since g_m^{-1}
grows only like √m). This is generalized averaged H8_Σ.

*Proof.* Use Theorem 3 with Corollary 4, insert (H-dec) at depth m - t
(the level-j terms live on level-j images, which have L^{4(m-t)}
placements per terminal block times the fine sub-placements counted in
M_{m,t}), and sum. ∎

## 5. What this changes

Generalized averaged H8 is no longer a separate kind of estimate. By (3.1)
it is a covariance between a terminal test and a local gauge-invariant
function. That is the same object as the irrelevant-defect decorrelation of
P4 (note 18 §9, item (iii)) and the averaged mechanism verified in the
Gaussian model (note 19: L^{-4m} per placement). The 4D programme's
interacting cores therefore share one kind of estimate:

- decorrelation of local gauge-invariant functions from terminal tests
  (H-dec), here and in P4;
- the single-step Lipschitz bounds (S1)-(S3) of note 29, whose O(g²)
  mechanism is note 31.

(H-dec) for local functions should itself follow from (S1)-(S3). A local
function inserted at scale k is a local perturbation of the effective
action, and its influence on terminal tests is its tangent-flow transport,
which contracts in irrelevant directions. Making that implication precise,
with the L^{-4m} rate for a single rooted insertion, is the natural next
theorem. It would connect H8 to note 29 directly.
