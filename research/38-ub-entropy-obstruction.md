# (UB): what CMP 122 II gives, a lemma, and why a single-scale (UB) cannot give (P)

Status: **failed attempt** (T30), with one proved lemma and a correction to
note 26.

- **Source reading.** CMP 122 II, (1.14)-(1.37) and (1.48), pp. 359-369,
  separates from the effective action a **positive** Wilson term on the
  large-field domain, with the position-dependent coupling 1/g_k(·)².
  Balaban: "the gauge field in the Wilson action on the right-hand side is
  G-valued, hence the action is positive, and it provides the necessary
  bounds for large plaquette variables" (p. 368). Normalizations cost
  O(1) log g_j^{-2} per MR_j-cube of the large-field domain (p. 381). So an
  action-weighted upper bound **does** hold on the label's own large-field
  domain, with volume counted in level-adapted cubes.
- **Proved here.** Lemma 1: on small fields, the difference of a
  gauge-invariant analytic polymer activity between U and a flat
  configuration is bounded by its norm times the local Wilson action.
  Irrelevant terms therefore cannot spoil an action-weighted bound by an
  extensive amount.
- **Obstruction.** Note 26 Prop. 1 ("(PA) + (UB) ⇒ (P)") is incomplete. Its
  proof turns a lower bound on the action into a mass bound with no
  entropy term. On the persistence event the configuration differs from a
  non-persistent one on a region of scale-k volume about L^{4t}. Any
  single-scale Peierls bound then pays a normalization of at least
  c log(1/δ) per scale-k degree of freedom, that is exp(c L^{4t}), which
  overwhelms e^{-at}. So (P) needs a **multi-scale** suppression: the
  persistence at level j must be paid by the level-j integration, with
  entropy O(1) per level-j cube. Balaban's per-scale large-field factors do
  exactly this, but only for R-modified histories (note 26 §2).
- **Corrected reduction.** (P) ⇐ (PA) + (UB-ms), where (UB-ms) is stated in
  §4. Notes 34-37 supply (PA). (UB-ms) is open.

## 1. Source reading

In CMP 122 II §1 the R-operation at scale k treats the numerator of (1.1) as
follows:

