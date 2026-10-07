# (C) of note 22: geometric convergence of the free increments from operator convergence

Status:

- **Proved here.** Proposition 1: a perturbation lemma. If the free step
  operators and their background vertices converge geometrically in an
  exponentially weighted operator norm, and the step propagators are
  uniformly bounded in that norm, then the free increments β_j^0 converge
  geometrically. This is (C) of note 22.
- **Inputs.**
  - (O1) uniform weighted propagator bounds. These are published for the
    trivial background: CMP 95/96 and CMP 99 Theorem 3.3 at U = 1.
  - (O2) geometric convergence of the rescaled free step operators. For the
    composite linear average this is the exact box formula of note 19 (2.1),
    a Riemann sum with error O(L^{-j}). For the Laplacian and gauge-fixing
    parts it is lattice discretization at spacing L^{-j}. (O2) is checked
    here only for the averaging kernels and the weights a_j.
- **Effect.** H0 ⇐ (D) + (S) + (O2) + published inputs (note 22 Prop. D).
  The one remaining free-field input of H0 besides (S) is now an explicit
  convergence statement about Balaban's free operators.

## 1. Setting

At step j, after rescaling the coarse lattice to unit spacing, the free
(U = 1) fluctuation integral has a quadratic form K_j. It includes:

- the gauge-fixed lattice Laplacian on the finest lattice, which has spacing
  L^{-j} in these units;
- the averaging penalty Σ_{i<=j} a_i (L^{i-j})^{d-2} |Q_i A|² (CMP 99 (3.16));
- the ghost part.

Let V_j' and V_j'' be its first and second background derivatives. These are
local operators composed with the averaging maps. The free vacuum
polarization is the background Hessian of ½ log det K_j(U) at U = 1:

    Π_j = ½ Tr(G_j V_j'') - ½ Tr(G_j V_j' G_j V_j'),   G_j = K_j^{-1}.

Here the traces are per unit volume, with block-periodic kernels averaged
over block positions. Then β_j^0 = -½ ∂²_{p_μ p_ν} Π̂_j(0), μ ≠ ν
(CMP 109 (5.37)). Equivalently, β_j^0 is a fixed linear combination of
second moments Σ_y (x-y)_μ (x-y)_ν Π_j(x, y).

**Weighted norm.** For a kernel A(x, y) put

    ||A||_δ := sup_x Σ_y |A(x, y)| e^{δ|x-y|}.

It is submultiplicative, and |second moment of A| <= C_δ ||A||_δ.

## 2. Proposition 1

Assume:

- **(O1)** sup_j ||G_j||_δ <= C_G, sup_j ||V_j'||_δ, ||V_j''||_δ <= C_V;
- **(O2)** there are limits K_∞, V_∞', V_∞'' with
  ||K_j - K_∞||_δ, ||V_j' - V_∞'||_δ, ||V_j'' - V_∞''||_δ <= C_O ϑ^j, ϑ < 1.

Then G_∞ := K_∞^{-1} exists with ||G_∞||_δ <= 2C_G for large j, and

    |β_j^0 - β_∞^0| <= C ϑ^j,   C = C(C_G, C_V, C_O, δ).

*Proof.*

1. *Propagators.* By the resolvent identity,
   G_j - G_l = G_j (K_l - K_j) G_l. With (O1),
   ||G_j - G_l||_δ <= C_G² · 2C_O ϑ^{min(j,l)}. So G_j is Cauchy in ||·||_δ.
   Its limit G_∞ inverts K_∞, and ||G_j - G_∞||_δ <= 2C_G² C_O ϑ^j.
2. *Polarization kernels.* The kernels of G_j V_j'' and of G_j V_j' G_j V_j'
   are products of three or four weighted-bounded factors. A telescoping
   difference with one factor replaced at a time gives
   ||Π_j - Π_∞||_δ <= C' ϑ^j. The trace per unit volume of a block-periodic
   kernel is an average of finitely many diagonal entries, so the same
   bound holds for the kernels whose moments define β.
3. *Moments.* |β_j^0 - β_∞^0| <= C_δ ||Π_j - Π_∞||_δ <= C ϑ^j. ∎

Combined with note 22 Prop. D, this gives (U), and then (W) by Cor. C. The
limit β_∞^0 is forced to equal 2b_0 log L by (S).

## 3. What (O1) and (O2) are

