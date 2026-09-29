# Three dimensions: exact \(T\)-transport and the absence of \(R\)-bias

Status: **Propositions 1--2 and the scale-series computation are proved
here.**  The identification of Balaban's three-dimensional flow as the exact
\(T\)-iteration is a published input, verified on the primary scan.  This
removes the complete-\(R\) observable obstruction from the three-dimensional
terminal-source problem.  It does **not** prove adjacent-cutoff convergence
or M1.

## 1. The decisive source fact

Balaban's three-dimensional paper starts from

\[
 \rho_0(U)=\exp[-g_0^{-2}A(U)-E],
 \qquad g_0^2=g^2\varepsilon
 \tag{1.1}
\]

and defines the complete flow by

\[
 \boxed{\rho_{k+1}=T\rho_k.}
 \tag{1.2}
\]

This is Eq. (2) on printed p. 256 of CMP **102**.  The construction stops at
\(K\) with \(L^K\varepsilon=\varepsilon_0\), where
\(\varepsilon_0\) is a fixed terminal spacing.  Theorem 1, printed p. 257,
states its bounds (5) for the densities defined by (1.2), and Eq. (6) records
the exact normalization identity

\[
 \int \rho_k=\int T^k\rho_0=\int\rho_0=Z^\varepsilon.
 \tag{1.3}
\]

There is no large-field \(R\)-replacement in this flow.  The \(R\)-operation
was introduced later to repair the four-dimensional large-field induction.
The decompositions of unity, saddle expansions, and resummations inside the
three-dimensional proof analyze \(T\rho_k\); they do not replace it by a
different equal-integral density.

## 2. Terminal sources pass through every step exactly

For clarity, write one exact block transformation in its deterministic
group-delta form

\[
 (T_k\rho)(V)
 =\int dU\,
   \delta_G\!\left(VQ_k(U)^{-1}\right)\rho(U),
 \tag{2.1}
\]

where \(Q_k\) is Balaban's gauge-covariant block average.  This is the
published \(T\)-dictionary audited in research note 04.

### Proposition 1: exact three-dimensional terminal-source identity

Let \(F\) be any bounded measurable function of the terminal block field and
put

\[
 Q^{(K)}=Q_{K-1}\circ\cdots\circ Q_0.
 \tag{2.2}
\]

For the three-dimensional densities (1.2),

\[
 \int F(V_K)\rho_K(V_K)\,dV_K
 =\int F(Q^{(K)}(U_0))\rho_0(U_0)\,dU_0.
 \tag{2.3}
\]

More generally, for bounded terminal tests \(F_1,\ldots,F_r\) and arbitrary
complex sources \(z_1,\ldots,z_r\),

\[
 \int \exp\!\left(\sum_{\alpha=1}^rz_\alpha F_\alpha(V_K)\right)
       \rho_K(V_K)\,dV_K
 =
 \int \exp\!\left(\sum_{\alpha=1}^rz_\alpha
       F_\alpha(Q^{(K)}(U_0))\right)\rho_0(U_0)\,dU_0.
 \tag{2.4}
\]

**Proof.**  Integrating (2.1) against a bounded function \(f(V)\) and using
the group delta gives

\[
 \int f(V)(T_k\rho)(V)\,dV
 =\int f(Q_k(U))\rho(U)\,dU.
 \tag{2.5}
\]

Iterating (2.5) proves (2.3).  The exponential in (2.4) is bounded for every
fixed complex source because the family \(F_\alpha\) is bounded, so the same
identity applies to it. \(\square\)

### Corollary 1: the \(R\)-bias series is identically absent

The physical three-dimensional density at every depth is the exact
\(T\)-pushforward.  Hence there are no pre-/post-\(R\) laws, no
fiber-template mean shift, and no H6\(_\Sigma\)--H8\(_\Sigma\) contribution
to a terminal observable.  In the notation of the four-dimensional
observable telescope,

\[
 D_m^{(R)}(F)=0
 \quad\text{for every }m.
 \tag{2.6}
\]

Thus the question whether the three-dimensional large-field factor makes the
\(R\)-bias summable has a stronger answer: the published three-dimensional
construction never creates that bias.

## 3. What remains open for three-dimensional M1

Proposition 1 is an identity at each fixed ultraviolet depth.  It does not
compare two different bare lattices.  For M1 one still has to place

\[
 (Q^{(K)})_*\bigl(\rho_0^\varepsilon dU/Z^\varepsilon\bigr)
 \quad\text{and}\quad
 (Q^{(K+1)})_*
 \bigl(\rho_0^{\varepsilon/L}dU/Z^{\varepsilon/L}\bigr)
 \tag{3.1}
\]

