# Equal mass per label: the \(R'\)-proof and the complete-\(R\) stopping point

Status: **The abstract normalization lemmas and the matching of the first one
to CMP 122 I, Eq. (1.100), are proved here.**  The actual partial denominator
does preserve conditional fiber mass for every fully resolved,
pre-localization \(R'\)-summand.  Thus the warning on printed p. 177 is not a
counterexample to labelwise normalization.  It means that the introductory
formula (0.3) is not the formula from which that fact must be proved.

The stronger claim for arbitrary labels after polymer localization,
exponentiation, history regrouping, and the final reverse
Faddeev--Popov equivalence is **not proved by Part I**.  This note gives the
exact identity that is available, the label resolution it requires, and the
precise formula still needed if one insists on transporting those labels
through the final non-pointwise step.  T11 therefore takes option (a): the
equal-mass hypothesis used by the positive sequential telescopes is proved
when their labels are placed at the explicit \(R'\)-stage.  This does not
identify those labels with final signed polymer activities.

## 1. The normalization mechanism

Let \(V_c\) denote exterior data, let \(W\) be a fiber variable with measure
\(dW\), and let \(\lambda\) contain every history, component, graph, cutoff,
and integration-region choice.  Suppose a positive pre-replacement summand
has density \(p_\lambda(W,V_c)\), with conditional mass

\[
 C_\lambda(V_c)=\int p_\lambda(W,V_c)\,dW.
 \tag{1.1}
\]

For a finite set of auxiliary choices \(a\in\mathscr A_\lambda\), let
\(q_{\lambda,a}(W,V_c)\ge0\), put

\[
 Q_{\lambda,a}(V_c)=\int q_{\lambda,a}(W,V_c)\,dW>0,
 \tag{1.2}
\]

and take nonnegative weights \(\theta_{\lambda,a}\) with
\(\sum_a\theta_{\lambda,a}=1\).

### Proposition 1: a partial template denominator is enough

Define

\[
 r_\lambda(W,V_c)
 =C_\lambda(V_c)
  \sum_{a\in\mathscr A_\lambda}\theta_{\lambda,a}
  {q_{\lambda,a}(W,V_c)\over Q_{\lambda,a}(V_c)}.
 \tag{1.3}
\]

Then, for almost every fixed exterior field,

\[
 \int r_\lambda(W,V_c)\,dW
 =C_\lambda(V_c)
 =\int p_\lambda(W,V_c)\,dW.
 \tag{1.4}
\]

In particular, the pre- and post-replacement exterior marginals agree, and
their total masses agree label by label.

#### Proof

Every normalized template in (1.3) has fiber integral one.  Integrating and
using \(\sum_a\theta_{\lambda,a}=1\) proves (1.4). \(\square\)

The denominator in (1.2) need not be the integral of the whole old summand.
It only has to be the integral of the same template that appears in the
numerator.  The old summand enters through its already computed conditional
mass \(C_\lambda\).  This is exactly the structural distinction obscured by
the short warning on printed p. 177.

## 2. What can go wrong for a genuinely mismatched partial denominator

For comparison, let \(p^\sharp_\lambda,q^\sharp_\lambda\) be selected parts
used only in a normalization ratio, and write

\[
 \begin{aligned}
 P_\lambda&=\int p_\lambda\,dW,&
 Q_\lambda&=\int q_\lambda\,dW,\\
 P^\sharp_\lambda&=\int p^\sharp_\lambda\,dW,&
 Q^\sharp_\lambda&=\int q^\sharp_\lambda\,dW.
 \end{aligned}
 \tag{2.1}
\]

If one instead defines

\[
 r_\lambda={P^\sharp_\lambda\over Q^\sharp_\lambda}q_\lambda,
\]

then its exact post/pre conditional-mass ratio is

\[
 \Gamma_\lambda
 ={\int r_\lambda\,dW\over\int p_\lambda\,dW}
 ={P^\sharp_\lambda/P_\lambda\over
   Q^\sharp_\lambda/Q_\lambda}.
 \tag{2.2}
\]

Thus conditional mass is preserved if and only if the two selected fractions
agree.  Positivity of \(Q^\sharp_\lambda\) alone gives no quantitative bound.
If

\[
 0<a_-\le {P^\sharp_\lambda\over P_\lambda}\le a_+,
 \qquad
 0<b_-\le {Q^\sharp_\lambda\over Q_\lambda}\le b_+,
\]

then the exact available estimate is only

\[
 {a_-\over b_+}\le\Gamma_\lambda\le {a_+\over b_-}.
 \tag{2.3}
\]

Alternatively,
\(\left|P^\sharp_\lambda/P_\lambda-Q^\sharp_\lambda/Q_\lambda\right|
\le\eta\,Q^\sharp_\lambda/Q_\lambda\) gives
\(|\Gamma_\lambda-1|\le\eta\).  No such selected-fraction comparison is
stated in the global normalization identity of CMP 122 I, Eq. (1.102).

### Counterexample to inference from total normalization

Let the exterior space be \(\{0,1\}\), the fiber be \(\{a,b\}\), and use
counting measure.  Take the selected part to be restriction to \(\{a\}\), and
define

| \(V_c\) | \(p(a)\) | \(p(b)\) | \(q(a)\) | \(q(b)\) |
|---|---:|---:|---:|---:|
| \(0\) | \(3/2\) | \(1/2\) | \(1\) | \(1\) |
| \(1\) | \(1/2\) | \(3/2\) | \(1\) | \(1\) |

Then \(P=Q=2\) at both exterior points, whereas
\((P^\sharp,Q^\sharp)=(3/2,1)\) at \(0\) and \((1/2,1)\) at \(1\).  The rule
above has post masses \(3\) and \(1\), instead of \(2\) and \(2\), but both
total masses equal \(4\).  For the exterior test
\(F=\mathbf1_{\{V_c=0\}}\), the normalized expectation changes from
\(1/2\) to \(3/4\).

This example does **not** model Eq. (1.100), which has the matched form
(1.3).  It proves only that Eq. (1.102), or any other equality after the
final integration, cannot by itself be promoted to the conditional identity
(1.4).

## 3. Matching CMP 122 I, Eq. (1.100)

The introductory operation on printed p. 176 decomposes \(Z=Z'\cup Z''\)
and uses

\[
 \rho(Z'',V)
 {\int dV|_{Z'}\rho(Z,V)\over
  \int dV|_{Z'}\rho(Z'',V)}.
 \tag{3.1}
\]

For each fixed \((Z',Z'')\) and fixed exterior field, integrating (3.1) over
\(V|_{Z'}\) gives the numerator.  The prototype therefore has (1.4) term by
term.  Equation (0.4) is its total-mass consequence.

Printed p. 177 says that the actual denominators are not integrals of the
whole densities in (3.1).  They are integrals of parts localized near \(Z'\),
independent of \(Z''\), and determined only by the small-field effective
action.  The detailed proof of normalization is consequently not (3.1), but
Eq. (1.100), printed p. 201.

The construction through Eq. (1.75) only rewrites the density.  The next
operation integrates each summand over its own domain \(\Lambda\).  Printed
pp. 193--194 explicitly replace equality of densities by the equivalence
relation

\[
 f\equiv g
 \quad\Longleftrightarrow\quad
 \int f(V_k)\,dV_k=\int g(V_k)\,dV_k,
 \tag{3.2}
\]

and note that \(\Lambda\) usually varies with the summand.  Retaining that
summand and its \(\Lambda\) in \(\lambda\), denote the resulting conditional
coefficient by \(C_\lambda(V_c)\).

After writing \(Z=X_1\cup\cdots\cup X_n\), the integrations and remaining
choices factorize in these components.  For a component \(X_i\), Eq. (1.100)
inserts a normalized finite graph average of

\[
 {q_i(V'_k;V_{\Lambda_i})\over Q_i(V_{\Lambda_i})},
 \tag{3.3}
\]

where, suppressing only the resolved label indices,

\[
 q_i(V'_k;V_{\Lambda_i})
 =\delta_{G_i}(V'_k)\,\chi(\Lambda_i)
 \exp\!\left[-{1\over g_k^2}
 A\!\left(\zeta_i,
 U_{k,X_i}(V'_kV_{\Lambda_i})\right)\right]
 \tag{3.4}
\]

and

\[
 Q_i(V_{\Lambda_i})
 =\int dV''|_{\Lambda_i}\,
 q_i(V'';V_{\Lambda_i}).
 \tag{3.5}
\]

The positivity statement in Part I makes \(Q_i>0\).  More importantly,

\[
 \int dV'_k|_{\Lambda_i}
 {q_i(V'_k;V_{\Lambda_i})\over Q_i(V_{\Lambda_i})}=1
 \tag{3.6}
\]

for every fixed exterior field.  The other component factor in (1.100) is
the old summand after the label-dependent integrations in
Eqs. (1.76)/(1.99), namely \(C_\lambda\).  Hence the actual \(R'\)-summand is
of the form (1.3), not the mismatched form (2.2).

### Theorem 2: labelwise mass for the actual basic \(R'\)-operation

Resolve \(\lambda\) by all the data summed in Eq. (1.100): the large-field
history, \(Z_k\), the ordered components \(X_i\), localized domain sequences,
graph and gauge choices, cutoffs, and integration regions \(\Lambda_i\).
Before polymer localization and exponentiation, the pre- and
post-\(R'\) summands satisfy

\[
 \int dV'_k|_{\Lambda_i}\,
 r_{\lambda,i}(V'_k,V_c)
 =
 \int dV'_k|_{\Lambda_i}\,
 p_{\lambda,i}(V'_k,V_c)
 \quad\text{for a.e. }V_c
 \tag{3.7}
\]

for every component \(i\).  In particular they have the same exterior
marginal and the same total mass label by label.

#### Proof

Equation (1.100) is (1.3) componentwise: the previously integrated old factor
is \(C_{\lambda,i}(V_c)\), and every term of the normalized graph average has
fiber integral one by (3.5)--(3.6).  Apply Proposition 1.  The factorization
over the disjoint \(X_i\) permits any deterministic component order; treating
the other components as exterior data proves (3.7) one component at a time.
\(\square\)

The global identity Eq. (1.102) follows by summing the labels and integrating
the exterior fields, but it is weaker than (3.7).

## 4. What Theorem 2 does and does not discharge

For the positive sequential terms in research notes 13 and 16, Theorem 2
supplies exactly the equal-mass hypothesis if their label \(\lambda\) is placed
at the explicit \(R'\)-stage and retains the full data above.  It gives both

\[
 P_\lambda(\Omega)=R_\lambda(\Omega)
\]

used by the covariance identity and the stronger fixed-exterior equality
used by the normalized-tail identity.  The p. 177 caveat should therefore be
read as a demand to use Eq. (1.100), not as evidence that these identities
fail.

The conclusion cannot be transferred verbatim to labels of the final polymer
activities.  Printed p. 201 calls \(R'\) only a basic part of \(R\), and
printed p. 202 defers extraction of the effective action, localization, and
exponentiation.  Those operations split, merge, and resum the original
positive summands into generally signed activities.  Such an activity need
not have a positive conditional law, and it has no canonical one-to-one
pre-\(R'\) label.  The product-space total-variation formulation in research
note 11 is the correct statement after that regrouping.

CMP 122 II adds one further non-pointwise operation.  On printed p. 378 the
reverse Faddeev--Popov removal is possible only after integrating the density
over the relevant components; the densities before and after removal are
called equivalent, not equal.  To extend (3.7) through that step one needs a
resolved formula of the form

\[
 \int r^{\mathrm{FP}}_\lambda(W,V_c)\,dW
 =\int p^{\mathrm{FP}}_\lambda(W,V_c)\,dW
 \quad\text{for a.e. }V_c,
 \tag{4.1}
\]

with the same measurable label on both sides, before the histories are
regrouped.  The published text states the integrated equivalence and later
uses normalized component operations, but it does not display (4.1) with the
complete pre/post label correspondence that would be required to reuse the
same labels after that operation.  This is the exact additional step for
arbitrary labels of the complete \(R\); it is not needed for Theorem 2's
pre-localization telescope.

Thus Theorem 2 removes the denominator/mass objection for the actual positive
\(R'\)-replacement.  It does not remove the broader Robs obligation: sources
or terminal tests must still be carried through localization,
exponentiation, the history sum, and the reverse Faddeev--Popov equivalence.

## 5. T11 verdict

The source audit gives a two-level answer and resolves T11 by option (a).

1. **Proved:** the actual partial-denominator rule in CMP 122 I,
   Eq. (1.100), preserves conditional fiber mass for each fully resolved
   pre-localization \(R'\) label.  No bound on a ratio of mismatched partial
   masses is needed.
2. **Not proved:** an equal-mass identity for arbitrary final signed/polymer
   labels, or the resolved fixed-exterior identity (4.1) for the final
   reverse Faddeev--Popov step.  Total normalization alone is insufficient,
   as the finite example in Section 2 shows.

Thus the labelwise equal-mass assumption in the positive \(R'\)-stage is no
longer an unsupported hypothesis.  The result still stops short of an
observable theorem for the complete \(R\)-operation.

## Primary sources

- T. Balaban, *Large Field Renormalization. I. The Basic Step of the
  \(R\) Operation*, CMP **122** (1989), 175--202: Eqs. (0.2)--(0.6), printed
  pp. 176--177; the equality-to-equivalence transition and term-dependent
  integrations, printed pp. 193--194; Eqs. (1.99)--(1.102), printed
  pp. 200--201; the deferred completion, printed p. 202.
- T. Balaban, *Large Field Renormalization. II. Localization,
  Exponentiation, and Bounds for the \(R\) Operation*, CMP **122** (1989),
  355--392: the reverse Faddeev--Popov equivalence, printed pp. 378--379;
  localization and exponentiation through Eqs. (1.98)--(1.100), printed
  pp. 389--390.
