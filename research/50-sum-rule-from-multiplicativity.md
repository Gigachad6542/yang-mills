# (S) of note 22: only bounded edges are needed

Status:

- **Proved here.**
  - Lemma 1 (additivity): the n-step composite of limit steps has one-loop
    shift n β_∞^0(L).
  - Proposition 3: (S) follows from Lemma 1, note 48 (C), and the edge
    bound (E).
- **Sketch.** Lemma 2 (E): β_∞^0(L) = 2b_0 log L + O(1) uniformly in L. It
  follows from power-law edge corrections of the block-constrained
  propagator and the standard one-loop background-field computation.
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

## 2. Lemma 2 (edge bound (E); sketch)

    β_∞^0(L) = 2b_0 log L + O(1),   uniformly in L.

*Sketch.* β_∞^0(L) is the p² coefficient of the one-loop polarization of
the limit step, which integrates the modes between the UV block scale 1 and
the IR block scale L (rescaled units). Its propagator G_L(q) differs from
the massless (gauge-fixed) propagator G_0(q) as follows.

- *IR edge* (|q| <~ 1/L, from the block constraint): the correction is the
  W^T C^{-1} W term. Its weight is |ŵ_L(q)|², a product of squared Dirichlet
  (sinc) factors. For |q| >> 1/L it decays like (L|q|)^{-2} per transverse
  coordinate (note 47 steps 2-3). The relative correction is therefore
  O((L|q|)^{-2}).
- *UV edge* (|q| ~ 1, lattice): the lattice symbols differ from the
  continuum ones by O(|q|²) relative errors (note 47 step 5).

In the window 1/L << |q| << 1 the polarization integrand is the standard
one, Π ~ ∫ d⁴q (vertex·G_0·vertex·G_0)'', whose p² coefficient is
(universal tensor) × ∫ d⁴q/|q|⁴ over the window = 2b_0 log L + O(1). The value
2b_0 = 11N/(3·8π²) (normalization of note 22) is the standard
background-field result, independent of gauge. The edge corrections are
power laws, so their contributions to ∫ d⁴q/|q|⁴ are O(1) uniformly in L.

What is not written out: the vertex algebra of the gluon and ghost loops in
Balaban's gauge-fixed scheme, and uniform bounds on the edge integrals. The
first is textbook; the second follows from the stated power laws.

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
