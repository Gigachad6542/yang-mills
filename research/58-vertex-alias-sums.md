# Vertex Riemann sums for (C): a general alias-sum convergence lemma

Status:

- **Proved here.** Lemma A, a quantitative convergence lemma for alias sums
  Σ_n f_M(n) W_M(n) with Dirichlet-product weights and symbols growing like
  (1 + |q|)^s, s < 1. It contains note 47 Theorem 1 as the case s = 0.
- **Proved here (§2a).** Lemma A2, the extension to several coupled alias
  variables (the background's own aliases), and convergence of the
  P-derivatives by analyticity in a strip.
- **Proved here (§6, T69).** The ghost and gauge-fixing vertices, expanded to
  second order in the background, have alias symbols with growth exponent
  s <= -3 (unweighted middle lines of chains: s = 0), so (V)(b) holds for them,
  under the readings R1-R4 of §6.0. For sums in which the background's own
  aliases couple lines that carry only one power of the Dirichlet product,
  Lemma A2 does not apply as stated; §6.5 proves a replacement (Lemma A3, rate
  M^{-1+ε}).
- **Conditional.** Proposition B. Assume the structural form (V) below.
  Then item 4 of note 48 (the vertex Riemann sums) holds with rate
  O((1 + log M)/M), and (C) of note 22 follows with rate
  ϑ = L^{-1+ε}.

Item 4 of note 48 thereby moves from "stated" to "reduced to the form
(V)". (V) is a statement about how Balaban's free vertices are written in
alias variables. It is checked here for the leading gluon terms, but not
for every term of CMP 109 §5.

## 1. Notation (as in note 47)

- d >= 1. Fix K ∈ (-π, π]^d and an integer M >= 2.
- For n ∈ Z^d, put q_n = K + 2πn and p_n = q_n/M. Let
  B_M = {n : -M/2 < n_j <= M/2}.
- Coordinate weights (note 47 step 2):

      δ_M(n_j) = |sin(K_j/2)| / (M |sin(q_{n,j}/(2M))|)   (n ∈ B_M),
      δ_∞(n_j) = 2 |sin(K_j/2)| / |q_{n,j}|               (n ∈ Z).

- For exponents a_j >= 2, put W_M(n) = Π_j δ_M(n_j)^{a_j} and
  W_∞(n) = Π_j δ_∞(n_j)^{a_j}.

Elementary facts:

- (W1) δ_∞(n_j) <= min(1, 2/|q_{n,j}|). Also δ_M <= (π/2) δ_∞, because
  |sin x| >= 2|x|/π on |x| <= π/2.
- (W2) 0 <= δ_M² - δ_∞² <= sin²(K_j/2)/M² <= M^{-2}, by note 47 step 3.

## 2. Lemma A

Let f_∞ : R^d -> C and f_M : B_M -> C satisfy, for some F < ∞ and s < 1:

- (F1) |f_∞(q)| <= F (1 + |q|)^s;
- (F2) |f_M(n) - f_∞(q_n)| <= F |p_n| (1 + |q_n|)^s for n ∈ B_M.

Write s_+ = max(s, 0). Then the sum S_∞ := Σ_{n∈Z^d} f_∞(q_n) W_∞(n)
converges absolutely, and

    |Σ_{n∈B_M} f_M(n) W_M(n) - S_∞| <= C_{d,a,s} F (1 + log M) M^{s_+ - 1}.

*Proof.*

1. *Reductions.* Since 1 + |q| <= Π_j (1 + |q_j|), we have
   (1 + |q|)^s <= Π_j (1 + |q_j|)^{s_+}. Since a_j >= 2 and δ <= π/2, we have
   δ^{a_j} <= (π/2)^{a_j - 2} δ². So every sum below factorizes into
   one-dimensional sums of the form

       Σ_{|n|<=R} δ_∞(n)² (1 + |q_n|)^{s_+} |q_n|^e,   e ∈ {0, 1}.

   By (W1), δ_∞(n)² <= C(1 + |q_n|)^{-2}. So such a sum is <= C when e = 0,
   since s_+ - 2 < -1. When e = 1 it is <= C R^{s_+} (or C log R if
   s_+ = 0). Tails Σ_{|n|>R} δ_∞² (1 + |q|)^{s_+} are <= C R^{s_+ - 1}.
2. *Symbol error.*
   Σ_{B_M} |f_M - f_∞(q_n)| W_M <= F Σ_{B_M} |p_n| (1 + |q_n|)^s W_M.
   Bound |p_n| <= Σ_j |q_{n,j}|/M. The coordinate carrying |q_{n,j}|/M
   contributes C M^{-1} M^{s_+} (1 + log M). The other coordinates give
   bounded factors. Total: <= C F (1 + log M) M^{s_+ - 1}.
3. *Weight error.* Telescope one coordinate at a time. On the changed
   coordinate, |δ_M^{a} - δ_∞^{a}| <= C |δ_M² - δ_∞²| <= C M^{-2} by (W2).
   The sum over the M values of n_j, weighted by (1 + |q_{n,j}|)^{s_+} <= C M^{s_+},
   is <= C M^{s_+ - 1}. The unchanged coordinates give bounded factors.
4. *Tail.* Σ_{n∉B_M} |f_∞(q_n)| W_∞(n) <= C F M^{s_+ - 1}, by step 1 with
   R = M/2 in one coordinate.
5. Absolute convergence of S_∞ is step 1 with R = ∞. Adding steps 2-4
   gives the claim. ∎

*Remarks.*

- Note 47 Theorem 1 is the case s = 0. There f is the projector, and (F2)
  holds with |p_n| from the phases (note 47 step 5).
- The constant is uniform in K. If F depends on K, as an alias-0 symbol
  singular at K = 0 does, the bound holds pointwise with F(K).

## 2a. Lemma A2 (several coupled alias variables) and P-derivatives

**Lemma A2.** Consider sums over r alias variables n^{(1)}, ..., n^{(r)} ∈ Z^d.
Their weights are Π_i W^{(i)}(ℓ_i), where each ℓ_i is an integer linear
combination of the n^{(k)}, with independent coordinates. Example: for the
background-coupled vertex, r = 2 and the weights are
W(n) W'(n - m) W_b(m), with coarse momenta K, K - P and P. Each W^{(i)} is a
Dirichlet product as in §1, with exponents >= 2. Suppose the symbols satisfy
(F1)-(F2) with (1 + |q|)^s replaced by Π_i (1 + |q^{(i)}|)^{s_i}, each s_i < 1,
and |p| replaced by max_i |p^{(i)}|. Suppose also that the map
(n^{(1)}, ..., n^{(r)}) ↦ (ℓ_i)_i, restricted to any r of the ℓ_i, is
injective. Then the conclusion of Lemma A holds with s_+ := max(0, s_1, ..., s_r)
and a constant depending on r.

*Proof.* Everything factorizes by coordinates, as in Lemma A step 1. For
fixed j, change variables to r of the ℓ_i, which is injective by
assumption. Each remaining factor (1 + |q^{(i)}|)^{s_i - 2} is <= 1. So the
sum is at most a product of r one-dimensional sums of the type in Lemma A
step 1. The rest is the same:
- one coordinate, in one variable, carries |p|;
- one weight factor is changed at a time, at cost M^{-2} per term over the
  M values of that variable;
- tails are as in Lemma A step 4.

The coupling n' = n - m holds exactly mod M on the fine torus. The
wrap-around terms lie in the tails. ∎

**P-derivatives.** Without absolute values, the weights are products of
D_M(p) = sin(Mp/2)/sin(p/2) and phases, with p = (P + 2πm)/M. These are
analytic in P on the strip |Im P_j| <= η, and for small η the bounds (W1)
and (W2) hold there with constants depending only on η. So the sums of
Lemmas A and A2 converge uniformly on a complex neighbourhood of P = 0, at
the stated rate. By Cauchy's estimate, so do their P-derivatives of every
fixed order. In particular the P² coefficients converge, and these define
β_j^0 (note 41 §1). They include the background's own alias components,
which contribute at order P_j in every coordinate with m_j ≠ 0.

## 3. Proposition B (vertex sums, conditional on (V))

**(V) Structural form.** At the trivial background, each contribution to
the free polarization Π_j of note 41 §1, after the fine-site sums inside
blocks and rescaling to the step-j unit lattice, has coarse momentum
symbol equal to a finite sum of products of two kinds of factor:

- (a) coarse symbols already known to converge at rate O((1 + log M)/M):
  the block-flux covariance and its inverse on the exact subspace
  (note 47), the induced minimizer symbol (note 48 item 2), the averaging
  weights (note 41) and the step propagator G_j (note 41 Prop. 1, step 1);
- (b) alias sums Σ_{n∈B_M} f_M(n) W_M(n) satisfying (F1)-(F2) with s <= 0,
  with F(K) such that F(K) times the accompanying (a)-factors is integrable
  over K ∈ (-π, π]^4 uniformly in M.

**Proposition B.** Under (V), |Π̂_j(K) - Π̂_∞(K)| is bounded by
C (1 + log M)/M times an integrable majorant. Hence the second moments
converge, and

    |β_j^0 - β_∞^0| <= C (1 + j log L) L^{-j}.

*Proof.* Each (b)-factor converges at the rate of Lemma A with s_+ = 0.
Each (a)-factor converges at the same rate by the cited notes. A product of
finitely many convergent, bounded factors converges at the slowest rate,
by telescoping. The second moment ∂²_{p_μ p_ν} at background momentum 0 is a
fixed finite combination of such symbols, as in note 41 §1. Integrate over
K using the majorant in (V)(b). ∎

## 4. Checking (V) on the leading gluon terms

At the trivial background, the fine fluctuation field is A = H_j B, the
abelian minimizer map tensored with the identity on su(2) (notes 36 §2 and
48). In Landau gauge, A = Δ^{-1} J with J co-closed (note 44 step 1 and
note 45). Hence

    Â(p_n) = A_ρ(p_n) c(K) / |r(p_n)|²,   |A_ρ(p_n)| = M^{d+1} Π_j δ_M(n_j) · δ_M(n_ρ),

and |r(p_n)|² >= (4/π²)|p_n|² (note 44 step 3). Here c(K) collects the coarse
data and converges as in (a).

The background derivatives of the Wilson action at the trivial background
give the following lattice vertices between two fluctuation fields:

- V' (linear in the smooth background field b): symbols of degree 1 in the
  fine momenta, of the form ⟨∂A, [b, A]⟩;
- V'' (quadratic in b): symbols of degree 0, of the form ⟨[b, A], [b, A]⟩.

In the rescaled variable q_n = M p_n, a degree-k trigonometric polynomial
v satisfies |M^k v(p_n)| <= C|q_n|^k, and |M^k v(p_n) - v_cont(q_n)| <= C|p_n||q_n|^k.
This is the usual O(|p|) relative error of lattice symbols, with the phases
included. In an induced vertex Σ_n Â(p_n)* v(p_n) Â(p_n), each Â carries
the weight Π δ and a factor |q_n|^{-2} relative to its coarse prefactor.

So the alias symbol is f(q) ~ |q|^{k-4} relative to W, with
W = Π_j δ_M(n_j)² · δ_M(n_ρ)² (exponents a_j >= 2). That is:

- s = -3 for V';
- s = -4 for V''.

Both are within (F1)-(F2) with s <= 0. The alias-0 term is singular at
K = 0 like |K|^{k-4}. The accompanying step propagator G_j is the inverse
of the constrained quadratic form, which has the averaging penalty, and it
is bounded with exponential decay (O1). So the integrand of the second
moment is integrable. This is the integrability clause of (V)(b), checked
for these terms.

**Background aliases.** The background b on the fine lattice is itself
H_j applied to a coarse field of momentum P. Its alias components (P + 2πm)/M
contribute to the P² coefficient through sums coupled by n' = n - m. These
are covered by Lemma A2 together with the P-derivative remark of §2a.

**Not checked here (§4).** The same form for (the first item is done in §6):

- the ghost and gauge-fixing vertices (§6);
- the background dependence of the covariant average Q(U) inside the
  penalty Σ_i a_i |Q_i(U) A|² (note 50 §1 flags its second-order part);
- the exact way CMP 109 §5 groups the terms.

Each is a finite combination of lattice symbols and averaging kernels. For
each, (V) amounts to bounding the degree k <= 2 and identifying the
Dirichlet weights. The averaging-kernel derivatives carry the same δ-products
as W, by note 19 (2.1).

## 5. Effect

(C) of note 22 now rests on:

- Lemma A (proved);
- notes 41, 47 and 48 (proved);
- the bookkeeping statement (V), checked for the leading gluon vertices.

The other H0 inputs are unchanged: (S) needs the edge bound (E) of note 50,
and (D) needs the single-step inputs.

## 6. Ghost and gauge-fixing vertices (T69)

Result. Under the readings R1-R4 below, every vertex of the ghost operator
and of the gauge-fixing operators `D_b D_b^*` and `D_b R_b D_b^*` has an
alias symbol of total growth exponent s <= -3, and every weighted line decays
at least like (1 + |q|)^{-1}. So (V)(b) holds with s <= 0, with rate
(1 + log M)/M for uncoupled sums (Lemma A) and M^{-1+ε} for
background-coupled sums (Lemma A3). No vertex has exponent >= 1. Status:
**proved here**, modulo R1-R4 and the items of §6.8.

### 6.0 Operators and reading

Balaban's scheme, from the OCR. The displayed formulas are garbled, so the
following symbols are **reconstructed**, not read off.

- CMP 99 (3.23)-(3.25): the covariant Laplacian on gauge parameters is
  `Δ_U = D_U^* D_U` (OCR: "Δ ηv = DΐDl"); `Δ'_a = Δ_U + Q'^* a Q'` with
  Dirichlet conditions (3.24); `G' = (Δ'_a)^{-1}`; the Landau projector
  `R(U) = I - G' Q'^*(Q' G'^2 Q'^*)^{-1} Q' G'` (3.25) is an orthogonal
  projection onto `Δ_U N(Q')` (3.21).
- CMP 99 (3.26): `Δ_a = Δ + D R D^* + Q^* a Q`. The first term is OCR'd as
  "A"; I read it as the quadratic form of the action (not needed here).
  `D R D^*` is the gauge-fixing term.
- CMP 99 (3.160)-(3.166): the Faddeev-Popov identity inserts
  `|det(Δ_U|_{N(Q')})|`, the ghost determinant on `N(Q') = {λ : Q'λ = 0}`.
- CMP 109 (0.14)-(0.16), (2.5): after the Faddeev-Popov step the gauge
  fixing is an exponential density in the contour variables `U(y,x)`. In the
  fluctuation variable `B'` of (2.5) it reads `W_2(B') + G_3(B')`, with `W_2`
  a sum of `|B'(y,x)|^2` and `G_3` cubic and localized in blocks. I read
  `W_2` as independent of the background. Then it contributes no `V', V''`,
  and its background dependence sits in the maps `H_k` and `Q` (the
  (a)-factors). See §6.8 for the alternative.

Readings used (R1 and R2 are the conventions of notes 23 §1 and 58 §4):

- **R1.** Fixed linear averages `Q' = Q_0` (box average; exact at `U = 1`).
  The `U`-dependence of the covariant average `Q(U)`, in `N(Q'(U))`, `G'(U)`
  and `R(U)`, is out of scope (T69 statement; note 50 §1).
- **R2.** Fluctuation fields entering vertices are *minimizer-type* (MT):
  `F̂(p_n) = ŵ(p_n) m(p_n) c(K)` with `|ŵ(p_n)| = Π_j δ_M(n_j)` (times one extra
  `δ_M(n_ρ)` for the 1-form flux), `|m(p)| <= C|r(p)|^{-2}`, and `c(K)` coarse
  data. The gluon `A = H_j B` is as in §4 (Landau, `R D_0^* A = 0`; in the
  abelian trivial-background case even `D_0^* A = 0`). The ghost is
  `λ = G Q_0^*(Q_0 G Q_0^*)^{-1} ĉ`, so `|λ̂(p_n)| = Π_j δ_M(n_j) |r(p_n)|^{-2} c_gh(K) |ĉ|`
  (the scalar box average has Dirichlet factor `ŵ_0`, `|ŵ_0| = Π_j δ_M(n_j)`).
  The background `b` is the *linear* lift `H_j b_c` of a coarse field, so it
  is MT with decay 2. Its second-order part is not treated (§6.8).
- **R3.** Traces are taken in the Schur form
  `log det_{ker Q} H = log det H + log det(Q H^{-1} Q^*) + const` (note 23
  (2.1)). The first term is an unconstrained fine-lattice loop with no
  Dirichlet weights. It is **not** of the form (V)(b), and is not treated
  here, for gluons or ghosts. The same gap is present in §4.
- **R4.** Rescaling as in §4: a vertex with `k` lattice differences has
  rescaled symbol `M^k v(p)`, with `|M^k v| <= C|q|^k` and
  `|M^k v - v_cont(q)| <= C|p||q|^k`.

### 6.1 Ghost operator to second order

Let `X_μ(x) = ad b_μ(x)` (antisymmetric on `su(2)`), `E = e^{X}`,
`(D_b λ)(x,μ) = λ(x+μ) - E_μ(x) λ(x)`, `M(b) = D_b^* D_b`. Since `E` is
orthogonal, `|D_bλ|^2 = |λ(x+μ)|^2 + |λ(x)|^2 - 2⟨λ(x+μ), E λ(x)⟩` exactly. With
`E = 1 + X + X²/2 + O(b³)` the symmetric bilinear forms are

    ⟨λ, M_0 λ'⟩ = Σ ⟨∂_μλ, ∂_μλ'⟩,   symbol |r(p)|^2,  r_μ(p) = e^{ip_μ} - 1,
    ⟨λ, M_1 λ'⟩ = -Σ [⟨∂_μλ, X_μ λ'⟩ + ⟨∂_μλ', X_μ λ⟩],                k = 1,
    ⟨λ, M_2 λ'⟩ = -½ Σ [⟨λ(x+μ), X_μ² λ'(x)⟩ + ⟨λ'(x+μ), X_μ² λ(x)⟩],  k = 0.

`M_1` has one lattice difference because `⟨λ, Xλ'⟩ + ⟨λ', Xλ⟩ = 0`. `M_2` has
none: the would-be derivative seagull `-⟨∂λ, X²λ⟩` combines with
`|Xλ|^2 = -⟨λ, X²λ⟩` into `-⟨λ(x+μ), X²λ(x)⟩`, a phase times `b²`.

Put `T(b) = Q_0 M(b)^{-1} Q_0^*` on coarse sites. Then the constrained ghost
term of note 23 (1.1) is `-log det_{ker Q_0} M = -log det M - log det T + const`.
With `G = M_0^{-1}`, `T_0 = Q_0 G Q_0^*`, `T_1 = -Q_0 G M_1 G Q_0^*`,
`T_2 = Q_0 G M_1 G M_1 G Q_0^* - Q_0 G M_2 G Q_0^*`,

    second order of log det T = Tr T_0^{-1} T_2 - ½ Tr(T_0^{-1} T_1 T_0^{-1} T_1).

In alias variables (`e(n) = (G Q_0^*)(p_n) = ŵ_0(p_n)^* |r(p_n)|^{-2}`,
`c(K) = T_0(K)^{-1}`, background aliases `m, m'`, `ℓ = n - m`) there are three
terms:

    (Gh1) seagull:  c(K) Σ ē(n) M_2(n,ℓ') e(ℓ')                      lines n, ℓ' = n-m-m'
    (Gh2) chain:    c(K) Σ ē(n) M_1(n,ℓ) |r(p_ℓ)|^{-2} M_1(ℓ,ℓ') e(ℓ')
    (Gh3) bubble:   c(K) c(K-P) |Σ ē(n) M_1(n,ℓ) e(ℓ)|²-type product

In (Gh1) and (Gh2) both background aliases are summed, and in (Gh2) the middle
line `ℓ` carries no Dirichlet weight.

### 6.2 Gauge-fixing operators to second order

`(D_b^* a)(x) = Σ_μ [a_μ(x-μ) - E_μ(x)^{-1} a_μ(x)]`, so `D_b^* = D_0^* + D_1^* + D_2^* + ...` with

    D_0^* a = Σ_μ [a_μ(x-μ) - a_μ(x)]            (k = 1),
    D_1^* a = Σ_μ [b_μ, a_μ]                       (k = 0),
    D_2^* a = -½ Σ_μ [b_μ,[b_μ, a_μ]]             (k = 0).

**Feynman-type** (note 23 (1.1)): `⟨D_b^* a, D_b^* a'⟩` has

    V'  = ⟨D_0^*a, D_1^*a'⟩ + ⟨D_1^*a, D_0^*a'⟩                          k = 1,
    V'' = ⟨D_1^*a, D_1^*a'⟩ (k = 0) + ⟨D_0^*a, D_2^*a'⟩ + ⟨D_2^*a, D_0^*a'⟩ (k = 1).

If `D_0^*a = 0` (abelian trivial background, §4) then `V' = 0` and only
`⟨D_1^*a, D_1^*a'⟩` survives in `V''`. In general (`D_0^*a ≠ 0`, or an internal
unweighted line in a chain, which is not co-closed) the k = 1 entries stay.

**Balaban's** `D R D^*` (CMP 99 (3.26)): `⟨D_b^*a, R_b D_b^*a'⟩`, `R_b = 1 - P_b`,
with `P_b` the orthogonal projection of (3.21),
`P_b = G'Q^*(Q G'^2 Q^*)^{-1} Q G'`, `G' = G'(b) = (M(b) + Q^* a Q)^{-1}` under R1.
Since `P_b² = P_b` for all `b`: `P_0 P_1 P_0 = 0` and `(1-P_0) P_1 (1-P_0) = 0`.
For MT `a, a'` the Landau condition `R_0 D_0^* a = 0` says `v := D_0^*a ∈ ran P_0`.
Then:

