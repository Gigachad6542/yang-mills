# T7a: the three-dimensional adjacent-depth comparison (P4-3D) as a conditional theorem

Status summary.

- **Proved here:** the interpolation between the two initial densities on the common lattice; the exact
  covariance formula for d/ds of the normalized terminal generating function; the exact formula for the
  terminal log Radon–Nikodym derivative as an s-integral of conditional expectations of the defect (the
  "tangent T-flow"); the zero-free strip in complex s and its sharpness; the implications
  (H3D-0 + H3D-1) => P4-3D => convergence of all fixed cumulants; (H3D-0 + H3D-3 + H3D-4) => P4-3D;
  the exact matching of Balaban's scale couplings between depths; exact cancellation of all vacuum constants.
- **Conditional:** everything about Yang–Mills beyond this, through the hypotheses H3D-0 .. H3D-4, none of
  which is published. The CMP 102 bounds (5) are used only as a published input, and the paper calls its own
  proof "very sketchy".
- **Heuristic:** the power count giving sigma = 1 without improvement, and the claim that the vacuum
  constant is the only counterterm needed.
- **Failed:** two-sided stability bounds, even when extended uniformly to the interpolating complex family,
  give no Cauchy estimate by themselves.
- **Computation:** an exact 3D Gaussian model with the same block-average geometry. The fine-level defect is
  extensive, while the terminal-level defect is O(eps^2).
- **Not addressed:** nondegeneracy of the limit (the second half of M1).

---

## 1. Setup

Physical torus of side ell. Terminal spacing eps_0 = ell / n_0, block factor L >= 2, and depth-N spacing
eps_N = eps_0 L^{-N}. Lambda_N is the periodic cubic lattice of spacing eps_N, with |Lambda_N| = n_0^3 L^{3N}
sites. Omega_N = SU(2)^{links(Lambda_N)} carries product Haar measure dU, and Omega_* = Omega_0 is the
terminal configuration space.

**Bare measures (CMP 102, Eq. (1), d = 3).**

  rho_0^{(N)}(U) = exp(-beta_N A_N(U) - E_N),   beta_N = 1/g_0^2(eps_N) = 1/(g^2 eps_N) = L^N/(g^2 eps_0),

and mu_N = rho_0^{(N)} dU / Z. Here A_N is the Wilson action on Lambda_N, g > 0 is the fixed dimensionful
coupling, and E_N is Balaban's field-independent constant.

**Block maps.** Q is Balaban's deterministic gauge-covariant average, and T is the group-delta map

  (T rho)(V) = ∫ dU delta_G(V Q(U)^{-1}) rho(U).

This gives ∫ f (T rho) dV = ∫ (f∘Q) rho dU (research/14, Prop. 1). We write

- q_N : Omega_{N+1} -> Omega_N for one block step,
- b_N = Q^{(N)} : Omega_N -> Omega_* for the N-fold composition,
- nu_N = (b_N)_* mu_N for the terminal law.

**Tests.** Take bounded measurable terminal tests F_1..F_q with |F_j| <= B_j, for example functions of traces
of holonomies of closed coarse loops of the terminal block field. For a polyradius rho, set
S_rho = sum_j B_j rho_j < log 2 and

  Z_N(z) = nu_N(exp(z·F)),   z in D_rho.

### H3D-0 (common lattice and absolute continuity)

(a) **Compatibility.** b_{N+1} = b_N ∘ q_N for every N.

(b) **Absolute continuity.** mu~_N := (q_N)_* mu_{N+1} = (T rho_0^{(N+1)}) dV / Z is mutually absolutely
continuous with mu_N. Its log-density

  D_N := log( T rho_0^{(N+1)} / rho_0^{(N)} ),

defined up to an additive constant, is a bounded measurable function on Omega_N for each fixed N. No
uniformity in N is assumed.

*Status.*

- Part (a) holds by construction when the same deterministic average Q (in lattice units) is used at every
  scale, as in CMP 102, where one map T is iterated by rho_{k+1} = T rho_k. It then reduces to
  Q^{(N+1)} = Q^{(N)} ∘ Q. This is a source-reading, and I did not re-verify the scale-independence of Q in
  CMP 98.
- Part (b) is **not published**. The lower bound in CMP 102 (5) holds only on the small-field domain chi.
  Part (b) is qualitative and at fixed N, and it is used only to make the manipulations below finite.

---

## 2. Deliverable 1: interpolation and exact identities (proved)

