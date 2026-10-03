# The three-dimensional adjacent-depth comparison (P4-3D)

Status, item by item:

- **Proved here.** The interpolation identities (Props. 1-3). The conditional
  theorems: (H3D-0 + H3D-1) => P4-3D => convergence of the M1-3D generating
  functions (Thm. 1); the L^1 variant (Thm. 1'); the split route
  (H3D-0 + H3D-3 + H3D-4) => P4-3D (Thm. 2). Prop. 4: complex-coupling
  boundedness implies H3D-3. Thm. 5: the same split route in d = 4, with the
  marginal coupling made explicit. Coupling matching between depths and exact
  cancellation of vacuum constants.
- **Computation.** An exact 3D abelian Gaussian model with Balaban's linear
  block average. The kernel and Fourier formula match brute force to machine
  precision. Adjacent-depth differences decay like L^{-2N}. The one-step
  defect has no dimension-4 part. Inserted dimension-4 and dimension-6
  defects give L^{-N} and L^{-2N}. The kernel identity and the brute-force
  check are exact. The decay rates are numerical, with a proof sketch.
- **Failed attempts.** F1: two-sided stability bounds, even complex ones,
  give no Cauchy estimate. F2: a fine-level oscillation criterion fails.
- **Literature.** Neither Dimock's φ⁴₃ / QED₃ series nor CMP 102 proves
  convergence as the cutoff is removed, or analyticity in the coupling.
- **Heuristic.** σ = 1 for Yang-Mills without improvement, and that the
  vacuum constant is the only counterterm.
- **Proved later.** H3D-0(b) (note 53: the push-forward density of Balaban's
  average is bounded above and below at each fixed N).
- **Open.** H3D-1 (or H3D-3 + H3D-4) for SU(2) Yang-Mills.
  P4-3D, and hence M1-3D, are **not** proved.

Draft history: lead drafts in `wip/round3-2026-09-30/T7a` (sections 1-6 below)
and `T7c` (superseded by section 8). Scripts are in `research/scripts/t7_*.py`.

## 1. Setup

Physical torus of side ℓ. Terminal spacing ε0 = ℓ/n0, block factor L >= 2,
depth-N spacing ε_N = ε0 L^{-N}. Λ_N is the periodic cubic lattice of
spacing ε_N. Ω_N = SU(2)^{links(Λ_N)} carries product Haar measure dU, and
Ω_* = Ω_0 is the terminal configuration space.

Bare measures (CMP 102, Eq. (1), d = 3):

    ρ_0^{(N)}(U) = exp(-β_N A_N(U) - E_N),   β_N = 1/(g² ε_N) = L^N/(g² ε0),

and μ_N = ρ_0^{(N)} dU / Z. Here A_N is the Wilson action on Λ_N and g is the
fixed dimensionful coupling. Q is Balaban's gauge-covariant block average, and
T is the group-delta map, (Tρ)(V) = ∫dU δ_G(V Q(U)^{-1}) ρ(U). By
research/14 Prop. 1, ∫f (Tρ) dV = ∫(f∘Q) ρ dU. Write q_N : Ω_{N+1} -> Ω_N
for one block step, b_N = Q^{(N)} : Ω_N -> Ω_* for the N-fold composition,
and ν_N = (b_N)_* μ_N for the terminal law. Tests F_1..F_q are bounded,
|F_j| <= B_j. For a polyradius ρ with S_ρ = Σ_j B_j ρ_j < log 2, put
Z_N(z) = ν_N(exp(z·F)) for z ∈ D_ρ.

**H3D-0.** (a) b_{N+1} = b_N ∘ q_N. (b) μ̃_N := (q_N)_* μ_{N+1} has density
proportional to Tρ_0^{(N+1)}, is mutually absolutely continuous with μ_N, and
D_N := log(Tρ_0^{(N+1)} / ρ_0^{(N)}) is bounded on Ω_N for each fixed N. No
uniformity in N is assumed.

(a) holds when the same lattice-unit average Q is used at every scale. CMP 102
iterates a single T. (b) is not published: the lower bound of CMP 102 (5)
holds only on the small-field set χ. (b) is a qualitative, fixed-N statement.
It is proved in note 53 (Theorem 5).

## 2. Exact identities (proved)

Fix N. Write μ_0 = μ_N, D = D_N, b = b_N and G = exp(z·F)∘b, so |G| <= e^{S_ρ}.
For s ∈ C, set Ξ(s) = μ_0(e^{sD}), μ_s = e^{sD}μ_0/Ξ(s) (where Ξ ≠ 0) and
Z_s(z) = μ_s(G).

**Proposition 1.**

- (i) Z_0 = Z_N and Z_1 = Z_{N+1}.
- (ii) On {Ξ ≠ 0}, which contains R, d/ds Z_s = Cov_{μ_s}(G, D).
- (iii) Z_{N+1} - Z_N = ∫_0^1 Cov_{μ_s}(G, D) ds.

*Proof.* (i) μ_1 = μ̃_N by H3D-0(b). Then
μ̃_N(e^{z·F}∘b_N) = μ_{N+1}(e^{z·F}∘b_N∘q_N), which is Z_{N+1} by H3D-0(a).
(ii) D is bounded, so we may differentiate under the integral; apply the
quotient rule. (iii) For real s, e^{sD} > 0. Integrate (ii). ∎

**Proposition 2 (the tangent T-flow).** Let κ(W, dU) be a regular conditional
distribution of μ_0 given b. It exists because the spaces are compact
metrizable. For real s, put

    Y_s(W) = ∫κ(W,dU) e^{sD},   m_s(W) = ∫κ(W,dU) D e^{sD} / Y_s(W).

Then:

- (i) b_*μ_s has density Y_s/Ξ(s) with respect to ν_N.
- (ii) m_s = E_{μ_s}[D | b].
- (iii) For every W, log(dν_{N+1}/dν_N)(W) = ∫_0^1 (m_s(W) - μ_s(D)) ds.
- (iv) osc log(dν_{N+1}/dν_N) <= sup_{s∈[0,1]} osc m_s.
- (v) With D_0^{(s)} = D and D_{k+1}^{(s)} = E[D_k^{(s)} | Q], one has
  m_s = D_N^{(s)}, and D_k^{(s)} = ∂_s log T^k ρ^{(s)} up to constants.

*Proof.* (i)-(ii) follow by disintegration. (iii): ∂_s log Y_s = m_s,
∂_s log Ξ = μ_s(D), and Y_0 = Ξ(0) = 1. (iv) is subadditivity of
oscillation, with the constant terms dropping out. (v) is the tower property,
since σ(Q^{(k+1)}) ⊂ σ(Q^{(k)}). ∎

Since the 3D flow is exact T-iteration with no R-step (note 14), D ->
D_k^{(s)} is exactly the linearized Balaban flow along the direction D. So
P4-3D is the statement that **the one-step defect is irrelevant under the
exact linearized T-flow.** `t7_identity_check.py` checks (iii) and 1(ii) on a
random finite space (errors 3e-8 from the trapezoid rule, and 8e-11).

**Proposition 3 (sharp zero-free strip).** Ξ(s) ≠ 0 for |Im s| < π/osc D,
and the width cannot be improved in general. *Proof.* Center D at the
midpoint c of its range. Then Re e^{s(D-c)} > 0 when |Im s| osc D/2 < π/2.
Sharpness: on a two-point space with D = (0, M), Ξ(iπ/M) = 0. ∎ Since osc D_N
is extensive (section 8, F2), this strip has width O(ε_N^3). Only real s is
used below.

## 3. Hypotheses on the 3D RG

Let σ > 0 be fixed.

- **H3D-1 (terminal tangent decay).**
  η_N := sup_{s∈[0,1]} osc m_{N,s} <= C_1 L^{-σN}.
- **H3D-1' (local L^1 form).** D_N = c_N + Σ_x D_{N,x} with bounded local
  pieces, and Σ_x sup_s E_{μ_{N,s}}|E[D_{N,x}|b_N] - μ_{N,s}(D_{N,x})| <=
  C_1' ε_N^σ. This is implied by H3D-1.
- **H3D-2 (polymer form).** For s ∈ [0,1], the terminal tangent defect has a
  connected-polymer representation modulo constants with rooted oscillation
  norm <= η̄ L^{-σN}. By research/09 Prop. 4 on the fixed terminal lattice,
  H3D-2 => H3D-1 with C_1 = n0^3 η̄.
- **H3D-3 (uniform coupling differentiability).** With
  Φ_N(z; β) = μ_{N,β}(e^{z·F}∘b_N), there are r, M' with
  |∂_{g'²} Φ_N(z; 1/(g'² ε_N))| <= M' for all N, z ∈ D_ρ and |g'² - g²| <= r.
  Equivalently, |Cov_{μ_{N,β}}(e^{z·F}∘b_N, A_N)| <= M' g'^4 ε_N.
