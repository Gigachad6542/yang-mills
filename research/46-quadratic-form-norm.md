# The norm in which (S1) holds: quadratic forms relative to the marginal energy

Status: **proved** (T40), for the abelian linearization and quadratic
(two-point) parts of effective-action perturbations. It is a direct
reformulation of note 44.

## Why quadratic forms

A gauge-invariant analytic perturbation δE of the effective action has no
linear term at the flat field. This is note 33 Lemma 1, and Balaban's
CMP 102 (31)-(32): "there are no relevant variables". So near the
small-field configurations its leading part is a quadratic form in the
curvature,

    δE(F) = Q(F) + O(|F|³),   Q(F) = Σ_{x,y} F(x) q(x, y) F(y),

with q local (exponentially decaying) and block-periodic. One RG step
transports δE to δE ∘ (minimizer map). In the abelian linearization the
leading part is

    Q' := Q ∘ T,   T : Φ ↦ F_min(Φ).

The marginal reference form is the minimal energy
S(Φ) = ½||F_min(Φ)||² = ½||TΦ||².

**Definition (form norm).** ||Q||_S := sup_{Φ exact} |Q(TΦ)| / S(Φ).

This is the operator norm of Q restricted to the range of T, which consists
of minimizers, relative to their energy.

## Proposition 1 (contraction of irrelevant forms)

Let Q_1(F) := Σ_{x,ν} |∇_ν F(x)|² (dimension 6) and
Q_2(F) := Σ_{x,μ,ν} |∇_μ∇_ν F(x)|² (dimension 8), at the fine scale. In
coarse-lattice units, with differences taken over the coarse spacing M:

- Q_1^{coarse} := M² Q_1 ∘ T satisfies ||Q_1^{coarse}||_S <= 8 C², where
  C <= 60 is the constant of note 44 Theorem 1 (about 4 sharp).
- The one-step map from level m-1 to level m multiplies the Q_1-type
  coefficient by at most (C/L)² relative to the marginal form, by note 44
  Corollary 2. For Q_2-type coefficients the factor is C_3² L^{-3} (note 44
  Theorem 3).
- Any local form with |Q(F)| <= c Q_1(F) inherits the bound with constant c.

*Proof.* By note 44 Theorem 1, Q_1(TΦ) <= 4 C² M^{-2} ||TΦ||² = 8 C² M^{-2} S(Φ)
(the factor 4 is the number of directions ν). Multiply by M². The one-step
statements are Corollary 2 and Theorem 3 of note 44, squared. ∎

## Reading

- The marginal form (the action density F²) has transported form norm
  <= 1, by note 44 Corollary 2 (||W|| <= 1). This is charge conservation
  (note 33).
- The first irrelevant forms contract by (C/L)² per step, which is
  (4/L)² with the sharp constant. Note 35's sup-norm obstruction does not
  arise, because the form norm is relative to the energy.
- Higher-order terms O(|F|³) are of relative size O(ε_0) on the small-field
  set, and sit in Balaban's sup norms. This is the mixed structure: forms
  measured relative to energy for transport, sup norms for analytic
  remainders.
- Non-abelian, small-field: by note 45, the same bounds hold with
  C -> C + C_1(L) ε_0, given (NA).

So (S1) for the two-point (quadratic) part of the effective action is a
theorem in the abelian linearization, and conditional on (NA) for SU(2).
Its natural norm is the form norm ||·||_S relative to the minimal energy.
