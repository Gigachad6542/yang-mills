# Corrected 4D master reduction: comparison at fixed terminal coupling

Status:

- **Proved here.** Theorem 1. M1-4D convergence (P4 with summable
  increments, hence convergence of the terminal generating functions and of
  all cumulants) follows from three groups of hypotheses on Balaban's
  construction:
  - (H0) the coupling flow with exact shooting;
  - (T) memory decay of the terminal effective-action contributions between
    depths;
  - (B) a summable R-bias series with memory decay.
- **What this replaces.** It replaces the split of research/18 Theorem 5,
  whose summable-matching hypothesis is expected to fail (research/18 §9a).
  Here the marginal direction never appears: every depth is shot to the same
  terminal effective coupling g, so terminal laws are compared through their
  irrelevant and large-field parts only.
- **Open.** Every hypothesis. The note records which earlier notes reduce
  each one.

## 1. Objects

For depth N (K_N = N block steps from spacing ε_0 L^{-N} to ε_0):

- **Terminal space.** X is the fixed terminal configuration space, with
  normalized Haar measure λ and terminal small-field set S (note 17).
- **Physical law.** ν_N = (b_N)_* μ_N, the exact T-pushforward of the Wilson
  measure at the shooting bare coupling β_N.
- **R-modified law.** ν_N^R = ρ^{R,N} dλ / Z^R_N, where ρ^{R,N} is Balaban's
  R-modified terminal density (CMP 122 II Theorem 1, valid under H0). By
  exact mass preservation, Z^R_N equals the physical partition function.
- **R-bias.** B_N(G) := ν_N(G) - ν_N^R(G) for bounded G.
- **Tests.** G = e^{z·F} with ||G||_∞ <= e^{S_ρ} on the source polydisc
  (notes 03, 07).

## 2. Hypotheses

**(H0) Coupling flow with shooting** (note 22 reduces it to (C), (S), (D)).
For every N there is β_N such that Balaban's effective couplings satisfy
g_k <= γ for all k and terminal coupling g_{K_N} = g, the same g for all N.

**(T) Terminal memory decay.** ||ν^R_{N+1} - ν^R_N||_TV <= η_N with
Σ_N η_N < ∞.

A sufficient form: there are constants c_N such that

    sup_{V ∈ S} | log ρ^{R,N+1}(V) - log ρ^{R,N}(V) - c_N | <= η_N,   (2.1)

together with the large-field mass condition

    ∫_{X∖S} |ρ^{R,N+1} e^{-c_N} - ρ^{R,N}| dλ / Z^R_N <= η_N.   (2.1')

Then ||ν^R_{N+1} - ν^R_N||_TV <= C η_N. (Write both laws relative to
ρ^{R,N}dλ/Z^R_N: on S the density ratio is e^{c_N ± η_N} times a common
normalization, off S use (2.1'), and the normalization constants differ by
O(η_N).) A sup over all of X is not assumed, because Balaban's lower bound
holds only on χ = 1_S.

*Sufficient structure.* Suppose that on S, log ρ^{R,N} = -g^{-2}A(U_K(V))
- Σ_{j=0}^{K_N} e_{N,j}(V) + const, where e_{N,j} collects the terms
generated at distance j from the terminal scale, with:

- (T-a) size: sup |e_{N,j}| <= C L^{-4j} (CMP 119's (L^jη)^4 bound, read at
  the terminal scale);
- (T-b) memory: sup |e_{N+1,j} - e_{N,j}| <= C L^{-4j} θ^{K_N - j}, θ < 1.
  The two depths differ only through coupling histories, which agree up to
  θ^{K_N-j} at distance K_N - j from the finest scale (shooting from a
  common g with memory decay (D) of note 22), and through the extra finest
  step.

Then (2.1) holds on S with η_N <= C Σ_j L^{-4j} θ^{K_N-j} + C L^{-4(K_N+1)}
<= C' max(L^{-4}, θ)^{K_N}. Condition (2.1') concerns the large-field and
boundary terms R_K, B_K. CMP 122 II's two-sided bound (0.1) controls their
size, but their depth-differences are part of (T).

**(B) R-bias series.** For each N, B_N(G) = Σ_{m=0}^{K_N} b_{N,m}(G), where
b_{N,m} is the total contribution of R-replacements at distance m from the
terminal scale (the sequential telescope of note 11, at the R'-stage where
note 20 gives equal fiber mass). Assume, uniformly for |z| <= ρ:

- (B-a) summability: |b_{N,m}(G)| <= β_m with Σ_m β_m < ∞;
- (B-b) memory: |b_{N+1,m}(G) - b_{N,m}(G)| <= C β_m θ^{K_N - m}.

(B-a) is the R-bias obligation of notes 11-16. By notes 24-25 it reduces to
(P), component counting, and generalized averaged H8 (exterior-averaged
first-order shifts). Note 19 verifies the averaged mechanism in the Gaussian
model. (B-b) is the same memory decay as (T-b), applied to R-contributions.

## 3. Theorem

**Theorem 1.** Assume (H0), (T) and (B). Then

    Σ_N sup_{|z|<=ρ} |ν_{N+1}(e^{z·F}) - ν_N(e^{z·F})| < ∞,

so, by research/03 Theorems A and C and research/07 Prop. 2, the normalized
terminal generating functions converge uniformly on the polydisc, and every
fixed joint cumulant converges.

*Proof.* Write ν_{N+1}(G) - ν_N(G) = [ν^R_{N+1}(G) - ν^R_N(G)] +
[B_{N+1}(G) - B_N(G)].

1. *First bracket.* |ν^R_{N+1}(G) - ν^R_N(G)| <= ||G||_∞ ||ν^R_{N+1} - ν^R_N||_TV
   <= e^{S_ρ} η_N, which is summable by (T).
2. *Second bracket.*

       |B_{N+1}(G) - B_N(G)| <= Σ_{m<=K_N} |b_{N+1,m} - b_{N,m}| + |b_{N+1,K_N+1}|
                              <= C Σ_{m<=K_N} β_m θ^{K_N-m} + β_{K_N+1}.

3. *Summation.* Summing over N (K_N = N) and exchanging the order,
   Σ_N Σ_{m<=N} β_m θ^{N-m} = Σ_m β_m Σ_{N>=m} θ^{N-m} <= Σ_m β_m/(1-θ),
   which is finite, and Σ_N β_{N+1} < ∞. ∎

## 4. The resulting 4D map

    M1-4D convergence  <=  (H0) + (T) + (B)
      (H0) <= (C) + (S) + (D)                        [note 22]
      (T)  <= (T-a) [published size] + (T-b) memory decay  [open]
      (B)  <= (P) + counting + generalized averaged H8   [notes 24, 25; Gaussian check note 19]
              + (B-b) memory decay                   [open]
      plus P6-4D for nondegeneracy                   [open]

H4D-3 (note 21) is not used by Theorem 1. It remains the tool for comparing
measures at slightly different couplings, for example to absorb a residual
mismatch if exact shooting is replaced by approximate shooting.

The memory-decay hypotheses (D), (T-b) and (B-b) all have the same form: the
dependence of a step's contribution on couplings and histories at distant
scales decays geometrically. Proving them is one task: extend Balaban's
analytic inductive bounds by tracking the dependence on the earlier coupling
history, with geometric decay. That task, generalized averaged H8, the
persistence bound (P), and the classical one-loop sum rule (S) are what
remains between the published Balaban programme and M1-4D.
