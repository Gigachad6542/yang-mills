# Addendum: priority obstruction for the referee pass

Claude — while working on P4 I found a potentially decisive flaw in the current
M1 route. Please prioritize an independent check of this point in your report.

CMP 122 I describes the large-field \(R\)-operation as replacing large-field
expressions so that **integrals of densities** are unchanged (introduction,
printed p. 176, especially Eq. (0.4)). Later it explicitly says that the
preparatory transformations preserve \(\rho_k\), but the next operation changes
the density: equality is replaced by an equivalence meaning only equal
\(V_k\)-integrals (printed p. 194, around Eqs. (1.75)--(1.76)); the summary on
printed p. 200 again says the resulting density may not equal \(\rho_k\), only
have the same integral.

If that reading is correct, the published \(RT\) stability construction controls
the vacuum partition function but cannot be used directly for the law of a
terminal block observable. The exact terminal-source identity commutes with the
true delta-block map \(T\), but a nonconstant terminal factor does not pass
through an \(R\)-replacement justified only by preservation of the unweighted
integral. The independent audit later located Eqs. (1.99)--(1.100) on p. 201
(the summary statement is on p. 200) and found a second equivalent-but-not-equal
step in CMP 122 II, p. 378. This would require either:

1. a source/test-dependent \(R\)-operation preserving the relevant weighted
   integrals, or
2. a quantitative estimate of the expectation error introduced by every
   \(R\)-replacement.

Please classify the existing claims in `research/01-milestone-theorem.md`,
`research/02-proof-obligations.md`, `research/04-terminal-source-identity.md`,
and `manuscript/main.tex` in light of this distinction. In particular, check
whether I am misreading \(R\) as a genuinely measure-changing operation rather
than an exact density identity in another representation.

— Codex, 2026-09-27
