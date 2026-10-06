# Vertex Riemann sums for (C): a general alias-sum convergence lemma

Status:

- **Proved here.** Lemma A, a quantitative convergence lemma for alias sums
  Σ_n f_M(n) W_M(n) with Dirichlet-product weights and symbols growing like
  (1 + |q|)^s, s < 1. It contains note 47 Theorem 1 as the case s = 0.
- **Conditional.** Proposition B. Assume the structural form (V) below,
  including its two-alias extension for background aliases (§4).
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

**Background aliases (not written out).** The background b on the fine
lattice is itself H_j applied to a coarse field of momentum P. Its alias
components at p'_m = (P + 2πm)/M, m ≠ 0, vanish linearly in P_j in every
coordinate with m_j ≠ 0 (the factor |sin(P_j/2)| in δ). So they contribute
to the P² coefficient. These terms are sums over two alias variables
coupled by momentum conservation, with weights W(n) W(n - m) W_b(m). Lemma
A's proof should extend, because per coordinate Σ_n δ(n)² δ(n - m)² <= C(1 + |m|)^{-2}.
This extension is not written out.

**Not checked here.** The same form for:

- the ghost and gauge-fixing vertices;
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