Fix N. Write mu_0 := mu_N, D := D_N, b := b_N and G := exp(z·F) ∘ b, so |G| <= e^{S_rho} on D_rho.

**Interpolation.** For s in C,

  rho^{(s)} := (rho_0^{(N)})^{1-s} (T rho_0^{(N+1)})^{s} = rho_0^{(N)} e^{sD}   (up to s-dependent constants),
  Xi(s) := mu_0(e^{sD}),
  mu_s := e^{sD} mu_0 / Xi(s)   (where Xi(s) ≠ 0),
  Z_s(z) := mu_s(G).

### Proposition 1 (endpoints and covariance identity)

(i) Z_{s=0}(z) = Z_N(z) and Z_{s=1}(z) = Z_{N+1}(z) for every z in C^q.

(ii) The numerator s -> mu_0(G e^{sD}) and Xi are entire. On {Xi ≠ 0}, which contains the real axis,

  d/ds Z_s(z) = mu_s(G D) - mu_s(G) mu_s(D) = Cov_{mu_s}(G, D).

(iii) Z_{N+1}(z) - Z_N(z) = ∫_0^1 Cov_{mu_s}(exp(z·F)∘b, D) ds. Every mu_s with s in [0,1] is a probability
measure.

*Proof.*

(i) mu_1 = e^D mu_0 / mu_0(e^D) = mu~_N by H3D-0(b). Then
mu~_N(exp(z·F)∘b_N) = mu_{N+1}(exp(z·F)∘b_N∘q_N) = mu_{N+1}(exp(z·F)∘b_{N+1}) = Z_{N+1}(z) by H3D-0(a).

(ii) D and G are bounded, so e^{sD} and G D e^{sD} are dominated uniformly for s in compact sets. We may
therefore differentiate under the integral, which gives entirety. Apply the quotient rule to
mu_0(G e^{sD}) / Xi(s).

(iii) For real s, e^{sD} > 0, so Xi > 0. Integrate (ii) over [0,1]. ∎

### Proposition 2 (terminal Radon–Nikodym derivative: the tangent T-flow)

Let kappa(W, dU) be a regular conditional distribution of mu_0 given b. It exists because Omega_N and
Omega_* are compact metrizable. For W in Omega_* and real s, define

  Y_s(W) = ∫ kappa(W,dU) e^{sD(U)},   m_s(W) = ∫ kappa(W,dU) D(U) e^{sD(U)} / Y_s(W).

Then:

(i) nu_s := b_* mu_s has density h_s = Y_s / Xi(s) with respect to nu_0 = nu_N. In particular
dnu_{N+1}/dnu_N = h_1.

(ii) m_s is a version of E_{mu_s}[D | b = W].

(iii) For **every** W,

  log (dnu_{N+1}/dnu_N)(W) = ∫_0^1 ( m_s(W) - mu_s(D) ) ds,   and mu_s(D) = nu_s(m_s).

(iv) osc_W log(dnu_{N+1}/dnu_N) <= ∫_0^1 osc_W m_s ds <= sup_{s in [0,1]} osc m_s.

(v) Covariance form: d/ds Z_s(z) = nu_s( exp(z·F) (m_s - nu_s(m_s)) ).

(vi) Multi-step (tangent) recursion. Put nu_{k,s} = (Q^{(k)})_* mu_s on Omega^{(k)} (spacing L^k eps_N)
and D_k^{(s)} := E_{mu_s}[D | Q^{(k)}]. Then

  D_0^{(s)} = D,   D_{k+1}^{(s)} = E_{nu_{k,s}}[ D_k^{(s)} | Q ],   m_s = D_N^{(s)},

and ∂_s log(T^k rho^{(s)}) = D_k^{(s)}, up to an s-dependent constant. Here T^k rho^{(s)} is read as the
Radon–Nikodym derivative of (Q^{(k)})_*(e^{sD} mu_0) with respect to nu_{k,0} when a Haar density is not
available.

*Proof.*

(i) Disintegration gives mu_0(f∘b e^{sD}) = ∫ nu_0(dW) f(W) Y_s(W) for bounded f.

(ii) Replace e^{sD} by D e^{sD} in the same identity.

(iii) D is bounded, so for each fixed W the map s -> Y_s(W) is smooth with ∂_s log Y_s = m_s, and
∂_s log Xi = mu_s(D). Since Y_0 = Xi(0) = 1, integrating from 0 to 1 gives the formula.

(iv) Oscillation is subadditive under ∫ ds, and the constants mu_s(D) drop out.

(v) Combine Prop. 1(ii) with the tower property.

