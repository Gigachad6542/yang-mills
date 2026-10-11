# The fibre Gibbs measure: (EQ') is false, and (R) in the abelian Gaussian model (T80)

Status (T80):

- **Proved here.** Proposition 67.1 (the fibre measure of the abelian
  non-compact Gaussian model of Balaban's average is exactly Gaussian, with
  linear mean and V'-independent covariance); Proposition 67.3 (exact
  quadratic structure of D_N(V) − D_N(V^Z) in the model, and a necessary
  locality condition for (R)); Proposition 67.5 (the corrected relative bound
  with an exponentially decaying tail, on each finite torus, with computed
  constants).
- **Counterexample.** (EQ') of note 64 §7.4 is false (Corollary 67.2: the
  classical part of E[β_{N+1}A_q] is 0.171 β_{N+1}θ_0² for L = 2); (EQ) is
  false; the G_η route of Proposition 64.3 loses a factor 400-2400 at the
  classical level (§2). **(R) itself is false in the abelian Gaussian model**
  for L = 2, 3 and every Z and every gauge for V^Z tested (§3): V = θ(e_b +
  t dλ) with b the bond next to c on the same line has A_Z(V) = 0 and
  D_N(V) − D_N(V^Z) = −0.234 θ² β_N (L = 2), −0.434 θ² β_N (L = 3). (In this
  example Z is not a large-field region of V: the flux near Z appears only in
  V^Z = V with Z set to 1. Prop. 67.5 bounds the defect by an exponentially
  decaying tail of the coarse energy of V^Z away from Z.) Cause:
  the Schur complement A_min has an exponentially decaying but not
  finite-range kernel, rate m_w = 1.774 (L = 2), 1.525 (L = 3) per coarse unit.
- **Proved (T82).** Q = A_N − L·A_min <= 0 for all V: proved by the argument of note 61 Lemma 6c.2 (T76): for every A with qA = V, d(qA) = W(CA) with W >= 0 of row sums L² and column sums 1/L (the kernel identity of note 18 §8(a), note 19 (2.1)), so |dV|² <= L|CA|² by Cauchy-Schwarz (Schur test), i.e. A_N(V) <= L·A_min(V); for the q of t80_abelian_fibre.py the representation is confirmed to 1e-16 with ||W||_2² = L exactly (`t82_kernel_check67.py`, L = 2, n = 3 and L = 3, n = 2).
- **Computation.** Q = A_N − L·A_min <= 0 for all k (L·A_min >= A_N), with
  inf Q/A_N = −(L²−1) attained at k = (π,π,π) for L = 2, so Theorem 64.1's
  coefficient is sharp; −5.276 for L = 3. The corrected form
  D_N(V) − D_N(V^Z) >= −β_N[C_near A_Z(V) + C_T Σ_x e^{−m d_x}A_x(V^Z)] holds
  with (C_near, C_T(2)) = (2.84, 8.8) for L = 2 and (4.39, 20.6) for L = 3,
  m < 2m_w. §5 states what Lemma 6b.2 of note 61 needs instead.
- **Not done.** The transfer to compact U(1) and SU(2); uniformity in n beyond
  n = 8 (argued, not written). (Q <= 0 is now proved; see above.)

Scripts (all in `research/scripts/`, outputs next to them):
`t80_abelian_fibre.py` (`.out`), `t80_jensen.py` (`.out`); §3-§4 use
`t80_gaussian_Q.py`, `t80_bloch_kernel.py`, `t80_tail.py` (`t80_tail_n12.out`:
`python3 t80_tail.py n12`, 8 minutes).
Every number below is printed there.

## 0. The model

