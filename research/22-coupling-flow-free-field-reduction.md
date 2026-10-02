# Reducing the coupling-flow theorem H0 to a free-field statement

Status, item by item:

- **Proved here.**
  - Thm. A (windowed shooting): Balaban's announced conclusion, CMP 109
    Theorem 2 (bare coupling with every g_k in (0,γ] and g_K = g, plus linear
    bounds on g_k^{-2}), follows from three inputs: the published smoothness
    of the β-functions in their last argument, a memory-decay bound (D) on
    their dependence on earlier couplings, and windowed positivity (W) of the
    **free** (g = 0) increments. (W) is weaker than positivity of every
    increment.
  - Lemma B (one-loop additivity): free increments add up over a window to
    the one-loop coupling shift of the composite multi-step fluctuation
    integral. This is an exact Laplace/Schur-complement identity.
  - Cor. C: (W) follows from one-loop universality with bounded window edges
    (U).
- **Open.** (D) and (U). (U) is a statement about Gaussian (free-field)
  integrals in Balaban's scheme. **H0 is not proved here.**

Compared with note 08 §"Exact missing inputs", item 2 (uniform positive
increments) splits into a free-field one-loop statement (U) and a
memory-decay bound (D). Note 08's sufficient hypothesis β = b_* + O(u²) is
not needed.

## 1. Published definitions

- **Recursion** (CMP 109 (0.18), (0.20)). With h_k = g_k^{-2},
  h_{k+1} = h_k - β_{k+1}, where β_{k+1} = β_{k+1}(g_k; g_0, ..., g_{k-1})
  (p. 298: "depends also on all preceding coupling constants").
