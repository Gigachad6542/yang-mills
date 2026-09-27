# Coupling-flow shooting reduction

Status: **proved here as a scalar-recursion lemma**. The uniform Yang--Mills
beta-increment estimates needed to apply it are open in this project and are the
missing input behind Balaban's announced CMP **109**, Theorem 2.

## Published recursion and target

Balaban defines the effective coupling recursively in CMP **109**, Eqs. (0.18)
and (0.20), in the form

\[
 g_{k+1}^{-2}=g_k^{-2}-\beta_{k+1}(g_k).
\]

Theorem 2, Eq. (0.31), asserts for \(SU(2)\) a choice of the bare coupling with
prescribed terminal value \(g_K=g\) and two-sided linear control of
\(g_k^{-2}\) in \(K-k\). The paper promises a separate proof; CMP **122 II**
later says it was not published.

Here \(\epsilon=L^{-K}\), so \(K=\log_L(1/\epsilon)\). CMP **109** defines
\(\beta_{j+1}\) through the vacuum-polarization Hessian/moment in Eqs. (1.20)--
(1.22), printed p. 264. It proves smoothness/analyticity and uniform boundedness,
but no positive lower bound and no uniform expansion
\(\beta_j(u)=b_*+O(u^2)\). The paper also warns on printed p. 298 that
\(\beta_j\), although displayed as a function of \(g_{j-1}\), depends on all
preceding couplings. Thus every hypothesis below must ultimately hold uniformly
over admissible coupling histories.

The lemma below isolates the elementary shooting argument from the hard field-
theoretic assertion that the increments \(\beta_{k+1}\) really have uniform
positive bounds along the full RG trajectory.

## Theorem 1: backward shooting

Put \(h_k=g_k^{-2}\). Fix \(h_*=\gamma^{-2}>0\), a terminal value
\(h_K\ge h_*\), and constants \(0<b_-\le b_+<\infty\). For
\(j=1,\ldots,K\), let

\[
 B_j:[h_*,\infty)\longrightarrow[b_-,b_+]
\]

be continuous, and suppose \(F_j(h)=h-B_j(h)\) is strictly increasing. Then
there is a unique backward trajectory satisfying

\[
 h_j=h_{j-1}-B_j(h_{j-1}),
 \qquad j=1,\ldots,K,
\]

with the prescribed \(h_K\). It obeys

\[
 h_K+b_-(K-k)
 \le h_k\le
 h_K+b_+(K-k),
 \qquad 0\le k\le K.
\]

Equivalently,

\[
 g_k\le g_K\le\gamma,
\]

and the bare coupling satisfies

\[
 \frac{1}{h_K+b_+K}
 \le g_0^2\le
 \frac{1}{h_K+b_-K}.
\]

### Proof

Assume \(h_j\) is known and set
\(x_-=h_j+b_-\), \(x_+=h_j+b_+\). Then

\[
 F_j(x_-)=x_--B_j(x_-)\le h_j,
 \qquad
 F_j(x_+)=x_+-B_j(x_+)\ge h_j.
\]

Continuity gives a solution of \(F_j(h_{j-1})=h_j\) in
\([x_-,x_+]\); strict monotonicity makes it unique. Backward induction constructs
the trajectory and summing the one-step brackets gives the displayed bounds.
Inversion gives the coupling bounds. \(\square\)

A convenient sufficient condition for strict monotonicity is

\[
 |B_j(h)-B_j(h')|\le q|h-h'|,
 \qquad q<1,
\]

uniformly in \(j\). Existence alone needs only continuity and the two-sided
increment bound; uniqueness is not required merely to produce one bare coupling.

## Proposition 2: two-term asymptotics

Let a reverse-scale sequence \(H_m\), starting at the fixed terminal coupling,
satisfy

\[
 H_{m+1}=H_m+b+\frac{c}{H_m}+r_m,
 \qquad b>0,
 \qquad |r_m|\le\frac{C}{H_m^2},
\]

and assume \(H_m\ge H_0+a m\) for some \(a>0\). Then

\[
 H_m=bm+\frac cb\log(m+1)+O(1).
\]

### Proof

The linear lower bound makes \(\sum_{j<m}H_j^{-1}=O(\log(m+1))\) and
\(\sum_jH_j^{-2}<\infty\). Summing the recursion first gives
\(H_m=bm+O(\log(m+1))\). Hence, for \(j\ge1\),

\[
 \frac1{H_j}-\frac1{bj}
 =O\!\left(\frac{\log(j+1)}{j^2}\right),
\]

whose series converges. Therefore

\[
 \sum_{j<m}\frac1{H_j}=\frac1b\log(m+1)+O(1).
\]

Summing the original recursion once more and using
\(\sum_jr_j=O(1)\) proves the claim. \(\square\)

For \(m=K\) and \(a=L^{-K}\), this is the abstract source of a leading
\(\log(1/a)\) term and a subleading \(\log\log(1/a)\) correction in the inverse
bare coupling. It does not identify \(b\) or \(c\) with Yang--Mills beta-function
coefficients; that identification requires the missing uniform RG calculation.

## Exact missing Yang--Mills inputs

To apply Theorem 1 to the Balaban flow one must prove, rather than assume:

1. the effective increment is defined consistently with the complete
   \(E/R/B\) density and all irrelevant coordinates;
2. \(0<b_-\le\beta_{k+1}(g_k)\le b_+\) uniformly in scale and ultraviolet
   depth, and uniformly in the preceding coupling history, on the required
   analytic domains;
3. enough continuity or monotonicity for the terminal-coupling shooting map;
4. compatibility of those estimates with the large-field \(R\)-operation.

For the two-term asymptotic one additionally needs a uniform expansion of the
increment through order \(H^{-1}\), with a summable \(O(H^{-2})\) remainder.
Formal perturbative coefficients do not supply these nonperturbative uniform
bounds by themselves.

A concrete sufficient one-loop hypothesis would be

\[
 \beta_n(u;\text{history})=b_*+r_n(u;\text{history}),
 \qquad b_*>0,
 \qquad |r_n|\le Cu^2,
\]

plus the derivative bound needed for monotonicity. Choosing
\(C\gamma^2<b_*\) gives \(b_\pm=b_*\pm C\gamma^2\) in Theorem 1. The
irrelevant-polymer estimate CMP **109**, Eq. (0.29), does not provide this
remainder bound; it controls a different part of the effective action.
