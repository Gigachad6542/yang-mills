# Mixed-norm compatibility: Balaban's sup-norm activities in the form norm

Status: **proved** (T45). This is the glue between Balaban's sup-norm
framework and the energy/form-norm transport bounds of notes 44-46.

## Setting

Balaban's effective-action terms are gauge-invariant polymer activities
h_X, analytic on complex small-field domains, with sup bounds (CMP 109
(1.18)):

    |h_X| <= ||h_X|| <= E_0 e^{-κ d(X)},

in a complex neighbourhood where, in a local axial gauge on X, every link
has |a_b| <= α. The form norm (note 46) of a quadratic form Q is
||Q||_S = sup |Q(TΦ)|/S(Φ), where S(Φ) = ½||TΦ||² is the minimal energy.

## Lemma 1 (quadratic part of one activity)

Write h_X(a) = h_X(0) + Q_X(a) + O(|a|³) near the flat field, where Q_X is
the quadratic Taylor term. Since h_X is Ad-invariant, its linear term
vanishes (note 33 Lemma 1; CMP 102 (31)-(32)). In a local axial gauge on X
the links satisfy |a_b| <= C R_X max_{p⊂X} |F_p|, where R_X = diam X. Then

    |Q_X(a)| <= C ||h_X|| R_X² α^{-2} Σ_{p⊂X} |F_p|².

*Proof.* By Cauchy on the polydisc of radius α, |D²h_X(0)[a, a]| <= 2||h_X|| |a|_∞²/α².
Use |a|_∞ <= C R_X max_p |F_p| and max_p |F_p|² <= Σ_p |F_p|². ∎

## Proposition 2 (form-norm bound for the sum)

Let Q := Σ_X Q_X be the total quadratic part of the activities. Then for
every field F,

    |Q(F)| <= C_Q ||F||_2²,   C_Q := C α^{-2} sup_p Σ_{X ∋ p} ||h_X|| R_X².

With Balaban's bounds, C_Q <= C' E_0 α^{-2} (the sum over X ∋ p converges
because of e^{-κ d(X)} with κ large). In particular ||Q||_S <= 2C_Q: the
quadratic part of Balaban's activities is bounded in the form norm by a
constant times his activity norm.

*Proof.* Sum Lemma 1 over X and exchange the sums over X and p. Then use
||TΦ||² = 2S(Φ) for F = TΦ. ∎

## Proposition 3 (higher orders)

On the small-field set, |F_p| <= ε_0 for all p. The cubic and higher
remainders of the activities satisfy

    |Σ_X (h_X - h_X(0) - Q_X)(a)| <= C ε_0 α^{-1} C_Q' ||F||².

So they are smaller than the quadratic part by a factor ε_0 in the form
norm.

*Proof.* Cauchy gives |D³h_X| <= C||h_X||/α³. Then
|a|³ <= (C R_X ε_0)·(C R_X)² max|F|², and sum as in Proposition 2. ∎

## Consequence: the mixed-norm framework is consistent

1. Balaban's activities have quadratic parts of form norm O(E_0)
   (Proposition 2). The cubic and higher parts are O(ε_0 E_0)
   (Proposition 3).
2. After subtracting the marginal F² coefficient (Balaban's
   renormalization, the β-function term), the remaining quadratic part is
   irrelevant. By CMP 109's fifth-order local expansion it is a form in
   gradients of F (dimension >= 6), with the same Cauchy bounds.
3. Transport multiplies the form norm of such irrelevant forms by
   (C/L)² per step (note 46; SU(2) via note 45). Generation adds
   O(g² p(g)²) (note 42, given (A_s)). The higher-order parts stay
   O(ε_0) in the form norm and are controlled analytically in sup norms.

So (S1) and (S2) of note 29, with δ_k := form norm of the irrelevant
quadratic part plus ε_0^{-1} times the sup norm of the higher-order part,
hold with:

- θ = (C/L)² + O(ε_0);
- b, c = O(g² p²);
- e = O(g⁴) (smoothness of β, CMP 109 p. 265).

Note 29 Theorem 1 then gives memory decay. What remains open is only what
was already listed: (A_s), (NA) constants, and Balaban's fifth-order
expansion statement in the form used in item 2.