d = 3 torus, coarse side n, block size L, fine side nL. The fine variables are
real angles A(x,μ) (the non-compact lift of U(1)); the fine action is
½|CA|², C the fine plaquette matrix, and the weight is exp(-β_{N+1}·½|CA|²)
with β_{N+1} = Lβ_N. Balaban's average CMP 98 (42),
(qA)(c) = L⁻³ Σ_{x∈B(y)} (contour sum of A along Γ_{c,x}), is **linear** in
the lift. The coarse action is A_N(V') = ½|dV'|² (d the coarse plaquette
matrix). The fibre over V' is F(V') = {A : qA = V'}.

Checked by the script (Part 1): q has full rank n_c = 3n³; the reduced
Hessian H_K = KᵀCᵀCK on K = ker q (K an orthonormal basis, eigh) has exactly
(L³-1)n³ zero modes, the gauge transformations that vanish at the block
corners (they change no Y and no coarse variable), and a spectral gap
1.934 (L=2, n=3), 0.834 (L=3, n=3). All functionals used below are gauge
invariant (plaquette fluxes); this is asserted in the code.

This is the abelian projection of the SU(2) theory at small field. It is a
model, not the SU(2) theory; what it refutes and what it does not is said at
each statement.

## 1. (EQ') is false as stated

**Proposition 67.1 (exact Gaussian fibre; proved here).** Let H = CᵀC,
H_K = KᵀHK, N_0 = ker H_K = {z : CKz = 0} (the gauge modes), and A_p(V') =
Qᵀ(QQᵀ)⁻¹V' the minimal-norm point of F(V') (Q is the matrix of q). Then:

1. In the coordinates A = A_p + Kz the fibre weight is
   e^{-β A_min(V')} · exp(-(β/2)(z - z_cl)ᵀH_K(z - z_cl)), where the
   classical fibre minimizer A_cl(V') = A_p + Kz_cl, z_cl = -H_K⁺KᵀHA_p
   (z_cl ⟂ N_0), is **linear** in V', and
   A_min(V') = ½|CA_cl(V')|² = ½V'ᵀMV' with M = SᵀHS, A_cl = SV'.
2. Under the fibre probability measure μ_{V'}, every gauge-invariant linear
   functional f(A) = c·A (c ∈ range H) is Gaussian with mean c·A_cl(V') and
   variance β⁻¹ cᵀK H_K⁺ Kᵀ c, **independent of V'**.
3. For a fine plaquette q (f = θ_q := (CA)_q, c = Cᵀe_q),

       E_{μ_{V'}}[ β A_q ] = ½ β θ_cl,q(V')² + ½ v_q,    0 <= v_q := cᵀKH_K⁺Kᵀc <= 1,

   with θ_cl,q := (CA_cl(V'))_q linear in V', and v_q independent of V' and
   of β.
4. Tρ^{(N+1)}(V') = c_{n,L,β} · e^{-β_{N+1} A_min(V')} with c independent of V'
   (the Jacobian of the linear map q and the Gaussian fluctuation integral
   do not depend on V').

*Proof.* Expand ½|C(A_p + Kz)|² = ½A_pᵀHA_p + zᵀKᵀHA_p + ½zᵀH_Kz. For
z_0 ∈ N_0, z_0ᵀKᵀHA_p = (CKz_0)·(CA_p) = 0, so Kᵀ HA_p ⟂ N_0 = ker H_K and
H_Kz = -KᵀHA_p is solvable, with solution set z_cl + N_0; completing the
square gives (1). z_cl = -H_K⁺KᵀHA_p and A_p are linear in V'. (2) If
c = Cᵀγ then c·Kz_0 = γ·CKz_0 = 0 for z_0 ∈ N_0, so f does not depend on the
(flat, Lebesgue) gauge coordinate; on N_0^⊥ the weight is Gaussian with
precision βH_K, so f is Gaussian with variance β⁻¹cᵀKH_K⁺Kᵀc. (3) E[A_q] =
½E[θ_q²] = ½(θ_cl,q² + β⁻¹ v_q). For v_q <= 1: v_q = sup_z [2c·Kz - zᵀH_Kz]
(finite because c·KN_0 = 0) <= sup_{A∈R^{N_l}} [2c·A - AᵀHA] = cᵀH⁺c =
(C(CᵀC)⁺Cᵀ)_{qq}, the diagonal entry of the orthogonal projector onto range C,
which is <= 1. (4) integrate the Gaussian over z: the gauge orbit volume and
det'(H_K)^{-1/2}(2π/β)^{r/2} do not depend on V', and the pushforward density
under the linear surjection q carries the V'-independent factor det(QQᵀ)^{-1/2}. ∎

*Check (script, Part 1).* max_q v_q = 0.6477 (L=2, n=3) and 0.6572 (L=3, n=3);
the unconditional value (no fibre constraint) is 0.6636 and 0.6658, and the
conditional values are <= the unconditional ones on all plaquettes, as the
variational bound predicts.

**Corollary 67.2 (counterexample to (EQ'); computation + Proposition 67.1).**
Take V' = θ_0 on one coarse bond (axis 0 at the origin) and zero elsewhere.
Then θ_cl,q = θ_0 · g_q with (script, Part 2)

| L, n | max_q g_q | max_q E[β_{N+1}A_q] / θ_0² | β_{N+1} = 10³, θ_0 = 1 | 10⁵ |
|---|---|---|---|---|
| 2, 3 | 0.58481 | 0.17100 β_{N+1} + [0, 0.324] | 171.0 | 17100 |
| 3, 3 | 0.36985 | 0.06839 β_{N+1} + [0, 0.329] | 68.4 | 6839 |

(the maximum is attained at the L corner plaquettes of the coarse plaquette
(y_0; axes 0, 2), where the coarse flux θ_p = 1 is carried: the L = 2 corner
plaquettes carry 0.585 each, against 1 for "all of it on one plaquette" and
0.25 for the uniform spread). So no constant C_A independent of V' satisfies
E_{μ_{V'}}[β_{N+1}A_q] <= C_A: the left side is >= 0.171 β_{N+1}θ_0², which
exceeds any fixed C_A as soon as β_{N+1}θ_0² > 5.9 C_A (L = 2). In particular
**(EQ') of note 64 §7.4 is false "uniformly in V'"**.

*Scope.* This is exact in the non-compact Gaussian model. In the compact
U(1) or SU(2) theory the same leading term appears as β_{N+1} → ∞ at fixed
V' (Laplace method at the classical fibre minimizer, whose fine fluxes are
<= 0.585 θ_0 and so in the quadratic range for θ_0 <= 1); I did not prove
that transfer. There is a cleaner reason that does not use the Gaussian
fibre (argument, not run). The functional f(A) = (d qA)_p is supported on the
links of the four cells y, y+e_μ, y+e_ν, y+e_μ+e_ν (the contours Γ_{c,x} of
the four bonds of p), it vanishes on gradients (q(dλ) is the coarse gradient
of λ at the block corners, and d of a gradient is 0), and that set of links
lies in a contractible box, so f factors through the fluxes of the plaquettes
in the box: (d qA)_p = Σ_{q∈N(p)} c_{pq}(CA)_q with N(p) a bounded set. By
Cauchy-Schwarz, Σ_{q∈N(p)} A_q >= A_N(V'(∂p)) / Σ_q c_{pq}² **pointwise on
the fibre**, so Σ_{q∈N(p)} E[β_{N+1}A_q] >= c β_N A_N(V'(∂p)) for every fibre
measure, whatever it is. This is the abelian content of (I-LF)(a) of note 61
(CMP 102 (70)-(71), a published input there); so (EQ') contradicts (I-LF)(a)
as soon as β_N A_N(V'(∂p)) is large. The constant c is not computed.

**(EQ) fails too.** By §2, β_{N+1}E_{μ_{V^Z}}[G_η] >= β_{N+1}G_η(A_cl(V^Z)) =
β_N R_G A_Z(V^Z) (Jensen: G_η is a sum of squares and maxima of squares of
gauge-invariant linear functionals, hence convex), which grows linearly in
β_N whenever A_Z(V^Z) > 0; the bound β_{N+1}E[G_η] <= Γ|Z| of note 64 §7.4
is false.

**What can be true: the corrected form.** By Proposition 67.1(3),

    E_{μ_{V'}}[ β_{N+1} A_q ] = ½ β_{N+1} θ_cl,q(V')² + ½ v_q   <=   ½ + ½ β_{N+1} θ_cl,q(V')²,

and θ_cl,q is a linear function of the coarse **fluxes** (gauge invariance)
with an exponentially decaying response kernel (§4). So the form that can
hold is

    (EQ'')   E_{μ_{V'}}[ β_{N+1} A_q ] <= C_A + K Σ_{p'} e^{-m d(q,p')} β_N A_N(V'(∂p')),

with C_A = ½ in the Gaussian model: equipartition for the fluctuation part
plus a classical part controlled by the coarse energy nearby. (EQ'') has a
large right side exactly where V' has large coarse plaquettes. For V^Z that
is small-field except at the plaquettes touching Z this is what (EQ) can be
replaced by; but see §3: it is not enough, because (R) itself fails.

## 2. Proposition 64.3's G_η route fails at the classical level

(Script `t80_abelian_fibre.py`, Part 4, the table in `t80_abelian_fibre.out`.)
For Z = {(y_0, last axis)} and V^Z with a unit flux on one coarse bond c'
(every c' for which some coarse plaquette touching Z contains c'), evaluate
Lemma 64.5's loop functionals at the classical fibre minimizer
A_cl(V^Z) (by Proposition 67.1 this is the mean of μ_{V^Z}, and E[G_η] >=
G_η(A_cl) because the squared loop sizes are convex in the Gaussian
fluctuation: so G_η(A_cl) is a **lower** bound for E[G_η]). Put

    R_G(η) := L · G_η(A_cl) / A_Z(V^Z).

Proposition 64.3 drops the term [(1-η)L²-1] β_N A_Z(V^Z) ≥ 0 and keeps
-β_{N+1}E[G_η]. The slack could absorb the loss only if R_G <= (1-η)L²-1.

| L | η | slack (1-η)L²-1 | min over c' of R_G | max over c' of R_G |
|---|---|---|---|---|
| 2 | 0.10 | 2.600 | 1760.65 | 2778.22 |
| 2 | 0.25 | 2.000 | 800.57 | 1263.39 |
| 2 | 0.50 | 1.000 | 480.55 | 758.45 |
| 2 | 0.75 | 0.000 | 373.87 | 590.13 |
| 3 | 0.10 | 7.100 | 7944.62 | 16792.90 |
| 3 | 0.25 | 5.750 | 3611.58 | 7634.82 |
| 3 | 0.50 | 3.500 | 2167.24 | 4582.13 |
| 3 | 0.75 | 1.250 | 1685.79 | 3564.57 |

So R_G exceeds the slack by a factor of 400-1100 (L = 2, η <= 1/2; at η = 3/4 the
slack is 0) and 600-2400 (L = 3).
It is the κ-term that dominates: for L = 2, c' = (origin, axis 0), η = 1/2,
the type-A part of G is 0.127, the Λ part is 0.000 and the κ part is
3·40.003 = 120.0; A_Z(V^Z) = 0.5. κ_c := max_x |Y_{c,x}X_c⁻¹| is the
variation of the contour sums over the block, which is of order
L·(classical flux) when the classical field is not constant across the block,
and Lemma 64.5(b) enters it squared with the factor 32 (Cauchy-Schwarz over
eight terms) and (1 + 1/η). No choice of η repairs a factor 10²-10³.

**The Jensen step is not what is lost.** In the Gaussian model the exact
identity of Theorem 64.2 can be evaluated: with V = V^Z + r e_{c_0},
Z = {c_0}, the transport is the shift of the L² crossing links of c_0 by r,
q(σ) = r e_{c_0}, and (units of β_N, β_{N+1} = Lβ_N)

    exact:   [D_N(V) − D_N(V^Z)]/β_N = Q(V) − Q(V^Z),   Q := A_N − L A_min,
    Jensen:  A_N(V) − A_N(V^Z) − L E_{μ_{V^Z}}[ΔA]  =  exact − (L/2) r² σᵀCᵀΣCσ,

where Σ := β·Cov of the fine fluxes in μ_{V^Z} (the dropped term of (7.1) is
nonnegative and of the same order in β as the classical term). Script
`t80_jensen.py`, which asserts exact = Jensen + loss to 1e-9: L = 2, n = 3,
c' = (origin, axis 0), r = 1: exact −1.013, Jensen −4.334, Proposition 64.3
(η = 1/2, G_η at the classical point) −247.8, with A_Z(V) = 1.5 and
A_Z(V^Z) = 0.5; r = 1/2: exact +0.163, Jensen −0.667, Proposition 64.3
−242.8. L = 3: r = 1: −1.486, −13.50, −1102.4. The Jensen step drops (L/2)r²σᵀCᵀΣCσ = 3.3 (L = 2) and 12.0 (L = 3) at r = 1,
against |exact| = 1.0 and 1.5: a loss of the same order as the quantity
itself, and of the order of A_Z(V). The Lemma 64.5 bound loses 10²-10³ on top
of that. The exact value satisfies the (R) target −C_-β_NA_Z(V) with
C_- = L² − 1 in all rows printed (for example −1.013 >= −3·1.5 for L = 2).

Status: Corollary 67.2 and the table of §2: **counterexample / computation**.
Proposition 67.1: **proved here**. The conclusion for Proposition 64.3: its
proof is correct, and (EQ), the only hypothesis it needs beyond the algebra,
is false as (EQ') is; see §3 for the stronger statement that (R) itself fails.

## 3. The decisive test: (R) in the abelian Gaussian model

Scripts: `t80_gaussian_Q.py` (fine-lattice matrices, real space, n = 3, 4),
`t80_bloch_kernel.py` (Bloch decomposition: any n, checked against the
real-space M to 2e-14 and 6e-14), `t80_tail.py`.

### 3.1 Reduction to a quadratic-form inequality

By Proposition 67.1(4), in the model

    D_N(V) = log Tρ^{(N+1)}(V) + β_N A_N(V) + E_N = β_N Q(V) + c_N',
    Q(V) := A_N(V) − L·A_min(V)      (β_{N+1}A_min = Lβ_N A_min),

with c_N' independent of V. So D_N(V) − D_N(V^Z) = β_N [Q(V) − Q(V^Z)]
**exactly** (no Jensen, no entropy: the fluctuation determinant and the
Jacobian of q are V-independent). Write Q(V) = ½VᵀQ_m V with
Q_m = D_c − L M (D_c = dᵀd, M from Proposition 67.1(1)), A_Z(V) = ½VᵀD_zV
(D_z = Σ_{p∼Z} d_pᵀd_p) and D(V) := Q(V) − Q(V^Z) = ½VᵀD_dV,
D_d = Q_m − PᵀQ_mP, P = identity with the Z entries zeroed.

**(R_0)**: there is C < ∞ with D_d + C·D_z ⪰ 0 on all of R^{n_c}.

If (R_0) fails for every C, then (R) fails for every C and e_ent: pick V_*
with D(V_*) + C·A_Z(V_*) = −δ < 0; D and A_Z are quadratic, so for every
ε > 0 the configuration εV_* gives D + C A_Z = −ε²δ, and (R) would require
β_N ε²δ <= e_ent|Z| log β_N, which is false for β_N large at fixed ε. The
logarithm never rescues a quadratic form that is not positive.

### 3.2 Exact structure for one bond

**Proposition 67.3 (proved here).** Let Z = {c}, t := V_c, V^Z = V − t e_c,
w := Q_m e_c (the column of Q at c), q := (Q_m)_{cc}. Then for every V:

1. D(V) = t·wᵀV^Z + ½ q t² = ½(−q) t² + t·wᵀV.
2. wᵀV depends on V only through its coarse fluxes θ = dV (Q_m annihilates
   ker d, the coarse gauge transformations and the three constant flat
   connections: D_c does, and so does M because A_min(V + h) = A_min(V) for
   h ∈ ker d; numerically |M·ker d| <= 4e-14).
3. (Necessary condition for (R_0)). If (R_0) holds for some finite C then
   w ∈ S := span{e_c, d_pᵀ : p ∼ c}, a 5-dimensional space; that is, the
   column of the quadratic form Q at c is supported on the 13 bonds of the
   four coarse plaquettes at c.

*Proof.* (1) Q(V^Z + t e_c) = Q(V^Z) + t e_cᵀQ_mV^Z + ½qt²; then V^Z = V − te_c.
(3) If w ∉ S there is V_1 ⟂ S, that is (V_1)_c = 0, d_pV_1 = 0 for p ∼ c and
wᵀV_1 ≠ 0. Let φ := dλ with λ the indicator of the head vertex of c:
φ_c = 1, the four plaquettes at c are flat in φ, and wᵀφ = 0 by (2). For
V = sV_1 + tφ we have A_Z(V) = 0 and, by (1), D(V) = ½(−q)t² + st·wᵀV_1,
which is negative for s, t of suitable signs with |t| << |s|. So
D_d + C·D_z is not PSD for any C. ∎

(3) is a locality statement. D_c e_c = Σ_{p∼c} ±d_pᵀ ∈ S always (the coarse
action has range one). So (R_0) can hold only if **M e_c ∈ S: the kernel of
A_min has the same finite range as the coarse action.** It does not; it
decays exponentially but is nowhere zero. Numerically the component of w
outside S is 37.5% (L = 2) and 41.4% (L = 3) of ‖w‖ (n = 8).

### 3.3 Results

**(a) Is Q <= 0, i.e. L·A_min >= A_N for all V?** Yes: proved by the argument of note 61 Lemma 6c.2 (T76): for every A with qA = V, d(qA) = W(CA) with W >= 0 of row sums L² and column sums 1/L (the kernel identity of note 18 §8(a), note 19 (2.1)), so |dV|² <= L|CA|² by Cauchy-Schwarz (Schur test), i.e. A_N(V) <= L·A_min(V); for the q of t80_abelian_fibre.py the representation is confirmed to 1e-16 with ||W||_2² = L exactly (`t82_kernel_check67.py`, L = 2, n = 3 and L = 3, n = 2). [Audit 2026-10-09, T82; earlier this read "(computation, not a proof)".] The numbers:

| | Q/A_N range | where the extreme is attained |
|---|---|---|
| real space, L=2, n=3 | [−1.718, −0.600] | |
| real space, L=2, n=4 | [−3.0000, −0.3333] | k = (π,π,π): exactly L²−1 = 3 |
| real space, L=3, n=3 | [−2.632, −0.800] | |
| real space, L=3, n=4 | [−5.276, −0.421] | k = (π,π,π) |
| Bloch, L=2, 4000 random k | [−2.9971, −0.0108] | corner (π,π,π): −3.00000 |
| Bloch, L=3, 4000 random k | [−5.243, −0.0128] | corner (π,π,π): −5.2758 |

The largest eigenvalue of Q_m is 0 (the gauge directions) to 3e-14 in all of
them. As k → 0, Q/A_N → −(L−1)²|k|²/L³ along the axes (−0.12501 and −0.14817
at |k| = 0.05 against the limits −0.125 and −0.14815 for L = 2, 3), so
Q < 0 off the gauge directions, with a gap that closes quadratically. Hence
(i) D_N <= const in the model (the effective action never exceeds the
vacuum), and (ii) **the coefficient L²−1 of Theorem 64.1 is sharp** for
L = 2 (the infimum of Q/A_N is attained at the corner mode), and is
not attained for L = 3 (5.276 against 8).

**(b) Is D_d >= 0 on ker(A_Z)?** **No**, in every case (**computation**;
`t80_gaussian_Q.out`). Z = one bond of axis 0, 1 or 2; two collinear bonds of
the last axis; two bonds sharing a vertex; L = 2, 3; n = 3, 4. The least
eigenvalue of D_d on ker(A_Z) is negative (−0.53 for L = 2, n = 3; −1.22 for
n = 4; −0.85 and −2.37 for L = 3), and the worst vector has A_Z(V) = 5e-18.
So **C = ∞**: there is no finite C for which (R_0) holds, and (R) is false
in the Gaussian model for every C_- and every e_ent.

**Explicit counterexample** (`t80_tail.py`, `explicit_example`). Z = {c},
c = (origin, last axis); b = the next bond on the same line (it shares no
plaquette with c); V = θ(e_b + t dλ_{head(c)}). The four plaquettes at c are
flat in V, so A_Z(V) = 0, V_c = θt, and by Proposition 67.3

    D(V) = θ² ( ½|q| t² + t Q_bc ),   min over t = −θ² Q_bc²/(2|q|),   t* = −Q_bc/|q|.

L = 2: q = −5.688, Q_bc = +1.6317, t* = −0.2869, **D = −0.2340 θ²**
(in units of β_N). L = 3: q = −8.776, Q_bc = +2.7616, t* = −0.3147,
**D = −0.4345 θ²** (n = 16 and 12 tori, Bloch kernel). For θ = 1 and e_ent = 3(L³−1) = 21 (L = 2), (R) would
require 0.234β_N <= 21 log β_N, false for β_N >= 10³; for θ = 0.1 false for
β_N >= 10⁶. The identities 3.2(1)-(2) agree with the full quadratic forms to 3e-14 on 20
random V each (`verify_formula`). **Independent check without the Schur
complement or the Bloch kernel** (`brute_force_counterexample`): with the
fine-lattice constrained minimiser of `t80_abelian_fibre.py`, L = 2, n = 4,
A_Z(V) = 0 exactly and D(V) = [A_N(V) − L·A_min(V)] − [A_N(V^Z) − L·A_min(V^Z)]
= −0.2165, −0.2231, +0.1977, +0.7654 for t = −0.4, −0.2, +0.1, +0.3, equal to
½|q|t² + tQ_bc to six digits (q = −5.743, Q_bc = 1.690 on that torus), with
minimum −0.2486 at t* = −0.294; L = 3, n = 3: minimum −0.2585. (The n = 4, 3
values differ from the n = 16, 12 values above by finite-size effects.)

**The violation decays exponentially with the distance of the flux from Z.**
The same construction with b at Chebyshev distance r from c (best b, L = 2):
min D = −0.2340, −0.02002, −5.78e-4, −1.66e-5, −4.79e-7, −1.38e-8 for
r = 1,...,6, ratios 0.086, 0.029, 0.029, 0.029, 0.029. The kernel is exactly
exponential: the Bloch/FFT kernel of Q_m on the 24³ torus has
max_{|r|_∞ = r}|Q_m(r)| decaying with ratio **0.1697** per coarse unit for
r >= 3 (L = 2) and **0.2176** for L = 3 (12³ torus), that is, a decay rate

    m_w = 1.774 (L = 2),   m_w = 1.525 (L = 3)    per coarse lattice unit,

and the violation, which is quadratic in the kernel, decays at 2m_w =
3.547, 3.051. For extended flux the generalised eigenvalue
κ(r) := sup(−D/A_flux) over V flat at distance < r from c is (n = 8, L = 2)
0.332, 0.0896, 9.47e-3, 2.53e-3, 3.08e-4, 9.8e-5, 1.14e-5 for
r = 1, 1.5, ..., 4; per unit of r the ratio tends to e^{−2m_w} = 0.0288.

**Gauge.** Q and A_Z are gauge invariant; P_Z is not. For a single bond the
pairs (V, V^Z) obtained from all gauges of a given flux configuration are
exactly the pairs (t, V^Z) with V^Z_c = 0 and t free (a coarse gauge
transformation shifts V_c arbitrarily), so "(R) for all V" is "(R) for all
(t, flux of V^Z)". Fixing a gauge (V = 0 on a spanning tree of the coarse
torus that avoids Z) turns t into a fixed linear function of the fluxes (the
flux through a surface spanning c and the tree path). I tested 11 such
gauges for each (L, n) (the comb tree with the cut at Z and three random
spanning trees for each of two single-bond Z, and three random trees for
two collinear bonds; L = 2, 3; n = 3, 4): D_d + C·D_z is not PSD for any finite C
in **all** of them. In one tree (n = 3) the tree path closes around a single
coarse plaquette at c, so t is pinned by the four near fluxes and D = 0
identically on ker(A_Z); the coupling of the near fluxes to the far flux
still gives a violation, by the same completion of the square, of size
ℓ²/(2(|q| + C/|α|²)) (t = α·a, α the pinning vector; derived, not run), which
decreases like 1/C but never vanishes. So gauge fixing does not rescue (R).

**(c) The optimal C.** None: C = ∞. What exists is a **lower** bound valid
for every relative bound of this type: V = te_c has A_Z = 2t² and
Q(V) = ½qt², so C >= |q|/4 = 1.4221 (L = 2), 2.194 (L = 3) (n = 8; the n = 24 Bloch value of q gives 1.4221).
Both are below Theorem 64.1's L²−1 = 3, 8 and below (1+η)L²−1.

### 3.4 Verdict on (R)

(R) with a Z-local right-hand side, as stated in note 61 §6b ((I-LF)(b))
and note 64 §5, is **false in the abelian Gaussian model**, for L = 2, 3 and
every Z tested, whatever the gauge convention for V^Z. The mechanism is
Proposition 67.3(3): D_N(V) − D_N(V^Z) involves the column of the Schur
complement A_min at c, and that column is exponentially decaying but not
finite-range. The counterexample has an O(1) flux at a bond b at distance
r >= 1 from Z and none at Z itself (A_Z(V) = 0; the near flux appears only in
V^Z). Since D is homogeneous of degree 2 in V, (R) fails as soon as
0.234 β_N θ² > e_ent|Z| log β_N, which includes small-field values of θ
(β_N θ² up to p², and p² >> log β_N). So the failure is a failure of
locality of the interaction between Z and the flux elsewhere, of size
O(p²) per bond in a small-field exterior (Prop. 67.5 and the linear
programme after it), not of the bound for an isolated large-field region
(§5). [Lead review, 2026-10-09: this sentence corrected; the worker's text
called the configuration "large-field outside Z", which the
homogeneity argument shows is not needed.] What
this does not show: that (R) fails for SU(2). The abelian model is the
small-field limit of SU(2); the violation is O(β_N θ²) for small θ, and I expect the non-abelian
corrections to be O(β_N θ³), smaller for small θ; I did not carry the Laplace
argument through, so the SU(2) status stays open. What is established is that
any proof of (R) for SU(2) would have to use non-abelian structure that is
absent at small field.

## 4. The corrected form that the model does satisfy

**Proposition 67.5 (proved here for each finite torus; constants computed).**
Let Z = {c}, q = Q_cc < 0 (computed: q = −5.688, −8.776), and let u be
any real function on the coarse plaquettes with dᵀu = w (it exists: w ⟂ ker d).
For a plaquette x put d_x := the Chebyshev distance between the centre of x
and the midpoint of c, near := {x ∼ c} (d_x = ½), T_m(V) := ½ Σ_{x∉near}
e^{−m d_x} θ_x(V)². Then for every V and every m >= 0

    D_N(V) − D_N(V^Z)  >=  −β_N [ C_near A_Z(V) + C_T(m) T_m(V) ],
    C_near = 2‖u_near‖²/|q|,   C_T(m) = (2/|q|) Σ_{x∉near} u_x² e^{m d_x}.

(For x ∉ near, θ_x(V) = θ_x(V^Z), so T_m(V) = Σ_{x∉near} e^{−md_x}A_x(V^Z) with
A_x = ½θ_x²: the tail is the exponentially weighted coarse energy of V^Z away
from Z.)

*Proof.* By Proposition 67.3(1) and (2), D(V) = ½|q|t² + t·uᵀθ(V) >=
−(uᵀθ)²/(2|q|) (minimise over t). Then uᵀθ = u_near·a + u_far·θ_far with
a = near flux of V, so (uᵀθ)² <= 2(u_near·a)² + 2(u_far·θ_far)²; Cauchy-
Schwarz on the first term gives 2‖u_near‖²·2A_Z(V), and with weights e^{−md}
on the second, (u_far·θ_far)² <= (Σu_x²e^{md_x})(Σe^{−md_x}θ_x²). Collect
the factors. ∎

The best u for given m is the weighted minimum-norm solution of dᵀu = w,
Σ_x e^{md_x}u_x² minimal (eigh; `explicit_constants`). Results (n = 6 | 8):

| L | C_near | C_T(0) | C_T(1) | C_T(2) | C_T(3) |
|---|---|---|---|---|---|
| 2 | 2.845 \| 2.844 | 0.669 \| 0.664 | 2.26 \| 2.23 | 9.04 \| 8.83 | 49.3 \| 52.9 |
| 3 | 4.392 \| 4.388 | 1.317 \| 1.296 | 4.68 \| 4.53 | 21.1 \| 20.6 | 142 \| 181 |

(L = 2, n = 12, `t80_tail_n12.out`: C_near = 2.844, C_T = 0.664, 2.222, 8.770,
56.25 for m = 0, 1, 2, 3: converged to three digits for m <= 1, still moving
at the 1% level for m = 2 and at 6% for m = 3, which is closer to the
threshold 2m_w = 3.55.)

So **C_near = 2.84 < L²−1 = 3 (L = 2) and 4.39 < 8 (L = 3)**, the tail
constants are stable between n = 6 and n = 8 for m <= 2 and begin to grow
with n at m = 3 (L = 2, threshold 2m_w = 3.55) and faster for L = 3
(threshold 3.05), as the decay rate says they must. The optimal pairs
(C, C_T), from the exact PSD condition D_d + C D_z + C_T T_m ⪰ 0 (bisection
by eigh, `t80_tail.out`, L = 2, n = 8, m = 2): (C, C_T) = (1.5, 85.0),
(2, 15.3), (3, 8.4), (6, 5.8), (20, 4.75); as C decreases to |q|/4 = 1.422,
C_T diverges (C = 1.43: 801). For m = 0 (global tail) C_T = 0.36-6.4.

The **small-field value** of the tail. If β_N A_x(V) <= p²/2 at every
plaquette x ∉ near (|θ_x| <= p/√β_N), Proposition 67.5 gives
β_N T_m(V) <= ½p²N_m with N_m := Σ_{x∉near}e^{−md_x} (N_2 = 17.14, N_1 =
108.8, N_3 = 4.91 on the 8³ torus), so the tail costs at most
½C_T(m)N_m p² = 76 p² (L = 2, m = 2), 177 p² (L = 3, m = 2) per bond. For V
flat at Z (A_Z(V) = 0, the situation of the counterexample) the sharp
constant comes from the linear programme

    ℓ_* := sup{wᵀV : V_c = 0, near flux 0, |θ_far| <= 1} = 7.31 (L = 2), 14.27 (L = 3)
    (n = 8; 7.30 and 14.23 at n = 6),   Λ := ℓ_*²/(2|q|) = 4.69 (L = 2), 11.60 (L = 3),

and then β_N D >= −Λ p² (D = ½|q|t² + tℓ >= −ℓ²/(2|q|) with ℓ = wᵀV <= ℓ_*p/√β_N).
So for a large-field region in an otherwise small-field background the
failure of (R) costs a constant times p² per bond of Z (p² the small-field
threshold), and this is the only place where the exterior enters.

Two collinear last-axis bonds (L = 2, 3, n = 8): the same inequality holds
with finite constants, from the PSD test; for example L = 2, m = 2: (C, C_T) =
(2, 41.9), (3, 9.13), (6, 5.12), (20, 3.92); no finite C for C <= 1.5
(L = 2). I did not derive the sum-over-bonds analogue of the explicit
formula.

Status: Proposition 67.3, Proposition 67.5 (each finite torus): **proved
here**, with the constants **computed**. Uniformity in n: **computation**
(n = 6, 8; kernel decay measured to n = 24, 12) plus an argument: a flux
representative u with Σu_x²e^{md_x} < ∞ uniformly in n for m < 2m_w exists by
a radial-gauge (cone) construction, u_x being a sum of w_b over bonds b
behind x, so |u_x| <~ d_x² e^{−m_w d_x}. This is not written out.

## 5. What note 61 Lemma 6b.2 needs instead

**What (I-LF)(b) says and what is false.** Note 61 §6b states: there is
C_- > 0 with D_N(V|_Z) >= −C_-β_NA_Z(V) − e_ent|Z| log β_N on each large-field
region Z. Two readings.

1. *V|_Z = V on Z, flat elsewhere.* Then A_N(V|_Z) = A_Z(V|_Z) and the
   statement is Q(V|_Z) >= −C_-A_Z(V|_Z), true in the model with
   C_- = L²−1 (Theorem 64.1's inequality; (a) above, sharp for L = 2), with no
   entropy term needed (the vacuum constant cancels). This reading does not
   involve a comparison with a non-flat exterior and is not contradicted by
   §3.
2. *The weight of the actual configuration V, with whatever (small-field)
   exterior it has, compared with the vacuum value:* this is how the
   lemma uses it in the σ < 0 case, bounding ρ_0 e^{−τD_N(V)}. Then one needs
   D_N(V) − c_N >= −C_-β_NA_Z(V) − (entropy) + [D_N(V^Z) − c_N] with
   D_N(V^Z) − c_N controlled by the small-field theory (I-L) — that is, the
   relative form (R), which is **false** (§3). (Any other route to a
   Z-local lower bound of D_N(V) − c_N would have to reproduce the same
   interaction between Z and the exterior flux: in the model
   D_N(V) − c_N = β_NQ(V) is a quadratic form with an exponentially decaying
   but infinite-range kernel, so Z is coupled to every plaquette of V.)

**What the Gaussian model supports instead (I-LF)(b′):** for a region Z of
coarse bonds and every V,

    D_N(V) − D_N(V^Z) >= −C_- β_N A_Z(V) − C_T β_N Σ_{c∈Z} Σ_{x ∌ Z} e^{−m d(x,c)} A_x(V^Z) − e_ent|Z| log β_N,

with (C_-, C_T, m) = (2.84, 8.8, 2) for L = 2 and (4.39, 20.6, 2) for L = 3 in
the model (single bond; the multi-bond constants are computed by the PSD test
only), m < 2m_w, and e_ent = 0 in the model (the Gaussian fibre has no V-dependent
entropy; for SU(2) the entropy term is what note 64 Theorem 64.1 bounds). In
Lemma 6b.2 the following changes:

- The σ = −τ bound becomes exp(−β_NA_P(1 − τC_-) + τ[e_ent|Z| log β_N +
  C_T Σ_{c∈Z}Σ_x e^{−m d(x,c)}β_N A_x(V^Z)]). If the exterior of Z is
  small-field, β_N A_x(V^Z) <= p²(g_k)/2 for x ∉ near, the tail is <=
  ½C_T(m)N_m p² per bond (76 p² for L = 2, 177 p² for L = 3 at m = 2; with
  the sharp constant of the linear programme, Λ p² = 4.7 p², 11.6 p², when V
  is flat at Z). Since p²(g_k) ~ (log ε_k⁻¹)^{2p_0} dominates log β_N
  (the lemma's own argument), the extra term has the same shape as the entropy
  term, and s_0^{LF} acquires one more condition, schematically
  τ·½C_TN_m p²|Z| <= (c_1/8)β_NA_P, i.e. τ <~ c_1/(c·C_TN_m) with c a
  combinatorial constant from |Z| <= 4|P| and β_N A_P >= p²|P| (I did not redo
  the lemma with it).
- **Large-field regions must not interact through the tail.** If V has a
  second large-field region Z' at distance r, the tail charges
  C_T e^{−mr}β_NA_{Z'}(V) to Z. This is absorbed by the weight
  exp(−c_1β_NA_{P'}) of Z' if τ C_T e^{−mr} <= c_1/2, so regions closer than
  r_0 = m⁻¹ log(2τC_T/c_1) have to be merged into one polymer (the polymer
  connectivity radius must be at least r_0). Without this the lemma's
  factorisation over large-field regions is not justified, for a reason
  independent of any fibre estimate.
- (I-LF)(b′) needs, for the true SU(2) theory, the transport identity of
  Theorem 64.2 (last axis only) **and** a bound on the response of the fibre
  mean to far fluxes (the nonabelian analogue of Proposition 67.5's w).
  Neither is available: (EQ), the replacement used in note 64 §7.4, is
  false (§1). Status of (I-LF)(b′) for SU(2): **target**, with the
  Gaussian-model form as the guide.

**What was not done.** (i) The transfer of §1 and §3 to compact U(1) and SU(2)
(Laplace method). (ii) [Done in T82: Q <= 0 is the Cauchy-Schwarz bound
‖dq A‖² <= L‖CA‖² of note 61 Lemma 6c.2; its constant is sharp as k → 0.] (iii) Uniformity in n of Proposition 67.5 beyond n = 8, and
the multi-bond explicit formula. (iv) Axes 0 and 1 for the non-abelian
transport (note 64 §7.5(2)); the abelian model treats all three axes alike
up to the contour order, and the real-space computations of §3.3(b) give
identical numbers for the three axes. (v) A fibre estimate of the (EQ'') form for SU(2).

Status labels. Proposition 67.1: **proved here**. Corollary 67.2 and the
table of §2: **counterexample / computation**. (EQ'), (EQ): **false** (in the
Gaussian model; contradicted for SU(2) by (I-LF)(a) if that is read as an
inequality for the Wilson action on the cell). (R) (relative form, Z-local
right-hand side): **false in the abelian Gaussian model**, **open** for SU(2).
Proposition 67.3: **proved here**. Proposition 67.5: **proved here** on each
finite torus; uniformity in n **computation**. (I-LF)(b′): **target**. Note
61 §6b.2 (I-LF)(b): **not discharged**, and in its relative reading
**cannot be discharged in that form**.
