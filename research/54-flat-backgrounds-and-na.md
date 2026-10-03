# (NA) on the torus: flat backgrounds with holonomy, a counterexample and the corrected statement

Status:

- **Counterexample (proved).** (NA) as stated in note 45 fails on the
  torus. It compares H(U) with the flat-background operator H_0 in a global
  Landau gauge. Flat backgrounds with nontrivial holonomy lie in E_0 for
  every ε_0 > 0, but H(U) - H_0 does not vanish for them.
- **Proved.** The transport theorem of notes 44-45 holds exactly, with the
  same constants, at every flat SU(2) background (Theorem 2). Every
  background on E_0 is within o(1) (as ε_0 -> 0, for fixed terminal torus)
  of a flat one, after a gauge transformation (Lemma 3).
- **Corrected input (NA♭).** Compare H(U) with H(U♭) for the nearest flat
  background U♭, not with H_0. With (NA♭), note 45's Proposition 1 holds as
  stated, with covariant differences ∇_{U♭} in place of ∇, and with C_1 ε_0
  replaced by C_1(L) ω(ε_0), where ω(ε_0) -> 0. (NA♭) has the same source
  status as the old (NA): Cauchy plus Schur from CMP 99 Theorem 3.4, around a
  flat background. Theorem 3.4 is local in the background, so holonomy plays
  no role in it.
- **Effect.** The chain M1-3D <= (A_s) + (NA) of notes 52-53 stands with
  (NA) replaced by (NA♭). Notes 45 and 52 are corrected in place.

## 1. The counterexample

Let the coarse lattice be the torus (Z/n_0)^d and the fine lattice
(Z/(n_0 M))^d. Fix θ ∈ (0, π) and let V♭ be the constant coarse
configuration

    V♭_c = e^{i(θ/n_0)σ_3} on direction-1 bonds,   V♭_c = 1 otherwise.

Every coarse plaquette equals 1, so V♭ ∈ E_0 for every ε_0 > 0. Its
holonomy around the 1-cycle is e^{iθσ_3}, which is not central.

- *The minimizer is flat.* The constant fine configuration
  U♭_b = e^{i(θ/(n_0 M))σ_3} on direction-1 links has action 0. Its Balaban
  average is V♭: the configuration is abelian and constant, so every log in
  CMP 98 (42) equals the straight-line value. So U♭ is the minimal
  configuration. It also satisfies the Landau condition, because a constant
  potential has zero divergence.
- *The linearized minimizer twists the charged components.* The background
  is diagonal, so ad(σ_3) decouples su(2) into the neutral component (σ_3)
  and the charged components σ_± = σ_1 ± iσ_2. The linearized action, the
  linearized covariant average (parallel transport by U♭ along the contours
  Γ_{c,x}) and the background Landau condition all act:
  - on the neutral component as in the flat theory;
  - on σ_± as the flat theory conjugated by the phases e^{±2iθ x_1/(n_0 M)}.

  So, in the global gauge of note 45,

      H(U♭) = H_0 on σ_3,   (H(U♭)B)_±(b) = Σ_c K_0(b, c) e^{±2iθ(x_b - x_c)_1/(n_0 M)} B_±(c).

- *Conclusion.* Take B supported on one coarse bond c with values along σ_1.
  Then H_0 B lies along σ_1, while H(U♭)B has σ_2-component
  Σ K_0(b,c) sin(2θ(x_b - x_c)_1/(n_0 M)) B(c). That is nonzero, because K_0
  has range of order one coarse block. So ||(H(U♭) - H_0)B|| >= c(θ, n_0)||H_0 B||
  with c > 0 independent of ε_0, and the second line of (NA) fails for all
  small ε_0.

The flaw is in note 45's "Cauchy" step. That step needs the background to be
small in sup norm in one global gauge. A small plaquette bound does not
imply this on a torus: the holonomies are unconstrained. The fixed-torus
measures of the M1 problem give every holonomy sector positive weight, so
the gap is real.

## 2. Theorem 2 (transport at every flat background)

Let U♭ be any flat SU(2) configuration on the fine torus. Its linearized
minimizer map H(U♭) satisfies

    ||∇_{U♭,ν} H(U♭) B||_2 <= (2π/M) √(1 + π²/c_0) ||H(U♭) B||_2,

and the curvature version of note 44 Theorem 1 holds with the same constant
2π/√c_0. Here ∇_{U♭} is the covariant forward difference. The sharp
constants are those of `t37_energy_s1_constant.py`, which already samples
generic (non-lattice) K.

*Proof.*

1. *Normal form.* A flat lattice connection on the torus is determined up
   to gauge by its holonomy homomorphism Z^d -> SU(2). The images commute.
   - If one of them is not central, its centralizer is a maximal torus,
     which contains all the others.
   - Otherwise all of them are central.

   Either way, conjugate them into the diagonal torus. Then U♭ is gauge
   equivalent to the constant diagonal connection
   U♭_ν = e^{i(θ_ν/(n_0 M))σ_3}. Gauge covariance of the averaging (CMP 98
   (11)), of the action and of the background Landau condition makes H(U♭)
   covariant, and both sides of the claim are gauge invariant. So we may
   assume this normal form.