- *order 1*: `⟨D_1^*a, R_0 v'⟩ + ⟨v, R_0 D_1^*a'⟩ - ⟨v, P_1 v'⟩ = 0 + 0 - 0`.
  So **V' = 0** on MT pairs, in general, not only when `v = 0`;
- *order 2*: `⟨D_1^*a, R_0 D_1^*a'⟩` (k = 0), the `P_1` cross terms
  `-⟨D_1^*a, P_1 v'⟩ - ⟨v, P_1 D_1^*a'⟩`, and `-⟨v, P_2 v'⟩`. The `D_2^*` terms drop
  because `R_0 v' = 0`.

`P_1` and `P_2` consist of `G'`-derivatives, `-G' M_1 G'` and the like, that is,
the ghost vertices of §6.1, together with the weights `ŵ_0` from `Q_0^*`, `Q_0`
and the coarse factors `(Q_0 G'^2 Q_0^*)^{-1}` and `(a^{-1} + Q_0 G Q_0^*)^{-1}`.
These are scalar Dirichlet sums of the same type as `T_0` (Lemma A with
s = -4 and s = -2). For a multi-level `Q'` (levels `i <= j`) each such factor is
a finite matrix in the level index with the same symbols.

### 6.3 Power counting (Lemma G)

A *term* is a chain of lines (fine momenta `p_i`) joined by vertices. End lines
and background lines are MT. Internal lines are propagators `G` or `G'`, with
`|G(p)| <= |r(p)|^{-2}`; `G'` differs from `G` by rank-one terms whose ends are
again MT lines with weight `ŵ_0`.