- **Definition of β** (CMP 109 (1.20)-(1.22) and §5, (5.37)-(5.42)). Let
  E^{(j+1)}(g_j, ·) be the effective action produced by the (j+1)-st
  fluctuation-field integral. Its background Hessian is the vacuum
  polarization tensor Π_{j+1,μν}(g_j; x - x'), taken in the infinite-volume
  limit. Then (5.37) gives
  Π̂_{μν}(p) = β(δ_{μν}Δ(p) - ∂̄_μ∂_ν) + Π'_{μν}(p), with Π' = O(p³), and
  β_{j+1} = -(1/2) ∂²_{p_μ p_ν} Π̂_{j+1,μν}(g_j, 0) for μ ≠ ν.
- **Regularity** (CMP 109 p. 265, part of the inductive assumptions that
  Theorem 3 asserts). β_{j+1} "is a smooth function defined on the interval
  [0,γ] (or analytic), uniformly bounded on this interval together with all
  derivatives". So **g_j = 0 is in the domain.** The value β_{j+1}(0; ...)
  is the one-loop (Gaussian) coefficient: at g_j -> 0 the scaled fluctuation
  integral is Gaussian, and E^{(j+1)}(0, ·) is -(1/2) log det of the
  constrained, gauge-fixed fluctuation Hessian in the background.
- **R-compatibility** (CMP 119 §2, the text at (2.23) and at (2.30)-(2.31)). The terms R_k produced by the
  R-operation are "fully renormalized ... For this term we perform the
  vacuum energy renormalization only". Coupling renormalization comes from
  the small-field terms E_k alone, so the β_j above are the complete
  increments. Item 4 of note 08 is therefore a source reading. It holds up to
  the general caveat that CMP 119/122 are inductive descriptions.

Write β_j^0 := β_j evaluated with every coupling set to 0 (the free
increment), and h_* = γ^{-2}.

## 2. Hypotheses

- **(B)** (published, CMP 109 p. 265). |β_j| <= b_+ on the admissible domain
  (every coupling in [0,γ]).
- **(D) (memory decay; open).** On the admissible domain,
  |∂β_{j+1}/∂g_i| <= C_D θ^{j-i} for 0 <= i <= j, with θ < 1. The case i = j
  is the published derivative bound. The cases i < j say that the
  dependence on earlier scales decays geometrically, as in research/21 (F3).
- **(W) (windowed free positivity; open).** There are ℓ >= 1 and c > 0 such
  that Σ_{j=i+1}^{i+n} β_j^0 >= c n for every i >= 0 and every n >= ℓ.
- **(U) (one-loop universality with bounded edges; open).** There is C_U
  such that, for all i >= 0 and n >= 1,
  |Σ_{j=i+1}^{i+n} β_j^0 - 2b_0 n log L| <= C_U, with b_0 = 11 C_A/(48π²)
  (SU(2): C_A = 2), in the normalization h = g^{-2}.

## 3. Windowed shooting (Theorem A; proved)

**Lemma A0.** Under (D), on the admissible domain,
|β_{j+1}(g) - β_{j+1}^0| <= η := C_D γ/(1-θ).

*Proof.* Integrate along the segment from 0 to (g_0, ..., g_j). The domain
is a product of intervals, so the segment stays in it. Bound the gradient by
Σ_i C_D θ^{j-i} g_i <= C_D γ/(1-θ). ∎

**Theorem A.** Assume (B), (D) and (W), and suppose η <= c/2. Put
I = [h_*, ∞) and I' = [h_* + 2ℓb_+, ∞). For every K >= ℓ and every
t ∈ I', there is a bare value h_0 such that the trajectory has every h_k in I
(every g_k <= γ) and h_K = t. Every such trajectory satisfies
h_k - h_{k'} >= (c/2)(k' - k) - 2ℓb_+ for all k < k'.

*Proof.* Split {1, ..., K} into consecutive windows W_1, ..., W_r, each of
length in [ℓ, 2ℓ), counted from the fine end. This is possible because
K >= ℓ. Let e_0 = 0 < e_1 < ... < e_r = K be the window endpoints.

1. *Within a window.* If h_{e_{s-1}} ∈ I', then every h_k with
   e_{s-1} <= k <= e_s satisfies h_k >= h_{e_{s-1}} - 2ℓb_+ >= h_*, by (B).
   So the history stays admissible and all β's are defined.
2. *Window decrements.* By Lemma A0 and (W), the window decrement
   B̃_s := h_{e_{s-1}} - h_{e_s} = Σ_{j∈W_s} β_j lies in
   [|W_s|(c - η), |W_s| b_+], which is contained in [ℓc/2, 2ℓb_+].
3. *Continuity.* B̃_s depends continuously on h_0 wherever it is defined,
   since β_j is smooth and h_k depends continuously on h_0.
4. *Shooting.* Apply note 08 Theorem 2 to the window recursion
   h_{e_s} = h_{e_{s-1}} - B̃_s on I', with b_- = ℓc/2 and b_+ replaced by
   2ℓb_+. The proof there uses only continuity, the first-contact argument
   (one window after a first contact with the boundary of I' leaves I',
   because B̃ >= b_- > 0), and the intermediate value theorem. The
   "history" there is now the window-endpoint history, and by step 1 the
   intermediate couplings stay admissible. This gives h_0 with h_K = t and
   all endpoints in I'.
5. *Bounds.* The two-sided endpoint bounds of note 08 Theorem 2, together
   with step 1, give the stated linear bound. ∎

**Remarks.**
- (W) does not require each β_j^0 to be positive. Initial or
  scheme-dependent steps may have either sign, provided the bounded edge
  effects are beaten by the windows.
- Without (D), Lemma A0 fails. A history-dependent O(1)·γ shift summed over
  j steps could make |β_{j+1}(g) - β_{j+1}^0| grow with j.

## 4. One-loop additivity (Lemma B; proved)

**Lemma B (Laplace/Schur).** Let f(x, y) be smooth near a nondegenerate
minimum, with y ∈ R^p (fine variables integrated first) and x ∈ R^q. Put
F(x) = f(x, y*(x)), where y*(x) minimizes f(x, ·). Then at the joint minimizer

    det ∂²f = det ∂²_{yy} f · det ∂²F,

because ∂²F is the Schur complement of ∂²_{yy}f in ∂²f. As g -> 0, the
one-loop (det^{-1/2}) factor of the joint Gaussian integral therefore equals
the product of the one-loop factors of the iterated integrals. Each iterated
factor is evaluated at the background given by the minimizer of the
remaining variables. The same holds with linear constraints Qy = fixed and
with fixed gauge-fixing slices: restrict to the affine constraint
subspaces, and the identity holds on them.

*Proof.* Differentiate F(x) = f(x, y*(x)) twice. With ∂_y f(x, y*(x)) = 0
and implicit differentiation, ∂²F = f_xx - f_xy f_yy^{-1} f_yx, which is the
Schur complement. Then apply the block-determinant formula. ∎

**Consequence.** Balaban's background at step j is the minimizer U_j(V)
determined by the coarser field (CMP 102, 277-309). His one-loop terms are
logs of exactly these iterated determinants. Lemma B therefore gives

    Σ_{j=i+1}^{i+n} E^{(j)}(0, ·) = E_{[i,i+n]}(0, ·)   (one-loop composite, up to constants),

as functions of the scale-(i+n) background. Taking the transverse p²
coefficient, which is dimensionless in d = 4 and so scale-invariant, gives

    Σ_{j=i+1}^{i+n} β_j^0 = β^0_{[i,i+n]},

the one-loop coupling shift between scales i and i+n of the composite
fluctuation integral. Two caveats are left as part of the open input:
infinite-volume limits must be taken consistently, and Balaban's
"localized parts" must contain the complete p² coefficient (CMP 109 (5.43)
says this is so).

**Corollary C.** (U) implies (W) with c = b_0 log L and
ℓ = ⌈C_U/(b_0 log L)⌉ + 1.

*Proof.* For n >= ℓ, Σ >= 2b_0 n log L - C_U >= b_0 n log L. ∎

## 5. What (U) is, and why it is the right target

- β^0_{[i,i+n]} is the coefficient of tr(dB)² in -(1/2) log det of
  Balaban's composite fluctuation operator over n scales (Lemma B). That
  operator integrates the field modes between the lattice cutoffs at scales
  i and i+n.
- Standard one-loop background-field power counting says the transverse p²
  coefficient grows like 2b_0 log(L^n). The scheme enters only through the
  two edges (the block constraint at the coarse end, and the history of
  finer averaging plus the lattice at the fine end). That is (U).
- (U) involves **no interacting measure, no large fields and no R**. It is a
  statement about determinants of explicit lattice operators: Balaban's
  propagators G_k(U), at the trivial background and to second order in the
  background. It is the free-field core of the unpublished CMP 109
  Theorem 2. Balaban called its proof "based on second order perturbative
  calculations ... very awkward and long" (CMP 122 II, introduction).
- Balaban's propagator estimates (CMP 95, 96, 99) give exponential decay
  and convergence of the step operators as j -> ∞. They should make
  β_j^0 -> β_∞^0. Lemma B and (U) then force β_∞^0 = 2b_0 log L (Cesàro),
  so only finitely many initial steps are scheme-specific. This step is
  heuristic: the convergence of β_j^0 is not extracted from the sources
  here.

### Proposition D: (U) from convergence plus the one-loop sum rule (proved)

Assume:

- **(C) geometric convergence of the free increments.**
  |β_j^0 - β_∞^0| <= C_c ϑ^j for some β_∞^0 and ϑ < 1. This is expected
  from Balaban's definitions: the step-j fluctuation operator involves the
  composite average Q_j (whose kernel converges at rate L^{-j}, cf. the
  kernels of research/18 §8 and research/19 §2) and the weights
  a_j = a(1-L^{-2})/(1-L^{-2j}) (rate L^{-2j}). Not extracted from the
  sources here.
- **(S) one-loop sum rule.**
  Σ_{j=1}^{K} β_j^0 = 2b_0 K log L + O(1), uniformly in K. This is one-loop
  universality of the relation between the bare Wilson coupling and
  Balaban's terminal coupling (by Lemma B, the sum is the composite one-loop
  shift). It is classical lattice perturbation theory: the coefficient of
  log(a μ) in the one-loop vacuum polarization is universal. Matching it to
  Balaban's normalization of β_j is part of (S).

