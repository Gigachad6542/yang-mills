# H3D-0(b): the push-forward density of Balaban's average is bounded above and below

Status: **proved** (T47; §6, the extension to CMP 109 (0.4), T59). For each fixed N, the push-forward of the depth-(N+1)
measure under one step of Balaban's average (CMP 98 (42)) has a density that
is bounded above and below. Hence D_N of note 18 is bounded, and H3D-0(b)
holds as stated in note 18. The weaker condition (b') of note 52 §4a is no
longer needed. The proof is self-contained: an exact separation of one link
per coarse bond (Lemma 1), a Jacobian lower bound from operator concavity
(Lemma 3, Theorem 2), and a degree count (Theorem 4). The bounds are not
uniform in N, and H3D-0 does not ask for that.

Script: `research/scripts/t47_average_jacobian.py` (output `.out`).

## 0. Setting

Lattice notation follows note 18 §1 in any d >= 2. One step
q : Ω_{N+1} -> Ω_N is Balaban's average (CMP 98 (42)):

    (q U)(c) = exp( Σ_{x ∈ B(c_-)} L^{-d} Log(U(Γ_{c,x}) U(c)^{-1}) ) U(c).

Here:

- the blocks B(y) = {y_ν <= x_ν < y_ν + L} are those of CMP 95 (1.6);
- Γ_{c,x} = Γ_{c_-,x} ∪ [x, x(c)] ∪ Γ_{x(c),c_+}, with x(c) = x + L e_μ for
  c = (c_-, c_- + L e_μ) (CMP 98 (14));
- the in-block contours Γ_{y,x} of CMP 95 (1.7) run along the coordinate
  axes in a fixed order and stay inside B(y);
- U(c) := U(Γ_{c,c_-}) is the straight product of the L fine links from c_-
  to c_+;
- Log is the principal logarithm of CMP 98 (22). On SU(2) it is
  real-analytic on SU(2) \ {-1}, with |Log Z| < π there. (Normalise so that
  e^{h} = -1 exactly when |h| = π.)

Haar measure on Ω_{N+1} is λ and on Ω_N it is λ'. Write
μ_{N+1} = h λ, where h = ρ_0^{(N+1)}/Z, and e^{-a} <= h <= e^{a} for some
a = a(N) < ∞. This holds because the Wilson action is bounded on the finite
lattice.

## 1. Lemma 1 (one private link per coarse bond)

For c = (y, y + L e_μ), let b*_c be the last link of the straight path, from
y + (L-1)e_μ to y + L e_μ. Write U(c) = W_c U_{b*_c}. Let S ⊂ B(y) be the set
of points off the central line {y + t e_μ}. Then:

1. For x on the central line, U(Γ_{c,x}) = U(c) identically, so these terms
   contribute Log 1 = 0.
2. For x ∈ S, Y_{c,x} := U(Γ_{c,x}) does not contain b*_c. W_c does not
   contain b*_c either.
3. b*_c enters no contour of any other coarse bond c' ≠ c.

So, with U_rest := all links other than {b*_c}_c,

    (q U)(c) = Φ_{Y_c}(W_c U_{b*_c}),   Φ_Y(X) := exp( L^{-d} Σ_{x∈S} Log(Y_x X^{-1}) ) X,

where W_c and Y_c = (Y_{c,x})_{x∈S} are functions of U_rest only.

*Proof.*

1. For x = y + t e_μ, Γ_{y,x} is straight along μ. Hence Γ_{c,x} runs from y
   to y + (L+t)e_μ and back to y + L e_μ. The backtracking cancels in the
   group product.
2. For x ∈ S, the contour Γ_{c,x} consists of:
   - in-block pieces;
   - one crossing link, at the transverse position of x, which is not
     central.

   b*_c is a crossing link, so it is not in-block. It is central, so it is
   not the crossing link of any x ∈ S.
3. A crossing link of c' lies between B(c'_-) and B(c'_+) in direction μ'.
   The only crossing links in direction μ between B(y) and B(y + L e_μ) are
   those of c. ∎

*Checked numerically* (script, part 1) for d = 3, L = 2, 3: the central
terms vanish to 1e-16, and no Y_x changes when b* is resampled.

Several x ∈ S can have identical Y_{c,x}. For example, when μ is the last
axis in the contour order, points of S on the same transverse line give the
same reduced contour. So group equal Y's: write Y_1, ..., Y_n for the
distinct classes, with weights p_j = (multiplicity)/L^d > 0. Then

    Σ_j p_j = |S|/L^d = 1 - ε,   ε := L^{1-d}.

Two contours that are not identical as reduced loops have
Y_x Y_{x'}^{-1} ≠ 1 for λ-a.e. U_rest. (tr(Y_x Y_{x'}^{-1}) - 2 is a
real-analytic function on the connected manifold Ω_{N+1} that is not
identically 0.) So for a.e. U_rest, the Y_j are pairwise distinct.