2. *Decoupling.* As in §1, the neutral component is exactly the flat
   problem. The σ_± components form the flat problem twisted by the
   characters x ↦ e^{±2iθ·x/(n_0 M)}. Equivalently, it is the flat problem
   on the universal cover, restricted to Bloch fields with quasi-momentum
   ±2θ/(n_0 M).
3. *Bloch sectors.* The flat minimizer commutes with coarse translations, so
   it preserves Bloch sectors. In the twisted sector the coarse momenta run
   over K ∈ (2π/n_0)(Z^d + ±θ/π), shifted from the periodic lattice, and the
   fine aliases are p_ℓ = (K + 2πℓ)/M.
4. *Note 44 per K.* Every step of the proof of note 44 Theorem 1, and of
   the potential version (note 45, Remark), is a statement about a single
   K. Each step uses only Mp_ℓ = K + 2πℓ and a choice of the alias p_0 with
   |K_j| <= π:
   - the identity (1 - e^{-ip_ν})D_M(p_ν) = 1 - e^{-iK_ν};
   - the Fejér/Parseval sums;
   - the alias-0 fraction;
   - the bound |r_ℓ| >= 2/M for ℓ != 0.

   None of these requires K to lie on the periodic lattice. In a twisted
   sector K ≠ 0, so there is no zero mode, and closed twisted forms are
   exact. (The twisted cohomology of the torus vanishes.) Hence the bounds
   hold sector by sector, and summing over sectors gives the claim. ∎

## 3. Lemma 3 (every small-field background is near a flat one)

Fix n_0, M and d. Let

    ω(ε) := sup { inf_{g, U♭ flat} max_b |U^g_b - U♭_b| : U a coarse configuration with max_p |U(∂p) - 1| <= ε }.

Then ω(ε) -> 0 as ε -> 0. The same holds for the minimal fine
configurations of such coarse configurations.

*Proof.* The function U ↦ dist(U, Flat) := inf_{g, U♭} max_b |U^g_b - U♭_b|
is continuous on the compact configuration space and vanishes exactly on
Flat. The sets E(ε) = {max_p |U(∂p) - 1| <= ε} are compact and decrease to
Flat as ε ↓ 0. A continuous function on a decreasing family of compact sets
has sup over E(ε) tending to its sup over the intersection, which is 0. For
the fine minimizers, use the continuity of the minimizer map on the
small-field set (CMP 102b Theorem 1, uniqueness), and the fact that the
minimizer of a flat coarse configuration is flat (§1). ∎

The rate is not quantified. Examples suggest ω(ε) is of order √ε, not ε.
Two almost-commuting holonomies e^{iασ_3}, e^{iασ_1} have commutator of
order α², spread over n_0² plaquettes, but their distance to a commuting
pair is of order α. A √ε rate is harmless for Proposition 1, which needs
only C_1(L) ω(ε_0) <= 1.

## 4. The corrected input and Proposition 1

**(NA♭).** For U on E_0, let U♭ be a flat configuration attaining
dist(U, Flat) <= ω(ε_0) (Lemma 3). Write U = U' U♭ in that gauge, with U'
small. Then

    ||∇_{U♭}(H(U) - H(U♭)) B||_2 <= C_1(L) ω(ε_0) M^{-1} ||H(U♭) B||_2,
    ||(H(U) - H(U♭)) B||_2 <= C_1(L) ω(ε_0) ||H(U♭) B||_2.

*Source status.* This is the derivation of note 45 ("Where (NA) comes
from"), run with the background U♭ in place of 1. CMP 99 Theorem 3.4 gives
analyticity of the background-field operators at configurations U'U♭ with U'
small. Its hypotheses are local regularity conditions, which a flat U♭
satisfies with zero curvature, and they involve no holonomy. Cauchy's
estimate in U' and Schur's test then give (NA♭), with C_1(L) untracked, as
before.

**Proposition 1 (corrected).** Assume (NA♭). For B in the small-field
domain,

    ||∇_{U♭} ℋ(B)||_2 <= (C_ab + C_1(L) ω(ε_0)) M^{-1} ||ℋ(B)||_2,

with C_ab the constant of Theorem 2 (about 3.1 sharp, potential version).

*Proof.* Note 45's proof applies verbatim, with:

- H_0 replaced by H(U♭);
- ∇ replaced by ∇_{U♭};
- note 44 replaced by Theorem 2;
- (NA) replaced by (NA♭). ∎

So the contraction rate stays the sharp abelian one, (C_ab + 1)/L per step,
on the whole small-field event, all holonomy sectors included. The
smallness condition ε_0 <= ε(L, n_0) is now on ω(ε_0). It depends on the
fixed terminal torus n_0, which is fixed in M1.
