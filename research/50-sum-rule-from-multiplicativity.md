# (S) of note 22: only bounded edges are needed

Status:

- **Proved here.**
  - Lemma 1 (additivity): the n-step composite of limit steps has one-loop
    shift n β_∞^0(L).
  - Proposition 3: (S) follows from Lemma 1, note 48 (C), and the edge
    bound (E).
- **Proved here (T67, structure only).** The IR edge is exactly
  ½ log det C(A) (Prop. 2.1), and at the lowest alias the edge correction is
  100 per cent, 1 - f_0 = O(|K|^4) (Prop. 2.2).
- **Open (T67 failed-attempt).** Lemma 2 (E): β_∞^0(L) = 2b_0 log L + O(1)
  uniformly in L. The earlier sketch (power-law edge corrections to G_0) does
  not work at n = 0 (§2.3); §2.4-2.5 give the remaining steps.
- **Effect.** (S) no longer needs the scheme constant (the edge value that
  note 23 / T19 could not compute). Only an O(1) bound on the edges is
  needed, and the exact value 2b_0 is then forced.

## 1. Lemma 1 (additivity over composites, in the limit)

For the n-step composite of limit steps (factor L each), the one-loop shift
is n β_∞^0(L).

*Proof.* By note 22 Lemma B (Schur-complement additivity), the one-loop
shift of the composite of steps k+1, ..., k+n equals Σ_{i=1}^n β^0_{k+i}. Let
k -> ∞ and use note 48. ∎

*Correction (same day).* An earlier version claimed the stronger
cross-scheme identity β_∞^0(L^n) = n β_∞^0(L), with the factor-L^n scheme as a
separate scheme. That rests on "the composite of n averages is the L^n
average". This is exact for the **linear** block average (note 19 (2.1)).
For Balaban's **covariant** non-abelian average, the composition differs at
second order in the background, which is exactly the obstacle noted in
note 23 §7. The cross-scheme identity is not needed. Lemma 1 as now stated
uses only the composite of the L-scheme steps.

## 2. Lemma 2 (edge bound (E)): T67 attempt, not proved

    β_∞^0(L) = 2b_0 log L + O(1),   uniformly in L.      (E)

**Outcome (T67, failed-attempt).** (E) is not proved. What was done:
two exact structure results about the IR edge (2.1, 2.2, proved), which
show that the earlier sketch ("G_0 plus a power-law-small edge") is wrong
at the lowest alias and so cannot be completed as written (2.3); the exact
step where a proof stops, with the integrals involved (2.4); and the next
concrete step (2.5). The status of Lemma 2 stays **sketch / open**.

The earlier sketch is kept in 2.3 only to say which part is wrong.

### 2.1 Exact form of the IR edge (proved)

Setting (notes 23 (2.1), 47, 48). Let K(A) be the fluctuation operator
in a background A (gluon or ghost), G(A) = K(A)^{-1}, and Q the **linear**
block average (note 19 (2.1)); it does not depend on A. The block-constrained
Gaussian integral has one-loop action Γ_Q(A) = ½ log det(K(A)|_{ker Q}), and
the constrained covariance is (note 23 (2.1))

    G_Q = G - g C^{-1} g^*,   g = G Q^*,   C = Q G Q^*.

**Proposition 2.1 (determinant identity).** For finite-dimensional K > 0
and Q surjective,

    det(K|_{ker Q}) = det K · det(Q K^{-1} Q^*) / det(Q Q^*).

Hence, for A-independent Q,

    Γ_Q(A) = ½ log det K(A) + ½ log det C(A) + const,   C(A) = Q G(A) Q^*.

*Proof.* Split V = N ⊕ R, N = ker Q, R = ran Q^*, and write K in blocks.
Then det K = det K_NN · det(K^{-1}_{RR})^{-1} (Schur). Since Q = [0, Q_R]
with Q_R : R -> W invertible, det(Q K^{-1} Q^*) = det(Q_R Q_R^*) · det K^{-1}_{RR}
and det(Q_R Q_R^*) = det(Q Q^*). ∎

So the IR edge of the effective action is exactly ½ log det C(A), the
log-determinant of the **block covariance in the background**. The p²
coefficient of Γ_Q is that of the unconstrained ½ log det K(A) plus that of
½ log det C(A). For the ghost the sign is reversed. Each is IR divergent
separately (standard: the unconstrained polarization has ∫ d⁴q/|q|⁴ at
q -> 0, cut off by the volume), and only the sum is finite. So there is no
termwise bound "unconstrained + O(1)".

### 2.2 Alias structure of E at the lowest alias (proved; scalar toy)

