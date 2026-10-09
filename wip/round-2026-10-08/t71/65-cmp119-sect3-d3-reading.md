# CMP 119 Sect. 3 at d = 3 with R = identity, read from the page images (T71)

Status:

- **Published input, read from the page images (not the OCR), equation by
  equation.** Table 1 (§2) lists every numbered estimate of Sect. 3 (printed
  pp. 264-284) with its status at d = 3 and R = identity. Result: the
  (k+1)-st-step form preservation for the regular terms E, R, B goes through
  at d = 3 with R = identity after **four changes** (§3): the 4D coupling
  inequalities (2.6)-(2.9) are replaced (single step only, factor L^{1/2});
  there is no coupling counterterm; the L-exponents improve from 5 - 4 to
  5 - 3; two lines of 4D geometric wording are dimension-specific. No
  obstruction was found *inside* Sect. 3. The estimates imported from
  CMP 109 [I], CMP 98 [12], CMP 99 [13, 14], CMP 102 [15, 16] were not
  rechecked.
- **Not in Sect. 3 (failed-attempt for the requested form).** CMP 119 Sect. 3
  contains **no bound on the large-field operations T_k**. The conditional
  integral over the large-field part Ω_{k+1} ∩ Λ_{k+1}^c is left as the
  operation T^{(k+1)} ((3.23), p. 270) and is never expanded or estimated.
  So the bound |activity(X)| <= C ε_j^q e^{-κ d(X)} is **not** a CMP 119
  statement. What Sect. 3 and Sect. 2 give for polymers meeting a large-field
  region is B_0 e^{-κ d_j(X)} with B_0 = O(p_0³(g_k)), with no small
  prefactor ((2.42), (3.47); p. 262 gives the variant with d_j(X \ Z_j)). The small prefactor comes from the
  weight of T_k, which CMP 122 II bounds ((1.85), (1.97); T72).
- **Proved here (elementary).** Lemma 65.2 (sum over creation scales is
  dominated by the current scale; this is why no R-operation is needed at
  d = 3, and why it is needed at d = 4) and Lemma 65.3 (a persisting
  large-field domain stays within O(M R_j) of its seed).
- **Conditional reduction.** §5: with two inputs (W) and (E), both
  published but outside Sect. 3, the bound
  |activity(X)| <= C_q g_j^q e^{-κ d_j(X)} follows for every q. It is not
  proved here that (W) and (E) hold without loss when R = identity; that is
  CMP 122 II (1.83)-(1.85), (1.89) (T72).
- **Corrections to notes 61 §6a and 49 §5 (the "fix" part, §6).** (i) T62's
  claim that (2.6)-(2.9) "hold in 3D, with room" and that no reverse
  inequality occurs is wrong: four of the eight inequalities fail on the exact
  3D flow (two for every n - m, two beyond a window). (ii) The d = 3 coupling statement is CMP 109 **p. 259**, not
  p. 255. (iii) The sentence "the analysis presented in [16] for
  three-dimensional models is enough here" (p. 276) is about the R_k terms
  only. (iv) CMP 119 (1.1), p. 246, states p_0 >= 5r; this settles the
  "actual choice was not located" remark of note 49.

Script: `research/scripts/t71_cmp119_sect3_d3_checks.py`, output
`research/scripts/t71_cmp119_sect3_d3_checks.out`. Every number below is
printed there (scalar flow only; no linear algebra is involved). Balaban's
constants (A_0, A_1, B_3, M, δ, κ) are not specified in the paper, so the
script tests only the d-dependent inequalities, not his constants.

**One-line verdict.** Sect. 3 at d = 3 with R = identity survives (four
changes, no obstruction found in Sect. 3 itself), but it does not contain the
large-field activity bound; (H4a) still rests on CMP 122 II (1.79)-(1.99).

## 0. Sources, notation, OCR

- PDF `sources/papers/Balaban1988-CMP119-convergent-expansions.pdf`;
  printed page = PDF page + 242 (PDF p. 22 = printed p. 264, Sect. 3 starts
  there; the paper ends on printed p. 285, PDF p. 44 is blank).
- Reference numbers inside CMP 119 are those of CMP 109's list: [I] = CMP 109,
  [II] = CMP 116, [6] = (Higgs)_{2,3} II, CMP 86, 555-594 (not in `sources/`),
  [12] = CMP 98, [13] = CMP 99 (propagators), [14] = CMP 99 (regular
  configurations), [15] = CMP 102 (variational problem), [16] = CMP 102
  (UV stability, 3D).
- Balaban's indexing: step j acts on T^{(j)} (spacing L^j in bare units);
  T_η with η = L^{-k} is the bare lattice measured in units of the current
  (k-th) lattice. The 3D couplings are exactly
  g_k² = g² L^k ε (CMP 109 p. 259, d = 3 sentence), so g_K = g on the unit
  lattice K = log_L(1/ε) and g_j² = g² L^{j-K}. Put
  λ_j = log g_j^{-2} = λ_K + (K-j) ln L, ℓ = ln L.
- **Notation clash.** In note 61 §6, ε_j means the small bare-spacing
  parameter (note 61 scale k corresponds to Balaban's j = K - k, with
  g_k² = g² ε_k there). Balaban's ε_j of (2.4) is the large-field threshold
  ε_j = g_j p_0(g_j), p_0(g) = A_0 (log g^{-2})^{p_0}. Below, ε_j always means
  Balaban's (2.4). In terms of note 61's parameter, g_j² = g² ε_k, so
  "any power of ε_k" and "any power of g_j" are the same statement.
- Constants: δ_k = (A_1/A_0) ε_k ((3.3), reconstructed from (3.9) and (1.8));
  R_j = smallest power of L with R_j >= λ_j^r ((2.5)); M, M_2 are the cube
  parameters of p. 245; p_0 >= 5r by (1.1), p. 246; d in constants such as
  30d²L²B_3, (4dL)², 44d², 11d², dM(n-j+2) is the lattice dimension; d(g) in
  (1.15), (3.15) is dim of the Lie algebra.
- OCR reconstructions are listed in Appendix A.

## 1. What Sect. 3 is

Sect. 3 constructs T ρ_k from ρ_k and proves that the result again has the
form (2.18)-(2.23). In order:

1. Geometry and regularity: new decompositions of unity, nesting of
   small-field characteristic functions (3.1)-(3.22).
2. The fluctuation integral and its structure (3.23)-(3.25).
3. The s,t-interpolation splitting log of the fluctuation integral into
   boundary, R and regular parts (3.26)-(3.38).