From now on, Φ_Y(X) = exp(w(X)) X with w(X) = Σ_j p_j Log(Y_j X^{-1}). It is
real-analytic on O_Y := SU(2) \ {-Y_j}_j. Since |w| <= (1-ε)π < π, Φ_Y is
well defined there.

## 2. Theorem 2 (Jacobian lower bound)

For every Y and every X ∈ O_Y, the Jacobian of Φ_Y with respect to Haar
measure satisfies

    J_Y(X) >= c_L := ε³ (sin(επ) / ((1-ε)π))²   (ε = L^{1-d}).

*Proof.*

1. *Formula.* Put h_j = Log(Y_j X^{-1}) and φ(z) = z/(1 - e^{-z}),
   ψ = 1/φ. The left-trivialised differential of exp is
   d exp_h = e^h ψ(ad h). Perturb X -> e^{η} X. Then
   h_j -> h_j - φ(ad h_j) η, so δw = -Mη with M = Σ_j p_j φ(ad h_j), and
   Φ -> e^{w} e^{η - ψ(ad w) M η} X. In orthonormal left-invariant frames
   (Ad is orthogonal with determinant 1),

       J = det(I - ψ(ad w) M) = det ψ(ad w) · det(φ(ad w) - M).

2. *First factor.* ad w has eigenvalues 0 and ±2iθ_w, with θ_w = |w|. So
   det ψ(ad w) = |ψ(2iθ_w)|² = (sin θ_w/θ_w)². Since sin θ/θ decreases on
   [0, π] and θ_w <= (1-ε)π, this factor is >= (sin(επ)/((1-ε)π))².
3. *Second factor.* The symmetric part of φ(ad h) is

       S(h) = P_h + |h| cot|h| (I - P_h),

   where P_h is the projection on h. (φ(±2iθ) = θ cot θ ± iθ on the plane
   ⊥ h, and φ(0) = 1.) Now w = Σ_j p_j h_j + ε·0 is a convex combination of
   points of the open ball |h| < π. By Lemma 3, S is operator-concave on that
   ball, so

       sym(φ(ad w) - M) = S(w) - Σ_j p_j S(h_j) >= ε S(0) = ε I.

4. *Determinant.* A real 3×3 matrix A with sym A >= εI has every eigenvalue
   with Re λ >= ε. (Take u*Au for a unit eigenvector u.) So det A >= ε³,
   since real eigenvalues are >= ε and conjugate pairs give |λ|² >= ε². ∎

**Lemma 3 (operator concavity).** S(h) = P_h + |h| cot|h| (I - P_h) is
operator-concave on {h ∈ R³ : |h| < π}.

*Proof.* From π z cot(π z) = 1 + Σ_{n>=1} 2z²/(z² - n²), we get
θ cot θ = 1 - Σ_n 2θ²/(n²π² - θ²). Since θ²(I - P_h) = |h|² I - h hᵀ,

    vᵀ S(h) v = |v|² - Σ_{n>=1} 2 |h × v|² / (n²π² - |h|²).

Each summand is convex in h on the ball. It is f(Ah, n²π² - |h|²), where:

- f(x, t) = |x|²/t is the perspective of |x|², jointly convex on t > 0 and
  nonincreasing in t;
- A h = h × v is linear;
- n²π² - |h|² is concave.

The standard composition rule then gives convexity. The series converges
uniformly on compact subsets of the ball. ∎

*Checks* (script, parts 3-5):

- J = L^{3(1-d)} = ε³ exactly at U = 1.
- Under Haar sampling (d = 3; 2·10⁵ samples at L = 2, 4·10⁴ at L = 3), J > 0
  always. min J/ε³ = 1.82 (L = 2) and 50.1 (L = 3), against the proved
  c_L/ε³ = 0.090 and 0.015.
- Midpoint concavity of S: the minimum eigenvalue of
  S(mix) - mix(S) is >= -1e-15 in 2·10⁵ random tests.

## 3. Theorem 4 (at most one preimage)

Let the Y_j be pairwise distinct. For a.e. V ∈ SU(2),

    #Φ_Y^{-1}(V) = 1 - #{j : |ξ_j - c_j| < p_j π} ∈ {0, 1},

where:

- ξ_j := Log(-V Y_j^{-1}) (defined for a.e. V);
- c_j := Σ_{k≠j} p_k Log(-Y_k Y_j^{-1}).