- **H3D-4 (one-step structure).**
  - (a) D_N = -c_N - δ_N A_N - P_N, with |δ_N| <= δ̄, and P_N bounded and
    gauge invariant with its A_N component removed by a fixed convention.
  - (b) For μ^#_{N,s} ∝ exp(-(β_N + δ_N)A_N - sP_N), the bound
    sup_s osc E_{μ^#_{N,s}}[P_N | b_N] <= C_4 L^{-σ'N} holds.

**Proposition 4 (complex-coupling boundedness => H3D-3; proved).** Suppose
β -> Φ_N(z; β) extends holomorphically to the disc |β - β_N| < r β_N with
|Φ_N| <= M there, uniformly in N and z ∈ D_ρ. Then H3D-3 holds with
r replaced by a smaller r', and M' = 4M/(r g²).

*Proof.* For |β' - β_N| <= rβ_N/2, Cauchy on a disc of radius rβ_N/2 gives
|∂_βΦ| <= 2M/(rβ_N). Since β = 1/(g'²ε_N), we have
|∂_{g'²}Φ| = |∂_βΦ|/(g'^4 ε_N) <= 2M/(r β_N g'^4 ε_N) = 2M g²/(r g'^4).
For g'² >= g²/√2 this is <= 4M/(r g²), and that range contains a fixed
neighborhood of g². ∎

The hypothesis is on the **normalized** expectation. The partition function
itself cannot be bounded on such a disc uniformly in N: log Z_N is extensive
in |Λ_N|. So complex-coupling versions of the unnormalized bounds (5) are not
enough. See F1.

## 4. Conditional theorems (proved)

**Theorem 1 (H3D-0 + H3D-1 => P4-3D => M1-3D convergence).** For every
bounded test family with S_ρ < log 2:

- (a) osc log(dν_{N+1}/dν_N) <= C_1 L^{-σN}.
- (b) sup_{D_ρ} |Z_{N+1} - Z_N| <= e^{S_ρ}(e^{C_1 L^{-σN}} - 1).
- (c) W_N = Log Z_N converges uniformly on D_ρ to a holomorphic limit. Every
  joint cumulant satisfies |κ_α(∞) - κ_α(N)| <= α! ρ^{-α} C L^{-σN} /
  ((2 - e^{S_ρ})(1 - L^{-σ})).
- (d) ν_N converges in total variation.

*Proof.* (a) is Prop. 2(iv). Research/07 Prop. 1 turns it into
|ν_{N+1}(f) - ν_N(f)| <= ||f||_∞(e^{η_N} - 1), which gives (b). For (c),
|Z_N| >= 2 - e^{S_ρ} (research/03 Thm. C). Sum the geometric increments and
apply Cauchy (Thm. A). For (d), the increments are summable in TV. ∎

**Theorem 1'.** H3D-0 + H3D-1' => sup_{D_ρ}|Z_{N+1} - Z_N| <= e^{S_ρ} C_1'
ε0^σ L^{-σN}, hence conclusion (c). *Proof.* Use Prop. 1(iii) and the tower
property, as in research/07 Prop. 1'. ∎

**Theorem 2 (split route: H3D-0 + H3D-3 + H3D-4 => P4-3D).** For N with
δ̄ g² ε_N <= 1/2,

    sup_{D_ρ}|Z_{N+1} - Z_N| <= e^{S_ρ}(e^{C_4 L^{-σ'N}} - 1) + 2M' g^4 δ̄ ε0 L^{-N}.

*Proof.* Insert μ^# at β_N + δ_N. Then
Z_{N+1} - Z_N = [μ̃_N - μ^#](G) + [μ^# - μ_N](G).

- First bracket: μ̃_N = e^{-P_N}μ^#/norm by H3D-4(a). Apply Props. 1-2 with
  base μ^# and defect -P_N, then H3D-4(b) and research/07 Prop. 1.
- Second bracket: it equals Φ_N(β_N + δ_N) - Φ_N(β_N). The corresponding
  g'² = g²/(1 + δ_N g² ε_N) differs from g² by at most 2g^4 δ̄ ε_N. Apply
  H3D-3 on that segment. ∎

**Corollary 3.** Under H3D-3, any bounded shift of the bare inverse couplings,
β_N' = β_N + b_N with sup|b_N| < ∞, changes Φ_N by O(ε_N). Both choices have
the same limit, if either has one.

## 5. Matching, counterterms, power counting

- **Matching (proved).** Balaban's scale couplings g_k = g(L^k ε)^{1/2} agree
  between depth N+1 at step k+1 and depth N at step k. The terminal coupling
  g² ε0 is common to all N.
- **Vacuum constants (proved).** E_N and c_N cancel from every normalized
  quantity.
- **Counterterms (heuristic or source reading).** The one-loop shift δ of
  1/g_0² is O(1) in lattice units. By Cor. 3 it is summable (σ = 1), so no
  coupling counterterm is needed. Gauge invariance forbids a mass term. The
  parity-odd Chern-Simons density is excluded if Q commutes with lattice
  reflections; that commutation is not checked here. The first nontrivial
  gauge-invariant operator is tr F² (dimension 4).
- **Power count (heuristic).** A local defect that mixes into a dimension-Δ
  operator contributes ε^{Δ-3}, with an extra 1/g_0² = 1/(g²ε) at tree level.
  So quantum tr F² gives ε (σ = 1), and classical dimension 6 gives ε².
  Section 8 confirms both rates exactly in the Gaussian model.

## 6. Failed attempts

**F1 (stability bounds give no Cauchy estimate).** Suppose bounds of type (5)
held uniformly for the complex family in a tube around [0,1]. Cauchy then
bounds ∂_s log ρ_K^{(s)} by O(1)|T^{(K)}|/s_0, which is an N-independent
constant, not a decaying one. The obstruction is structural. The bounds (5)
hold, with the same form and O(1) uniform for g_k in a bounded set, for the
alternating sequence g, 2g, g, 2g, .... If (5) alone implied the Cauchy
property, the alternating terminal laws would converge. At N = 0 they differ:
the Wilson measures at β = 1/(g²ε0) and 1/(4g²ε0) are distinct. That the
limits also differ is expected but not proved, so this step is heuristic.
Smallness must come from a tangent (difference) estimate. This matches the
research/13 counterexamples.

**F2 (fine-level oscillation).** Applying research/07 Prop. 1 on Λ_N needs
osc D_N small, but D_N is extensive. Section 8(c) shows that the per-mode
defect is O(1) at high momentum. The contraction osc m_s <= osc D is
trivially true but gives ε^{-3}. All the gain comes from the terminal
projection.

## 7. Literature check

- **CMP 102** (`sources/text/Balaban1985-CMP102-UV-stability-3D.txt`) gives
  bounds (3) and (5) on ρ_K uniform in ε. It states no comparison between
  depths and no convergence. Its proof is "very sketchy" (p. 257), and the
  lower bound is "easier", with only a few remarks given.
- **Dimock-Balaban I-III (φ⁴₃).** RG-III Theorem 2 gives a polymer
  representation of log Z_{M,N}/Z_{M,N}(0) on the unit-scale lattice, with
  |H(X)| <= O(1)λ^{β/2} e^{-κ0 d_M(X)}, uniform in N. Its corollary is
  stability (225). The papers say their goal is "the illustration of
  Balaban's method". Analyticity is proved in the fields (domains R_k, P_k)
  and in random-walk parameters s, t. **No analyticity in the coupling λ and
  no N -> ∞ convergence is stated.** Counterterms ε_0^N, μ_0^N are selected
  dynamically, which is not needed in YM3.
- **Dimock QED₃** (paper and 2022 overview). Theorem 1 is stability,
  K_- <= Z_N(e)/Z_N(0) <= K_+. The overview, lines 89-93, says that adding
  sources and taking "the continuum limit N -> ∞ for the partition function,
  generating function, and correlation functions should also be feasible".
  So the continuum limit is **not** proved there.

**Conclusion.** No published Balaban-method paper, in any model, proves the
adjacent-depth comparison. H3D-1 / H3D-2 would be new even for φ⁴₃. The
closest available structure is Dimock's terminal polymer form (RG-III
Thm. 2). Its N-differences are exactly H3D-2.

## 8. Exactly solvable check: 3D noncompact U(1)

**Model.** Fine torus (Z/n)^3, n = n0 M, M = L^N. Action (β/2)|dA|² with
β = 1/(g² ε_N). Units g² ε0 = 1, so β = M. Q is Balaban's linear average
(research/10 (7.1)-(7.2)).

**(a) Kernel identity (exact; `t7_kernel_check.py`).** d_c(Q^N A) = w * dA,
with w_j = (M-box average) * (M×M square perpendicular to j). The radial
contour terms cancel, and iterated boxes compose to one box. Brute force
gives errors <= 6e-15 for (s, L, N) = (4,2,1), (6,3,1), (8,2,2).

**(b) Exact Fourier formula (`t7_gauss3d.py`).** The flux covariance is
β^{-1} times the projection onto ker(Bianchi). So the terminal covariance at
terminal momentum K is

    C_jk(K) = M^{-4} Σ_{m∈[0,M)^3} P_jk(p) conj(ŵ_j(p)) ŵ_k(p),   p = (K + 2πm)/M,
    P_jk = δ_jk - conj(r_j) r_k/|r|²,   r_j = e^{ip_j} - 1.

It agrees with the real-space covariance (d_cQ^N)(d^Td)^+(d_cQ^N)^T/β to
2e-16 (`t7_brute_check.py`; an eigendecomposition is needed, because `pinv`'s
default tolerance gives 1e-5 errors).

**Adjacent-depth differences, n0 = 4, sup over K and j,k:**

| L | N=2 | N=3 | N=4 | N=5 | N=6 | N=7 | ratio |
|---|---|---|---|---|---|---|---|
| 2 | 1.25e-1 | 3.13e-2 | 7.81e-3 | 1.95e-3 | 4.88e-4 | 1.22e-4 | 4.000 |
| 3 | 6.58e-2 | 7.32e-3 | 8.13e-4 | | | | 9.000 |

The differences equal (2/3)(L²-1)/M² exactly, so σ = 2. At some K, for
example K = (0,0,π/2), C_M(K) is exactly 2/3 + 1/(3M²). At generic K it is
C_∞ + b(K)/M² + O(M^{-4}).

*Proof sketch of σ = 2.* With k = K + 2πm, one has
D(p_i) = (1 - e^{-iK_i})/(1 - e^{-ik_i/M}). So C_M(K) is a window-truncated
sum Σ_k P_M(k) conj(W_j)W_k whose terms converge to the continuum terms
(1 - e^{-iK})/(ik) with relative corrections O(k²/M²). The projection makes
Σ_k |k|²|term| converge, and the truncation |k_i| > πM costs O(M^{-3}).
The cancellation of the first-order phases is checked numerically, not
proved.

**(c) One-step defect structure (`t7_defects.py`).** Compare the once-blocked
finer theory with Wilson on the same lattice, for transverse flux at small
momentum κ:

    C_blocked/C_Wilson - 1 = -(1 - L^{-2}) κ²/6 + O(κ^4)

(L = 2: -0.12497 κ²; L = 3: -0.14812 κ²). So **δ = 0**: the one-step defect
has no dimension-4 (coupling) component, and its leading part is dimension-6
type. This is H3D-4(a) with δ = 0, in the model. At high momentum the
per-mode defect is O(1) (F2).

**(d) Inserted defects at the finest scale.**

- An O(1) lattice-unit tr F² defect (β -> β + 1) gives sup|ΔC| ratios
  1.82, 1.84, 1.90, 1.94, 1.97 -> L. So σ = 1.
- A β-weighted dimension-6 defect β|∇B|² gives ratios
  2.33, 2.94, 3.50, 3.76, 3.89 -> L². So σ = 2.

This is the power count of section 5, exact in the model.

**Limits of the check.** The fields are unbounded. Gaussian log-likelihood
ratios are unbounded quadratic forms, so the sup-oscillation form H3D-1 is
infinite here. The check validates covariance convergence and the
operator-dimension mechanism, not the oscillation hypothesis. There is no
coupling renormalization, no large fields, and no non-abelian structure.

## 9. Transfer to four dimensions (proved implication; the target is d = 4)

Everything in sections 2 and 4 is dimension-free, given a common terminal
lattice and the exact block map. That holds verbatim for the **physical** 4D
Wilson measures: μ̃_N = (q_N)_*μ_{N+1} is an exact T-pushforward, and **no
R-operation enters the comparison itself**. (Correction, 2026-10-02: an
earlier version said the R-bias had to be absorbed into the defect here. That
is wrong. R enters only when the hypotheses below are proved from Balaban's
R-modified densities; see note 21 Prop. 5 and notes 24-25.) Two things
change.

1. **The coupling is marginal.** β = 1/g_0² is dimensionless. Asymptotic
   freedom gives a terminal coupling with dg_*²/dβ ≈ -g_*^4 = O(1). An O(1)
   shift of β is therefore **not** suppressed by ε. The analogue of H3D-3 is
   only a uniform bound:

   **H4D-3.** |∂_β Φ_N(z; β)| <= M' for β in a neighborhood of the
   trajectory β_N, uniformly in N and z ∈ D_ρ.

2. **The bare couplings must follow the flow.** Let δ_N be the dimension-4
   component of the one-step defect, as in H3D-4(a), for the chosen sequence
   β_N. Smallness of the second bracket in Thm. 2 then needs:

   **H4D-0 (summable matching).** Σ_N |δ_N| < ∞.

   This is the coupling-flow interface H0 / note 08 in exact form. β_N must
   lie on the exact one-step matching trajectory up to a summable error.

**Theorem 5 (proved implication).** Assume H3D-0, H4D-3, H4D-0, and H3D-4(b)
with the physical one-step defect P_N (the irrelevant operators; no R-term)
and rate Σ_N ε_N' < ∞, where ε_N' := C_4 L^{-σ'N} or any summable sequence.
Then Σ_N sup_{D_ρ}|Z_{N+1} - Z_N| < ∞, and conclusions (c)-(d) of Thm. 1
hold.

*Proof.* Theorem 2 verbatim. The second bracket is bounded by
M'|δ_N| (fundamental theorem of calculus in β, with H4D-3). The first bracket
is bounded by e^{S_ρ}(e^{ε_N'} - 1). Both are summable. ∎

**What Theorem 5 says.** For the original problem, the 4D adjacent-depth
comparison splits into exactly three estimates:

- (i) H4D-3: a uniform β-derivative bound for normalized terminal
  expectations. This is a susceptibility bound, not an ε-gain.
- (ii) H4D-0: summable matching of bare couplings. This is the
  coupling-flow theorem.
- (iii) H3D-4(b) in 4D: tangent decay of the irrelevant part of the physical
  one-step defect. In the L^1 form of Thm. 1' this is a placement-summed
  decorrelation bound, sup_s Σ_x |Cov_{μ_s}(e^{z·F}∘b_N, P_{N,x})| <= ε_N'.
  If it is proved through Balaban's R-modified densities, the R-bias must be
  controlled (notes 11-16, 20, 24, 25). There the remaining core,
  generalized averaged H8, is the same kind of estimate: decorrelation of a
  local even defect from terminal tests. Note 19 (T8) verifies it in the
  Gaussian model, with L^{-4m} per placement for dimension 4.

Heuristically, a finite-loop explicit choice of β_N leaves δ_N = O(N^{-p}),
with p depending on the loop order and the scheme. Since β_N ~ b0 N log L,
one-loop running alone leaves the O(log N / N)-size two-loop drift, which is
not summable, so a higher-loop choice is needed. The real content of H4D-0 is
non-perturbative control of the remainder. That is the unpublished
coupling-flow theorem, or exact shooting (note 08). Item (iii) is where the 3D Gaussian
mechanism, δ = 0 and dimension >= 6 tangent decay, is the model. T8
(research/19) tests its 4D Gaussian analogue.

### 9a. Correction (2026-10-02): H4D-0 in the form Σ|δ_N| < ∞ is expected to fail

Theorem 5 is a correct implication, but its hypothesis H4D-0 is probably
**false** for the natural convention, and then Theorem 5 is vacuous in 4D.
Reason (heuristic, one loop):

- Choose the bare couplings by exact shooting, so that depths N and N+1
  reach the same terminal effective coupling g.
- The once-blocked Wilson action Tρ_0^{(N+1)} is not a Wilson action. Its
  tree-level irrelevant terms carry the coefficient β = 1/g_0², and at one
  loop they feed the dimension-4 coupling of later steps at order
  g² · g^{-2} = O(1).
- So the dimension-4 coefficient δ_N of D_N, measured against the shooting
  value β_N, is O(1) (the Λ-parameter mismatch between the blocked and the
  Wilson discretizations) and does not tend to 0.
- In Theorem 2's split, the second bracket δ_N ∂_βΦ_N is then O(1). It
  cancels against the first bracket at leading order instead of each
  bracket being small.
- For the same reason, the absolute placement-summed (L^1) decorrelation of
  the full defect fails: a dimension-4 defect is marginal, and its L^{4m}
  rooted responses of size L^{-4m} sum to O(1) (note 19 (3.8)).

**What the correct 4D statement must contain.** The comparison must be made
at **fixed terminal effective coupling**, with an exact marginal
cancellation. One formulation is a constant-terminal-coupling interpolation.
For s ∈ [0,1] let

    μ_s ∝ exp(-(β_N + c(s))A_N + s(D_N + δ_N A_N)) dU,   c(0) = 0, c(1) = δ_N,

with c(s) chosen so that μ_s has terminal effective coupling g for every s.
This needs Balaban's effective coupling to be defined for these
Wilson-plus-irrelevant actions. Then

    d/ds Z_s = Cov_{μ_s}(e^{z·F}∘b_N, P_N) + c'(s) ∂_βΦ_s,   P_N := D_N + δ_N A_N (+ const),

and P4-4D requires the **signed** combination to be summable. The marginal
part of P_N's terminal effect is exactly compensated by c'(s), because the
terminal coupling stays fixed. Only the residual, irrelevant at the terminal
scale, must decay. This is the same structure as Balaban's terminal
representation (terminal action = g^{-2}A + irrelevant + large-field terms)
and as the route in note 09. H4D-3 (note 21) still controls ∂_βΦ_s, but
the decay now has to come from the **terminal-scale** irrelevant
differences between depths N and N+1, not from a fine-scale split.
Theorem 5, and item (ii) above, should be read with this correction.

## 10. Next concrete steps

1. **H3D-2 for a single block step at fixed N** in the small-field sector.
   Show that Dimock-style polymers H_N(X) at depth N and N+1 differ by
   O(L^{-N}) in the rooted norm when the first step is done exactly. This is
   the smallest piece of H3D-1 not yet attempted.
2. **4D (main line).** Turn H4D-3 into a statement about Balaban's 4D
   effective densities: the β-derivative of a normalized terminal expectation
   is a terminal covariance with A_N, and A_N's block-transported
   dimension-4 content is the effective coupling's derivative. Compute this
   in the 4D Gaussian model (T8) before attempting it non-perturbatively.