1. The Wilson term A(1/g_k(·)², U'_k) is split as in (1.14)-(1.15). Here
   g_k(·) is the position-dependent coupling, equal to g_j on
   Ω_j \ Ω_{j+1}, and 1/g_j² >= 1/g_k² for j <= k.
2. The part on the large-field domain is kept as a Wilson action, the third
   term of (1.37). Its complex extension is shown to be a small
   perturbation of a positive Wilson action, (1.38)-(1.48).
3. The resulting bound, CMP 122 II §1 at pp. 380-381, has three kinds of
   factors:
   - exp(-γ_0 p_0(g_j)²) per large-field region at scale j (Theorem 1 of
     CMP 102b and (71) of CMP 102);
   - exp(O(1) M^{dR_d+1} d'_j(Z_j)) per large-field domain;
   - O(1) log g_j^{-2} per MR_j-cube from the normalizations.

So at scale k there is a statement of the form

    numerator(U) <= exp(-(1-δ) Σ_Z g_{j(Z)}^{-2} A(U | Z) + C Σ_Z d'_{j(Z)}(Z) log g_{j(Z)}^{-2}) × (small-field part),

where the volume d'_j is counted in level-j cubes. This is (UB) of note 26 on
the label's **own** large-field domain Z.

## 2. Lemma 1: irrelevant terms are dominated by the action

**Lemma 1.** Let h_X be a gauge-invariant polymer activity on a polymer X of
diameter R_X. Suppose h_X is analytic on the complex domain where, in an
axial gauge on X, every link satisfies |a_b| <= α, and |h_X| <= ||h_X|| there.
Suppose U on X has all plaquette angles <= κ, with R_X κ <= α/2. Then

    |h_X(U) - h_X(1)| <= 2 ||h_X|| (C R_X)² Σ_{p⊂X} ϑ_p² / α².

*Proof.* In the axial gauge on X the links satisfy |a_b| <= C R_X κ, as in
note 24 Lemma B. Note 33 Lemma 1 (Ad-invariance and the Schwarz lemma) gives
|h_X(U) - h_X(1)| <= 2||h_X||(C R_X κ/α)². Finally κ² = max_p ϑ_p² <= Σ_p ϑ_p². ∎

**Consequence.** Sum over Balaban's polymers, whose norms satisfy
||h_X|| <= E_0 e^{-κ_0 d(X)}. Each plaquette lies in polymers whose
contributions sum to C E_0. Hence, on the small-field set,

    |E_k(U) - E_k(1)| <= δ_E A_k(U),   δ_E = O(E_0),

with no extensive constant. The irrelevant part of the effective action
changes the Wilson suppression g_k^{-2}A_k only to (g_k^{-2} - δ_E)A_k.

## 3. The entropy obstruction

Consider the persistence event for an R'-label at depth m (note 25 (4.1)).
By note 37, persistence on t levels forces g_k^{-2}A_k(U) >= a t, with a
large. Note 26 Prop. 1 concluded M_{m,t} <= C w_m L^{4m} e^{-at}. This needs
a bound on the mass of a set of configurations whose action exceeds the
reference by at least a t.

*The configurations differ on a large region.* By note 37 Lemma 2, the
action that forces persistence is spread over the annuli ann_0, ..., ann_t.
In scale-k units these have volume about L^{4t}. The fields there are small
(angles of size about ε_j L^{-2(j-l)} in ann_l), so they are inside the
small-field domain. There is no large-field region at scale k on most of
this volume.

*A single-scale Peierls bound pays entropy on that volume.* The standard
step is

    ∫ e^{-g^{-2}A} 1{g^{-2}A >= at} <= e^{-(1-θ)at} ∫ e^{-θ g^{-2}A}.

Compared with ∫ e^{-g^{-2}A}, the last integral is larger by about
θ^{-n/2}, where n is the number of degrees of freedom involved. Here
n ≈ L^{4t}, so the factor is exp(c L^{4t} log(1/θ)), which is far larger
than e^{-at}. Conditioning on the exterior does not help. The fiber
variables W of a label are local, but persistence is a property of the
images, which depend on the exterior V_c, and (P) integrates over V_c with
ν.

*What does work.* In a multi-scale argument the cost at level j is paid by
the level-j fluctuation integral. The relevant volume is the level-j
neighborhood of Λ, which is O(1) level-j cubes. The entropy is then O(1) per
level, against a cost of order p(γ)² per level (note 34 Theorem 3, or the
telescoping of note 34 Lemma 2, which pays exactly one fluctuation per
level). This is how Balaban's per-scale large-field factors work. Notes 34
and 37 are already written level by level, so the deterministic part is
compatible.

## 4. Corrected requirement

**(UB-ms) Multi-scale action-weighted bound (open).** For an R'-label at
scale k and its future history at levels k+1, ..., k+t, the label's mass
restricted to histories in which a level-j fluctuation φ_j near Λ has
|φ_j|_∞ >= ηε_j at every level j of a set G is at most

    C^{|G|} exp(-(1-δ) c_1 Σ_{j∈G} η² p(g_{k+j})²) × (mass with no restriction),

and similarly, with δ_SER/γ² in place of the per-level cost, for the set I of
large levels.

(UB-ms) is the scale-by-scale form of the large-field factors. With note 34
Lemma 2 (telescoping), note 37 and the pigeonhole step, it gives (P) with
a = c p(γ)²/(R+1) - log C. Unlike (UB), it has no entropy problem, because
each factor is produced by one level's own integration over O(1) cubes.

**Where (UB-ms) can come from.** Balaban's history expansion gives exactly
such factors for the **R-modified** densities ρ_k (note 26 §1). The open
point is unchanged from note 26 §2: transferring them to the
pre-replacement label of note 25. What has changed is the diagnosis. The
transfer is **needed**, and no single-scale substitute exists.

## 5. Corrections made

- Note 26, Prop. 1: marked as incomplete (entropy). The corrected statement
  is (P) ⇐ (PA) + (UB-ms).
- README: the (P) line now says (P) ⇐ (UB-ms) + (SER) + notes 34-37.
