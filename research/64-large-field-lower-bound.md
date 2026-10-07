# The large-field lower bound for D_N, (I-LF)(b) of note 61 §6b (T74)

Status:

- **Proved here (Theorem 64.1).** For d = 3, SU(2), the Wilson action and
  Balaban's average (CMP 98 (42)), for every coarse configuration V and
  every N with β_{N+1} >= β_*(L):

      D_N(V) >= -(L²-1) β_N A_N(V) - (E_{N+1} - E_N) - n_c [ 3(L³-1) log β_{N+1} + c_0(L) ].

  Here n_c is the number of coarse bonds and c_0(L) is explicit. So the
  *coefficient* is C_- = L² - 1 and the *entropy exponent* is
  e_ent = 3(L³-1) per coarse bond. The bound is a sum of one-plaquette and
  one-bond terms.
- **Not proved (failed-attempt).** The *relative, Z-local* form that note 61
  Lemma 6b.2 uses, D_N(V) - D_N(V^Z) >= -C_- β_N A_Z(V) - e_ent |Z| log β_N
  with V^Z = V with Z set to 1. The bound above has a V-independent
  **extensive** constant n_c·3(L³-1) log β_{N+1} that is not comparable with
  the vacuum constant c_N of CMP 102. Section 5 names the step that fails and
  the next concrete step.

Script: `research/scripts/t74_extension_check.py`, output
`research/scripts/t74_extension_check.out`. Every number below is printed
there. Notation and the private-link structure are those of note 53.

## 0. Setting and conventions

- d = 3, torus, L >= 2, ε := L^{-2} (= L^{1-d}). Haar measures are
  probability measures. Distance d(·,·) on SU(2) is the geodesic distance of
  S³, bi-invariant, with d(U,1) = θ iff (1/2) tr U = cos θ, 0 <= θ <= π.
- A_N(U) = Σ_p (1 - (1/2) tr U(∂p)) over plaquettes (each oriented plaquette
  once). For the normalization a_0 Σ_p (1 - (1/2) tr), replace β by a_0 β
  everywhere below.
- ρ^{(N)} = exp(-β_N A_N - E_N), β_{N+1} = L β_N, and Tρ^{(N+1)} is the
  density with respect to Haar on Ω_N of q_*(ρ^{(N+1)} dU), as in note 53 §4.
  So D_N = log Tρ^{(N+1)} - log ρ^{(N)} = log Tρ^{(N+1)} + β_N A_N + E_N.
- n_c = number of coarse bonds. Each coarse bond c has one private link b*_c
  (note 53 Lemma 1); U_rest denotes the other (L³-1) n_c fine links. Write
  U = (U_rest, b), W_c, Y_{c,x} for the data of note 53 §1, and
  Φ_c(X) = exp(w) X, w = Σ_j p_j Log(Y_j X^{-1}), weights p_j summing to
  1 - ε.

**Density formula.** By note 53 Lemma 1 (the coarse variables are functions
of independent Haar-distributed private links, given U_rest), Theorems 2 and 4
and the area formula, a version of the density is

    Tρ^{(N+1)}(V) = ∫ dU_rest Σ_{X ∈ Π_c Φ_c^{-1}(V_c)} ρ^{(N+1)}(U_rest, b(X)) / Π_c J_c(X_c),   (0.1)

with b_c = W_c^{-1} X_c, J_c the Haar Jacobian of Φ_c (> 0, note 53 Thm 2),
and at most one X per V_c (note 53 Thm 4).

## 1. The extension U⁰(V) and its action

**Definition.** U⁰(V): every in-block fine link is 1; every crossing link of
the coarse bond c (all L² transverse positions) is V_c.

**Lemma 64.1.** (i) q(U⁰) = V. (ii) Every fine plaquette of U⁰ has holonomy 1,
except that each coarse plaquette p (a corner y and a plane μν) produces
exactly L fine plaquettes, one at each of the L positions along the third
axis, whose holonomy is conjugate to V(∂p). Hence

    A_{N+1}(U⁰(V)) = L · A_N(V),   β_{N+1} A_{N+1}(U⁰(V)) = L² β_N A_N(V).