4. Localized expansions: E_0^{(k+1)} (3.39)-(3.43), exponentiated cluster
   expansion of the expectation values (3.44)-(3.47).
5. Renormalization (vacuum energy and coupling counterterm), p. 279.
6. Proof of Theorem 2, i.e. the bounds (2.43)-(2.44) on E and R, by Ward
   identities (3.48)-(3.67) and by gauge invariance (3.68)-(3.72).

What it does not do: bound T_k (see §4).

## 2. Table 1: Sect. 3, equation by equation

Codes. `=` unchanged at d = 3 (d-independent). `c` only constants change.
`x` the 4D form does not hold on the 3D flow and is replaced (§3.1).
`0` the term is absent when R = identity. `+` better exponent at d = 3.
`i` the step is an estimate imported from [I], [12]-[16], not rechecked here.
Printed page in the first column.

| p. | eq. | content (transcribed from the image) | d = 3, R = id |
|---|---|---|---|
| 264 | (3.1) | (Tρ_k)(V_{k+1}) = Σ ∫dV_k δ(V̄_k V_{k+1}^{-1}) χ_k T_k exp A_k. χ_k forces \|V_{k+1}(∂p') - 1\| < 2L² ε_k on Γ_k^{(1)}. Z_k = Λ_k^c, Z_k' = union of LMR_{k+1}-cubes meeting Z_k | `=` |
| 265 | (3.2) | on (Z_k'^{~4})^c: χ(sup_{p ⊂ □'~} \|U_{k+1,□'}(∂p) - 1\| < ε_{k+1}(L^{-1}η)²) and complement; P_{k+1} unions of L²M_2R_{k+1}-cubes | `=`; the only definition using ε_{k+1} |
| 265 | (3.3)-(3.5) | χ(sup_b \|V_k(b)(V^{(k)}_{□'}(b))^{-1} - 1\| < 2δ_k) on (B^{k+1}(P^1_{k+1}))^{~-1}; V^{(k)}_{□'} = M^k(U_{k+1,□'}); Ω_{k+1} = (Q'^{~2}_{k+1} ∪ (B^{k+1}(P^1_{k+1})^c)^{~3})^c | `=` |
| 266 | (3.6) | U_{k,□} = (exp iηH_{k,□}((1/i) log[M•(Q_k^{s*}V_k)(M•(U_{k+1,□'}))^{-1}]) U_{k+1,□'})^{u^{-1}_{k,□}} | `i`: exponential decay (190) [15] |
| 266 | (3.7) | \|H_{k,□}\| <= B_3(4δ_k + e^{-2δ M_2 R_k} · 30d²L²B_3(1+β_0) ε_k) < (4B_3 A_1/A_0 + 30d²L²B_3²(1+β_0) e^{-R_k}) ε_k < ε_k/10 | `c`: (1+β_0) -> L^{1/2}(1+β_0) if it encodes ε_{k+1}/ε_k; multiplies e^{-R_k}, harmless |
| 266 | (3.8) | \|U_{k,□}(∂p) - 1\| < (1 + (2/10)ε_kη) ε_{k+1}(L^{-1}η)² + (2/10) ε_kη²(1 + (4/10)ε_k) < 2(1+β_0)L^{-2} ε_kη² + (4/10) ε_kη² < ε_kη², hence χ_k(□) = 1 on Ω~_{k+1} | `c`; the **only** estimate with no exponentially small factor; see §3.2 |
| 266 | (3.9) | \|V_k(y,x) - 1\| = O(1)δ_k = O(1)(A_1/A_0)ε_k < ε_k on (Ω~_{k+1})^{(k+1)}; so χ_{Ax} = 1 | `=` |
| 266-267 | (3.10)-(3.11) | V^{(k)} = M^k(U_{k+1}) minimizes V_k -> A(U_k) with V̄_k = V_{k+1} on Γ_{k+1}; V_k' = V_k (V^{(k)})^{-1} | `=` |
| 267 | (3.12) | \|U_{k+1}(∂p) - 1\| < 2B_3L²(1+β_0) ε_k (L^{-1}η)² on □'~ (Thm 1 [16]) | `c`, `i` |
| 267 | (3.13)-(3.14) | \|V^{(k)} - V^{(k)}_{□'}\| < (4dL)²(1+β_0) B_3 ε_k (Lemma 1 [14]); \|V_k' - 1\| < 2δ_k + (4dL)²(1+β_0)B_3 ε_k = O(1)ε_k | `c`: d = 3 in (4dL)²; O(1) |
| 267-268 | (3.15) | fluctuation integral: T exp[A_k(1/g_k², U_{k+1}) + log g_k d(g)\|B(Γ_{k+1})*\| + log σ_0 \|B(Γ_{k+1})*\| - log z (L^4 - 1)\|Γ_{k+1}\|] z^{(k)} ∫dA_k χ_k' exp[-½⟨A_k, C*Δ^{(k)}CA_k⟩ + P^{(k)} + {(E_k+R_k+B_k)(U_k(exp i[g_kCA_k - hD~(g_kCA_k)]V^{(k)})) - (E_k+R_k+B_k)(U_{k+1}) + A(1/g_k²(·) - 1/g_k², U_k(...)) - A(1/g_k²(·) - 1/g_k², U_{k+1})}] | `c`: L^4 - 1 -> L^d - 1 = L³ - 1; `0`: R_k; `0`: the two A(1/g_k²(·) - 1/g_k²) terms (§3.3) |
| 268 | (3.16) | decomposition on Ω~^{-1}_{k+1}: χ(sup_b \|A_k(b)\| < δ_k) and complement; R_{k+1} unions of L²M_2R_{k+1}-cubes | `=` |
| 268 | (3.17) | U_{k+1} = (exp iL^{-1}ηH_{k+1,□'}(...) U_{k+1,□'})^{u^{-1}}; argument of H_{k+1,□'} \< 44d²B_3 ε_{k+1}; H_{k+1,□'} <= B_3 e^{-δLM_2R_{k+1}} 44d²B_3 ε_{k+1} <= 44d²B_3²(1+β_0) e^{-R_k} ε_k on □'~2 | `c`: uses ε_{k+1} <= (1+β_0)ε_k and R_{k+1} >= R_k/L; 3D: L^{1/2}(1+β_0) and §3.2 |
| 268 | (3.18) | V^{(k)}(b) = u^{-1}_{k+1,□'}(b_-) exp iQ_k(L^{-1}ηH_{k+1,□'}) R̄^k u_{k+1,□'}(b_+) V^{(k)}_{□'}(b) | `=`, `i` ((106)-(108), (159)-(163) [12]) |
| 268 | (3.19) | \|V^{(k)}(V^{(k)}_{□'})^{-1} - 1\| < O(1)44d²B_3²(1+β_0) ε_k e^{-R_k} = O(1)44d²B_3²(1+β_0)(A_0/A_1) e^{-R_k} δ_k < δ_k | `c`; needs e^{-R_k} (A_0/A_1) small: R_k >= λ_K^r with λ_K = log g^{-2} large |
| 269 | (3.20) | Λ_{k+1} = ((Ω_{k+1}^c)~2 ∪ R'_{k+1})^c = Ω~^{-2}_{k+1} ∩ (R'~_{k+1})^c; S_{k+1} = (Ω_{k+1} \ Ω~^{-1}_{k+1}) ∪ R_{k+1}; components of Λ^c in cubes of size 100LMR_{k+1} replaced by boxes | `=` |
| 269 | (3.21) | χ(Ω_{k+1} ∩ Λ^c_{k+1}, S_{k+1}) = χ^{(k)}(R^c_{k+1} ∩ Λ^c_{k+1}) χ^{(k)c}(R_{k+1}) χ_k'(S_{k+1}) | `=` |
| 269 | (3.22) | V^{(k)} (V^{(k)}_{Λ^c_{k+1} ∩ Λ_k})^{-1} = exp iH^{(k)}; H^{(k)} analytic in U_{k+1}, bounded on S_{k+1} by O(1) ε_k e^{-R_k} ("any positive power of g_k") | `c`, `i` |
| 270 | (3.23)-(3.25) | T^{(k+1)} = Σ_{S_{k+1}} ∫dV_k δ ζ z^{(k)} ∫dA_k χ exp[-½⟨A,C*Δ^{(k)}CA⟩ + ½⟨A_k, C*Δ^{(k)}CC^{(k)}(Λ_{k+1})C*Δ^{(k)}CA_k⟩]; T_{k+1} = T^{(k+1)}T_k; full density (3.25) | `=`; **T^{(k+1)} is not expanded** |
| 270-271 | text | R_k' = Σ_{j<=k_1} R^{(j)} absorbed in E_k, R_k'' = Σ_{j>k_1} R^{(j)} kept separately, k_1 largest with L^{-(k-k_1)} M R_j <= L | `0` |
| 271 | (3.26) | log[z^{(k)} ∫dA χ^{(k)} exp(-½⟨A, C*Δ^{(k)}CA⟩ - ...)] = ∫_0^1 dt ⟨B_k(U_k) - B_k(U_{k+1}) + A(1/g_k²(·) - 1/g_k², ...) + V^{(k)}(S_{k+1})⟩_{s=1,t} + ∫_0^1 ds ⟨R_k''(U_k) - R_k''(U_{k+1})⟩_{s,t=0} + log[... (s=0,t=0)] | `=`; second term `0` |
| 271 | (3.27) | measure Z_{s,t}^{-1} dμ_{C^{(k)}(Λ_{k+1})}(A) χ_k exp[-⟨A, C*Δ^{(k)}CA_k⟩ + P^{(k)} + {...}_{s,t} + tV^{(k)}(S_k)] | `=` |
| 272 | (3.28)-(3.30) | expansion in tA_k, (3.29) measure with t, (3.30) log = log[z^{(k)} ∫dA exp(-½⟨A,C*Δ^{(k)}CA⟩)] + log ∫dμ χ^{(k)} + g_k ∫_0^1 dt ⟨∂_{tg_k} P^{(k)} + ∂_{tg_k} E_k(U_k(... tg_kCA ...))⟩_t | `=` |
| 273 | (3.31)-(3.33) | ⟨V_k'(tg_k, A), CA⟩ = Σ_b tr V_k'(tg_k,A,b)(CA)(b); log ∫dμ χ^{(k)} = ∫_0^1 dt ∫dμ ∂_tχ_t^{(k)} (∫dμ χ_t^{(k)})^{-1}; log z^{(k)} - ½ log det(C*Δ^{(k)}C) + log ∫dA e^{-\|A\|²/2} | `=` |
| 273-274 | (3.34)-(3.36) | -½ log det via contour γ and resolvent (3.35); (3.36): -½ log λ_0 \|Λ^{(k)*}_{k+1}\| + ½ ∫_0^∞ dλ (λ_0+λ)^{-1} Tr(C*Δ^{(k)}C - λ_0 I)(C*Δ^{(k)}C + λ I)^{-1} | `=` |
| 274 | (3.37)-(3.39) | E_0^{(k+1)}(Λ_{k+1}, U_{k+1}, b) = χ_{Λ*}(b)[-½ log λ_0 + ½ ∫dλ (λ_0+λ)^{-1} tr(...)(b,b) + ∫_0^1 dt ∫dμ ∏_{b'≠b} χ^{(k)}(tA(b')) ∂_tχ^{(k)}(tA(b)) (∫dμ χ_t^{(k)})^{-1}] + g_k ∫_0^1 dt ⟨tr V_k'(tg_k,A,b)(CA)(b)⟩_t; Euclidean covariance (3.39) | `=` |
| 275 | (3.40)-(3.42) | h_z(x) = ∏_{μ=1}^d h(x_μ - z_μ), h(t) = max{1 - L^{-1}\|t\|, 0}; E_0^{(k+1)}(z) = Σ_{μ=1}^d [½(log z^{(k)}(⟨z - Le_μ, z⟩) + log z^{(k)}(⟨z, z + Le_μ⟩)) + Σ_x h_z(x) E_0^{(k+1)}(⟨x, x+e_μ⟩)] | `c`: d = 3 coordinates and bond directions |
| 275-276 | text | cover by cubes of size 2ML^jη in layers Ω_j \ Ω_{j+1}; Sects. 3-6 [I] repeated "with η replaced by L^{-n}"; generalized random-walk expansions Thms 3.7-3.10 [13] | `i` |
| 276 | (3.43) | analyticity space Ũ^c_{k+1}(Y, (1+β)α~_0, (1+β)α~_1) × {A: supp A ⊂ Y ∩ Λ^{(k)*}_{k+1}, \|A\| < C_1 p_1(g_k)} | `=` |
| 276 | text | R_k "treated in exactly the same way as E_k, except the second renormalization connected with the coupling constant renormalization counterterm ... In fact the analysis presented in [16] for three-dimensional models is enough here" | about R_k only; `0` at R = id |
| 277 | text | analyticity domains shrink by the factors (2.36)-(2.39); terms estimated as in (2.42) "with the additional factor O(ε_k)"; g_k^{-2}(·) - g_k^{-2} supported in Z_k; V^{(k)}(S_{k+1}) | `c`; the g_k^{-2}(·) terms `0` |
| 277-278 | (3.44)-(3.46) | nominator = Σ H'(Z_0) ... H(Z_n); Z_i ⊂ Z~_0^c: cubes not meeting Z_0 or meeting it "along a two-dimensional edge at most"; difference of exponents has a domain meeting Z_0 "along a three-dimensional wall at least" | `x` (geometry): d = 3 reads one-dimensional edge, two-dimensional wall |
| 278 | (3.47) | [expectation in (3.37)] = Σ_{X ∈ D_{k+1}, X ∋ b} E_0^{(k+1)}(Λ_{k+1}, X, b); terms satisfy (2.42) with B_0 replaced by O(p_0³(g_k)) | `=` |
| 279 | text | regular part ends; renormalization: vacuum energy by subtracting at U_{k+1} = 1; coupling counterterm β_{k+1}(g_k) A(φ_{k+1}, U_{k+1}) and g_k^{-2}(·) -> g_{k+1}^{-2}(·) by (2.24) | `0` for the coupling part (§3.3) |
| 280 | (3.48) | \|E^{(j)}(X,z)\| <= E_0 e^{-κ(L^jL^{-n})^{-1}} e^{-½κ d_j(X)}; sum over X <= O(1)(L^jL^{-n})^5 | `=` |
| 280-281 | (3.49)-(3.51) | Σ_{n=1}^4 (1/n!)⟨E^{(n)}(X,z), ⊗B⟩ = Σ_{μνκλ} [Σ_{x,y} E^{(2)}_{μν}(X,x,y,z)(x_κ-z_κ)(y_λ-z_λ)] ½ tr(...)(...) + irrelevant; antisymmetry (3.51) from the first Ward identity (I.4.15) | `=` |
| 281-282 | (3.52)-(3.61) | symmetric part vanishes (3.52)-(3.54); (3.55)-(3.56) antisymmetrization, sum over κ<μ, λ<ν; (3.57) Π^{(j)}_{μν,κλ}; (3.58)-(3.60) covariance; (3.61) = β_j' ½ Σ_{μ<ν} tr F_{μν}²(z), β_j' = Π^{(j)}_{22,11} | `=`: the reflection/permutation argument works verbatim for the three pairs 12, 13, 23 (§3.5) |
| 282-283 | (3.62)-(3.64) | β_j' = ½ (∂²/∂p_1²) Π_{22}^{(j)}(0) = β_j, the definition (I.1.22) | `=` |
| 283 | (3.65)-(3.67) | A(φ_j, U_k) = Σ_z A(h_zφ_j, U_k); A(h_z,U_k) = ½ Σ_{μ<ν} tr F_{μν}²(z) + irrelevant; E^{(j)}(Λ_j,U_k,z) - E^{(j)}(Λ_j,1,z) - β_jA(h_z,U_k) = O((L^jL^{-n})^{5-β}) | `+`: summed exponent 5 - d - β: 1 - β at d = 4, 2 - β at d = 3 (§3.4) |
| 283 | text | R: (3.49) with E^{(2)} -> R^{(2)}, bound O(1)(L^jL^{-n})^4 g_j^{κ_0} e^{-κ d_j(X)}, giving (2.44) | `0` (and `+` if kept: 4 - d = 1 per unit volume) |
| 283-284 | (3.68) | \|V' - 1\| < 11d²ε_n(L^jL^{-n})² + dM(n-j+2)ε_n(L^jL^{-n})² < 3dM(1 + log L^jL^{-n}) ε_n (L^jL^{-n})² | `c`: d = 3 |
| 284 | (3.69)-(3.72) | second proof by gauge invariance: E(X,U_k,z) - E(X,1,z) = ½⟨δ²E/δB'², B', B'⟩ + O(1)(L^jL^{-n})^{6-β} e^{-κ d_j(X)}; (3.70) with error O(1)(L^jL^{-n})^5; (3.71) B'(b) = (1/i) log Ū^j_k(Γ_{z,b_-} ∪ b ∪ Γ_{b_+,z}); (3.72) BCH remainder O(1)(L^jL^{-n})^3 | `=` (exponents 5, 6, 3 come from Taylor order, not from d) |

Two misprints in the printed text, noted for the record: p. 271 "On the
right-hand side of (3.6) we have the sum of three expressions" refers to
(3.26), whose number is missing from the display on p. 271; p. 266 "This
estimate and the equalities (3.7), (1.43) [14]" should read (3.6), (1.43).

## 3. The d-dependent inputs, in detail

### 3.1 Coupling inequalities (2.6)-(2.9): corrects T62

The text of CMP 119 p. 255-256 (transcribed from the image), for n > m:

    (2.6)  g_n <= (1 + g_n² β'(n-m))^{1/2} g_m <= (1+β_0)(n-m)^{1/2} g_m,
           g_m <= (1+β_0) g_n;
    (2.7)  (log g_n^{-2})^p <= (1+β_0)(log g_m^{-2})^p,
           (log g_m^{-2})^p <= (1+β_0)(n-m)^{β_0}(log g_n^{-2})^p;
    (2.8)  ε_n <= (1+β_0)(n-m)^{1/2} ε_m,
           ε_m <= (1+β_0)²(n-m)^{β_0} ε_n;
    (2.9)  R_n <= L R_m,   R_m <= (L+1)(n-m)^{β_0} R_n.

Balaban derives them from the 4D RG equation (0.20) [I] and the properties
of the β-functions (p. 256); the
hypothesis of Theorem 1 (p. 262) is the two-sided logarithmic bound on 1/g_k²
that CMP 119 cites as (I.0.33) and that is printed as (0.31) in the copy of
CMP 109 here (the same inequality: 1/g² + β log(L^kε)^{-1} <= 1/g_k² <=
1/g² + β' log(L^kε)^{-1}, valid for d = 4 only, CMP 109 Thm 2, p. 259).

At d = 3 the flow is g_k² = g² L^k ε exactly (CMP 109 p. 259). Then
g_n = L^{(n-m)/2} g_m and λ_m = λ_n + (n-m)ℓ. Part A of the script
evaluates the eight inequalities on this flow (L = 2, β_0 = 0.1, p = 2,
p_0 = 10, r = 2, λ_K = 400, K = 60, all 1830 pairs m < n):

- (2.6) first line: **violated** for 1830 of 1830 pairs, already at n - m = 1
  (g_{k+1}/g_k = L^{1/2} = 1.4142 > 1 + β_0). Any β_0 < L^{1/2} - 1 fails.
- (2.8) first line: **violated** for 1830 of 1830 pairs; the single-step ratio
  ε_{k+1}/ε_k lies in [1.3899, 1.3922] (below L^{1/2} = 1.4142 by the factor
  (λ_{k+1}/λ_k)^{p_0}).
- (2.7) second line and (2.9) second line: hold on this window but **fail
  for long chains**. For (m, n) = (0, K) with p = 2, β_0 = 0.1, λ_K = 400
  the first failing K is 215 (K = 10 for p = 20; K = 3306 for λ_K = 4000).
  For (2.9) second line (r = 2, λ_K = 400) the first failing K is 901
  (6048 for λ_K = 4000). The cause is polynomial growth,
  (λ_m/λ_n)^p ~ ((n-m) ℓ/λ_n)^p, against (n-m)^{β_0}.
- (2.6) second line, (2.7) first line, (2.8) second line, (2.9) first line
  hold, with room: g_m = L^{-(n-m)/2} g_n; (2.7a) since λ_n < λ_m; (2.8b)
  holds in the strong form ε_m <= ε_n when λ_n >= 2p_0 (1 + x <= e^x:
  ε_m/ε_n <= exp(-sℓ(½ - p_0/λ_n))); (2.9a) since R_n <= R_m.

So T62's statement that these inequalities "hold in 3D, with room" and that
"no inequality in the reverse direction ... was found" is incorrect: (2.6)
first line and (2.8) first line are exactly the reverse direction (coarser
bounded by finer) and are false; the two second lines hold only on a window
n - m <= s_*(g).

**Where Sect. 3 uses them.** In the visible text only with n - m = 1: the
factors (1+β_0) in (3.7), (3.8), (3.12)-(3.14), (3.17), (3.19) and the
comparison R_{k+1} ~ R_k in (3.17). Sect. 2 uses the multi-step form once,
in (2.46), where at d = 3 it is replaced by the convergent series
Σ_{j<=n} g_j^{κ_0} = g_n^{κ_0} Σ_s L^{-sκ_0/2} <= 2 g_n^{κ_0} for κ_0 >= 2
(so κ_0 >= 7 is not needed). The provenance of each (1+β_0) is not stated in the text, so
this is a reading; the imported estimates of [I], [12]-[16] might use the
multi-step form.

**3D replacements (all printed by the script).**

    g_n = L^{(n-m)/2} g_m;        g_m <= L^{-(n-m)/2} g_n;
    ε_{k+1} <= L^{1/2} ε_k;       ε_m <= ε_n (if λ_n >= 2p_0);
    R_{k+1} >= R_k / L            if λ_k >= ℓ/(1 - L^{-1/r});
    R_m <= L^{n-m} R_n.

For the single step: R_k < L λ_k^r and R_{k+1} >= (λ_k - ℓ)^r. If
R_{k+1} <= R_k/L² then (λ_k - ℓ)^r < λ_k^r/L, i.e. λ_k (1 - L^{-1/r}) < ℓ. So
λ_k >= ℓ/(1 - L^{-1/r}) forces R_{k+1} > R_k/L², hence (powers of L)
R_{k+1} >= R_k/L. The threshold is 2.367 for (L, r) = (2, 2) and 3.360 for
(2, 3). Part C of the script checks both R-statements on the rounded R_j for
six parameter sets: no violation for λ_K >= 5; for λ_K = 1.0 (g² = 0.37,
not small) there is one single-step violation and three violations of the
chain statement. Since g is small, λ_j >= λ_K is large for all j.

### 3.2 Single-step constants

Only (3.8) has no exponentially small factor. As printed it needs
2(1+β_0)L^{-2} + 4/10 < 1. With β_0 = 1/10, L = 2 the left side is 19/20 (script
Part B). At d = 3, ε_{k+1} <= L^{1/2} ε_k replaces ε_{k+1} <= (1+β_0)ε_k, and
the condition becomes (1+β_0)L^{-3/2} + 2/5 < 1, equivalent to
(1+β_0)² < (9/25)L³; for β_0 = 1/10 this is 900 L³ > 3025, true for all
L >= 2 (L = 2: left side of the inequality 0.7889). The printed
constant 2(1+β_0) = 2.2 suffices for L <= 4 (L^{1/2}(1 + (2/10)ε_kη) <= 2.2);
for L >= 5 it must be read as L^{1/2}(1+β_0). So (3.8), hence χ_k(□) = 1 on Ω~_{k+1}, holds for
every L >= 2.

(3.7), (3.17), (3.19), (3.22) carry e^{-R_k} with R_k >= λ_K^r (the unit
lattice coupling g is small), so any constant, including L^{1/2}(1+β_0) and
d² = 9, is absorbed.

### 3.3 No coupling counterterm at d = 3

CMP 109 p. 259: for d = 3 "it is not necessary to consider the β-functions
and the renormalization group equations (0.18), (0.20). The effective coupling
constants are given by g_k² = g² L^k ε". Applying this to CMP 119 (reading by
analogy; CMP 119 does not restate it): (2.24) is replaced by
g_j² = L g_{j-1}², β_j ≡ 0, g_j²(x) ≡ g_j². Then the following objects are
absent: the counterterm -β_j(g_{j-1}) A(φ_j, U_k) in (2.25); the terms
A(1/g_k²(·) - 1/g_k², ...) in (3.15), (3.26), (3.28); the discussion on p. 277
of supp(g_k^{-2}(·) - g_k^{-2}) ⊂ Z_k; the last step on p. 279. The F² term
that would have been subtracted stays in E^{(j)} as an irrelevant term: seen
from scale n it is bounded by (L^{-(n-j)})^{4-d} = L^{-(n-j)}, summable (§3.4).

### 3.4 Exponents of L: (2.31), (2.43)-(2.46), (3.67)

For a point z of the j-lattice, (3.67) gives the remainder
O((L^jL^{-n})^{5-β}) (the 5 is 2 + 3 from Taylor order, independent of d).
A unit n-cell contains L^{(n-j)d} j-points, so the summed bound per n-point is
(L^{-(n-j)})^{5-d-β}. At d = 4 this is the (2.43) exponent 1 - β; at d = 3 it
is 2 - β. The F² term itself, O((L^{-(n-j)})^4) per point (3.57)-(3.66),
sums to (L^{-(n-j)})^{4-d}: exponent 0 at d = 4 (the sum over scales grows
like n; this is why β_j and the factors g_j^{κ_0} are needed) and exponent
1 at d = 3 (geometric). Script Part D: Σ_{s=0}^{60} L^{-(4-d)s} is 61 at
(d, L) = (4, 2), 2.0000 at (3, 2), 1.5000 at (3, 3). Therefore at d = 3 the
inequality (2.43) holds without the counterterm with exponent 1 (this
exponent is exactly the F² term of (3.61), (3.66), which is no longer
subtracted; with the counterterm the exponent would be 2 - β), and (2.44),
(2.31) hold a fortiori, with the extra factor L^{-(n-j)}; at R = identity
they are void.

### 3.5 Geometry and symmetry

- (3.44)-(3.46): "two-dimensional edge", "three-dimensional wall" are the
  codimension-2 and codimension-1 faces of a 4-cube. At d = 3 they read
  one-dimensional edge and two-dimensional wall. This only changes which
  pairs of cubes count as overlapping in the Mayer expansion of
  [I] Sect. 7; it must be redone there (not rechecked).
- (3.40)-(3.41), (3.49): sums over μ, ν, κ, λ run over 3 directions;
  L^4 - 1 in (3.15) is L^d - 1 = 7 non-central sites per block at
  (d, L) = (3, 2) (script Part D).
- (3.55)-(3.61): the pair-index matrix M_{(κμ),(λν)} = Π_{μν,κλ} (κ<μ, λ<ν)
  is 3 × 3 at d = 3. Reflection in the hyperplane x_a = 0 multiplies the
  entry (P, Q) by (-1)^{[a ∈ P] + [a ∈ Q]}. Two different pairs P ≠ Q differ
  in at least one axis a, so M_{PQ} = 0 for P ≠ Q. The coordinate
  permutations (S_3) act transitively on {12, 13, 23}, so the diagonal
  entries are equal, giving (3.61) with β_j' = Π_{22,11}.
- Constants with d: 30d²L²B_3, (4dL)², 44d², 11d², dM(n-j+2), 3dM: smaller at
  d = 3 (d² = 9 instead of 16, script Part D).

### 3.6 What disappears at R = identity

All terms R^{(j)}, R_k, R_k', R_k'', R^{(k+1)}, R''^{(k+1)}: (2.30)-(2.33),
(2.44), (2.46), the R-parts of (3.15), (3.25), (3.26) (second integral over s),
the splitting at k_1 (p. 270-271), the sentence on p. 276 about R_k, the
R''-terms on p. 279, and the second half of the proof of Thm 2 on p. 283.
With no R-operation the characteristic functions of Z_j are never changed and
Λ_j ⊊ Ω_j whenever Z_j ≠ ∅; large-field components persist to the unit
lattice and Z_{k+1} ⊃ Z_k'.

## 4. What Sect. 3 does not contain

### 4.1 The structure

At the start of Sect. 2 (p. 254) the operations T_k are "left undefined, only
their basic general properties are formulated. Their inductive definition
will follow successively from the constructions of the subsequent section and
forthcoming papers." In Sect. 3 they are defined by (3.23)-(3.24):
T_{k+1} = T^{(k+1)}T_k with T^{(k+1)} the integral over V_k on Ω^c_{k+1} and
over A_k on Ω_{k+1} ∩ Λ^c_{k+1} (p. 270: "The remaining integration with
respect to A_k restricted to Ω_{k+1} ∩ Λ^c_{k+1} is included into the
operation T^{(k+1)}"). Only the small-field part Λ_{k+1} is expanded ((3.30),
(3.44)-(3.47)). Everything estimated is a term of E, R or B:

| object | bound in Sect. 2-3 | small prefactor? |
|---|---|---|
| E^{(k+1)}(X, z), X ⊂ Λ_{k+1} | (2.42)-type, (3.47): B_0 e^{-κ d_{k+1}(X)}, B_0 = O(p_0³(g_k)); (3.48) | no |
| B^{(k+1)}(X, ...), X ∩ Z~_{k+1} ≠ ∅ | (2.42) and (3.47); the terms from H_k carry "the additional factor O(ε_k)" (p. 277); in the alternative resummed form of the inductive assumption (p. 262, not the one adopted) the exponent is e^{-κ d_j(X \ Z_j)} | only the O(ε_k) |
| R^{(k+1)} | (2.31): g_j^{κ_0} e^{-κ d_j(X)}; (2.44) | g_j^{κ_0}; absent at R = id |
| ρ_k itself | Corollary 3 (2.50): χ_k(T_η) exp[-(1/g_k²)A(U_k(V_k)) - E_-\|T_η\|] <= ρ_k(V_k) <= e^{E_+\|T_η\|}; proof by (2.49) and "the same combinatorics as in [6]" (CMP 86, a 2-3 dimensional paper) | the Wilson factor, not localized |
| T_k | **nothing** | — |

Further: the terms with ∂_tχ^{(k)} in (3.37) are Gaussian tail probabilities
of the fluctuation field, of size exp(-c A_1² (log g_k^{-2})^{2p_0})
= exp(-c (A_1/A_0)² p_0(g_k)²) (inferred from (3.16), (3.32); Sect. 3 does not write
this bound). They enter E_0^{(k+1)}, which Sect. 3 bounds only by B_0 e^{-κd}.

### 4.2 Consequence for the requested bound

The statement |activity(X)| <= C ε_j^q e^{-κ d(X)} for large-field polymers
is therefore **not derivable from CMP 119 Sect. 3**. The exact step where the
attempt stops: the large-field weight sits in T_k, which is not expanded in
Sect. 3, so no polymer activity containing it exists in CMP 119. The
corresponding expansion is CMP 122 II after (1.89): the exponentiated cluster
expansion with activity bound (1.97), c_1 e^{-(1+β)κ d_k(X')}, c_1 =
exp(-p_0(g_k)) for X' meeting no large-field region and c_1 = α_1^{1/3}
otherwise (quoted from note 49 §6; T72 checks it at d = 3). Also: the
inductive assumption of CMP 119 contains no *quantitative* assumption on T_k,
so Sect. 3 cannot show where an R-operation is needed at d = 4 or that it is
not needed at d = 3. The claim "R = identity works for d < 4" is, in CMP 119,
only the heuristic of the introduction (pp. 244-245), made precise by the
weight-versus-entropy comparison of CMP 122 II (1.80)-(1.85).

## 5. Conditional reduction: the bound in the requested form

Inputs, all published but outside Sect. 3. Index conventions of §0.

- **(W) seed weight.** A large-field seed (a plaquette with
  |U(∂p) - 1| >= ε_i η² at scale i, or a fluctuation with
  sup|A_i| >= δ_i) carries a factor <= exp(-c p_0(g_i)²), c > 0: CMP 119
  p. 244 (Wilson factor exp(-(1/g_i²)(1 - Re tr U)) <= exp(-½ p_0²)), (3.16)
  and (3.32) for the Gaussian tail, (2.49) "the first term yields the small
  factors for large field characteristic functions". That it persists
  without loss through the unprocessed steps i+1, ..., j is CMP 122 II
  (1.83)-(1.85), (1.89) (not checked here).
- **(E) per-point loss.** Each point of Γ_t costs at most e^{O(1)} (CMP 119
  (2.49): "+ O(1) Σ|Γ_j|"; Cor. 3 (2.50)).
- **(D) domain growth.** Z_{k+1} ⊂ (Z_k')^{~m_0} ∪ (new seeds), m_0 a fixed
  number of layers of LMR_{k+1}-cubes (read off (3.2), (3.5), (3.20); the
  value does not matter).

**Lemma 65.2 (creation scales).** Let d >= 1, L >= 2, ℓ = ln L, q > 1, c > 0,
λ >= 0. Then

    Σ_{s>=0} L^{ds} exp(-c(λ + sℓ)^q) <= C_0 exp(-c λ^q),
    C_0 = Σ_{s>=0} exp(s d ℓ - c(sℓ)^q) < ∞.

*Proof.* For a, b >= 0 and q >= 1, (a+b)^q >= a^q + b^q: write
a^q + b^q = (a+b)^q [(a/(a+b))^q + (b/(a+b))^q] and use (·)^q <= (·) on
[0,1]. Apply with a = λ, b = sℓ termwise. C_0 is finite since q > 1. ∎

Script Part E: C_0 = 8.99476 for (d, L, c, q) = (3, 2, 1, 20), 143.118 for
(3, 2, 0.1, 4), and the direct check of the lemma at λ = 1, 2, 3, 5.

*Meaning.* A seed at creation scale i = j - s has, at d = 3, weight
exp(-c p_0(g_i)²) = exp(-c A_0² λ_i^{2p_0}) with λ_i = λ_j + sℓ (exact 3D
flow), while the number of scale-i cubes in a scale-j cube is L^{ds}. By the
lemma (q = 2p_0, c -> c A_0²) the sum over creation scales is dominated by
the current scale: the persistence cost of an unprocessed domain is a
constant factor C_0. At d = 4, (2.7) second line gives
λ_i <= ((1+β_0) s^{β_0})^{1/p} λ_j, so the weight decays at most like
exp(-c' s^θ) with θ = 2p_0 β_0/p < 1 (β_0 small) while L^{ds} = e^{dℓ s}
grows exponentially: the sum diverges, and the R-operation is needed. This is the mechanism behind note 49's
a_eff, and the 3D reason that R = identity suffices. (The lemma is
elementary; what it needs from Balaban is (W).)

**Lemma 65.3 (persistence is local).** A domain created at scale i and
carried unprocessed to scale j (without merging with other seeds) lies
within distance m_0 L M R_j D_j (in j-lattice units) of its seed, where
D_j = Σ_{u>=0} (R_{j-u}/R_j) L^{-u} <= L/(1 - L^{-(1 - r/λ_j)}) for λ_j > r.

*Proof.* At step t the domain gains <= m_0 layers of thickness LMR_t
(t-lattice units) = m_0 L M R_t L^{t-j} (j-units). Sum over t <= j gives
m_0 L M R_j D_j. For D_j: R_{j-u} < L λ_{j-u}^r (smallest power) and
R_j >= λ_j^r, so R_{j-u}/R_j < L(1 + uℓ/λ_j)^r <= L · L^{ru/λ_j}; sum the
geometric series. ∎

Script Part C: max_j D_j = 2.0000 (L = 2, r = 2, λ_K = 400), 3.1331
(λ_K = 5), against the analytic bound 4.0139, 5.8781.

**Proposition 65.4 (conditional reduction).** Assume (W), (E), (D), and
the 3D inductive assumption at all scales <= j. The weight of a seed
created at scale i = j - s that is still alive at scale j and whose domain
contains a given point x of the j-lattice is at most

    C(MR_{j}D_j)^d L^{ds} exp(-c p_0(g_i)² + E_2 Σ_{t=i}^{j} (C ρ_t)^d),
    ρ_t = m_0 L M R_t D_t,

where ρ_t = O(R_t) = O(λ_t^r) and λ_t = λ_j + (j-t)ℓ. Since
Σ_t (Cρ_t)^d is bounded by a polynomial of degree rd + 1 in λ_j + sℓ, and
2p_0 >= 10r > rd + 1 by p_0 >= 5r ((1.1), p. 246) (also
rd + 1 <= (d+1)r; script Part F), the exponent is
<= -(c/2) A_0² (λ_j + sℓ)^{2p_0} once λ_j (that is, g small) is large. Lemma
65.2 then gives

    P(x lies in a large-field domain at scale j) <= C'(λ_j) exp(-(c/2) p_0(g_j)²)
                                                  <= C_q g_j^q   for every q,

with C'(λ_j) polynomial in λ_j and C_q depending on q, A_0, p_0, r, L, M. The
last step: exp(-(c/2)A_0²λ^{2p_0}) <= (g p_0(g))^q once λ is
large; script Part F gives, for A_0 = 1, p_0 = 10, the thresholds
λ >= 1.34, 1.47, 1.95, 2.53 for q = 5, 10, 100, 1000 (for exp(-p_0(g)) <=
(g p_0(g))^q, a weaker statement).

*Resulting bound, in the requested form* (status: **conditional
reduction**, inputs (W), (E), (D)). For a localization domain X of the final
expansion at scale j that contains a large-field component Z:

    |activity(X)| <= C_q g_j^q e^{-κ d_j(X)}      for every q,

obtained as the product of: the localized factor B_0 e^{-κ d_j(X \ Z)},
B_0 = O(p_0³(g_j)) ((2.42), (3.47); the d_j(X \ Z) form is the variant of
p. 262); the seed weight of Prop. 65.4,
which absorbs both the polynomial prefactor p_0³ and the lost part
e^{-κ d_j(Z)} of the exponent, since the weight per unit of Z is
exp(-c p_0(g_i)²) with p_0² >> κ. In Balaban's threshold notation,
g_j^q <= C (ε_j)^q (ε_j = g_j p_0(g_j) >= g_j). In note 61's parameter,
g_j^q = (g² ε_k)^{q/2}. What is **not** established here:

- that (W) survives the unprocessed steps without further loss when R is the
  identity: CMP 122 II (1.83)-(1.85), (1.89) (T72);
- merging of domains from different seeds (a chain of m seeds multiplies m
  weights; the standard polymer treatment is note 49 Lemma 1, applied
  to the exact expansion);
- the polymer decay e^{-κ d_j(X)} itself for the *final* exponentiated
  expansion: CMP 122 II (1.92)-(1.99).

## 6. Corrections to notes 61 and 49 (for the lead to apply)

1. Note 61 §6a, item 2, bullet (2.6)-(2.9). Replace by: "(2.6)-(2.9) encode the
   4D slowly-running coupling. On the exact 3D flow g_k² = g² L^k ε four of the
   eight inequalities fail ((2.6) and (2.8) first lines for every n - m >= 1;
   (2.7) and (2.9) second lines for n - m beyond a window ~ λ/ℓ; note 65 §3.1,
   Part A). Sect. 3 uses them with n - m = 1 only, with L^{1/2} in place of
   (1+β_0), and the estimates still close (note 65 §3.2)." Delete the clause
   "No inequality in the reverse direction ... was found".
2. Note 61 §6a, item 2, last bullet: "CMP 109 p. 255" is **p. 259**; the
   statement is "the effective coupling constants are given by g_k² = g²L^kε".
3. Note 61 §6a, item 1, second bullet: the sentence "the analysis presented
   in [16] for three-dimensional models is enough here" (p. 276) concerns the
   R_k terms (treated like E_k without the coupling counterterm); it is not a
   statement that all of Sect. 3 holds for d = 3.
4. Note 61 §6a, item 3 and the Verdict: Sect. 3 has now been read from the
   page images (note 65). Add: Sect. 3 contains no bound on T_k; the large-field
   activity bound is CMP 122 II, so (H4a) remains "published conditional input,
   checked at the level of the inductive assumptions and of Sect. 3's form
   preservation".
5. Note 61 §6, (H4b): the per-region factor is g_j^q times a polynomial in
   λ_j = log g_j^{-2} (Prop. 65.4), and a persisting domain has radius
   O(M R_j) j-cells (Lemma 65.3).
6. Note 49 §5 ("Source check 2p_0 > r: resolved") and the header remark "the
   actual choice was not located": CMP 119 (1.1), p. 246, states
   p_0 >= 5r (p_0 >= 5r, ε_0 = g_0 p_0(g_0), p_0(g_0) = A_0 (log g_0^{-2})^{p_0}).
   Then 2p_0 >= 10r > (d+1) r for d = 3 and d = 4 (script Part F). At d = 3
   the requirement from entropy is p_0 > 2r instead of p_0 > 5r/2.
7. Note 49 (T2-R) and note 39: these are the d = 4 persistence bounds with the
   R-operation. At d = 3 with R = identity, Z_{k+1} ⊃ Z_k' (§3.6), so a seed
   at scale i <= k near Λ makes the persistence event of note 39 hold at all
   later levels: P(E_t) does not decay in t. What note 61 (H4a) needs is the
   single-scale bound P(x ∈ Z_j) <= C_q g_j^q of Prop. 65.4, whose
   sum over creation scales converges by Lemma 65.2. Which uses of (T2-R)
   in notes 39/25 remain needed at d = 3 should be checked by the lead.

## 7. Next step

T72: confirm (W) at d = 3 with R = identity, i.e. CMP 122 II (1.83)-(1.85),
(1.89) and (1.97)-(1.99), in particular whether the exponent κ_j(Z) of
(1.83) still increases by -O(1)M^dR^d d'_{j+1}(Z) per unprocessed step and
whether that is compensated by Lemma 65.2 here; and whether CMP 122 II's
induction uses (2.6)-(2.9) with n - m > 1 anywhere (the T71 reading found
only n - m = 1 in Sect. 3).

## Appendix A. OCR reconstructions

`sources/ocr/cmp119.md` lines 514-1001 cover Sect. 3 but most displays are
garbled or missing. All formulas in Table 1 were transcribed from the page
images. Specific reconstructions:

- (3.3) the definition δ_k: OCR "δk = g kAί/A opo(g k)"; image reads
  δ_k = g_k A_1 p_0(g_k)/A_0; with (3.9) this is (A_1/A_0) ε_k.
- (3.7): the OCR keeps only a fragment ("(1+β_0)ε_k) < -ε_k on □~"); the full
  chain of inequalities was read from the image (p. 266). The exponent
  "δ2M_2R_k" is exp(-2δ M_2 R_k).
- (3.8): OCR keeps only "<2(1+β_0)L^{-2}ε_kη² + (4/10)ε_kη² < ε_kη²"; the
  first line with (1 + (2/10)ε_kη) and (2/10)ε_kη²(1 + (4/10)ε_k) is from the
  image.
- (3.9), (3.10): displays missing in the OCR.
- (3.12): OCR "2B_3L²(1+β_0)h(L'^{1}η)²": the letter "h" is ε_k and the
  argument is (L^{-1}η)².
- (3.13)-(3.14): OCR "(ί+β_0)" is (1+β_0); (4dL)² is as printed.
- (3.15): split across pages 267-268 and mostly lost in the OCR; the full
  display, including the lines with (E_k + R_k + B_k) and
  A(1/g_k²(·) - 1/g_k², ...), is from the image.
- (3.17)-(3.20): displays reconstructed from the image; "2LMγ" in the OCR of
  p. 268 is 2LM_1.
- (3.26): the equation number is missing in the printed display on p. 271
  (and the text calls it (3.6)); (3.28)-(3.38): displays reconstructed.
- (3.43): the analyticity space; the OCR drops it. (3.44)-(3.47): displays
  from the image; "three-dimensional wall" and "two-dimensional edge" are
  literal.
- (3.49)-(3.72): index placement (μ, ν, κ, λ and the sums over κ<μ, λ<ν),
  powers (L^jL^{-n})^{5-β}, ^{6-β}, ^{3}, and the bound (3.68) with
  11d², dM(n-j+2), 3dM(1 + log L^jL^{-n}) read from the image.
- Equation numbering: CMP 119 cites the coupling inequality as (I.0.33) and
  the copy of CMP 109 prints it as (0.31); I treat them as the same two-sided
  bound on 1/g_k².