(vi) sigma(Q^{(k+1)}) ⊂ sigma(Q^{(k)}), so the tower property applies. The derivative formula is (iii) with
b replaced by Q^{(k)}. ∎

In 3D the flow is the exact T-iteration with no R-step (research/14). The map D -> D_k^{(s)} is therefore
exactly the linearization of Balaban's flow at rho^{(s)} along the direction D. Proposition 2 turns P4-3D
into the **irrelevance of the one-step defect under the exact linearized T-flow**.

### Proposition 3 (complex s: zero-free strip, sharp)

Xi(s) ≠ 0 on the strip |Im s| < pi / osc D. Z_s(z) is holomorphic there and the identity of Prop. 1(ii)
holds on it. The width cannot be improved in general.

*Proof.* Let c be the midpoint of the range of D and D' = D - c, so |D'| <= osc D / 2. For s = t + iu,
Re e^{sD'} = e^{tD'} cos(u D') > 0 when |u| osc D / 2 < pi/2. Hence Re(e^{-sc} Xi(s)) > 0.

For sharpness, take the two-point space with mu_0 = (1/2, 1/2) and D = (0, M). Then
Xi(s) = (1 + e^{sM})/2 vanishes at s = i pi / M = i pi / osc D. ∎

Since osc D_N is extensive (Section 6), the proved strip has width O(eps_N^3). A complex s-disc of radius
independent of eps is therefore a genuine hypothesis and is not free. The proofs below use only real s.

---

## 3. Deliverable 2: hypotheses on the 3D RG

Notation: m_{N,s} = E_{mu_{N,s}}[D_N | b_N = ·], and sigma > 0 is fixed. The unimproved power count suggests sigma = 1.

**H3D-1 (terminal tangent decay, sup form).** There are C_1 < ∞ and sigma > 0 with

  eta_N := sup_{s in [0,1]} osc_W m_{N,s}(W) <= C_1 L^{-sigma N}   for all N.

**H3D-1' (local L^1 form).** The defect decomposes as D_N = c_N + sum_{x in Lambda_N} D_{N,x}, with bounded
D_{N,x}. With m_{N,s,x} := E_{mu_{N,s}}[D_{N,x} | b_N], the hypothesis is

  sum_x sup_{s in [0,1]} E_{mu_{N,s}} | m_{N,s,x} - mu_{N,s}(D_{N,x}) | <= C_1' eps_N^{sigma}.

On average this is C eps_N^{3+sigma} per site, times |Lambda_N| ~ (ell/eps_N)^3 sites. This is the task's
third candidate. H3D-1 implies H3D-1' (take D_{N,x} = D_N/|Lambda_N|; the sum is then mu_s|m_s - mu_s m_s| <= osc m_s), so it is
the weaker hypothesis.

**H3D-2 (RG polymer form; implies H3D-1).** For s in [0,1], the terminal tangent defect
m_{N,s} = D_N^{(s)} on the terminal lattice Lambda_0 has a connected-polymer representation modulo
constants, D_N^{(s)} = c + sum_X d_N^{(s)}(X), with rooted oscillation norm

  sup_x sum_{X ∋ x} osc d_N^{(s)}(X) / |X| <= etabar L^{-sigma N}.

A sufficient mechanism is a scale-by-scale contraction eta_{k+1} <= L^{-sigma} eta_k of the rooted norms of
D_k^{(s)} starting from eta_0 <= etabar. By power counting that would be the L^{3-4} = L^{-1} scaling of the
dimension-4 component. Note that eta_0 is O(1), not small, so all of the smallness must come from the
contraction.

H3D-2 => H3D-1 with C_1 = n_0^3 etabar, by research/09 Prop. 4 applied on the fixed terminal lattice. (Proved.)

**H3D-3 (uniform differentiability in the physical coupling).** For the Wilson family at spacing eps_N with
inverse coupling beta, let Phi_N(z; beta) := mu_{N,beta}(exp(z·F)∘b_N). There are r > 0 and M' such that for
all N, z in D_rho and g'^2 in [g^2 - r, g^2 + r],

  | ∂_{g'^2} Phi_N(z; 1/(g'^2 eps_N)) | <= M'.

