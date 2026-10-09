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
- **Update (T77, §7).** For Z in the last axis, (R) is reduced to an
  equipartition bound (EQ) on local loops under the fibre Gibbs measure, via an
  exact transport identity (Theorem 64.2). (EQ) is not proved. The claim in §5
  that local transport fails is corrected in §7.
- **Update (T80, note 67).** (EQ') and (EQ) of §7.4 are **false** as stated
  (exact abelian Gaussian fibre: the classical part of E[β_{N+1}A_q] grows
  linearly in β_{N+1} when V' has coarse flux near q), and G_η at the
  classical minimizer exceeds the slack of Prop. 64.3 by factors 10²-10⁴, so
  the route of §7.4 cannot close (R). Moreover **(R) itself, with a Z-local
  right-hand side, is false in the abelian Gaussian model** (note 67 §3); the
  form that holds there has an exponentially decaying tail of the coarse
  energy of V^Z away from Z (note 67 Prop. 67.5, (I-LF)(b′)). In the same
  model the coefficient L² - 1 of Theorem 64.1 is sharp for L = 2.

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

## 7. T77: exact left-translation transport; (R) reduced to an equipartition bound (failed-attempt at the last step)

Script: `research/scripts/t77_transport_check.py`, output
`research/scripts/t77_transport_check.out`. Every number below is printed
there.

**Status.**

- **Proved here:** Lemma 64.4, Lemma 64.5a, Theorem 64.2 (an exact identity for
  Tρ(V)/Tρ(V^Z)), Lemma 64.5 (the changed fine plaquettes and their bounds),
  Proposition 64.3 ((R) with C_- = (1+η)L² - 1, **given** the bound (EQ)
  below), Lemma 64.6 (log-convexity bound on local plaquette energies). All of
  it is for sets Z of coarse bonds in the **last axis** direction only (axis 3,
  the last axis in the contour order of CMP 95 (1.7)).
- **Not proved (the failed steps):** (EQ), an a priori bound on the Gibbs
  measure of the fibre over V^Z; and the extension to bonds in axes 1, 2.
- **Correction to §5.** The paragraph "The natural local-transport argument
  also fails" is wrong about the obstacle. The fibre over V is *exactly* the
  image of the fibre over V^Z under an explicit Haar-preserving map that
  changes only the crossing links of Z. The spread of the Y's is not an
  obstruction: the map sends Y to RY. No collar, no Hessian and no
  Gaussian-width ball is needed for the reduction, and the matched pair of §6
  is not the route. What remains is a bound on fluctuations of *local loops*
  under the Gibbs measure of the fibre.

No Balaban input is used in §7. It rests on note 53 Lemma 1 and the definition
CMP 98 (42) only.

### 7.1 Structure of Y for a last-axis bond

Let c = (y, μ) with μ the last axis (index 3). For a transverse offset
ξ ∈ {0,..,L-1}² (coordinates in the two other axes), the crossing link
u_{c,ξ} is the μ-link from y + ξ + (L-1)e_μ to y + ξ + L e_μ. The link with
ξ = 0 is the private link b*_c. Let a_{c,ξ} be the in-block path from y along
axes 1, 2 (contour order) to y + ξ, then along μ to y + ξ + (L-1)e_μ. Let
a'_{c,ξ} be the in-block path from the head y + ξ + L e_μ back to y + L e_μ
(axis 2, then axis 1, reversed). For ξ = 0, a_{c,0} = W_c and a'_{c,0} is empty.

**Lemma 64.4.** For x ∈ S of transverse offset ξ ≠ 0 and any μ-coordinate t,
Y_{c,x} = a_{c,ξ} u_{c,ξ} a'_{c,ξ}. Put Y_{c,0} := X_c = W_c b*_c. Then for
every ξ, u_{c,ξ} = a_{c,ξ}^{-1} Y_{c,ξ} a'_{c,ξ}^{-1}.

*Proof.* With μ last, γ(y,x) runs along axes 1, 2 to the transverse position
and then along μ from 0 to t. The straight segment [x, x+Le_μ] continues the
μ-run from t to L-1, crosses at u_{c,ξ}, and runs t more steps. The return
path γ(y', x+Le_μ) reversed first undoes these t steps and then runs along
axes 2, 1 back to y'. The t steps cancel in the group product. ∎

So the Y_{c,x} that share a crossing link are equal, as note 53 §1 says for
this case. (For μ = 1 or 2 the paths differ; see §7.5.)

### 7.2 The transport map and the exact identity

Let Z be a set of coarse bonds in the last axis, R = (R_c)_{c∈Z} ⊂ SU(2),
V^Z as in §5 (V^Z_c = 1 for c ∈ Z, V_c otherwise), so V_c = R_c V^Z_c with
R_c = V_c on Z and R_c = 1 off Z. Define 𝒯_R on Ω_{N+1}: for c ∈ Z and every
ξ (private link included)

    u_{c,ξ}  ->  a_{c,ξ}^{-1} R_c a_{c,ξ} u_{c,ξ},

all other links fixed.

**Lemma 64.5a.** (i) 𝒯_R is a bijection of Ω_{N+1} preserving Haar measure;
its inverse is 𝒯_{R^{-1}}. (ii) For every U and every coarse bond c,
q(𝒯_R U)_c = R_c q(U)_c.

*Proof.* (i) The paths a_{c,ξ} contain in-block links only, which 𝒯_R does not
change, so each modified link is left-multiplied by an element that does not
depend on any modified link. A triangular left translation preserves the
product Haar measure. (ii) For c ∈ Z, Lemma 64.4 gives Y'_{c,ξ} =
a (a^{-1} R a u) a' = R Y_{c,ξ}, including X'_c = W_c (W_c^{-1} R_c W_c b) =
R_c X_c. Covariance: Log(R Y X^{-1} R^{-1}) = Ad_R Log(Y X^{-1}), so
Φ_{RY}(RX) = R Φ_Y(X). For c ∉ Z, Y_{c,x} and X_c involve only in-block links
and the crossing links of c itself (note 53 Lemma 1), none modified. ∎

*Check (script, Parts 1-2).* max |R Φ_Y(X) - Φ_{RY}(RX)| = 5.6e-16 over 300
random cases; max relative |J_Y(X) - J_{RY}(RX)| = 2.9e-9. On a 3³ coarse torus
with L = 2, 3, fine links exp(iσ g·σ) (σ = 0.02, 0.01), private links solved so
that q(U) = Ṽ for random near-1 coarse values Ṽ: after 𝒯_R on four last-axis
bonds with Haar R_c, max |q(𝒯_R U) - R Ṽ| = 5.4e-14, 6.9e-14 (L = 2), 5.7e-14
(L = 3).

**Theorem 64.2 (exact transport identity; proved here).** For Z and R as above
and a.e. V,

    Tρ^{(N+1)}(V) / Tρ^{(N+1)}(V^Z) = E_{μ_{V^Z}} [ exp( -β_{N+1} ( A_{N+1}(𝒯_R U) - A_{N+1}(U) ) ) ],

where μ_{V'} is the conditional law of the Wilson Gibbs measure
e^{-β_{N+1}A_{N+1}} dU given q(U) = V'. Consequently, with
ΔA := A_{N+1}(𝒯_R U) - A_{N+1}(U),

    D_N(V) - D_N(V^Z) = β_N (A_N(V) - A_N(V^Z)) + log E_{μ_{V^Z}}[ e^{-β_{N+1} ΔA} ]
                       >= β_N (A_N(V) - A_N(V^Z)) - β_{N+1} E_{μ_{V^Z}}[ ΔA ].        (7.1)

*Proof.* For a test function f on Ω_N, substituting U -> 𝒯_R U (Lemma
64.5a(i)) and then using (ii),

    ∫ f(qU) ρ(U) dU = ∫ f(R·qU) ρ(𝒯_R U) dU,

where R· acts by V'_c -> R_c V'_c, which preserves Haar measure on Ω_N. So
Tρ(V) = T(ρ∘𝒯_R)(R^{-1}V) = T(ρ∘𝒯_R)(V^Z). Write ρ∘𝒯_R = ρ · g with g =
e^{-β_{N+1}ΔA} (E_{N+1} cancels). T(ρ g) = Tρ · (conditional expectation of g
under the fibre law). The second line is D_N = log Tρ + β_N A_N + E_N and
Jensen. ∎

Tρ(V^Z) > 0 for every V^Z by Theorem 64.1, so the ratio is defined. No
Jacobian, degree count or existence statement for Φ_Y is used: the fibre over
V is the image of the fibre over V^Z, point by point.

### 7.3 The changed plaquettes

A fine plaquette changes only if it contains a crossing link of a bond in Z.
In d = 3 these are of two kinds (the classification of Lemma 64.1(ii)):

- **Type A:** two crossing links u_1 = u_{c,ξ}, u_2 = u_{c,ξ'} of the same bond
  (ξ' = ξ + e_ν) and two in-block ν-links, ν_1 in B(y), ν_2 in B(y + Le_μ):
  h = u_1 ν_2 u_2^{-1} ν_1^{-1}.
- **Corner:** the L fine plaquettes (third-axis position r = 0..L-1) of each
  coarse plaquette p touching Z; four crossing links of the bonds
  c_1 = (y,μ), c_2 = (y+Le_μ, ν), c_3 = (y+Le_ν, μ), c_4 = (y,ν), and
  h = u_1 u_2 u_3^{-1} u_4^{-1}.

*Check (script, Part 3).* On the sampled configurations ΔA equals the sum of
the type-A and corner differences to 1e-9 (17.0299491591 = 17.0299491591;
15.9254286396 = 15.9254286396; 35.7157582430 = 35.7157582430), so there are
no other changed plaquettes.

Write A(g) = 1 - (1/2) tr g = 1 - cos d(g,1). For a closed lattice path ℓ let
|ℓ| := d(hol ℓ, 1).

**Lemma 64.5.** Let U be any fine configuration with q(U) = V^Z.

(a) For a type-A plaquette define the closed loops at y

    M = a_1 u_1 ν_2 u_2^{-1} a_2^{-1},    N = a_2 ν_1^{-1} a_1^{-1}

(a_i := a_{c,ξ_i}, ξ_1 = ξ, ξ_2 = ξ'). Then a_1 h a_1^{-1} = MN,
a_1 h' a_1^{-1} = R_c M R_c^{-1} N, and
A(h') - A(h) <= A(h') <= (|M| + |N|)²/2 <= |M|² + |N|².

(b) For a corner plaquette let Y_i := Y_{c_i,ξ_i}, Ṽ_i := V^Z_{c_i} = q(U)_{c_i},
V_i = R_i Ṽ_i, and let Λ_1, Λ_2, Λ_24, Λ_3 be the four in-block loops (at the
corners y, y+Le_μ, y+L(e_μ+e_ν), y+Le_ν)

    Λ_2^{-1} = a'_1^{-1} a_2^{-1},  Λ_24 = a'_2^{-1} a'_3,  Λ_3 = a_3 a'_4,  Λ_1 = a_4 a_1^{-1}

(a_i, a'_i the paths of the i-th crossing link). Then
a_1 h a_1^{-1} = Y_1 Λ_2^{-1} Y_2 Λ_24 Y_3^{-1} Λ_3 Y_4^{-1} Λ_1, and h' is the
same product with every Y_i replaced by R_i Y_i. With
κ_c := max_{x∈S} |Y_{c,x} X_c^{-1}|,

    d(Y_i, Ṽ_i) <= (2-ε) κ_{c_i},    δ := Σ_i 2κ_{c_i} + Σ_j |Λ_j|,

and for every η ∈ (0,1]

    A(h') - A(h) <= (1+η) A(V(∂p)) - (1-η) A(V^Z(∂p)) + (1 + 1/η) δ²,

with δ² <= 32 Σ_i κ_{c_i}² + 8 Σ_j |Λ_j|².

*Proof.* (a) Conjugate h' by a_1 and use a_1 G_1 = R a_1, G_2^{-1} a_2^{-1} =
a_2^{-1} R^{-1} (G_i = a_i^{-1} R a_i), u'_i = G_i u_i. For the bound:
d(R M R^{-1} N, 1) <= |M| + |N| by bi-invariance, and 1 - cos θ <= θ²/2.
(b) The chain is u_i = a_i^{-1} Y_i a'_i{}^{-1} multiplied out; each junction is
a loop inside one block. The replacement Y_i -> R_i Y_i is what 𝒯_R does. Next
Ṽ_i = e^{w} X with w = Σ p_j Log(Y_j X^{-1}) and |w| <= (1-ε)κ, so
d(Y_i, Ṽ_i) <= d(Y_i, X) + |w| <= (2-ε)κ (for the private position Y = X,
and the distance is |w|). In H' = (R_1Y_1) Λ_2^{-1} (R_2Y_2) Λ_24 (R_3Y_3)^{-1}
Λ_3 (R_4Y_4)^{-1} Λ_1 replace each Y_i by Ṽ_i and each Λ_j by 1: the result is
V_1V_2V_3^{-1}V_4^{-1} = V(∂p), at distance <= δ (bi-invariance, subadditivity
of d). The same replacement in H gives V^Z(∂p), also at distance <= δ. For
θ = d(g,1), θ' = d(g',1), |θ - θ'| <= d(g,g') <= δ, Taylor gives
A(θ') <= A(θ) + sin θ·δ + δ²/2 and A(θ') >= A(θ) - sin θ·δ - δ²/2. Also
sin²θ <= 2A(θ), so sin θ·δ <= √(2A) δ <= ηA + δ²/(2η). Combine the upper
bound for h' (around V(∂p)) with the lower bound for h (around V^Z(∂p)). The
last bound is Cauchy-Schwarz over eight terms. ∎

*Check (script, Part 3).* Type A: identity defects <= 1.2e-15 and
A(h') <= (|M|+|N|)²/2 on all type-A plaquettes tested. Corner (30, 30 and 45
fine corner plaquettes): chain identity defect <= 1.3e-15, and the inequality
of (b) with η = 1/2 holds, the worst slack being -1.694 (that is, LHS - RHS <=
-1.694 on every sample). The sampled fibres are not tuned to be tight; they test
the algebra, not the size of the constant.

### 7.4 Proposition 64.3: (R) given an equipartition bound

For Z, R as above and 0 < η <= 1 - L^{-2}, put (all sums over the loops of
Lemma 64.5; p ∼ Z means that p touches Z)

    G_η(U) := Σ_{c∈Z} Σ_{(ξ,ξ',ν)} ( |M|² + |N|² )
              + (1 + 1/η) Σ_{p∼Z} Σ_{r=0}^{L-1} [ 32 Σ_{i=1}^4 κ_{c_i(p)}² + 8 Σ_{j=1}^4 |Λ_j(p,r)|² ].

**Proposition 64.3 (proved here).** For every V,

    D_N(V) - D_N(V^Z) >= -[(1+η)L² - 1] β_N A_Z(V) - β_{N+1} E_{μ_{V^Z}}[ G_η ],       (7.2)

with A_Z(V) := Σ_{p∼Z} A_N(V(∂p)).

*Proof.* In (7.1), ΔA = Σ_A + Σ_corner. Lemma 64.5 gives
ΔA <= L Σ_{p∼Z} [ (1+η) A_N(V∂p) - (1-η) A_N(V^Z∂p) ] + G_η, since every coarse
plaquette has L corner plaquettes (Lemma 64.1(ii)). With β_{N+1} = Lβ_N,

    β_N (A_N(V) - A_N(V^Z)) - β_{N+1} E[ΔA]
      >= -[(1+η)L² - 1] β_N A_Z(V) + [(1-η)L² - 1] β_N A_Z(V^Z) - β_{N+1} E[G_η],

and the middle term is >= 0 because η <= 1 - L^{-2}. ∎

So the coefficient is C_- = (1+η)L² - 1, as close to Theorem 64.1's L² - 1 as
one likes. There is no entropy term: all the cost is in E[G_η].

**The bound that remains.**

**(EQ)** *There is Γ(L,η) < ∞, independent of N, of β_{N+1} >= β_*(L), of V and
of Z (last axis), with β_{N+1} E_{μ_{V^Z}}[G_η] <= Γ |Z|.*

Given (EQ), (R) holds in the form D_N(V) - D_N(V^Z) >= -C_- β_N A_Z(V) - Γ|Z|,
which is stronger than (R) (e_ent|Z| log β_N is replaced by a constant). Why
(EQ) has the right size: G_η is a sum of O(|Z|) terms (at most 4|Z| coarse
plaquettes touch Z), each the squared distance from 1 of the holonomy of a
loop of length at most 8L-6 inside a bounded cell. Such a loop is a product of
conjugated plaquette holonomies (cone from the base point), so |loop|² is at
most a constant (depending on L) times the sum of A_q over a bounded set of
plaquettes q, using θ² <= (π²/2)(1 - cos θ). Hence (EQ) follows from the
plaquette form

**(EQ')** E_{μ_{V^Z}}[ β_{N+1} A_q ] <= C_A for every fine plaquette q within
bounded distance (in coarse units) of Z, uniformly in V.

The constant relating Γ to C_A is a finite, explicit function of L and η (cone
multiplicities); it was not worked out because (EQ') is not proved.

### 7.5 What fails

**(1) (EQ') is not proved.** It says that the Gibbs measure conditioned on a
coarse configuration has bounded plaquette energy per plaquette (equipartition),
uniformly in the coarse configuration and the rest of the lattice. What was
done:

- *Log-convexity (proved, but it only reduces the question).*
  **Lemma 64.6.** Let 𝒫 be a set of fine plaquettes, ρ_λ := exp(-E - β A_{rest}
  - λ β A_𝒫) and F(λ) := log Tρ_λ(V'). Then F is convex and

      E_{μ_{V'}}[ β_{N+1} A_𝒫 ] <= F(0) - F(1) = log( Tρ_{drop 𝒫}(V') / Tρ(V') ).

  *Proof.* Tρ_λ(V') is a Laplace transform in λ of a positive measure (the
  law of βA_𝒫 on the fibre with weight e^{-E-βA_rest}), so log-convex;
  F'(1) = -E[βA_𝒫]; convexity gives F(0) >= F(1) + F'(1)(0 - 1). ∎
  So (EQ') follows from: dropping the plaquettes of 𝒫 changes the fibre
  partition function by at most e^{C|𝒫|} (or e^{C|𝒫| log β}, which would give
  e_ent|Z| log β in (7.2), still enough for (R)).
- *The step that fails: bounding Tρ_{drop 𝒫} / Tρ.* One needs a lower bound
  for Tρ, i.e. a lower bound for the probability, under the drop measure, that
  the links of 𝒫 sit in small balls around a configuration compatible with
  their neighbours. If one drops every plaquette touching a link set 𝔏, the
  links of 𝔏 are independent of the rest except through the Y's and the
  Jacobian weight Σ_X 1/J_c. But the in-block links of a block B(y) lie in the
  contours Γ_{c,x} of the six bonds at y, whose far endpoints lie in six other
  blocks, and so on: there is no finite link set 𝔏 closed under "appears in
  the same contour". For a bond c with one end in 𝔏 and one end outside, the
  weight Σ_X 1/J_c vanishes unless Y_c lies in the επ-ball around V^Z_c, and
  Y_c depends on outside links. So "all links of 𝒫 in a ball" has no
  probability bound uniform in the outside configuration. The missing
  statement is a finite-energy (conditional Gaussian-width lower bound) property
  of the fibre Gibbs measure for a rough outside. It is the boundary-condition
  version of the matched comparison of §6, in a smaller form, and was not
  obtained.
- *Gauge zero modes.* The fibre over V' contains L³-1 gauge directions per
  block (gauge transformations equal to 1 at the block corners; they leave all
  Y's invariant). The loops in G_η are gauge invariant under these modes (they
  are loops based at block corners), so (EQ) is not affected, but a proof of
  it that uses balls of radius ~ β^{-1/2} around 1 loses about
  (3/2)(L³-1) log β per block against the true orbit volume, and so has to be
  done in an orbit-saturated or gauge-fixed form.

**(2) Bonds in axes 1, 2.** For μ not the last axis, the Y_{c,x} that share a
crossing link have different a_x (the μ-run comes first or in the middle of
γ(y,x)), so no single left translation of a crossing link gives Y' = RY for all
x. *Check (script, Part 4).* With the reference path t = 0 and Haar R, the error
|q(𝒯_R U) - R| at the modified bond is 2.1e-2 (axis 1) and 1.2e-2 (axis 2) at
L = 2, and 1.5e-2, 1.3e-2 at L = 3 (σ = 0.02, 0.01), against 2.5e-16 and
1.0e-15 for the last axis. For those axes 𝒯_R is only an approximate map of
fibres. The next step is not to make it exact but to take the unique solution
X' of Φ_{Y'}(X') = V for the perturbed Y' (within 2 max_x |a_x a_{x_0}^{-1}| of
RY), compare Jacobians with c_L <= J <= J_max (note 53 Theorem 2, Lemma 64.2(3))
at cost (J_max/c_L)^{|Z|} = e^{O(|Z|)}, and add the displacement of the private
link to G_η. Not done.

**Impact on note 61 Lemma 6b.2.** The lemma needs (R) for large-field regions
of all directions. Proposition 64.3 covers regions whose changed bonds Z lie in
the last axis; a coarse plaquette in the plane of axes 1, 2 contains no such
bond. So (I-LF)(b) stays **not discharged**. What §7 changes is the shape of
the gap: it is now (EQ) for the fibre Gibbs measure (a Gaussian-equipartition
type bound on local loops) plus the approximate transport for axes 1, 2, and
no longer a matched Gaussian evaluation of two partition functions.

Status labels: Lemma 64.4, 64.5a, 64.5, 64.6, Theorem 64.2, Proposition 64.3:
**proved here** (last axis). (EQ), (EQ'): **open** (target) [superseded:
**false** as stated, note 67 §1 (T80); (R) is false in the abelian Gaussian
model, note 67 §3]. (R): **conditional
reduction** on (EQ) for last-axis Z; **open** otherwise. Note 61 §6b.2
(I-LF)(b): **not discharged**.