**Lemma G.** Suppose each vertex has at most one lattice difference (R4,
`k <= 1`), acting on one of its two adjacent non-background lines, and none
acts on a background line. Let every line have decay 2 before absorbing
differences. Then the rescaled symbol obeys

    |f_∞| <= C Π_i (1 + |q_i|)^{-σ'_i},
    |f_M - f_∞| <= C (Σ_i |p_i|) Π_i (1 + |q_i|)^{-σ'_i},

with `σ'_i >= 1` for every MT end line and every background line, and
`σ'_i >= 0` for every internal line. The total growth exponent is
`s_tot = Σ_v k_v - 2·#(MT end lines) - 2·#(internal lines)` (background lines
counted separately).

*Proof.* A difference at a vertex contributes `M|r_μ(p)|`, and
`M|r_μ(p)| <= |q| <= 1 + |q|` (R4). An end line is adjacent to one vertex, so it
receives at most one such factor: `σ' >= 2 - 1`. An internal line is adjacent
to two vertices: `σ' >= 2 - 2`. In (F2) each difference is replaced by its
continuum limit with error `<= C|p||q|`, because `|e^{ip} - 1 - ip| <= p²/2`.
The phases `e^{ip/2}` and the factors `M²|r|² = |q|²(1 + O(|p|²))` also differ
at relative order `|p|`. Telescoping over the factors gives the second line. ∎

### 6.4 Table of exponents

`s_tot` counts the two MT end lines (-4), internal lines (-2 each) and the
differences. The last column gives the per-line decays `σ'` of the worst
monomial after absorption (the others are better).

| family | term | k_tot | s_tot | σ' on weighted lines |
|---|---|---|---|---|
| ghost V' (`M_1`) | Gh3 factor `T_1` | 1 | -3 | (1,2) or (2,1); background 2 |
| ghost V'' seagull (`M_2`) | Gh1 | 0 | -4 | (2,2); backgrounds 2 |
| ghost chain (`M_1 G M_1`) | Gh2 | 2 | -4 | end lines (1,2), (2,1), (1,1) or (2,2); middle `>= 0`; backgrounds 2 |
| Feynman gauge fixing, V' | `⟨D_0^*a, D_1^*a'⟩` | 1 | -3 | 0 on MT pairs with `D_0^*a = 0`; else (1,2) |
| Feynman gauge fixing, V'' | `⟨D_1^*a, D_1^*a'⟩` | 0 | -4 | (2,2) |
| Feynman gauge fixing, V'' | `⟨D_0^*a, D_2^*a'⟩` | 1 | -3 | (1,2); absent if `D_0^*a = 0` |
| `D R D^*`, V' | all | - | - | vanishes on MT pairs (§6.2) |
| `D R D^*`, V'' | `⟨D_1^*a, R_0 D_1^*a'⟩` | 0 | -4 | (2,2) |
| `D R D^*`, V'' | `P_1`, `P_2` terms (ghost vertex inside) | 1-2 | -3 to -4 (as the ghost chain) | end lines `>= 1`; internal `>= 0` |

All entries have `s_tot < 1`; the largest is -3, equal to the gluon V' of §4.
The only lines with `σ' = 0` are *unweighted internal* lines, which sit
between two weighted lines and carry no Dirichlet factor.

For the uncoupled sums (P = 0, one alias variable, both ends carrying the same
`n`) the weight is `Π_j δ_M(n_j)^2 (· δ_M(n_ρ)^2)`, with exponents >= 2, and
(F1)-(F2) hold with `s = s_tot`. Lemma A then gives the rate
`C (1 + log M)/M`. The alias-0 term has `F(K) <= C |K|^{s_tot}`, as in §4.

### 6.5 Background-coupled sums: Lemma A3

*Gap in §4 and §2a.* With the background aliases `m`, each MT line carries a
single power of its Dirichlet product (`Π_j δ_M(n_j)`, `Π_j δ_M(ℓ_j)`, `Π_j δ_b(m_j)`),
not the exponent >= 2 required by Lemma A2. So Lemma A2 as stated does not
cover (Gh2), (Gh3) or the gluon V' with background aliases. The sentence in
§4 "covered by Lemma A2" should be read as "covered by Lemma A3". The decay of
the symbol, which Lemma A2 does not use in this way, compensates.

**Lemma A3.** Let `u` range over `(Z^d)^r` and let the lines be `ℓ_i = A_i u` (integer
forms, the same in every coordinate). Weighted line `i ∈ I_w` carries
`Π_j δ_i(ℓ_{i,j})^{a_{ij}}` with `a_{ij} >= 1` (`δ_i` for the coarse momentum `K_i`).
Assume `I_w` contains r lines with linearly independent forms, and that the
symbols satisfy the bounds of Lemma G with `σ'_i >= 1` on `I_w` (and
`σ'_i >= 0` on unweighted lines). Then, for every ε ∈ (0, 1/2),

    |Σ_u f_M W_M - Σ_{u ∈ Z^r} f_∞ W_∞| <= C_{ε,d,r,a} F M^{-1+ε}.

*Proof.* Let `s_j = |sin(K_j/2)|`, `x = q/(2M)`. From `0 <= 1/sin x - 1/x <= πx/12`
and `1/sin x <= π/(2x)` on `0 < x <= π/2`,

    (W3)  |δ_M(n) - δ_∞(n)| <= C s_j min(|q_n|/M², 1/|q_n|).

*Splitting the decay.* Since `1 + |q| >= 1 + |q_j|` for each coordinate, for any
θ_j >= 0 with Σ_j θ_j = 1 we have `(1+|q|)^{-1} <= Π_j (1+|q_j|)^{-θ_j}`. Fix a
coordinate j and take `θ_j = 1-ε`, `θ_{j'} = ε/(d-1)` for `j' ≠ j`.

(a) *Convergence.* In each coordinate the summand is at most
`Π_{i ∈ I_w} (1+|ℓ_i|)^{-1-θ}` with θ > 0. Choosing r independent lines, the
sum over u is a product of r one-dimensional sums with exponent > 1. So `S_∞`
converges absolutely.

(b) *Weight error.* Telescope one factor at a time (at most `d|I_w|` terms): the
factor of line i in coordinate j. Use the split with this j for all weighted
lines. The changed line contributes
`|δ_M - δ_∞| (1+|q_{ij}|)^{-(1-ε)} <= C min(|q|/M², 1/|q|)(1+|q|)^{-1+ε} <= C M^{-2+ε}`
for `|q| <= CM`, summed over the `<= CM` values of the variable along `ℓ_i`. Take
r−1 further weighted lines, independent of each other and of `ℓ_i`: each has
exponent `1 + (1-ε) > 1` in coordinate j, so they give a bounded factor. The
remaining weighted lines are bounded by `δ <= π/2`. The other coordinates give
bounded factors by (a). Total `C M^{-1+ε}`.

(c) *Symbol error.* A weighted line i carries `|p_i| <= Σ_j |q_{ij}|/M`. In
coordinate j, `|q_{ij}| (1+|q_{ij}|)^{-(1-ε)} <= (1+|q_{ij}|)^{ε}`, and with
`δ(ℓ_{ij}) <= C/(1+|q_{ij}|)` the sum along `ℓ_i` of `(1+|q|)^{-1+ε}` is
`<= C M^{ε}`. The other lines are treated as in (b). So the error is
`C M^{-1+ε}`.

(d) *Tail and wrap-around.* The finite sum runs over the torus. The terms with
some weighted line `|ℓ_{ij}| > M/2` are bounded by the same one-dimensional
sums over `|q| >= cM`, each `<= C M^{-1+ε}` by (a). I have **not** written the
wrap-around bookkeeping beyond this sentence; it is the one of the last
paragraph of Lemma A2 (§2a). ∎

*Application.* By Lemma G, `σ' >= 1` on all weighted lines of every entry of
the table (end lines and background lines), and in every sum the weighted
lines contain r independent ones: for (Gh3) r = 2 with lines `n, m` and
`ℓ = n-m`; for (Gh2) r = 3 with `n, m, m'` and `ℓ' = n-m-m'`. So (Gh1)-(Gh3) and
the gauge-fixing entries converge with rate `C_ε M^{-1+ε}` (coupled) or
`C(1+log M)/M` (uncoupled). That is within `ϑ = L^{-1+ε}` of note 22. The
P-derivatives are handled as in §2a (analyticity in a strip; the weights of
background lines with `m_j ≠ 0` carry `sin(P_j/2)`).

### 6.6 Integrability clause of (V)(b)

Take `F(K)` from the alias-0 value: `F(K) <= C |K|^{s_tot}` for single-variable
sums, and `|K|^{-a}|K-P|^{-b}` with `a + b = -s_tot` for coupled lines. The
accompanying scalar ghost factor is `c(K) = C_gh(K)^{-1}`, with
`C_gh^{(M)}(K) = Σ_n Π_j δ_M(n_j)² / (M²|r(p_n)|²)`. This is Lemma A with s = -2 and
`F(K) <= C|K|^{-2}`, so `|C_gh^{(M)} - C_gh^{(∞)}| <= C(1+log M)/M · |K|^{-2}`. From the
alias-0 term alone, with `δ_M(0) >= 2/π` and `M²|r(p_0)|² <= |K|²`,

    C_gh^{(M)}(K) >= (2/π)^{2d} |K|^{-2},  so  0 < c(K) <= C |K|²,

and `|c^{(M)} - c^{(∞)}| <= C(1+log M)/M · |K|²`. Then, uniformly in M:

- Gh3: `c(K) c(K-P) F <= C |K|²|K-P|² |K|^{-a}|K-P|^{-b}` with `a + b = 3`, `a, b ∈ {1, 2}`:
  bounded.
- Gh1: both ends at momentum K, `c(K) F <= C |K|² |K|^{-4} = C|K|^{-2}`, integrable
  over `(-π,π]^4`.
- Gh2: `c(K) F <= C|K|^{-2}` (the worst monomial, with middle line `σ' = 0`),
  integrable.

The gauge-fixing entries have the same end lines (A and b), hence the same
`F(K)`, and the accompanying gluon factors are those of §4. For the P²
coefficient (two P-derivatives acting on `c(K-P)` and on the line `K-P`) the
products `c(K')·|q_{K'}|^{-2}` are bounded and smooth in `K'`; I did not carry out
the derivative bookkeeping, which is the same as in §4.

### 6.7 Numerical check

`research/scripts/t69_vertex_exponents.py` (output in the `.out` file) evaluates the
rescaled alias sums at fixed `K ≠ 0`:

- d = 4, one variable: symbols `cos p_1` (k = 0, s = -4) and `sin p_1` (k = 1,
  s = -3) over `(M²|r|²)²`, and `C_gh^{(M)}(K)` (s = -2). The differences
  `|S_M - S_{2M}|` fall by a factor 4.0 per doubling of M (M up to 32).
- d = 2, two coupled variables `(n, m)`, `P ≠ 0`, with squared weights (the
  Lemma A2 structure) and with the true exponent-1 weights and an MT background
  line (the Lemma A3 structure): again a factor 4.0 per doubling (M up to 64).

So the measured rate is `M^{-2}` in all five cases, faster than the guaranteed
`M^{-1+ε}`, as for the covariance in note 47. This is evidence, not proof.

### 6.8 What is not covered

- The unconstrained terms `Tr(G V)`, `-log det M`, `½ log det H` of the Schur form
  (R3): no Dirichlet weights; the same gap as for the gluon in §4.
- The second-order part `b^{(2)}` of the background lift (quadratic in the coarse
  field). It enters through `M_1[b^{(2)}]` and `D_1^*[b^{(2)}]` with the same symbols,
  but its alias weights are those of a product of two MT fields and were not
  checked.
- The covariant-average dependence `Q'(U)` (out of scope) and the `U`-dependence
  of the Dirichlet domain `Ω_0`.
- The exponential gauge fixing of CMP 109 (2.5) in the variable `B'`: I read `W_2`
  as background independent from a garbled passage. If it is not, its vertices
  are line sums of `A` over block contours with parallel transport (degree 0,
  bounded symbols, Riemann-sum error `O(|p|)`), so s = -4 and the same lemmas
  apply.
- The wrap-around bookkeeping in Lemma A3 (d), and the P-derivative bookkeeping
  in §6.6.