Take one scalar component, the fine lattice Z⁴ with M^4 cells per block,
G_0(p) = (Σ_j 4 sin²(p_j/2))^{-1}, and the notation of note 58 §1: coarse
momentum K ∈ (-π, π]^4, aliases n ∈ B_M, p_n = (K+2πn)/M, and
δ_M(n_j) = |sin(K_j/2)|/(M|sin(p_{n,j}/2)|). Put w_n = Π_j δ_M(n_j) (up to a
phase), g_n = w_n G_0(p_n), C(K) = Σ_n |w_n|² G_0(p_n). On the alias sector of
K, E = G_Q - G_0 = -g g^*/C is **rank one**, with diagonal

    E_nn = -f_n G_0(p_n),   f_n := |w_n|² G_0(p_n)/C(K) ≥ 0,   Σ_n f_n = 1.

**Proposition 2.2.** There is an absolute constant C_0 such that for all
M ≥ 2 and K ∈ (-π, π]^4,

    0 ≤ 1 - f_0 ≤ C_0 |K|^4.

*Proof.* Lower bound for the denominator: |sin x| ≤ |x| gives
G_0(p_0) ≥ M²/|K|², and δ_M(0) ≥ 2|sin(K_j/2)|/|K_j| ≥ 2/π per coordinate,
so |w_0|² ≥ (2/π)^8 and C ≥ (2/π)^8 M²/|K|². Numerator: 1 - f_0 =
Σ_{n≠0} |w_n|² G_0(p_n)/C. For n ≠ 0, |q_n| ≥ π, and 4 sin²(p/2) ≥ 4p²/π²
on |p| ≤ π gives G_0(p_n) ≤ π² M²/(4|q_n|²) ≤ M²/4. By note 58 (W1),
δ_M ≤ (π/2) δ_∞, and δ_∞(n_j) ≤ |K_j|/(π|n_j|) when n_j ≠ 0, ≤ 1 when
n_j = 0. Every n ≠ 0 has some n_j ≠ 0, so |w_n|² ≤ c_1 |K|² Π_{j: n_j≠0} n_j^{-2}
with an absolute constant c_1 (use |K_j| ≤ π for the other nonzero
coordinates). Since Σ_{n∈Z⁴\{0}} Π_{j: n_j≠0} n_j^{-2} < ∞ (it factorizes as
(1 + 2ζ(2))⁴ - 1), Σ_{n≠0} |w_n|² G_0(p_n) ≤ C' |K|² M². Divide. ∎

*Numerical check.* `research/scripts/t67_alias_fraction.py` (output
`.out`), M = 4, 8, 4D: f_0 = 1 - O(|K|^4) (for example 1 - f_0 = 3.5e-6 at
|K| = 0.2, and 5.7e-5 at |K| = 0.4; the ratio 16 per doubling of |K|), and
max_{n≠0} f_n is another factor 10 smaller. At |K| = 4 (the edge of the
coarse Brillouin zone) f_0 has dropped to about 0.5.

Consequences:

- G_Q(0,0) = (1 - f_0) G_0(p_0) ≤ C_0 M² |K|² · const: **finite and
  vanishing at K -> 0**, whereas G_0(p_0) ≥ M²/|K|² is singular.
- E_00 = -f_0 G_0(p_0) cancels G_0(p_0) to relative accuracy |K|^4. In the
  region |p_0| ≲ 1/M (coarse |K| ≲ 1), the IR edge correction is **100 per
  cent**, not a small relative correction.
- The constrained field is, to leading order, G_0 with the lowest alias
  removed: a sharp cut at the coarse Brillouin-zone edge, smeared by the
  Dirichlet weights, and not a perturbation of G_0.

### 2.3 Where the earlier sketch fails

The sketch wrote G_L = G_0 + (UV edge) + (IR edge), with the IR relative
correction O((L|q|)^{-2}) and the edge contributions to ∫ d⁴q/|q|⁴ "O(1) by
power-law decay". Two things are wrong or missing.

1. *The relative power law holds only for n ≠ 0.* There f_n ≤ 1 - f_0 ≤ C_0|K|^4
   is small (2.2). At n = 0 the correction is -f_0 ≈ -1.
   By degree counting, the bubble terms built from G_0 alone at the lowest
   alias have a p² coefficient with integrand ~ (vertex ~ |K|)² · |K|^{-2} ·
   |K|^{-4} (two propagators, one extra |K|^{-2} from the second p-derivative),
   i.e. homogeneous of degree -4 in K near K = 0, so the G_0-only alias-0
   contribution is ∫_{|K|<π} d⁴K/|K|⁴ = ∞ (logarithmic). The E part cancels this exactly.
   A bound on the edge piece by its pointwise decay therefore does not
   exist: neither piece is integrable alone, and only the combination G_Q is.
   (This is the degree count, not a computation of the SU(2) vertices.)
2. *The sketch used the wrong propagator at the UV edge.* The sketch (and
   the toy model of 2.1-2.2) uses the **fine-lattice** G_0, whose Brillouin
   zone is |q| ≲ M -> ∞ in coarse units, so its window integral would be
   log M, not log L. In Balaban's step, as note 48 ("The ingredients")
   describes it, the step-k fluctuation B lives on the scale-k block lattice
   and enters the fine field through the minimizer map H_k. The UV edge is
   then the Brillouin-zone boundary of that lattice together with the
   symbol of H_k (note 48 item 2), and the lattice-symbol error O(|q|²) of
   note 47 step 5 is not the relevant quantity. Note 48 defines this model
   but does not give its propagator in a form where the UV edge integral can
   be bounded; that has to be written out first. (Lead correction at
   integration: the T67 draft said the model was not defined in the notes.)