Then (U) holds with C_U = 2C_c/(1-ϑ) + C_S.

*Proof.* By (C), Σ_{j<=K} β_j^0 = Kβ_∞^0 + O(C_c/(1-ϑ)). Comparing with (S)
for K -> ∞ gives β_∞^0 = 2b_0 log L. For any window,
Σ_{j=i+1}^{i+n} β_j^0 = nβ_∞^0 + O(C_c/(1-ϑ)) = 2b_0 n log L + O(1). ∎

So H0 now rests on (C), (S) and (D). Of these, (S) is classical perturbative
input, and (C) and (D) are geometric-decay statements about Balaban's own
operators.

## 6. Status of H0 after this note

    H0  <=  (B) [published]  +  regularity at g = 0 [published, CMP 109 p. 265]
          + (D) [memory decay of the history dependence; open]
          + (U) [one-loop universality with bounded edges, free field; open;
                 by Prop. D it follows from (C) geometric convergence of the free
                 increments plus (S) the classical one-loop sum rule]
          + γ small [Balaban's regime].

Next concrete steps:

- (i) Compute β^0_{[i,i+n]} for SU(2) in a simplified block scheme with the
  same structure (Gaussian block constraint, axial gauge in blocks) by exact
  lattice momentum sums. Verify 2b_0 n log L + O(1) and measure the edge
  constant. This is assigned as T13.
- (ii) Then identify the edge terms of Balaban's exact scheme (CMP 109
  (0.4) average, CMP 99 gauge fixing).
- (iii) Prove (D) from the localization structure of E^{(j)}: step-i
  contributions are marginal terms with factors (L^iη)^4 (CMP 119 §2, at (2.31)),
  so their effect on the step-j vacuum polarization should decay like
  L^{-(j-i)}.