*Proof.* (i) Note 53 Thm 5 step 3. (ii) Take a fine plaquette in the plane
μν with lower-left corner at position (a, b) inside its block (a, b ∈
{0,..,L-1} after reducing mod L). The μ-links at ν-positions b and b+1 start
at μ-position a, the ν-links at μ-positions a and a+1.

- a, b <= L-2: all four links are in-block, holonomy 1.
- a = L-1, b <= L-2: the two μ-links are crossing links of the same coarse
  bond (same block, ν-positions b, b+1 both in [0, L-1]), both equal V_c. The
  two ν-links are in-block (in B(y) and in B(y + Le_μ)), equal to 1. The
  holonomy is V_c V_c^{-1} = 1. The case a <= L-2, b = L-1 is symmetric.
- a = b = L-1: the four links are the crossing links of the four coarse
  bonds around the coarse plaquette with corner y, in loop order. The
  holonomy is V(∂p) up to cyclic rotation.

The third-axis coordinate is free (L values), and none of the links depends
on it. ∎

*Check (script, Part 1/2).* On a 3³ coarse torus, L = 2, 3, random Haar V:
max |q(U⁰) - V| = 3e-17, and |A_fine(U⁰) - L A_coarse(V)| <= 3e-15 relative.

## 2. Geometry of Φ_Y near the diagonal

**Lemma 64.2.** Let Y_1,..,Y_n be pairwise distinct, weights p_j > 0,
Σp_j = 1-ε, V ∈ SU(2), V ≠ Y_j, and suppose d(Y_j, V) <= r_Y < επ for all j.
Then:

1. Φ_Y(X) = V has exactly one solution X*.
2. d(X*, V) <= (1-ε) r_Y/ε = (L²-1) r_Y, and d(Y_j, X*) <= r_Y/ε.
3. If r_Y/ε <= π/2, then J_Y(X*) <= (1 + (1-ε)π/2)³ =: J_max < 17.

*Proof.* (1) By note 53 Thm 4 the number of solutions is
1 - #{j : |ξ_j - c_j| < p_j π}, ξ_j = Log(-V Y_j^{-1}), c_j = Σ_{k≠j} p_k
Log(-Y_k Y_j^{-1}). Here |ξ_j| = π - d(V, Y_j) >= π - r_Y (because -e^{iθn}
= e^{i(θ-π)n}) and |c_j| <= (1-ε-p_j)π. So
|ξ_j - c_j| >= (ε + p_j)π - r_Y > p_j π. The set of excluded (Y, V) is
{V = Y_j} ∪ {|ξ_j - c_j| = p_jπ}, and neither occurs.

(2) With X* = e^{-ξ}V, ξ = w(X*) and |ξ| = d(X*, V) =: ρ (note 53 Thm 4
step 1). Then d(Y_j, X*) <= r_Y + ρ and
ρ = |w| <= Σ p_j d(Y_j, X*) <= (1-ε)(r_Y + ρ), so ρ <= (1-ε) r_Y/ε and
d(Y_j, X*) <= r_Y + ρ <= r_Y/ε.

(3) By note 53 Thm 2 step 1, J = det(I - ψ(ad w) M), M = Σ p_j φ(ad h_j),
h_j = Log(Y_j X*^{-1}), |h_j| = d(Y_j, X*) <= π/2. The operator ad w is
skew, so ψ(ad w) is normal, with eigenvalues ψ(0) = 1 and
ψ(±2iθ_w) of modulus sin θ_w/θ_w <= 1. Likewise φ(ad h) is normal with
eigenvalue moduli 1 and θ/sin θ <= π/2 for θ = |h| <= π/2. Hence
‖M‖ <= (1-ε)π/2 and |J| <= ‖I - ψM‖³ <= (1 + (1-ε)π/2)³. ∎

