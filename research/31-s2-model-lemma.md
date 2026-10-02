# (S2) at the level of one fluctuation integral: the O(g²) mechanism, proved

Status:

- **Proved here.**
  - Lemma 1: a single input polymer term, integrated against a centered
    fluctuation measure through Balaban's substitution V = U e^{igB},
    produces a "new term" E[f(Ue^{igB})] - f(U) whose size is O(g²) times
    ||f||, measured in the analyticity norm.
  - Lemma 2: the nonlinear version, the log-Laplace map
    f ↦ -log E_μ[e^{-f(Ue^{igB})}], has derivative "transport + O(g²)" under
    the same hypotheses, with the tilted measure's moments controlling the
    constant.
- **Consequence.** The O(g_k²) Lipschitz constant in (S2) of note 29 is a
  Taylor/Cauchy fact for each polymer. By note 29 and the README's 3D route,
  M1-3D is reduced to the parts of (S2) that are **not** in Lemmas 1-2.
  Those are listed in §3.
- **Not proved.** Localization of the output into Balaban's polymer norms
  with exponential decay; large-field cutoffs; the interplay with the
  minimal-configuration background U = U_{k+1}(V').

## 1. Setting

Work with a finite set X of bonds, SU(2) links, and a real background U
on X. Let f be a function of the links on X that is analytic on the complex
neighborhood

    D_α(U) = {U e^{iZ} : Z ∈ sl(2,C)^X, |Z_b| <= α for all b ∈ X},

with ||f|| := sup_{D_α(U)} |f| < ∞, and assume also |f| <= ||f|| on the real
configurations U e^{igB}, B ∈ supp μ. (Balaban's terms are defined on his
small-field domains, and μ carries his small-fluctuation cutoff.) This is the form of CMP 109 (1.18): each
term is analytic on a fixed-size complex domain around the small-field
region, with a sup bound. Let B be a random su(2)^X-valued fluctuation with
law μ, satisfying:

- (M1) E_μ[B] = 0;
- (M2) E_μ|B|_∞² <= σ²(1 + log|X|), where |B|_∞ = max_b |B_b|;
- (M3) P_μ(|B|_∞ > s) <= |X| e^{-s²/(2σ²)} (sub-Gaussian per bond).

For Balaban's step-k fluctuation integral at weak coupling, μ is the
Gaussian with covariance C_k (bounded, exponentially decaying), possibly
tilted by small terms; (M1)-(M3) hold with σ = O(1).

## 2. The lemmas

**Lemma 1 (new term is O(g²)).** If 0 < g <= α/4, then

    |E_μ[f(U e^{igB})] - f(U)| <= ||f|| (C_1 g²σ²(1+log|X|)/α² + 2|X| e^{-α²/(32 g²σ²)}).

*Proof.*

1. Put φ(s) = f(U e^{isgB}) for complex s. For fixed real B with
   g|B|_∞ <= α/2, the path s ↦ U e^{isgB} stays in D_α(U) for |s| <= 2,
   because |s g B| <= α. So φ is analytic on |s| < 2 and bounded by ||f||.
2. By Cauchy on the circle |s| = 2: |φ''(s)| <= 2||f||/(2-|s|)² for |s| <= 1,
   so |φ(1) - φ(0) - φ'(0)| <= sup_{|s|<=1}|φ''|/2 <= ||f||.
3. Sharpen this by scaling. Taking the circle radius R = α/(g|B|_∞) >= 2
   gives |φ''(s)| <= 2||f||/(R-1)² <= 8||f|| g²|B|_∞²/α² on |s| <= 1.
4. The first-order term φ'(0) = g⟨∇f(U), B⟩ is linear in B, so its
   expectation vanishes by (M1).
5. On the event g|B|_∞ <= α/2, the remainder is bounded by
   ½ sup|φ''| <= 4||f|| g²|B|_∞²/α²; take expectations with (M2), so C_1 = 4.
6. On the complement, bound the difference by 2||f||, with probability at
   most |X| e^{-α²/(8g²σ²)} by (M3). The first-order term restricted to this
   event has E[|φ'(0)|; g|B|_∞ > α/2] = O(||f|| |X| e^{-α²/(32g²σ²)})
   (Cauchy-Schwarz with (M3)). ∎

**Lemma 2 (the nonlinear step; Gaussian base).** Let μ be the centered
Gaussian with covariance C, and assume (M2)-(M3) for the tilted measures
below with constant σ_f. For real f with ||f|| <= 1, put
Γ(f) := -log E_μ[e^{-f(Ue^{igB})}] and μ_f ∝ e^{-f(Ue^{igB})} μ. Then for
any h in the same class,

    d/dt Γ(f + t h)|_{t=0} = E_{μ_f}[h(U e^{igB})] = h(U) + R(h),
    |R(h)| <= ||h|| (4 g²σ_f²(1+log|X|)/α² + C_2 |X| e^{-α²/(32g²σ_f²)})
              + C_3 g² ||C||_{∞→∞} |X| ||f|| ||h|| / α².

*Proof.*

1. The derivative of Γ is the tilted expectation.
2. Apply the proof of Lemma 1 to h under μ_f. Only step 4 changes, because
   μ_f is not centered.
3. *Mean shift.* By Gaussian integration by parts (Stein's identity),
   E_{μ_f}[B] = -C E_{μ_f}[∇_B f(Ue^{igB})]. By Cauchy in B on the domain of
   Lemma 1, |∇_{B_b} f(Ue^{igB})| <= 2g||f||/α for each bond. So
   |E_{μ_f}[B]|_∞ <= 2g ||C||_{∞→∞} ||f||/α.
4. *First-order term.* E_{μ_f}[φ'(0)] = g⟨∇h(U), E_{μ_f}[B]⟩, with
   |∇_b h(U)| <= ||h||/α per bond. Summing over the |X| bonds gives the last
   term. ∎

**Reading.** Lemma 2 says that one fluctuation integral maps input data f to
output data whose dependence on f is

    transport (h ↦ h(U), which is (S1)) + O(g²)·||h|| (new terms).

That is (S2)'s Lipschitz constant a_k = O(g_k²) for a single polymer. The
dependence on the input coupling enters through the action term
g^{-2}A(U e^{igB}). Its h-derivative is h = δ(g^{-2})A, of size ||h||
about |δ(g^{-2})|·(local volume), so the same lemma gives b_k = O(g²) per
unit δ(g^{-2}) in the generated terms. That is (S3)'s c_k structure.

## 3. What remains for full (S2) in CMP 102 (3D) / CMP 109 (4D)

1. **Localization.** The output E_{μ_f}[h(Ue^{igB})] - h(U) must be written
   as a sum of polymers with exponential decay in Balaban's norm. For a
   single input polymer at weak coupling this follows from the exponential
   decay of C_k (random-walk expansions, CMP 95/96/99). For the full
   tilted measure it is Balaban's cluster expansion, here applied to a
   **difference** of inputs. That is the standard but long part.
2. **Background.** In Balaban's step the background U = U_{k+1}(V') depends
   on the coarse field. Lemma 1 holds pointwise in V', but the analyticity
   in V' of the output (needed for the next step) uses the analyticity of
   the minimizer map (CMP 102b), which is published.
3. **Large fields.** The cutoff χ(|B| <= p(g)) and the large-field regions.
   Lemma 1's tail term is already exp(-α²/(32g²σ²)), superpolynomially
   small, and the large-field sectors carry their own factors (note 26).

None of these is a new kind of estimate. Each is the difference (Lipschitz)
version of a step Balaban carries out for a single input. In 3D, where the
couplings are explicit and there is no R-operation (note 14), items 1-3 for
CMP 102 are what separates the README's 3D route from a complete M1-3D
proof.