In particular Φ_Y is injective off a null set.

*Proof.*

1. *Reduction to a zero count in a ball.* Fix V. Points X ≠ -V correspond
   to ξ = Log(V X^{-1}) in the ball B_π, via X = e^{-ξ} V. X = -V is never a
   preimage, since e^{w} ≠ -1. Since |w| < π, Φ_Y(X) = V if and only if
   F(ξ) := ξ - w(e^{-ξ} V) = 0.
   - F is real-analytic off the points ξ_j where e^{-ξ_j} V = -Y_j.
   - At a zero, DF = I - M ψ(ad w). By Sylvester's identity its determinant
     equals the Jacobian of Theorem 2, which is > 0. So every zero is
     nondegenerate with index +1.
2. *Outer sphere.* |w| <= (1-ε)π. Choose r < π with all |ξ_j| < r and
   r > (1-ε)π. On |ξ| = r, ξ·(ξ - t w) >= r(r - (1-ε)π) > 0 for t ∈ [0, 1].
   So deg(F, ∂B_r) = deg(id) = 1.
3. *Small spheres around ξ_j.* Put ζ(δ) := Log(e^{-ξ_j} e^{ξ_j + δ}).
   - ζ is analytic near δ = 0 with ζ(0) = 0. Its differential at 0 is
     ψ(ad ξ_j), whose determinant is (sin|ξ_j|/|ξ_j|)² > 0. So ζ is
     orientation-preserving.
   - With X = e^{-ξ_j - δ} V, we have Y_j X^{-1} = -e^{ζ}, and
     Log(-e^{ζ}) = -(π - |ζ|) ζ̂ exactly.
   - The other terms of w are continuous at ξ_j, with value c_j there,
     because the Y_k are distinct.

   Hence F(ξ_j + δ) = a_j + p_j π ζ̂(δ) + O(|δ|), with a_j := ξ_j - c_j.
   On a small sphere |δ| = ρ:
   - if |a_j| > p_j π, F/|F| has degree 0;
   - if |a_j| < p_j π, the homotopy a_j -> 0 gives the degree of δ ↦ ζ̂(δ),
     which is +1.

   In both cases F has no zeros in the small ball.
4. *Count.* Additivity of the degree on B_r minus the small balls gives
   1 = #zeros + #{j : |a_j| < p_j π}.
5. *Null set.* The excluded V are:
   - V with Y_j V^{-1} = 1, a finite set;
   - V with |ξ_j - c_j| = p_j π.

   The c_j do not depend on V, and V ↦ ξ_j is a diffeomorphism a.e. So the
   second set is the preimage of finitely many spheres, which is null. ∎

*Check* (script, part 6): vectorised Newton from 120 random starts, for 30
random (Y, V) in each of five weight patterns (|S|, L^d) = (6, 8), (24, 27),
(2, 3), (1, 2), (3, 4). The number of distinct solutions is always 0 or 1,
and it agrees with the count formula in 150/150 cases.

## 4. Theorem 5 (H3D-0(b))

There are constants 0 < m_N <= M_N < ∞ such that
m_N <= Tρ_0^{(N+1)} <= M_N λ'-a.e. on Ω_N. Hence D_N = log(Tρ_0^{(N+1)}/ρ_0^{(N)})
is bounded, μ̃_N and μ_N are mutually absolutely continuous, and H3D-0(b)
of note 18 holds.

*Proof.*

1. *Mixture formula.* By Lemma 1 and left invariance of Haar measure,

       q_* λ = ∫ λ_rest(dU_rest) ⊗_c (Φ_{Y_c})_* λ_{SU(2)}.

   (Given U_rest, the b*_c are independent and Haar distributed. The coarse
   links are functions of disjoint b*'s, and X_c = W_c U_{b*_c} is again
   Haar distributed.)
2. *Upper bound.* For a.e. U_rest, the Y_{c,j} are distinct for every c
   (§1). By the area formula on O_Y, together with Theorems 2 and 4,
   (Φ_Y)_* λ has density Σ_{X ∈ Φ^{-1}(V)} 1/J_Y(X) <= 1/c_L. Hence
   q_* λ <= c_L^{-n_c} λ', where n_c is the number of coarse bonds, and
   q_* μ_{N+1} <= e^{a} c_L^{-n_c} λ'.