Equivalently, |Cov_{mu_{N,beta}}(exp(z·F)∘b_N, A_N)| <= M' g'^4 eps_N at beta = 1/(g'^2 eps_N). The natural
stronger version (the task's second candidate) is analyticity of Phi_N in beta on the disc
|beta - beta_N| < r beta_N = r/(g^2 eps_N) with a uniform bound M. It implies H3D-3 by the Cauchy/Schwarz
estimate |Phi(beta_N + w) - Phi(beta_N)| <= 2M|w| / (r beta_N).

**H3D-4 (one-step structure plus tangent decay of the irrelevant part).**

(a) D_N = -c_N - delta_N A_N - P_N, with |delta_N| <= deltabar uniformly in N. Here P_N is bounded and
gauge-invariant, and its component along A is removed by some fixed convention.

(b) For the measures mu^#_{N,s} ∝ exp(-(beta_N + delta_N) A_N - s P_N), s in [0,1],

  sup_s osc_W E_{mu^#_{N,s}}[P_N | b_N = W] <= C_4 L^{-sigma' N}.

**H3D-5 (the task's first candidate; not sufficient alone; see Section 5).** The CMP 102 inductive bounds (5)
hold uniformly for the complex family exp(-(beta_N + s delta_N) A_N - s P_N), |dist(s, [0,1])| < s_0. For
this to help, the **s-dependent part** of the terminal activities must also be O(L^{-sigma N}) in the rooted
norm. That quantitative strengthening is exactly H3D-2.

---

## 4. Deliverable 3: the conditional theorem (proved)

### Theorem 1 (H3D-0 + H3D-1 => P4-3D => M1-3D convergence)

Assume H3D-0 and H3D-1. For every bounded test family with S_rho < log 2 and all N:

(a) osc log(dnu_{N+1}/dnu_N) <= C_1 L^{-sigma N}. Also ||nu_{N+1} - nu_N||_{TV,*} <= e^{C_1 L^{-sigma N}} - 1.

(b) sup_{z in D_rho} |Z_{N+1}(z) - Z_N(z)| <= e^{S_rho} (e^{C_1 L^{-sigma N}} - 1) <= C L^{-sigma N}, with
C = e^{S_rho} C_1 e^{C_1}.

(c) The normalized logarithms W_N = Log Z_N are holomorphic on D_rho and satisfy
||W_{N+1} - W_N|| <= C L^{-sigma N} / (2 - e^{S_rho}). They converge uniformly to a holomorphic W_∞, and
every joint cumulant satisfies

  |kappa_alpha(Z_∞) - kappa_alpha(Z_N)| <= alpha! rho^{-alpha} C L^{-sigma N} / ((2 - e^{S_rho})(1 - L^{-sigma})).

(d) nu_N converges in total variation to a probability measure nu_∞ on Omega_*.

*Proof.*

(a) Prop. 2(iv) and H3D-1 give the oscillation bound. Research/07 Prop. 1 turns it into
|nu_{N+1}(f) - nu_N(f)| <= ||f||_∞ (e^{eta_N} - 1).

(b) Apply (a) to f = exp(z·F), for which ||f||_∞ <= e^{S_rho}. Then use e^x - 1 <= x e^x.

(c) Research/03 Theorem C gives the zero-free disc and the Lipschitz bound for Log. Theorem A gives summation
of the geometric increments together with Cauchy's estimate.

(d) The increments are summable in the dual TV norm, which is complete on finite signed measures. The limit
is positive with mass 1. ∎

### Theorem 1' (the L^1 route)

H3D-0 + H3D-1' imply sup_{D_rho} |Z_{N+1} - Z_N| <= e^{S_rho} C_1' eps_N^sigma = e^{S_rho} C_1' eps_0^sigma L^{-sigma N}.
Hence conclusion (c) holds. In place of (d), Z_N converges uniformly on D_rho, but TV convergence is not claimed.

*Proof.* By Prop. 1(iii) and the tower property,

  |Cov_{mu_s}(G, D)| = |mu_s( G (m_s∘b - mu_s D) )| <= e^{S_rho} sum_x mu_s | m_{s,x}∘b - mu_s D_x |.

Integrate over s in [0,1]. ∎

### Theorem 2 (the split route: H3D-0 + H3D-3 + H3D-4 => P4-3D)

Assume H3D-0, H3D-3 and H3D-4, and let N be large enough that deltabar g^2 eps_N <= 1/2. Then

  sup_{D_rho} |Z_{N+1} - Z_N| <= e^{S_rho} (e^{C_4 L^{-sigma' N}} - 1) + 2 M' g^4 deltabar eps_0 L^{-N},

which is O(L^{-min(1, sigma') N}). Theorem 1(c) follows.

*Proof.* Insert the Wilson measure mu^# at beta_N + delta_N:

  Z_{N+1} - Z_N = [mu~_N - mu^#](G) + [mu^# - mu_N](G).

**First bracket.** From H3D-4(a), mu~_N = e^{-P_N} mu^# / norm. Apply Props. 1–2 with base mu^# and defect
-P_N, then use H3D-4(b) and research/07 Prop. 1.

**Second bracket.** It equals Phi_N(z; beta_N + delta_N) - Phi_N(z; beta_N). With
g'^2 = 1/((beta_N + delta_N) eps_N) = g^2 / (1 + delta_N g^2 eps_N), we have
|g'^2 - g^2| <= 2 g^4 deltabar eps_N <= r for large N. The fundamental theorem of calculus in g'^2, applied to the complex-valued function on the real segment
with H3D-3, bounds the bracket by 2 M' g^4 deltabar eps_N. ∎

### Corollary 3 (bounded bare-coupling shifts are irrelevant; proved conditional on H3D-3)

Under H3D-3, let beta_N' = beta_N + b_N be any bare couplings with sup |b_N| < ∞. Then
|Phi_N(z; beta_N') - Phi_N(z; beta_N)| <= 2 M' g^4 (sup|b|) eps_N -> 0 (for N with sup|b| g^2 eps_N <= 1/2). Both choices have the same limit,
if either has one.

---

## 5. Coupling matching and counterterms

**Explicit matching (proved, elementary).** Depth N uses beta_N = 1/(g^2 eps_N) with one fixed g. Balaban's
scale couplings are g_k = g (L^k eps)^{1/2}. Depth N+1 at step k+1 and depth N at step k both give

  g (L^{k+1} eps_{N+1})^{1/2} = g (L^k eps_N)^{1/2}.

The terminal coupling is therefore g_{K_N} = g eps_0^{1/2} for every N. In particular, the leading
coefficient of the once-blocked finer density (step 1 at depth N+1) equals 1/g_0^2(eps_N) in (5) exactly.
Classical scaling also matches: (1/(g^2 eps)) × eps^4 F^2 × eps^{-3} = (1/g^2) ∫ F^2 at every depth.

**Vacuum constants (proved).** E_N and c_N multiply densities by field-independent constants. The measures
mu_N, mu~_N and all normalized Z_N, nu_N are independent of them. This is also why the centering mu_s(D)
appears in Prop. 2(iii). The "identity operator" part of the defect cancels exactly.

**Finite coupling drift (heuristic).** The one-loop correction to 1/g_0^2 in lattice units is a pure number
delta = O(1), since the loop parameter is g_0^2 = g^2 eps. This corresponds to a relative physical-coupling
change of g^2 eps delta = O(L^{-N}). By Theorem 2 / Cor. 3 it is summable, so **no coupling counterterm is
needed**. Subtracting it (beta_N = 1/(g^2 eps_N) + delta_*) is an optional improvement. It would heuristically
raise sigma from 1 to 2 (classical dimension-6 artifacts ~ (1/g_0^2) eps^6 × eps^{-3} ~ eps^2, two-loop
~ (g^2 eps)^2).

**Other counterterms (heuristic / source-reading).**

- Exact lattice gauge invariance forbids a gauge-field mass term.
- The dimension-3 Chern–Simons density is parity-odd and is excluded if Q (hence T) commutes with lattice
  reflections. This symmetry of Balaban's average is a hypothesis I did not check.
- No other gauge-invariant local operator has dimension < 4. The first nontrivial one is tr F^2.
- CMP 102 Eq. (1) describes E as containing only normalization and vacuum-energy counterterms (source-reading).

Conclusion: under the hypotheses, the vacuum constant is the only counterterm, and it cancels exactly.

**Power count behind sigma (heuristic).**

- A gauge-invariant local defect D_x = O(1) in lattice units affects terminal observables only through its
  non-identity operator content. Mixing into dimension-Delta operators gives eps^Delta per site times
  eps^{-3} sites, i.e. eps^{Delta-3}. Tree-level pieces carry an extra 1/g_0^2 = 1/(g^2 eps).
- tr F^2 (Delta = 4), quantum: gives eps. This dominates.
- Dimension 6, tree-level: gives eps^2.
- So sigma = 1 unimproved, and 2 with one-loop improvement.

### F1 (failed: stability bounds alone give no Cauchy estimate)

Suppose bounds of CMP 102 type (5) held uniformly for the complex family in a tube of width s_0 around [0,1].
Assume further that the terminal log-densities are analytic in s in the tube and satisfy
|log rho_K^{(s)}(W) - log rho_K^{(0)}(W)| <= O(1) |T^{(K)}| with ε-independent constants. Here
|T^{(K)}| = n_0^3 is the number of terminal sites. Cauchy then gives |∂_s log rho_K^{(s)}| <= O(1) |T^{(K)}| / s_0. By Prop. 2 this bounds osc log(dnu_{N+1}/dnu_N)
by an **N-independent constant**, not by a decaying one.

The obstruction is structural. The bounds (5) have the same form, with O(1) uniform for g_k in a bounded set,
for the alternating sequence g at even N and 2g at odd N. Any argument using only them would therefore also
prove that the alternating terminal laws are Cauchy. That forces the limit to be independent of g. At N = 0 the terminal law is the Wilson measure at
beta = 1/(g^2 eps_0), which visibly depends on g. For the limit, g-dependence is expected but unproved. This last step is
heuristic, since it depends on the g-dependence of the limit.

Smallness requires the tangent (difference) estimate H3D-1/H3D-2, not two-sided bounds. This matches the
research/13 counterexamples.

### F2 (failed: fine-level oscillation criterion)

Applying research/07 Prop. 1 directly on Lambda_N needs osc D_N small. But osc D_N is extensive (Section 6:
the relative defect per mode is O(1) and the squared HS norm per site is a constant). The trivial contraction
osc m_s <= osc D (conditional expectation averages) is proved but gives an ε^{-3} bound. All the gain must come
from the terminal projection, which is why the hypotheses are formulated at the terminal scale.

---

## 6. Computation: exact 3D Gaussian model (scripts in /private/tmp/ym-r3/T7a/)

This is a scalar Gaussian stand-in for the linearized theory. It has no coupling renormalization, and it uses
the same geometry:

- unit torus;
- terminal lattice 4^3 (eps_0 = 1/4), L = 2;
- action (1/2) sum eps^3 [(grad phi)^2 + phi^2];
- block map = plain average over L^3 cubes.

**Terminal level (gauss3d.py).** The relative difference r = C_{N+1}/C_N - 1 of the terminal covariances,
per terminal momentum:

| N | eps_N | max \|r\| | HS norm |
|---|---|---|---|
| 1 | 1/8 | 0.499 | 3.26 |
| 2 | 1/16 | 0.353 | 1.88 |
| 3 | 1/32 | 0.182 | 0.760 |
| 4 | 1/64 | 0.0635 | 0.232 |
| 5 | 1/128 | 0.0178 | 0.0620 |
| 6 | 1/256 | 0.00461 | 0.0158 |

The successive ratios of the HS norm are 3.27, 3.74 and 3.92, approaching 4 = L^2. So sigma = 2 in the
Gaussian model, consistent with the power count for the leading artifact of this model (dimension 5 for a
scalar, i.e. eps^2).

**Fine level (gauss_fine.py).** On the common lattice Lambda_N, compare the once-blocked finer covariance with
the coarse lattice covariance per mode:

| sites | max \|r\| | HS^2 / sites |
|---|---|---|
| 64 | 0.499 | 0.166 |
| 512 | 0.500 | 0.167 |
| 4096 | 0.500 | 0.167 |
| 32768 | 0.500 | 0.167 |
| 262144 | 0.500 | 0.167 |

The defect is extensive: O(1) per UV mode. The terminal effect nevertheless decays like eps^2. This is the
mechanism behind H3D-1 in a model where everything can be computed.

**identity_check.py.** Numerical check of Prop. 2(iii) and Prop. 1(ii) on a random finite example. The errors
are 3e-8 (trapezoid rule) and 8e-11.

---

## 7. Logical summary

The Yang–Mills content of P4-3D is H3D-0 and H3D-1, or alternatively H3D-3 and H3D-4:

- H3D-0 + H3D-1 => P4-3D (Thm. 1). Thm. 1 then gives M1-3D convergence: geometric Cauchy bounds for Z_N on a
  fixed polydisc, convergence of every fixed cumulant, and TV convergence of the terminal laws.
- H3D-0 + H3D-1' => convergence of Z_N and of all cumulants (Thm. 1').
- H3D-0 + H3D-3 + H3D-4 => the same, with rate L^{-min(1, sigma') N} (Thm. 2).

The bare couplings are beta_N = 1/(g^2 eps_N) with a fixed g, and no counterterm besides the vacuum constant is
needed. That the vacuum constant is the only counterterm is conditional on the hypotheses and on the heuristic
power count. Nondegeneracy of the limit is not addressed.