**(O1)** At U = 1, Balaban's propagators have exponential decay uniformly
in the step, with the scale-dependent factors (L^jη)^{...} of CMP 99
(3.42)-(3.47) (Theorem 3.3, specialized to U = 1, which goes back to
CMP 95/96). In rescaled units these become uniform weighted bounds. The
vertices V', V'' are local in the fine lattice, composed with averaging
maps, so they are bounded in ||·||_δ.

**(O2)** has three parts.

1. *Averaging.* By note 19 (2.1), the composite linear average over M = L^j
   fine cells is the exact box formula M^{-4} Σ_{u∈[0,M)^4} Σ_{s,t}. In
   rescaled units it is a Riemann sum for the continuum box average, with
   kernel error O(1/M) = O(L^{-j}) in ||·||_δ. Each level i < j enters the
   penalty with relative weight (L^{i-j})^{d-2}, so the tail of the sum is
   O(L^{-(d-2)j'}) beyond depth j'.
2. *Weights.* a_j = a(1 - L^{-2})/(1 - L^{-2j}) converges to a(1 - L^{-2})
   at rate L^{-2j} (CMP 99, recursion before (3.26)).
3. *Laplacian, gauge fixing and ghosts* on the fine lattice with spacing
   L^{-j}: these are standard discretizations of their continuum limits.
   Acting on functions smooth at the coarse scale they converge at rate
   L^{-j}. Since G_j is smoothing at the coarse scale, the weighted
   convergence required in (O2) holds on the range that matters.

   This last point is stated, not proved. Making it precise needs two
   things:
   - a common space for the operators of different j, since the fine
     lattice changes with j; for example, piecewise-constant extension to
     the continuum, or comparison of the induced coarse-lattice kernels
     only;
   - a two-scale version of (O1): bounds on G_j(K_j - K_∞) that use the
     smoothing of G_j.

   Proposition 1 holds verbatim for the induced coarse-lattice kernels. So
   the second item is the one non-elementary step left in (O2).
   **§5 proves the second item** for the free abelian step with the top-level
   linear average (Theorem 2 there), with rate (1 + log M)/M.

So ϑ = L^{-1} is the expected rate. It is consistent with the scalar
calibration of note 23, where the window edge converges.

## 4. Status of H0 after this note

    H0 <= (B), regularity [published]
        + (D) memory decay [notes 29, 31, 40: single-step reduction; open]
        + (S) finite one-loop scheme matching [universal part published]
        + (O2) operator convergence [averaging and weights: done here;
               discretization part: two-scale (O1), stated]
        + (O1) [published].

## 5. Two-scale (O1): the induced coarse kernel of G_j converges (T68)

Status:

- **Proved here** (Theorem 2): for the free abelian Gaussian step with
  Balaban's linear average at the top level, in the alias model (M1)-(M3)
  below, the induced coarse kernels of G_j converge to those of G_∞ in
  ‖·‖_δ at rate C(1 + log M)/M = C(1 + j log L)L^{-j}, i.e.
  ϑ = L^{-1+ε}. The same argument gives (O1) for the induced kernels,
  uniformly in j. The inputs are Lemmas A and A2 of note 58 (proved there)
  and an explicit Schur-complement inverse (Lemma 3).
- **Not covered** (§5.6): the lower levels i < j of the penalty, the
  non-Feynman gauge fixing, the constrained ghost (a = ∞), and the
  background-dependent covariant average.
- Data: `research/scripts/t68_two_scale_green.py` (output `.out`).

### 5.1 The model

Take the infinite coarse lattice Z^d (d = 4 intended) and a coarse momentum
K in the strip S_η = {K ∈ C^d : Re K ∈ (-π, π]^d, |Im K_j| <= η}. Put
M = L^j, q_n = K + 2πn, p_n = q_n/M. The fine alias set is
B_M(K) = {n : Re q_{n,j}/M ∈ (-π, π]}. Every fine-lattice quantity below is
M-periodic in n, so the choice of residue system does not matter. The
*alias 0* is the n with Re q_{n,j} ∈ (-π, π] for all j.

- **(M1) Laplacian.** The fine Laplacian-type part is diagonal in the
  aliases, Λ_M = diag λ_M(n), with
  λ_M(n) = Σ_j (2M sin(q_j/2M))², and λ_∞(q) = |q|². This is the lattice
  Laplacian on a scalar, and also the Hodge Laplacian d*d + dd* on
  one-forms in Feynman gauge, componentwise.
- **(M2) Linear average.** The top-level average Q_j gives, per component,
  the alias vector w_M(n) = Π_j Φ_M(q_j)^{e_j}, with e_j ∈ {1, 2} (e_j = 2
  in the tent direction of a link), where

      Φ_M(q) = M^{-1} Σ_{s=0}^{M-1} e^{-iqs/M}    (entire),
      Φ_∞(q) = (1 - e^{-iq})/(iq).

  This is note 19 (2.2)-(2.3), with the normalization
  |w_M(n)| = Π_j δ_M(n_j)^{e_j} of note 58 §1. In particular Σ|w|² <= 1
  and |w_M(0)| >= (2/π)^{Σe_j} =: c_*.
- **(M3) Step operator.** K_M(K) = Λ_M + a_M w_M w_M^†, K_∞(K) = Λ_∞ +
  a_∞ w_∞ w_∞^† on ℓ²(Z^d), with a_∞ > 0 and |a_M - a_∞| <= C_a M^{-2}
  (note 41 §3, item 2: the error is L^{-2j}). Here w^†(K) := conj(w(conj K))^T
  is the analytic continuation of the adjoint, and G_M = K_M^{-1}. At real K
  this is the quadratic form "Laplacian + a_j|Q_jA|²" of §1 at coarse
  momentum K, with the coarse cell as unit of length.

**Test vectors.** A *test family* u = (u_M)_{M<=∞} is
u_M(n) = F_M(q_n) Π_j Φ_M(q_j)^{ε_j}, ε_j ∈ {1, 2}, with F_M analytic on the
strip and, for some s_u <= 1 and a constant C_u,

    |F_∞(q)| <= C_u(1+|q|)^{s_u},  |F_M(q) - F_∞(q)| <= C_u (|q|/M)(1+|q|)^{s_u}  (|q| <= πM√d).

Examples: w itself, the alias-0 vector e_0 (a single coarse point), and
y = Λ^{-1}w. These are the shapes in which G_j meets the vertices composed
with averaging maps (note 58 §4). The *induced coarse symbol* is
Ξ_M[u, v](K) := ⟨u_M, G_M v_M⟩ = u_M^† G_M v_M, and its coarse-lattice
kernel is the inverse Fourier transform in K.

### 5.2 Statement

**Theorem 2.** Fix d, e, a_∞, C_a and two test families u, v. There are
η_1 > 0, M_0 and C, depending on these data only, such that for all
K ∈ S_{η_1} and M >= M_0:

1. K_M(K) and K_∞(K) are invertible, and |Ξ_M[u,v](K)| <= C;
2. |Ξ_M[u,v](K) - Ξ_∞[u,v](K)| <= C(1 + log M)/M;
3. for the kernels on the coarse lattice,
   ‖Ξ_M - Ξ_∞‖_δ <= C_δ(1 + log M)/M and ‖Ξ_M‖_δ <= C_δ for every δ < η_1.

In particular, with M = L^j,

    ‖Ξ_j[u,v] - Ξ_{j+1}[u,v]‖_δ <= C (1 + j log L) L^{-j}.

This is the induced-kernel form of (O1) and (O2) for G_j, and it is what
Proposition 1 step 1 uses.

### 5.3 Lemmas

**Lemma 1 (uniform ellipticity).** There is η_1 > 0 such that for all
K ∈ S_{η_1}, M >= 2 and n ≠ alias 0, |λ_M(n)| >= 2 and |λ_M(n)| >= c|q_n|².

*Proof.* For real K and n ≠ 0, some j has |q_j| >= π and |q_j/2M| <= π/2,
so 2M|sin(q_j/2M)| >= 2|q_j|/π >= 2 and λ_M(n) >= (4/π²)|q_n|² >= 4. For
complex K, |dλ_M/dq_j| = |2M sin(q_j/M)| <= 2|q_j| e^{η/M},
so |λ_M(K+iτ) - λ_M(K)| <= C η(|q| + η), which is a fraction O(η) of
λ_M(K) for n ≠ 0. ∎

**Lemma 2 (the two-scale gain).** For n ∈ B_M(K) with real K,

    |1/λ_M(n) - 1/λ_∞(q_n)| <= (π²/48) M^{-2}.

For n ∉ B_M, 1/λ_∞(q_n) <= C M^{-2}. Hence D_M = Λ_M^{-1} on B_M, extended
by 0, differs from D_∞ = Λ_∞^{-1} (n ≠ 0) by at most C M^{-2} in operator
norm on ℓ²(Z^d).

*Proof.* λ_∞ - λ_M = Σ_j q_j²(1 - (sin x_j/x_j)²) with x_j = q_j/2M, and
1 - (sin x/x)² <= x²/3. So 0 <= λ_∞ - λ_M <= |q|⁴/(12M²). With
λ_M >= (4/π²)|q|² and λ_∞ = |q|²,
|λ_∞ - λ_M|/(λ_M λ_∞) <= (π²/4)/(12M²). If n ∉ B_M, some |q_j| > πM - π. ∎

*Remark (what "two-scale" means here).* K_M - K_∞ has size |q|⁴/M² and is
unbounded. Bounding (K_M - K_∞)G_∞ naively needs G_∞ to gain four powers
of |q|, which it does not: w ∈ H^t only for t < 1/2. The gain is in the
*resolvent* error (λ_∞ - λ_M)/(λ_M λ_∞) <= C M^{-2}: two factors of G
absorb the four powers of |q|. Exactly, let K̃_M be K_M extended to ℓ²(Z^d)
by λ_∞ outside B_M and by w̃_M = w_M extended by 0. Then

    G_∞ - G̃_M = G̃_M (K̃_M - K_∞) G_∞,

and the Laplacian part of K̃_M - K_∞ sits between two factors of size
|q|^{-2}. The proof below does not use this identity; it computes G_M
directly from Lemma 3.

**Lemma 3 (Schur inverse).** Let i_0 be the alias 0, write ⊥ for the other
aliases, and let ⟨x, z⟩ = x^† z. Put y = Λ_⊥^{-1} w_⊥, and

    τ = a⟨w_⊥, y⟩ = a Σ_{n≠0} w_n^† w_n/λ_n,   s = λ_0 + a w_0^† w_0/(1+τ),
    κ = a w_0^†/(1+τ),   κ' = a w_0/(1+τ).

Then, whenever 1 + τ and s are nonzero,

    G = diag(1/s, Λ_⊥^{-1}) - (κ'/s) e_0 y^† - (κ/s) y e_0^† + (κκ'/s - a/(1+τ)) y y^†.

Equivalently, for any u, v,

    ⟨u, G v⟩ = (u_0^† - κ A_{uw})(v_0 - κ' A_{wv})/s + A_{uv} - a A_{uw}A_{wv}/(1+τ),
    A_{xz} := Σ_{n≠0} x_n^† z_n/λ_n,   τ = a A_{ww}.

*Proof.* Write K in blocks (0, ⊥). The ⊥ block is S = Λ_⊥ + a w_⊥w_⊥^†.
Sherman-Morrison (Λ_⊥ is invertible by Lemma 1) gives
S^{-1} = Λ_⊥^{-1} - a y y^†/(1+τ), so S^{-1}w_⊥ = y/(1+τ). The off-diagonal
block is b = a w_0^† w_⊥ (a column), and S^{-1}b = κ y. The Schur complement
is s = λ_0 + a|w_0|² - b^†S^{-1}b = λ_0 + a|w_0|²(1 - a w_⊥^†S^{-1}w_⊥), and
1 - a w_⊥^†S^{-1}w_⊥ = 1/(1+τ). The block inverse
[[1/s, -b^†S^{-1}/s], [-S^{-1}b/s, S^{-1} + S^{-1}bb^†S^{-1}/s]] is the
stated formula. Pairing with u, v gives the second form. ∎

(Checked against the dense inverse from `numpy.linalg.eigh`: max
difference 2e-16 to 1e-14, d = 2, 4, M <= 16; see §5.5.)

**Lemma 4 (strip to weighted norm).** Let a(K) be 2π-periodic and analytic
on |Im K_j| < η, continuous on the closure, |a| <= ε there, and a(x) its
Fourier coefficients. Then for δ < η,

    Σ_x |a(x)| e^{δ|x|} <= ε (coth((η-δ)/2))^d.

*Proof.* Shift the contour K → K + iη sgn(x_j) in each coordinate:
|a(x)| <= ε e^{-η|x|_1}. Then use |x|_2 <= |x|_1 and sum the geometric
series. ∎

### 5.4 Proof of Theorem 2

*Step 1: building blocks.* By Lemma 3, Ξ_M[u,v] is a rational function R of
the following scalars, with the same R for M = ∞ (with Λ_∞, w_∞, u_∞, v_∞,
a_∞ and sums over Z^d ∖ {0}):

    λ_0, w_0, u_0, v_0, a, and the alias sums A_{uv}, A_{uw}, A_{wv}, A_{ww}.

*Step 2: the scalars converge.*

- λ_0 = λ_M(i_0): |λ_M(0) - |K|²| <= |K|⁴/(12M²), by Lemma 2.
- w_0, u_0, v_0 are single entries at q_0 = K, with |K| <= C. Since
  Φ_M(q) = Φ_∞(q)ρ_M(q) with ρ_M(q) = g(q/2M), g(ζ) = e^{iζ}ζ/sin ζ,
  analytic near |Re ζ| <= 2.5, |Im ζ| <= 1 with g(0) = 1, we get
  |ρ_M - 1| <= C|q|/M there. So |w_0^M - w_0^∞| <= C/M, and likewise for
  u_0, v_0 (by the assumption on F_M).
- Each A_{xz} is a sum Σ_{n∈B_M, n≠0} f_M(n)W_M(n) of the form in Lemma A
  (note 58 §2), with W_M = Π_j δ_M(n_j)^{ε_j+ε'_j} and exponents
  ε_j + ε'_j >= 2. For real K, Φ_M(q) = δ_M θ_M with
  θ_M = χ e^{-iq(M-1)/2M}, where χ = ±1 depends only on (K_j, n_j), not on
  M. So conj(Φ_M^{ε}) Φ_M^{ε'} = δ_M^{ε+ε'} θ_M^{ε'-ε}, and
  θ_M/θ_∞ = e^{iq/2M} differs from 1 by at most |q|/2M. Thus
  f_M(n) = F_x^† F_z θ_M^{ε'-ε}/λ_M(n) satisfies (F1) with
  s = s_x + s_z - 2 <= 0 < 1 (since λ_M >= c|q|² on n ≠ 0, Lemma 1), and
  (F2): |f_M - f_∞| <= C|p_n|(1+|q|)^s, using |1/λ_M - 1/λ_∞| <= C|p|²/λ_∞
  and the O(|p|) errors of F_M and of the phase ratio. Removing n = 0
  changes nothing (set f(0) = 0). Lemma A gives
  |A^M - A^∞| <= C(1 + log M)/M, uniformly in K. For complex K the same
  holds by the strip remark of note 58 §2a (the weights δ_M, δ_∞ are
  replaced by their analytic continuations; (W1), (W2) hold with
  η-dependent constants).

*Step 3: denominators.* For real K, A_{ww} = Σ_{n≠0}|w_n|²/λ_n ∈ [0, 1/4]
(Lemma 1 and Σ|w|² <= 1), so 1 + τ ∈ [1, 1 + a/4]. Further
s >= a|w_0|²/(1+τ) >= a c_*²/(1 + a/4) =: s_* > 0. All scalars of Step 1
are analytic on a strip of width 2η_1 and bounded there uniformly in M, so
by Cauchy's estimate they are Lipschitz in Im K with a uniform constant.
For η_1 small, |1+τ| >= 1/2 and |s| >= s_*/2 on S_{η_1}, for M and for ∞
(the limit is the same expression). This gives invertibility and
|Ξ_M| <= C (part 1): R is a rational function of bounded scalars with
denominators bounded below.

*Step 4: part 2.* R is Lipschitz on the bounded region of its arguments
where the denominators are at least s_*/2 and 1/2. So
|Ξ_M - Ξ_∞| <= C Σ |scalar_M - scalar_∞| <= C(1 + log M)/M. The change
a_M → a_∞ adds C_a M^{-2}.

*Step 5: part 3.* Ξ_M and Ξ_∞ are analytic on S_{η_1} with the bounds of
parts 1-2 on the closed strip. Apply Lemma 4 to Ξ_M - Ξ_∞ and to Ξ_M. ∎

**Corollary 5 (structure of G_j).** G_M = D_M + R_M with
D_M = diag(1/s, Λ_⊥^{-1}) and R_M of rank at most 3 on span{e_0, y_M}, with
coefficients (κ'/s, κ/s, κκ'/s - a/(1+τ)) that converge at rate
(1 + log M)/M by Steps 2-4. So any contraction of G_j with a vertex whose
alias symbol has the form (V) of note 58 §3 is a sum of
(i) Lemma A / A2 alias sums with weight symbol 1/λ_M (s = -2) from the
diagonal D_M, and (ii) products of the convergent scalars above. This is
what Proposition 1 needs from G_j, and it gives (O2) for the induced
kernels of G_j with the rate of note 58 Prop. B, provided (V) holds for
the vertices.

### 5.5 Numerical check

`t68_two_scale_green.py`: exact dense eigendecomposition (`numpy.linalg.eigh`,
no pseudoinverse) against the Schur formula; a = 1, e = (1,...,1), second
test vector w' with e' = (2,...,2). Sup over a K grid of |Ξ_M - Ξ_{2M}| for
Ξ = (⟨w,Gw⟩, ⟨w,Gw'⟩, G_00):

| d | M -> 2M | ⟨w,Gw⟩ | ratio | ⟨w,Gw'⟩ (mixed e) | ratio | G_00 | ratio |
|---|---|---|---|---|---|---|---|
| 2 | 8 -> 16 | 1.66e-3 | 3.96 | 1.12e-2 | 2.06 | 8.8e-4 | 4.10 |
| 2 | 16 -> 32 | 4.16e-4 | 3.99 | 5.54e-3 | 2.02 | 2.19e-4 | 4.02 |
| 2 | 32 -> 64 | 1.04e-4 | 4.00 | 2.76e-3 | 2.00 | 5.46e-5 | 4.01 |
| 4 | 8 -> 16 | 1.36e-3 | 3.75 | 1.88e-2 | 2.03 | 3.5e-4 | 3.99 |
| 4 | 16 -> 32 | 3.50e-4 | 3.89 | 9.36e-3 | 2.01 | 8.8e-5 | 4.00 |

(d = 4 on the K grid {0.9, 2.2, -1.4}⁴, using the Schur formula;
d = 2 on 5 points per axis. Schur and dense agree to 1e-14 for d = 2, 4,
M <= 16.) The Laplacian resolvent gap of Lemma 2 satisfies
M² sup_n|1/λ_M - 1/λ_∞| = 0.113, 0.128, 0.137, 0.143, 0.146, 0.147 for
M = 4, 8, ..., 128 (d = 1, K = π), below the proved constant
π²/48 = 0.206.

So pairings with matched exponents converge at M^{-2}. The mixed-exponent
pairing converges at exactly M^{-1}: the phase factor θ_M^{ε'-ε} has a
first-order error that does not cancel. Hence the rate L^{-j} is sharp for
this test family, and the proved (1 + log M)/M loses at most a logarithm;
no logarithm is visible numerically.

### 5.6 What extends, and what does not

- **Gauge-fixing term, Feynman gauge.** d*d + dd* is the Laplacian
  componentwise, which is (M1). Verbatim.
- **Gauge-fixing term, general α > 0.** The alias block is the d×d matrix
  |r|²(P_T + α^{-1}P_L), P_L = r r^†/|r|². Its inverse (P_T + αP_L)/|r|² is
  uniformly elliptic with constants min(1, α). The projectors carry phases
  and a symbol error O(|p|) as in note 47 step 5, so (F1)-(F2) hold with
  matrix-valued f. The Schur step of Lemma 3 becomes a d×d matrix Schur
  complement for the alias-0 block. Plausible, **not written**.
- **Ghost operator.** At U = 1 the ghost kernel is the scalar Laplacian
  Λ_M. With no penalty it is exactly Lemma 2 (rate M^{-2}), verbatim. If the
  ghost is constrained by Q_j ξ = 0, this is the limit a → ∞: then
  s → λ_0 + |w_0|²/A_{ww}, which is still bounded below, but
  κ = w_0^†/A_{ww} and A_{ww} → 0 as K → 0 (because |w_⊥|² = 1 - |w_0|² → 0
  for e = 1). The combination in Lemma 3 should stay finite, but the
  Lipschitz bound of Step 3 is not uniform as written. **Needs a separate
  estimate near K = 0**, not done.
- **Lower penalty levels i < j.** Each is a sum over cosets of rank-one
  terms with Dirichlet weights of block size M L^{i-j}, with prefactor
  (L^{i-j})^{d-2}. The structure is similar, but the Schur complement has
  rank growing with j - i. Truncating at depth k costs O(L^{-(d-2)k}) in
  operator norm only, and the weighted-norm version is not checked. Not
  written. This is the main gap between the model (M1)-(M3) and Balaban's
  K_j.
- **Covariant average at U ≠ 1.** Out of scope (note 50 §1).

### 5.7 Effect on H0

The second item of §3 (two-scale (O1)) is **proved for the model**, with the
rate of Lemma A, ϑ = L^{-1+ε} (measured: L^{-1} for mixed pairings, L^{-2}
for matched ones). With §3 items 1-2 this gives (O2) for the free abelian
step in Feynman gauge with the top-level penalty. In the §4 summary, "two-scale
(O1), stated" becomes "proved for the model; multi-level penalty and
constrained ghost open".