3. *Lower bound.* Fix V⁰ ∈ Ω_N and define U⁰:
   - all in-block links are 1;
   - every crossing link of c (all L^{d-1} transverse positions) is V⁰_c.

   Then every Y_{c,x} equals V⁰_c and X_c = V⁰_c. So all h_j = 0,
   q U⁰ = V⁰, and J = ε³ at U⁰. The map (U_rest, u) ↦ Φ_{Y_c}(W_c u) is
   analytic near U⁰. The inverse function theorem with parameters then gives
   neighbourhoods 𝒩 of U⁰_rest and B_c of V⁰_c such that, for U_rest ∈ 𝒩,
   each V_c ∈ B_c has a preimage with J <= 2ε³. Therefore
   q_* λ >= λ_rest(𝒩) (2ε³)^{-n_c} λ' on Π_c B_c. Ω_N is compact, so
   finitely many such neighbourhoods cover it, and q_* μ_{N+1} >= m λ' with
   m > 0.
4. *Conclusion.* ρ_0^{(N)} is bounded above and below on Ω_N, so D_N is
   bounded. ∎

## 5. Consequences

- **H3D-0 holds** for SU(2), any d >= 2, any L >= 2, at every fixed N.
  H3D-0(a) was already known (note 18: the same Q at every scale). So
  note 18 Propositions 1-3 and Theorems 1, 1' and 2 hold with H3D-0 as a
  verified input. Note 52 §4a (Proposition 4) is superseded, though still
  correct.
- [Superseded (audit 2026-10-09, T82): the current 3D route is note 61, M1-3D <= (NA♭) + (A_s) +
  (H4) + (L_s).] The 3D route now reads

      M1-3D <= (A_s) [CMP 102 remainder bound, complex coupling] + (NA♭) [3D; note 54],

  together with notes 17, 18, 42, 44-46, 51-54. This is a conditional
  reduction: the interacting H3D-1' assembly is outlined in note 52 §3 and
  not written out. The qualitative fixed-N input is gone.
- Theorem 2 is a statement about Balaban's average that does not depend on
  scale: one step never collapses volume by more than c_L in the private
  link. The sharp constant appears to be ε³ (attained at U = 1). Haar
  sampling gives min J/ε³ = 1.82 (L = 2) and 50.1 (L = 3), but the sampled
  minimum does not prove a bound.

## 6. Extension to Balaban's symmetric 4D average (CMP 109 (0.4))

Balaban's 4D papers use the Euclidean-symmetric average of CMP 109 (0.4).
There L is odd and the blocks B(y) are centred at y. Then

    Ū(c) = exp( Σ_{x ∈ B(c_-)} L^{-d} Σ_{Γ ∈ G(c_-, x)} Σ_{Γ' ∈ G(c_+, x')} |G|^{-1} |G'|^{-1}
                Log U(Γ ∪ [x, x'] ∪ (-Γ') ∪ (-c)) ) U(c),

where G(y, x) is the set of shortest axis-ordered contours from y to x
(all axis orders), x' = x + L e_μ, and U(c) is the straight product through
the block centres.

**Proposition 6.** Lemma 1 and Theorems 2, 4 and 5 hold verbatim for (0.4),
with "x ∈ S" replaced by the pairs (x, Γ, Γ') with x off the central line.
In particular H3D-0(b) holds for the 4D route, which is the H3D-0 input of
note 18 Theorem 5.

*Proof.*

1. *Lemma 1.* Each contour Γ ∈ G(c_-, x) is a monotone path inside the box
   spanned by c_- and x, so it lies inside B(c_-). The same holds for Γ' in
   B(c_+). [x, x'] crosses the face between the two blocks once, at the
   transverse position of x.
   - For x on the central line, every Γ and Γ' is straight along μ, and the
     contour reduces to c. So those terms are Log 1 = 0.
   - For x off the central line, the contour avoids the central crossing
     link b*_c.
   - No contour of another coarse bond contains b*_c, by the argument of
     Lemma 1, item 3.

   So (qU)(c) = exp(Σ_k w_k Log(Y_k X^{-1})) X, where X = U(c) = W_c U_{b*_c},
   the Y_k do not depend on U_{b*_c}, and the weights w_k > 0 sum to
   1 - L·L^{-d} = 1 - ε.
2. *Theorems 2 and 4.* Their proofs use only this form, with positive
   weights summing to 1 - ε (after grouping equal Y_k). They apply
   unchanged, with the same c_L.
3. *Theorem 5.* The mixture formula and the upper bound are as before. For
   the lower bound, U⁰ again has in-block links equal to 1 and every
   crossing link of c equal to V⁰_c. Then every contour of c gives
   Y = V⁰_c. ∎

*Remark.* The variant (0.12), with Federbush group averages
M({U(Γ)}_{Γ ∈ G(y,x)}), has the same structure wherever it is defined. It is
defined only for contour sets of small diameter, so it does not give a
global map on Ω_N. (0.4), with the principal logarithm, does.