*Check (script).* Part 2: Newton from X = V converges to residual 1e-15 in
every bond, with d(X*,V) at most 0.88 and 0.61 of the bound in (2) (L = 2, 3).
Part 3: stress test of (3) with random Y_j at distance <= π/2 from X, random
weights, L = 2, 3, 4: max J/J_max = 0.026. (The true J near the diagonal is
about ε³, so J_max is crude; it enters only the O(1) constant.)

## 3. A neighbourhood of U⁰ in the fibre

Fix V and r > 0 with r_Y := (7L-6) r <= επ/2, i.e.
r <= r_max(L) := επ/(2(7L-6)). Let

    𝒩_r := { U_rest : d(U_l, U⁰_l) <= r for every non-private fine link l }.

**Lemma 64.3.** For every U_rest ∈ 𝒩_r outside a null set, and every coarse
bond c, the hypotheses of Lemma 64.2 hold for (Y_{c,x})_{x∈S}, V = V_c. The
resulting fine configuration U = (U_rest, b), b_c = W_c^{-1} X*_c, satisfies
q(U) = V, and

    d(b_c, V_c) <= R_b r,   R_b := (L-1) + (L²-1)(7L-6),
    d(U_l, U⁰_l) <= r (non-private l),   J_c <= J_max.

*Proof.* The contour Γ_{c,x} has |x - y|_1 links in B(y), then L links of
[x, x+Le_μ], then |x - y|_1 links in B(y+Le_μ): at most 6(L-1) + L = 7L-6
links. In U⁰ exactly one of them is a crossing link (the one at the
transverse position of x), so Y⁰_{c,x} = V_c. Each link of U is within r of
its U⁰ value, and inverses preserve this. By bi-invariance,
d(Y_{c,x}, V_c) <= (7L-6) r = r_Y. Hence r_Y < επ and r_Y/ε <= π/2 give
Lemma 64.2. The null set is: V_c = Y_{c,x} for some x, or two Y's equal as
reduced words but not grouped (grouping them changes nothing: weights add).
{Y_{c,x} = V_c} is null because the crossing link of Γ_{c,x} appears once, so
U_rest ↦ Y_{c,x} is a submersion. Finally
d(b_c, V_c) <= d(W_c, 1) + d(X*, V_c) <= (L-1) r + (L²-1) r_Y. ∎

*Check (script).* L = 2 (β_{N+1} = 100, r = 0.01), L = 3 (β_{N+1} = 400,
r = 0.0025), with every non-private link moved by exactly r in a random
direction: max contour length 8 and 15 = 7L-6; d(Y_j,V)/r_Y <= 0.67, 0.58;
d(b,V)/(R_b r) <= 0.39, 0.20; and the full q(U) reproduces V to 1e-15.

## 4. Theorem 64.1 and its proof

Let β_*(L) := 1/r_max(L) = 2(7L-6)L²/π (20.4 for L = 2, 85.9 for L = 3,
224.1 for L = 4), and

    c_0(L) := (L³-1) log 6 + 3 log(1 + π/2) + 4[(L³-1) + R_b(L)]

(143.4, 641.4, 1699.7 for L = 2, 3, 4).

**Theorem 64.1 (absolute lower bound; proved here).** If β_{N+1} >= β_*(L),
then for every V ∈ Ω_N (for a.e. V if one insists on a genuine density)

    log Tρ^{(N+1)}(V) >= -E_{N+1} - L² β_N A_N(V) - n_c [3(L³-1) log β_{N+1} + c_0(L)],

hence

    D_N(V) >= -(L²-1) β_N A_N(V) - (E_{N+1} - E_N) - n_c [3(L³-1) log β_{N+1} + c_0(L)].

*Proof.* Put r := 1/β_{N+1} <= r_max. Restrict (0.1) to U_rest ∈ 𝒩_r (all
terms are >= 0) and use Lemma 64.3 for the unique X*:

1. *Weight.* Lipschitz: |(1/2) tr U - (1/2) tr U'| <= d(U, U') (the function
   x ↦ x_0 on S³ is 1-Lipschitz for the geodesic distance), and
   d(Π g_i, Π g'_i) <= Σ d(g_i, g'_i). So each plaquette term changes by at
   most the sum of the distances of its four links, and each link lies in 4
   plaquettes (d = 3). Using Lemma 64.3,
   A_{N+1}(U) <= A_{N+1}(U⁰) + 4[(L³-1) n_c r + n_c R_b r], and with
   r = 1/β_{N+1}:
   β_{N+1} A_{N+1}(U) <= L² β_N A_N(V) + 4 n_c [(L³-1) + R_b]
   by Lemma 64.1.
2. *Jacobians.* Π_c J_c <= J_max^{n_c}.
3. *Volume.* 𝒩_r is a product of (L³-1) n_c geodesic balls. The Haar
   probability of a ball is vol(B_r) = (r - sin r cos r)/π >= r³/6 for
   r <= 1 (script Part 3: min vol/r³ = 0.1736 > 1/6).

Multiplying: Tρ(V) >= e^{-E_{N+1}} (r³/6)^{(L³-1)n_c} J_max^{-n_c}
exp(-L² β_N A_N(V) - 4 n_c[(L³-1)+R_b]); take logs, r = 1/β_{N+1}.
The statement for D_N adds β_N A_N + E_N. ∎

**Constants.** C_- = L² - 1 (3, 8, 15 for L = 2, 3, 4). e_ent = 3(L³-1) per
coarse bond (21, 78, 189), i.e. 9(L³-1) per coarse block. The additive
O(1) per bond is c_0(L), which may be absorbed into e_ent log β if
β_{N+1} >= e^{c_0/δ} (costing e_ent → 3(L³-1) + δ).

**Remarks.**

1. Locality. The right-hand side is Σ_p (-(L²-1) β_N A(V_p)) + constant, so
   it is a sum of one-plaquette terms plus one V-independent number.
   Each fixed V-term is local. The constant K_N := (E_{N+1} - E_N) + n_c
   [3(L³-1) log β_{N+1} + c_0] is extensive.
2. It holds for all V, not only on large-field sets, but on the small-field
   set it is far from sharp (CMP 102 (47) is relative, Theorem 64.1 is not).
3. The coefficient L² in the exponent comes from the "one fine plaquette in
   L² is a corner" count; it does not use spreading of the holonomy. Spreading
   the flux over the L² fine plaquettes of a coarse plaquette would reduce
   C_- (the abelian estimate gives about L^{-1} up to π²/4), but it requires a
   non-abelian extension satisfying q = V exactly, which this note does not
   construct.
4. Two-sided sandwich at fixed N. With the upper bound of note 53 Thm 5
   step 2 (Tρ <= e^{-E_{N+1}} c_L^{-n_c}), for every V
   -(L²-1) β_N A_N(V) - K_N <= D_N(V) <= β_N A_N(V) + (E_N - E_{N+1}) + n_c log(1/c_L),
   where K_N is defined in Remark 1 (it includes E_{N+1} - E_N, so the two
   E-differences are the same quantity with opposite signs).
   The width between the two sides is n_c [3(L³-1) log β_{N+1} + O(1)] at
   A_N = 0: extensive and growing like log β.

## 5. What is not proved: the relative (Z-local) form

Lemma 6b.2 of note 61 needs, for complex s with Re s < 0, the weight bound
for ρ_0 e^{-τ(D_N - c_N)}, with c_N the vacuum constant of CMP 102, i.e.
a lower bound of D_N(V) *relative to a reference* D_N(V^Z) (or to c_N),
that costs only C_- β_N A_Z + e_ent |Z| log β_N.

Theorem 64.1 does not give this, for the following reason, which is the exact
step that fails.