### 2.4 The exact step where the proof stops

With G_Q = G_0 + E and (2.3) of note 23, the p² coefficient is

    β = (alias sums of vertex-weighted products of G_Q at aliases n, n + m),

where m runs over the background's own aliases (note 58 Lemma A2). A proof
of (E) needs, uniformly in the ratio L, three bounds:

1. *bulk*: the window n with 1 ≲ |q_n| ≲ L, where G_Q = G_0 up to the
   relative error f_n and the integral is (angular average) × ∫d⁴q/|q|⁴,
   giving 2b_0 log L plus O(1) from the boundary shells;
2. *IR shell*: aliases n = 0 and the couplings (0,n), (n,0) for |m| small
   (E_{0n} ≈ -(w_n/w_0) G_0(p_n), regular), with G_Q(0,0) as in 2.2.
   The integrand is bounded near K = 0, but its size on |K| ≲ π is an
   L-independent number only after the UV model (2.3, item 2) is fixed; and
3. *UV shell*: the previous-lattice edge, for the same reason.

Bounds 2 and 3 are the integrals that the sketch assumed to be O(1) and that
were not controlled. The first obstruction is that G_0 and E have to be
integrated together at n = 0 (2.3, item 1). The second is the vertex algebra
itself. In Balaban's scheme the vertices come from the covariant average
Q(U) and the gauge-fixing in the background. For the linear Q used in 2.1
the term ½ log det C(A) is not background-gauge-covariant, so its p²
coefficient has longitudinal artifacts that must be separated from the
transverse β (note 23, end of §2). For the covariant Q(U) there are extra
first and second derivatives of Q (note 23 §7). Neither the standard
background-field vertex algebra for a noncovariant constraint nor the second
derivatives of Q(U) were available, so the O(1) was not computed.

*Composites.* For the **linear** average, the n-step composite of the
limit step is exactly the limit step at block ratio L^n (note 19 (2.1); see
the Correction in Section 1). So the uniformity in n that Proposition 3
assumes is the uniformity in L of (E) itself, with no further input. For the
covariant average, composition fails at second order in the background
(Section 1), and the extra term is a bound on 2.4 item 2 for Q(U).

### 2.5 Next concrete step

Prove (E) for the scalar (orbital) part of the gluon loop in the linear
scheme, which has the same alias structure and no spin vertex:

1. write the propagator of note 48's model (B on the scale-k block lattice,
   entering through H_k, with the child symbol of note 48 item 2), so that
   the UV edge of 2.3 item 2 is explicit;
2. write the scalar bubble and seagull p² coefficient with G_Q = G_0 + E
   via Lemma A2 (note 58), treating n = 0 jointly (2.2: use f_0 ≤ 1 and
   1 - f_0 ≤ C_0|K|^4 to get the integrable majorant);
3. show the three shells of 2.4 are bounded independently of L.

Only after that scalar case is the spin vertex (constant matrix) and the
ghost added. The covariant Q(U) comes last.

## 3. Proposition 3: (S)

Assume Lemma 2 for the n-step composites (edges bounded uniformly in n).
Then β_∞^0(L) = 2b_0 log L, and

    Σ_{j=1}^{K} β_j^0 = 2b_0 K log L + O(1)   uniformly in K,

which is (S) of note 22.

*Proof.*

1. By Lemmas 1 and 2, n β_∞^0(L) = 2b_0 n log L + O(1) for all n. Divide
   by n and let n -> ∞.
2. By note 48, |β_j^0 - β_∞^0| <= C (1 + j log L) L^{-j}, which is summable
   in j. So Σ_{j<=K} β_j^0 = K β_∞^0 + O(1). ∎

## 4. Status of H0

[Superseded (audit 2026-10-09, T82): (E) is open after T67 (header, §2), so the "(E) sketched"
below is out of date; (C)'s vertex Riemann sums are reduced to (V) and
checked for the leading gluon, ghost and gauge-fixing vertices (note 58), and
the multi-level penalty is open (note 41 §5.6, T75).]

    H0 <= (B), regularity [published]
        + (C) [note 48; vertex Riemann sums stated]
        + (S) [this note; the edge bound (E) sketched]
        + (D) memory decay [single-step: (A_s), (NA), (S3)].

The scheme-specific finite constant that T19 could not compute is not
needed. (S) needs only bounded edges for the composites, and additivity then
forces the universal value. Lemma 2 for the composites must include the
second-order background dependence of the composite covariant average at the
IR edge. That is an O(1) edge contribution, not a bulk one, because the
constraint acts only at the coarsest scale of the window.