on their first common terminal lattice and prove a summable adjacent-depth
bound.  The two-sided ultraviolet-stability bounds (5) control each density
separately; they are not a Cauchy estimate for the pair (3.1).  This is the
three-dimensional P4 problem assigned separately in research note 18.

Likewise, a uniform upper and lower bound on the densities does not by itself
prove a positive limiting variance.  Three-dimensional nondegeneracy is a
separate question assigned in research note 17.  Nothing in this note
upgrades the published stability theorem to convergence.

## 4. Why the crude power count would also be harmless

Although no \(R\)-operation is present, the power count that motivated this
task is useful as a check.  The introduction of CMP **122 I**, printed
pp. 175--176, states that for \(d<4\)

\[
 g_0=g\varepsilon^{(4-d)/2}
 \tag{4.1}
\]

turns the original large-field factor into an arbitrarily large power of
\(\varepsilon\).  In \(d=3\), write the distance from the terminal scale as

\[
 m=K-k,\qquad
 \delta_m=L^k\varepsilon=\varepsilon_0L^{-m},\qquad
 g_k=g\delta_m^{1/2}.
 \tag{4.2}
\]

The published arbitrary-power statement has the form: for every \(N>0\),
after changing a constant,

\[
 w_m\le C_N\delta_m^N
 =C_N\varepsilon_0^NL^{-Nm}.
 \tag{4.3}
\]

There are \(O(\delta_m^{-3})=O(L^{3m})\) plaquette placements in fixed
physical volume.  To keep any additional fixed-anchor history entropy
explicit, let it be bounded by \(H_L^m\), where \(H_L\ge1\) depends only on
the fixed block size.

### Proposition 2: the hypothetical crude replacement series converges

If a hypothetical equal-mass local replacement at scale \(m\) changes a
bounded terminal test by at most its full oscillation and its fixed-anchor
absolute mass is bounded by \(C H_L^mw_m\), then its placement-summed defect
is at most

\[
 D_m\le C_F(H_LL^3)^mw_m.
 \tag{4.4}
\]

For every

\[
 N>3+\log_LH_L,
 \tag{4.5}
\]

the series is geometric:

\[
 \sum_{m\ge M}D_m
 \le {C_FC_N\varepsilon_0^N
       (H_LL^{3-N})^M\over1-H_LL^{3-N}}.
 \tag{4.6}
\]

**Proof.**  Combine the \(L^{3m}\) placements, the \(H_L^m\) fixed-anchor
loss, and (4.3).  The ratio is
\(H_LL^{3-N}<1\) precisely under (4.5), and summing the geometric tail gives
(4.6). \(\square\)

When \(H_L=1\), the large-field factor loses exactly three powers to
refining-lattice placements, so any \(N>3\) suffices.  At the newly added
ultraviolet level \(M=K\), \(L^{-K}=\varepsilon/\varepsilon_0\), and the
tail is \(O(\varepsilon^{N-3})\) up to fixed terminal-scale constants.

This calculation is only a consistency check.  It neither inserts an
unpublished \(R\)-operation into the 1985 proof nor supplies the
adjacent-depth comparison in (3.1).  Its role is to confirm Balaban's
qualitative statement that superrenormalizable large-field suppression beats
three-dimensional placement entropy.

## 5. Verdict

The observable-changing interface that dominates the four-dimensional
program is absent from Balaban's three-dimensional construction:

1. \(\rho_{k+1}=T\rho_k\) exactly;
2. bounded terminal sources commute with each \(T\)-step by Proposition 1;
3. therefore the cumulative \(R\)-bias is exactly zero, not merely
   summable;
4. even a hypothetical crude \(R\)-type replacement would have a convergent
   placement series by Proposition 2;
5. the genuine remaining M1 obligation is the adjacent-cutoff comparison of
   the two exact \(T\)-pushforward measures.

## Primary sources

- T. Balaban, *Ultraviolet Stability of Three-Dimensional Lattice Pure Gauge
  Field Theories*, CMP **102** (1985), 255--275: Eqs. (1)--(6), printed
  pp. 256--257, especially \(\rho_{k+1}=T\rho_k\) and Theorem 1.
- T. Balaban, *Averaging Operations for Lattice Gauge Theories*, CMP **98**
  (1985), 17--51: Eqs. (10)--(15), printed pp. 19--20, for the exact
  group-delta \(T\)-map and its deterministic gauge-covariant average.
- T. Balaban, *Large Field Renormalization I*, CMP **122** (1989), 175--202:
  Eq. (0.1) and the following \(d<4\) discussion, printed pp. 175--176, used
  only for the counterfactual power-counting check in Section 4.