**The failing step: matching the entropy outside Z.** Applying Theorem 64.1 to
V^Z itself gives D_N(V^Z) >= -K_N - ..., and the best upper bound available
for Tρ(V^Z) is the crude one of note 53 (density <= c_L^{-n_c} sup ρ), which
does not know about β. Their ratio loses n_c·3(L³-1) log β_{N+1} +
O(n_c), extensive in the volume, not |Z|-local. The true value of
D_N(V^Z) - (E_N - E_{N+1}) on the small-field set is c_N + (local terms)
(CMP 102 (62), note 61 §6b.1), and c_N has the Gaussian scaling
-(3(L³-1)/2) n_c log β + O(n_c), half of the coefficient obtained from a ball
of radius 1/β. Our ball has radius 1/β because the extension U⁰(V) is not a
critical point of the action in the fibre when V is large, so the linear
term of A forces r ~ 1/β; for flat V the point U⁰ is the minimum and radius
β^{-1/2} would be allowed, but even then the ball captures only a constant
fraction per link of the Gaussian mass, an extensive O(n_c) mismatch with
c_N. Closing the gap would require the full Gaussian evaluation, which is the
content of CMP 102 on the small-field set and is not available for V with
large plaquettes.

**The natural local-transport argument also fails.** One would map the fibre
over V^Z to the fibre over V by changing the fine links only near Z. Lemma 64.2
and note 53 Thm 4 show why this is not a small modification: if all Y_j
coincide, Φ_Y(X) lies on the geodesic from X to Y at distance ε·d(X,Y)
from Y, so the image of Φ_Y is the ball of radius επ about Y. For a
bond c ∈ Z with d(V_c, 1) > επ, the fibre over V does not contain any
configuration whose Y's are all near 1; it consists of configurations with
spread Y's. These are a different region of U_rest, not a perturbation of the
typical fibre over V^Z, and the collar between them needs the
boundary-value construction that was not attempted.

**Where the lead's statement is reproduced.** If the matching were true, i.e.
if for all V and Z

    D_N(V) - D_N(V^Z) >= -C_- β_N A_Z(V) - e_ent |Z| log β_N        (R)

then Theorem 64.1's constants (C_- = L²-1, e_ent <= 3(L³-1) per bond of Z)
would be the ones to use. Theorem 64.1 proves (R) only in the weaker
"absolute" form: replace D_N(V^Z) by -K_N, the V-independent lower bound.
K_N is common to all V, so it cancels in any ratio of weights at two
different V. That is not what is needed: Lemma 6b.2 compares the weight at V
(large field on Z) with the normalizing weight of the s-measure, which is
dominated by small-field V whose D_N is c_N + (local terms). Bounding that
denominator from above needs the *upper* bound on Tρ at small-field V with
the same extensive constant, which is the Gaussian evaluation again. So no
normalized corollary follows, and this section stands as a failed attempt at
(R).

## 6. Next concrete step

T74b (proposed, not claimed): prove the matched pair of Gaussian-width bounds

- (lower) Tρ(V) >= e^{-E_{N+1}} exp(-L² β_N A_N(V)) Π_{c ∉ Z⁺} g_- Π_{c∈Z⁺} (c β^{-3(L³-1)}),
  with Gaussian-width balls (radius κ β^{-1/2}) on the bonds outside a
  collar Z⁺ of Z, which needs the Hessian of A_{N+1} in the fibre at the
  constrained minimizer, and
- (upper) Tρ(V^Z) <= e^{-E_{N+1}} Π_{c ∉ Z⁺} g_+ Π_{c∈Z⁺} (C),

with g_-/g_+ = e^{O(1)} per bond. The second needs a Hessian lower bound
transversal to the gauge orbits, which is where note 57 (near-flat lemma)
and note 54 (flat backgrounds) would be used; and the collar construction of
the preceding paragraph. If that is done, (R) holds with the constants
above, and e_ent can be lowered to (3/2)(L³-1) per bond of Z.

Status labels: Theorem 64.1: **proved here**. (R): **open** (target). Note 61 §6b.2 (I-LF)(b): **not discharged**;
only its absolute form is.
