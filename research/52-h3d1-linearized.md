# H3D-1' at the linearized level, from note 44

Status: **proved** (T46) for the abelian Gaussian 3D model with Balaban's
linear block average. It applies to defects whose non-constant part is a
sum of local quadratic forms with no F² (marginal) part. The F² part is
removed by note 18's split H3D-4(a), and its coefficient is handled by
H3D-3.

## 1. d-dimensional version of note 44 Theorem 1

The proof of note 44 Theorem 1 uses:

- the alias factorization J_ρ(p_ℓ) = A_ρ(p_ℓ) c_ρ(K), from
  (1 - e^{-ip}) D_M(p) = 1 - e^{-iK};
- the Fejér/Parseval sums;
- the alias-0 fraction.

None of these depends on d. In d dimensions A_ρ = Π_{j=1}^d D_M(p_j) · D_M(p_ρ),
and

    c_0^{(d)} = (4/π²)^{d-1} · 16/π⁴,
    ||∇_ν F_min||_2 <= (2π √d / √(c_0^{(d)})) M^{-1} ||F_min||_2.

(The factor √d comes from |r(p_0)|² <= d π²·4/M².) Theorem 3 of note 44
(second differences) carries over in the same way.

## 2. Proposition (H3D-1', linearized)

Let the one-step defect at depth N have non-constant part
D_N - c_N = Σ_x P_x, where P_x(F) = Σ_{y,z} q_x(y, z) F(y) F(z) is a local
quadratic form in the curvature. Assume:

- the kernels q_x are symmetric, block-periodic and exponentially
  decaying;
- the total marginal coefficient vanishes (F² part removed):
  Σ_x Σ_y q_x(·, y) = 0 in the block-average sense of note 51 Lemma 4;
- the second moments satisfy M_2(Σ_x q_x) <= c_N (fine units).

Then in the Gaussian model, with M = L^N and terminal volume V_0 (number of
terminal plaquettes):

    Σ_x E|E[P_x | b_N] - E P_x| <= C c_N (M^{-1} ||v||_∞ + M^{-2} M_2) E[2S(Φ)],

where v is the redistribution field of note 51 Lemma 4, and
E[S(Φ)] = O(V_0) is the expected terminal minimal energy. With
c_N = O(g² ε_N) from the one-step defect, this is O(g² ε_N ε_N^{σ'}) with
σ' >= 1. That is H3D-1' with σ >= 2.

*Proof.*

1. *Gaussian conditioning.* F = TΦ + Ψ, with Ψ independent of Φ (the
   Gaussian fluctuation). So E[P_x(F) | Φ] = P_x(TΦ) + E P_x(Ψ) + (cross
   terms with zero mean). Hence E[P_x|b_N] - E P_x = P_x(TΦ) - E P_x(TΦ).
2. *Choice of local pieces.* H3D-1' sums absolute values over the pieces,
   so the decomposition must be chosen first. Apply note 51 Lemma 4's
   identity to each q_x. This gives P_x = Σ_y c_x(y) F(y)² - ½ Σ q_x (F(y) - F(z))².
   Collect all F² terms into Σ_y c(y) F(y)², with c = Σ_x c_x. This sum has
   zero block average by assumption. Rewrite it with note 33 Lemma 2 as
   Σ_{x,ν} v_ν(x)(F(x)² - F(x+e_ν)²). The new local pieces are
   D_{N,x} := -½ Σ_{y,z} q_x(y,z)(F(y) - F(z))² + Σ_ν v_ν(x)(F(x)² - F(x+e_ν)²).
   Each has zero marginal part.
3. *Pointwise bound for the absolute sum.* By Cauchy-Schwarz,
   Σ_x |Σ_ν v_ν(x)(F(x)² - F(x+e_ν)²)| <= 2 d ||v||_∞ ||F|| ||∇F||. Also
   Σ_x |½ Σ q_x (F(y) - F(z))²| <= M_2(|q|) Q_1(F), by the path bound of
   note 51 Lemma 4, item 1.
4. *Transport.* By §1, ||∇TΦ|| <= C M^{-1} ||TΦ|| and
   Q_1(TΦ) <= d C² M^{-2} ||TΦ||². Also ||TΦ||² = 2S(Φ).
5. Take expectations. The constant parts E P_x(Ψ) cancel in the
   centring. ∎

## 3. What this gives for M1-3D

- At the linearized level, H3D-1' holds with σ >= 2. That matches note 18's
  Gaussian computation (dimension-6 defects decay like L^{-2N}), and is now
  proved.
- The interacting version needs:
  - (i) the generated terms of each step, O(g_k² p²) by note 42 / (A_s),
    with g_k² = g² ε_k geometric in 3D;
  - (ii) the non-abelian transfer (note 45, (NA); corrected to (NA♭) in
    note 54, to cover holonomy sectors);
  - (iii) the large-field sectors of CMP 102. There the factors are
    arbitrary powers of ε (CMP 119 introduction: "for d < 4 ... the bound
    ... can be estimated by an arbitrarily large power of ε"), so they are
    harmless for H3D-1'.

*Status of this paragraph: conditional reduction, now written out in note 61
(Theorem 1, hypotheses (H1)-(H5)).* The interacting H3D-1' is obtained there by
transporting polymer activities in the mixed norm, not by the exact Gaussian
split of §2 step 1. That split fails under the interacting measures μ_{N,s}.
The summary below is superseded by note 61 §4, which replaces (NA) by (NA♭),
H3D-0(b) by note 53, and adds (H3)-(H5):

So **M1-3D ⇐ (A_s) [3D: reduced to CMP 102's sixth-order remainder bound]
+ (NA) [3D] + H3D-0(b) [qualitative, fixed-N]**, together with notes 17,
18, 44-46, 51-52. Each of these is either a reading of CMP 102 or a
fixed-N qualitative statement. The 3D continuum limit of terminal
observables is within reach of a careful check of CMP 102's single-step
analysis.

## 4. Remark on H3D-0(b) (qualitative, fixed N; not resolved)

H3D-0(b) asks, for each fixed N, that D_N = log(Tρ_0^{(N+1)}/ρ_0^{(N)}) be
bounded. ρ_0^{(N)} = e^{-β_N A_N} is bounded above and below, so the question
is whether the push-forward density of e^{-β A} dU under Balaban's average Q
(CMP 98 (15)) is bounded above and below.

- *Lower bound (plausible).* Q is real-analytic away from the measure-zero
  set where the logarithms of the loop holonomies U(Γ_{c,x}) U(Γ_c)^{-1}
  are undefined (SU(2) angle π). Its derivative at small fields is the
  linear average (CMP 98 (14)), which is surjective. If every fibre
  Q^{-1}(V) contains a regular point, then by lower semicontinuity and
  compactness the density is bounded below.
- *Upper bound (may fail).* Near critical values the coarea formula gives
  densities like ∫_{fibre} 1/J, which can be unbounded although integrable.
  Then D_N is unbounded above on a small set.

Note 18 uses boundedness of D_N to differentiate under the integral
(Prop. 1(ii)) and to get osc bounds. If the upper bound fails, the natural
replacement is exponential integrability of D_N together with bounds on
the small-field set (CMP 102 (5)). The large-field complement then
contributes through CMP 102's large-field factors, which are arbitrary
powers of ε. This adaptation is not carried out here. H3D-0(b) remains the
one qualitative item on the 3D route.

*Superseded by note 53, which proves H3D-0(b) itself (density bounded above
and below). §4 and §4a remain correct but are no longer needed.*

### 4a. Weakening H3D-0(b) (proved, except one integrability input)

**(b')** μ̃_N and μ_N are mutually absolutely continuous, with density
f = e^{D_N}/Ξ(1), and the relative entropy ∫ f log f dμ_N is finite.

**Proposition 4.** Under (b'), note 18 Proposition 1(iii) and Theorem 1' hold
as stated (with H3D-1' in place of H3D-1).

*Proof.*

1. Ξ(1) = μ_N(e^{D}) is finite, because μ̃_N is a probability measure. By
   Hölder, Ξ(s) = μ_N(e^{sD}) <= Ξ(1)^s < ∞ for s ∈ [0, 1], and Ξ(s) > 0
   because D is finite a.e.
2. For s ∈ [0, 1), D e^{sD} is integrable, since |D| e^{sD} <= C_s(1 + e^{D}).
   At s = 1, integrability of D e^{D} is the finite-entropy assumption. So
   s ↦ Z_s is differentiable on [0, 1) with derivative Cov_{μ_s}(G, D), and
   continuous on [0, 1] by dominated convergence with dominating function
   e^{S_ρ}(1 + e^{D}). Hence Z_{N+1} - Z_N = ∫_0^1 Cov_{μ_s}(G, D) ds,
   possibly as an improper integral at s = 1.
3. Theorem 1' uses only this identity, the tower property
   Cov(G, D) = Cov(G, E[D | b]) (valid for D ∈ L¹(μ_s)), and H3D-1'. ∎

**Where (b') comes from.**

- *Mutual absolute continuity.* Q is real-analytic off a measure-zero set,
  and its derivative is surjective at small fields. So it is surjective on
  an open dense full-measure set, and the push-forward of the absolutely
  continuous measure e^{-βA}dU is absolutely continuous. Its density is
  positive a.e. because a.e. fibre contains regular points (Sard). So (b')
  minus the entropy condition holds.
- *Finite entropy (assumed).* This holds if the push-forward density lies
  in L^p for some p > 1. That is the typical behaviour for push-forwards
  under real-analytic maps with generically surjective derivative
  (Łojasiewicz-type bounds on the Jacobian near the critical set). It is
  not verified here for Balaban's Q.

With Proposition 4, the 3D route is:

    M1-3D <= (A_s) + (NA) + [L^p, p > 1, push-forward density for fixed N],

together with notes 17, 18, 44-46, 51-52.
