Title: 1103941451.pdf

URL Source: http://projecteuclid.org/journals/communications-in-mathematical-physics/volume-95/issue-1/Propagators-and-renormalization-transformations-for-lattice-gauge-theories-I/cmp/1103941451.pdf

Number of Pages: 24

Markdown Content:
Communications in  

> Commun. Math. Phys. 95, 17-40 (1984) Mathematical

# Physics  

> © Springer-Verlag 1984

## Propagators and Renormalization Transformations for Lattice Gauge Theories. I 

T. Balaban* 

> Department of Physics, Harvard University, Cambridge, MA 02138, USA

Abstract. Lattice gauge theories may be looked at as perturbations of the theory of a vector field with a Gaussian action. We study this theory here and in following papers obtaining crucial results for understanding the renormali-zation group method in more complicated non-Abelian gauge field theories. 

Introduction 

In paper [3] a general strategy of constructing Yang-Mills field theories was described. It is based on the renormalization group ideas, as in the case of Abelian Higgs models [1]. We take a lattice regularization of the theory and we apply renormalization transformations similar to those proposed by Wilson [8]. To calculate results of these transformations we apply perturbative methods based on the expansion (18) of the action (11) in [3]. Main terms in this expansion are quadratic terms (20) in [3] equal to the simplest quadratic action for Abelian vector fields. Together with renormalization transformations and gauge fixing conditions they define propagators, i.e. covariances of the Gaussian measure defined by these terms. Understanding properties of the propagators is the most fundamental problem in the method. Properties we are especially interested in are local regularity properties and an exponential decay, the same as in paper [2]. Here we will prove these properties for the simplest propagators appearing in our constructions. We will apply the methods and results of paper [2]. 

A. An Action, Its Symmetries, and a Renormalization Transformation 

We consider the theory of one vector field with a quadratic action. Field con-figurations are real valued functions A defined at bonds of the lattice Γ ε. This is a d-dimensional torus which we identify with the subset {xeε Z d : — L ^x < L , 

μ = 1, ..., d] of the lattice εZ d. Bonds of T ε are ordered pairs of nearest neighbor   

> ^Research supported in part by the National Science Foundation under Grant PHY-82-03669 18 T. Balaban

points. We denote them by b, V, c, or <x, x'>, <x, x -f εe μ> Thus ^4 are functions ^4 : {fo ci Tj -> [R. We identify them with vector valued functions defined on Tε by the formula  

> μ

μ = l , . . . , d . (1.1) Other important geometric objects are plaquettes. They are oriented elementary squares of the lattice Tε (or other lattices). We denote them by p, p' and so on. If p is a plaquette p = <x, y, z, w>, where x, y, z, w are corners of the square p

written in an order indicated by the orientation of p, then we define a plaquette variable F(p) = (dA)(p) = ε~ lA(dp) = z~ l(A(x, y) + A(y, z) + A(z 9 w) + A(w, x)) = (d μAv)(x) - (d vAμ)(x) = Fμv (x) = - F vμ (x). (1.2) The last equalities hold if we identify p with <x, x + εe μ, x + εe μ + εe v, x -f εe v> for some μ <v. For an explanation of other symbols the reader is referred to [1]. We assume that Ab is defined for bonds b with arbitrary orientation and that 

A<χ χ / > = — A<χl χ> . The action is defined by the quadratic form SV) = i Σ εd |F(p)| 2 =f Σ εd |(δ^)(p)| 2 =t Σ £" F ,vW| 2 ' ί1-3)    

> p c Γ εp c Γ exeT ε,μ,v

The covariant derivative dA, and so the action above, are invariant with respect to a group of guage transformations. A guage transformation is determined by a real valued function λ : T g -> R, and is defined by - λ(b_)\ b = <b_,b^. (1.4) This invariance of the action (1.3) is a fundamental symmetry of the theory. We will introduce renormalization transformations which preserve this symmetry. To make the considerations more clear we rescale the action from the ε-lattice to the unit lattice by transformation A(εx) = ε~ (d ~2}l2 Aμ(x\ xeT 1 5 and we get X \(dA)(p)\ 2. (1.5) 

Let us introduce some new definitions and notations. We define a new lattice T[ υ = 7\ nLZ d and we divide T1 into blocks B(y) parametrized by the points of  

> T(!) -1L '

B(y)={xεT 1:y μ^x μ<yμ + L,μ=l,...,d}, yeTΪ\ (1.6) In each block B(y) we introduce a family of contours Γ^ χ connecting the points 

y and x :

( y ί 9 ...,x μ ,x μ + 1 , ...,x d )]u...u[(); 1 ,x 2 9 ...,x d ),x], (1.7) where [x 1 ? x2 ] is a line segment connecting points x 1 ? x 2 . We consider Γyχ ,

and all other contours appearing in the paper, as oriented contours, with initial point y and final point x. To introduce a renormalization transformation we have to define an averaging operation. It transforms field configurations on the old Propagators for Lattice Gauge Theories. I 19 

lattice Tί into field configurations on the new lattice T^ υ and is given by the formula 

Bc= Σ L-« +

> jceB(c-)

(1.8) 

where A(Γ) = Σ \ f° r arbitrary contour Γ, and x(c) denotes a point in the block 

> bcΓ

B(c + ) obtained by translation of x by the bond c, so if c = <y, j; + Le > then 

x(c) = x + Le μ.

If we make a gauge transformation A, then for the averaged field B we have 

Bλc =B c- L~\λ(c +}- λ ( c _ } } = B c- (dλ)(c) 9 (1.9) so fixing the average, we restrict the gauge transformations by the condition 

λ(y) = 0, ye T (£\ for nonconstant λ. We still have the invariance with respect to the restricted transformations and we remove it by introducing Axial (Ax) gauge fixing conditions A(Γ y X) = Q, xeB(y), x ^ y, yeT^ If we denote 

# <U^)= Π Π 

> ye7γ> xeB(y)

xϊy 

(QA\= £ L~^VA(\x,x(c)-}),δ(B-QA)= \\ δ(B c-(QA\), (1.11)   

> xeB(c-) c c Γ ( 1 )

then the renormalization transformation T is defined by 

(Te~ s)(B) = $dAδ(B - QA)δ^(A)e-S(A \ (1.12) We may look at this expression also in a little bit different way. We may define the averaging operation as given by Q directly. Then the average field B transforms 

as   

> xeB(c + )xeB(c _ )

= Bc - L-\(Q'λ)(c +) - (Q fλ)(c_)) = B c- (d'Q'λ)(c). (1.13) Fixing it we restrict the gauge transformations by the condition (Qλ)(y) = 0. The remaining gauge degrees of freedom are removed by the term δAχ (A). In the future we will use both points of view. The integral in (1.12) is obviously a Gaussian integral. We will prove later that the quadratic form (δA, δAy is positive on the subspace of A satisfying QA = 0, 

A(Γ yx ) = Q, xeB(y\ yeT (L1} . A result of the integration is obviously a Gaussian density 

(Te-s)(B) = Z(0) exp( - \<£, z^B)) = Z(0) exp( - S^B)). (1.14) The form <£, A ΐBy is gauge invariant. l f λ ί is a gauge transformation on T(£\ then defining λ on Tl as constant on each block, λ(x) = λ ί(y) for xεB(y), we have Z(0) exp( - ^<5 λl , AlBλί y) = $dAδ(B λί - QA λ)δ^ χ(A λ) exp( - S(A λ)) - dλ^ -QA + dQ'λ)δ Aχ (A) exp( - S(A)) = Z(0) exp( - ^<5, AίB».  

> (1.15) 20 T. Balaban

The density (1.14) is defined on the L-lattice T^ 0 and our final operation is the rescaling from this lattice to the unit lattice T(^\ The operation of rescaling is denoted by S. 

B. Compositions of Renormalization Transformations. Basic Sequence of Actions 

We can apply the renormalization transformation again to (1.14). A composition of two transformations is easy to calculate :

((ST) 2e~ s)(C) = z(2 ^dBδ(C - QB)δ Aχ (B)$dAδ(B - QA)δ Aχ (A)exp( - SL~\A)) = z^$dA($dAδ(C - QB)δ(B - QA)δ Aχ (B))δ Aχ (A) exp( - SL'2(A)) 

= z™$dAδ(C - Q 2A)δ /JiQA)δ^(A)ap( - S L~\A)) 9 (1.16) where z (2) is a numerical factor coming from scaling transformations and Q2

is defined as Q only with the number L replaced by L 2 in all definitions. It is easily seen that a composition of k transformations is given by 

((SΊy te-s)(B) = z< k^dAδ(B^Q kA)δ AJiQ k_1A) ..... δ^A^e'^^ (1.17) where 

(Qk A\ = Σ ηd+1 A([x, X(b)-]) 9bcTM = Z. dnT η,η = L-k, (1.18)  

> xeB*(b _ )

and x(b) is a point in Bk(b + ) obtained from x by translation by b. If b = <y, y + ^ μ>, then x(b) — x + e . We define 

((ST) ke-s)(B) = Z k A χ exp( - ±<B, AkBy). (1.19) It is easily seen that Zk Aχ = Z (/c "1} ..... Z (0) , where Z O) is a normalization factor connected with j + 1 integration. Under a gauge transformation A the field A

and the averaged field QkA transform as follows 

Σ Ά*)- Σ ίf     

> βfc(b +)xeβfc(b_) /

(1.20) 

or denoting (Q' kλ)(y) = X r/ dA(x), we have QkAλ = Q kA - dQ kλ. 

The ^-function δ(B — Q kA) is invariant with respect to gauge transformations λ

satisfying Q' kλ = 0 and we can look at the integral (1.17) as obtained by removing this gauge freedom by the help of the ^-functions £ Aχ .

C. Change of Gauge 

To calculate the integral (1.17) and to introduce some important Green's functions we have to change the gauge fixing terms. In continuum the best gauge from the point of view of regularity properties of Green's functions is the Feynman gauge. We will introduce a similar gauge for the lattice theory using the Faddeev-Popov Propagators for Lattice Gauge Theories. I 21 

procedure. The action can be written as 

(dA,dAy=± ]Γ ηd\F v(x)| 2 = £ ηά\(d ^4 v)(x)| 2    

> xeTη,μ,v x,μ,v
> x,μ,v μXμμ

where A is ^-lattice Laplace operator for scalar functions and d* is the divergence operator for vector functions, d*A = Y d*A . We want to remove the second term in the action by a gauge fixing term, so we introduce under the integral (1.17) the identity 1 = - - - .The restrictions on the gauge transformations given by the (5-functions above are chosen in such a way that all the expressions in the integral (1.17) with the exception of gauge fixing terms <5 Aχ are invariant. Next we will calculate the expression in the numerator and denominator above and we will see that it is different from 0, but now let us transform (1.17). We change the order of integrations \dA ^dλ' ..., and we make the gauge transformation — λ' in the integral §dA.... We change the order of integrations again and we make a translation λ -> λ + λ' in the integral 

$dλ.... We get (1.17) = z(k ^dAδ(B - QkA)(\dλ'δ(Q kλ') 

2α —

(1.23) Now we will calculate the integral inside the above expression: —1| d*dλ I

2α" '\ / \

exp(-- inf i||5M - d*dλ\\ 2 Y (1.24) and the infimum can be calculated using Lagrange multipliers. Introducing 22 T. Balaban 

g(λ, ω) = \ II d*A — Δλ || 2 + < ω, β^l >, we have the equations 

# = β;ι = o. (1.25) 

Now we use spectral properties of the Laplace operator A on the torus T . It is a symmetric, non-negative operator, and 0 is its eigenvalue. Constant functions form the eigenspace corresponding to the eigenvalue 0, and on the subspace orthogonal to constant functions the operator Δ is positive. Hence it is an invertible operator and by Δ ~ l we denote its inverse on this subspace. We extend it to the whole space by linearity, putting its value on constant functions equal to 0. Let us notice further that the operator Q' k transforms constant functions on the η-

lattice into constant functions on the unit lattice, and similarly for the orthogonal subspaces. This implies the corresponding property for β^*, and for other operators constructed with the help of these mentioned above. Let us consider Eqs. (1.25). In the first equation the terms A2λ and Ad* A are orthogonal to constant functions, hence β^*ω has to be orthogonal also. We assume that λ is orthogonal and we get 

λ = A~ ld*A — A~ 2Q'*ω. Substituting in the second equation we get Qkλ = Q' kA~ ld*A — Q' kA~ 2Q'*ω = 0. The operator A~ 2 is positive on the subspace orthogonal to constant functions, hence QkA~ 2Q'* is positive also on the corres-ponding subspace on the unit lattice. Because ω belongs to the subspace, so ω = (Q' kA ~ 2Q'*) ~ 1 Q' kA ~*d*A and the infimum in (1 .24) is acquired at the function 

λ0 = Δ-ld*A-Δ-2Q(*(QίΔ-2Q'*Γ 1Q' kA-lB*A. 

The value of the infimum is equal to 

= ί2(d*A,Δ-ίQ'*(Q: kΔ-2Q'*Γ lQ' kΔ-id*Ay, (1.26) where we have used the fact that the quadratic form in d* A is defined by a projec-tion operator. We have finally 

> eχ

# p -^-< 

(1.27) It is easy to verify that the operator I — Δ ~ lQ*(Q kΔ~ 2Q*)~ lQkή ~ l is a projection in the space L2(T η) of scalar functions, so we can write also 

1'2α / / 

Δ~ iQ'*(Q'Δ~ 2Q'*)~ 1Q'Δ~ ί)d*A\\ 2 I. (1.28) Propagators for Lattice Gauge Theories. I 23 

To understand better regularity properties and bounds of the operators involved we write them in momentum representation. The momentum representation on    

> iη-i^^η/ d'

Fourier transform 

# 7(P) = Σ 

an arbitrary torus T' = {xeηZ d : — L' μ^ x μ < I/ , μ = 1, . . . , d} is introduced by the 

,

/(*) = (2πΓ d Σ ( Π 7Γ K' P/(P)> (1.29) 

> pef' r,\μ=l Lj μ/

where TJ is a dual torus f' n = {p = (p 15 ... 5 J pd ): pμ = (π/L μ)n μ, nμ is an integer,  

> 1

^n μ<L μη~ l, μ= l,...,d}. In the case considered now we have the 

tfe)' 1

equations we have solved: torus Tη with L' = Lμ(L kε) . Let us write in the momentum representation the ' Δ2(p)λ(p) - A(p)(d*A)(p) + uk(p]ώ(p') = 0, X« t(p' + /)I(p' + 0 = 0, (1.30)  

> d^ϊ^/^ — 1

# = Σ |3 μ(p)| 2,a μ(p) = - ,

(L31) 

where p' belongs to a dual torus T[ k} = {p 1 = (p' ί9 ... 9p' d): p'^ = (π/L μ)L kεn μ, nμ is an integer, - L μ/L kε<^n μ< L μ/L kε, μ=l,...,d} 9 pef η is represented as a sum 

p = p' + /, p' G f (k} and / = (/!,..., /,), / - 2πm μ, m μ is an integer, - (L k - l)/2 ^ 

mμ ^ (L k - l)/2 for L odd, - L k/2 ^m μ< L k/2 for L even. The first equation in (1.30) can be solved uniquely for p ^ 0 and we get = A ~ \p)(d*A}(p] - Δ-2(p}u k(p}ώ(p'\ p + 0, (1.32) for p = 0 the equation implies ώ(0) = 0. The second equation gives Because uk(ΐ) = 0 for / ^ 0, w fc (0) = 1, so this equation implies also 1(0) = 0. Thus we get the solution for p'^0,I 0(/) = ( ) ( / ) f o r / ^ 0 , I 0 ( 0 ) = 0. (1.34) 24 T. Balaban 

Substituting it into the expression in the exponent of (1.24) we get || d*A - Δλ 0 P = (2πΓ d

(1.35)   

> /d\

where § dp ... denotes the sum Σ ί ]j[ (π/L μ)L kε 1. . . , similarly J dp . . . , and we      

> T* peί, \ μ= i /ίf)

have used the decomposition p = p' + /, writing j dp . . . = J dp' 2] .... We have 

f,, fί fc > i__ 

used also the equality (d*A)(p)= Σ5(p)^ί(p), more exactly its consequence )= 0. The expression (1.34) can be rewritten in a way which makes clear its possible bounds. From (1.30) we have Δ(p)= 0(|p | 2) in a neighbourhood of 0. Let us 

d

introduce the unit lattice operator AQ(p f) = £ \e ip 'μ — 1 1 2. It has the same asymp-

> μ = l

totic behaviour ^ 0(p r) = 0(|p'| 2) in a neighbourhood of 0 as Δ(p\ so the quotient 

ΔQ(p)/Δ(p) is bounded, more exactly we have Λ 0(p')/^(p'+ /)<; 0(1)1/(1 + |/| 2 ). Similarly we have 

\u k(p' + 01 g 0(1) Π J^LgOd) Π T-^-I. (1.36)     

> μ = l l^μ "f" V l -"=1 I VI

The expression in the exponent in (1.28) can be written as Now all the expressions above are well defined and bounded even at p' = 0 if we extend them by continuity. The expression in | |2 defines the projection operator acting on d*A and appearing in (1.27). Let us denote the projection operator by R, so we have The gauge fixing density has the form ' , (1.39) Propagators for Lattice Gauge Theories. I 25 

and from its definition it follows that ldλδ(Q' kλ)^ Ά(d^A λ) = 1. The projection operator R has a clear meaning. It is an orthogonal projection on the linear subspace ΔN(Q' k] of L2(T η\ N(Q' k) = {λ:Q' kλ = 0}. Indeed RΔλ = Δλ if Qkλ = 0, and if Rω = ω then A0Q' kA ~ 1ω = 0, and taking λ = A ~ lω we have ω = Δλ and β^l = 0. Let us denote this subspace by R also, R = AN(Q' k). We have 

= f

> N(Q' k)

(1.40) 

Λ \ /α /

so the density <^ α has a limit as α -> 0 

9f(d*A) -> |det(J U δfc) )|<y3*Λ), (1.41) 

> α-»0

where 3 Λ is a δ-ΐuncύon concentrated at the origin of the sub-space R. By definition 

$dλδ R(λ)f(λ) = $dλδ R(Rλ)f(λ) = J dλ^dλ, δ R(λ,}f(λ, + Λ 2 ) = j dλ 2/μ 2). Let us   

> RRΛ

recall also that the operator Δ is positive definite on N(Q' k), thus invertible, as it follows from [2]. Let us sketch briefly another possible approach to the calculation of the integral (1.23). We write (1.24) = \dλδ(Q' kλ) exp( - ~ \\ d*A -Δλ- aQ'*Q' kλ || 2), (1.42) with a > 0 (we will take eventually a = 1), and let us denote Δ' a = Δ + aQ' k*Q' k =A + aP' k. The properties of this operator were investigated in [2], its inverse is a bounded operator G' k with good regularity properties described in Theorem of [2]. We repeat the calculations done after the formula (1.24) with the operator A' a

instead of A and we get the following formulas for the minimizing function λ0 ,

λ0 = G' kd*A - G' k2Q' k*(Q' kG' k2Q'*Γ lQ' kG' kd*A, (1.43) and for the projection operator R

Now all the operators appearing in these formulas are well defined. We have to verify it only for (Q^G^Q'*)' 1. It is enough to prove that QfifQ'* is positive definite. This operator is of course nonnegative and if for some ω defined on Tf } we have <ω, Q'fi'ΐQ'fωy = || G' kQ'*ω\\ 2 = 0, then Q'*ω = 0, hence ω = 0. We have bounds 0 < Q^G'^Q'* ^a~ 2, and they imply the existence of the inverse operator and a bound from below. To understand better the properties of this operator we calculate the Fourier transform. It is a translation invariant operator on the unit lattice T^ and its Fourier transform can be written using formula (2.48) 26 T. Balaban 

from [2]. From this representation and from the bounds (2.51), (2.52) of that paper, it follows that there are positive constants 7 0 ,7 1 ? in fact y0 dependent only on 

d, y l = α~ 2 , such that y 0 ^ Q' kG' kQ'^ ^ yί. This property and the representation (1.44) are crucial for the later considerations when we will have operators dependent on external gauge field. The operator J^ given by (1.44) is of course by definition independent of a and we can take arbitrary a in the representation, e.g. a = 1, which is most convenient for bounds. 

D. Operators Hk and a Calculation of the Actions 

The equality (1.23) gives us a composition of k renormalization transformations with the new gauge fixing density ^ α. In the sequel it will be convenient to take the limit α -> 0, i.e. to consider Landau gauge. We may introduce this gauge from the beginning using the equation 

\dλδ(Q kλ)\άzϊ(Δ \N(Qk) )\δ R(d*A - Δλ) = 1. (1.46) We have to calculate the integral 

((ST) ke~ s)(B) = z/(/c) |det(zl \N(Qk) )\$dAδ(B - Q kA)δ R(d*A)exp(-±(dA, dAy). 

(1.47) With this integral an operator of fundamental importance is connected. It is defined on configurations B on the lattice T^ and its value on such a configuration is equal to a configuration A on T minimizing the form ^(dA, dA) under the conditions QkA = B, Rd*A = 0. Let us calculate this minimum. We introduce the function 

h(A, ω, λ) = ^(dA, dAy -f <ω, QkA — J5) + <λ, Rd*Ay 

, QkA - By + </l, Rd*Ay, Rλ = λ, (1.48) and we consider the equations 

δh 

~δA 

~ = ΔA- dd*A + β*ω + dλ = 0, 

-=Q kA-B = 0, = Rd*A = Q. (1.49) 

^ω δλ 

We have Rd*A = d*A- A~ iQ^(Q' kΔ~ 2Q'^Γ lQkΔ~ ld*A = 0, so the first equation has the form 

A A - dA ''Q'^QίA-iQ'*)- 1Q'A ~ ld*A + Q*ω + dλ = 0. (1.50) Propagators for Lattice Gauge Theories. I 27 

It implies that ω is orthogonal to constant functions. Introducing the new variables 

A' = A 112 A, and dividing by A1/2 , we have 

= Q^ (1.51) Let us notice that A is orthogonal to constant functions also. This can be written 

as 

(/ - P)A + A- l/2 Q*ω + A- l/2 dλ = 0. (1.52) A solvability condition for this equation is 

PA ~ 1/2 6*ω + PA ~ l/2 dλ = PA~ l/2 Q*ω + dΔ ~ 1/2 (/ - R)λ = PA~ 1/2 Q*ω - 0. (1.53) We have the decomposition 

A' = (I- P)A + PA' = A\ + A' 2

A[= -A' 1/2 β*ω -A' Il2 dλ, A 2 = dA~ 3/2 Q'*(Q kA ~ 2ρ;*Γ lλ'. (1.54) where λ' = Q kA~ 3/2 d*A'. The configuration A can be expressed in terms of A' as follows: A = A ~ l/2 A + A0, where AQ is a constant configuration. Substituting it into the other two equations in (1.49) and using the identity 

Qk3 = 8&, (1-55) 

di is the unit lattice differentiation, we get 

QkΔ -1/2 A[ + d^λ' + QkAQ = - Q kA ^Qfa - Q kA ~ ldλ + d,λ' + QkA0 = B, - R8*A -lQ*ω - Rd*A ~ ldλ H- RA ~ lQ'*(Q! kA-2Q'*Y lλ' = -RA ~ lQk*d*ω - Rλ = - λ = 0, (1.56) so for λ = 0 the third equation in (1.49) is satisfied automatically. The second equation gets the form - QkΔ-lQ*ω + d^λ' + QkA0 = B. (1.57) It implies that B — Q kA0 is orthogonal to constant functions. Taking the de-composition B = B' + J3 0, where BQ is a constant configuration and B' is in the orthogonal subspace, we can identify QkA0 = B 0, or A0 = Q*B 0. Further we have the solvability condition (1.53) 

# p^-^ρ^^^-^ρ ^ρ^^ρ η-^ j-^afω-o, 

which is equivalent to 3*ω — 0. Let us introduce the operator 

Φ = Q kΔ~ lQ*. (1.58) Equation (1.57) can be solved with respect to ω and we get ω = -f φ~ 1d1λf — φ~ lB'. 

The solvability condition gives the equation δ*ω = d*φ" ίdίλ/ - d*φ~ iBf = 0. This equation can be solved with respect to λ', and we get λ' = (d*φ~ 1d1}~ ld*φ ~ lBf.

These calculations lead to the following result for the minimal configuration 28 T. Balaban 

A, i.e. for the solution of Eq.. (1.49) : 

> 0

# . (1.59) 

This defines the operator HkB = A, thus we have 

HkB =

•(d*φ-ld,Γ ίS*φ-ίB' + Q*B 0. (1.60) Let us write this operator in momentum representation. 

'

(Q kA) μ(p r) = £φ' + l)v μ(p' + l)A μ(p' + I), v μ(p) = (1.61)  

> IUμ\P)

and operator φ as where we have omitted the subscript k. Multiplying φμ(p'} by ΔQ(p'\ we get a well-defined positive function for all p'εT (*\ 0 < y 0 ^ ΔQ(p')φ μ(p'} ^ γ χ . We have the following momentum representation for HkB : 

## Φ' + O ( P ' + 

# [ v (p' -

Δ(p f

-B λ(p'\ (1.63) 

This expression is well defined and bounded for all values of I and p', including 

p' — 0 where it is defined as a limit for p' -> 0. Another important property is that the sum over / of the absolute value of this expression multiplied by | dv(p' + /) ]| p1 + /| α is bounded by a constant dependent on Propagators for Lattice Gauge Theories. I 29 

d only. This implies bounds on (l/\x'-x\*)\d v(H kB) μ(χ')--d v(H kB) μ(x)\ (see the proof of Lemma 2.4 in [2].) Using (1.60), or better (1.63), we can verify all the properties oϊH kB: QkHkB = B, Rd*H kB = 0, HkB is a minimum of ^<βA, dAy on the hyperplane {A:Q kA = B, Rd*A=Q}, which means that (dA',dH kB> = 0 on the subspace [A':Q kA' = 0, Rd*A r = 0}. Let us now come back to the integral (1.47). We make the translation A = A +

HkB and using the above properties of HkB, we get ) = Zk exp( - ±<dH kB, dH kBy). (1.64) The action Ak is thus defined by <B, ΔkBy = <dH fc β, d# k£>. (1.65) Using formulas (1.60) or (1.63) we obtain the following expression 

K«ι«),,(rtl ! (1.66) 

The function under the integral is bounded from below and above by positive constants yQ9 yί dependent on d only, so we have  

> 7o

<3 1β, ^B> ^ <β, Zl fcJ B> ^ 7l <3 1B, δ.B) . (1.67) We will need also a representation of Hk similar to the representation (1.44) of the projection #. It will be expressed in terms of well-defined bounded operators. We are going to define them now. 

E. Operators G

The integral (1.47) can be written in the following way 

((ST) k exp( - S))(B) - z'< k>| det(Λ \N(Qk) )\ίdAδ(B - QhA)δ R(d*A) 

(1.68) The additional terms vanish because of the delta-functions. The quadratic form in the fields A in the exponential is equal to - <Λ ΔAy - <Λ dPd*Ay + a(A, Q*QAy, (1.69) 

# A - d*d + aa*, R = I-P 30 T. Balaban 

where we have omitted subscripts. The configuration d*A is orthogonal to constant functions and on such configurations the operator P is given by the formula 

p = A -lQf*(Q'Δ-2Q'*Γ lQ'Δ ~ *. (1.70) We will obtain an explicit representation of 

A~ l = Gfc , or simply G. (1.71) At first let us prove that Δa is a positive operator. Of course it is a symmetric operator and it is non-negative as a sum of two non-negative operators A — dPd* 

and ββ*β, a > 0. Thus if for some A we have AaA = 0, then 

A A - dPd*A = Q 9QA = 0. (1.72) From the first equation we get A = dΔ~ 2Q'*(QΔ~ 2Q'*}~ 1 ω + AQ9 where AQ is a constant vector function and ω is a function on unit lattice T/ Λ) orthogonal to constant functions. Using (1.55) we have 

QA = d&'Δ-iQ'^Q'Δ-tQ'*)- lω + A 0 = d^ω + AQ = 0, hence δ*3 1ω = 0, and this implies ω — 0. The above equation implies AQ — 0, so A = 0 and the positivity of Aa follows. It is an invertible operator and the equation 

A A - dA -1Q'*(Q'Δ ~ 2Q'*Γ 1 Q'Δ ~ *d*A + aQ*QA = J (1.73) has a unique solution for the arbitrary vector function J. We consider A also as a vector valued function on the lattice T . To solve this equation explicitly we calculate at first a projection of A on the subspace of constant functions. For each component A we have from (1.73) *6 = a<\ 9 Ay = <1, J > , (1.74) so <1,^> =«~ 1 <1, J >, 1 denotes here a function on Tη identically equal to 1. From now on we will assume that each component of A and J is orthogonal to constant functions. Applying the operator QA~ l to (1.73) and using (1.55) we get 

QA - d l QΔ ~ lΰ*A + aQΔ ~ 1Q*QA = QA~ 1J. (1.75) Of course < 1, QA > - < 1, QΔ ~ l J > = 0. Let us denote 

φ = I + aQA-lQ*. (1.76) It is a well-defined and positive operator on the subspace of vector functions defined on the unit lattice T(® and orthogonal to constant functions. Applying 

φ~ l to (1.75) we get 

φ-1QΔ-lJ. (1.77) Substituting it in (1.73) and applying A ~ 1 we have 

A - dΔ-2Q'*(Q'Δ-2Q*y lQ'Δ ~ ld*A + aΔ~ lQ*φ~ ldvQ'Δ ~ ld*A + aA~ lQ*φ~ lQΔ -1J = A-1J. (1.78) Now we will calculate Q A~ ld*A. Let us apply QΆ~ ld* to the above equation: Propagators for Lattice Gauge Theories. I 31 

aQ'Δ ~ 2Q'*d*φ- ^QΔ ~ 1J = QΔ~ 2d*J. (1.79) We know that the operator Q'Δ~ 2Qf* is positive on the considered subspace. It is easy to see that d*φ~ ίdl is positive also because φ~ l is positive, so φ~ 1 ^ α > 0 and d*φ~ 1dί ^ ud*d 1 = uΔ 0 > 0. Thus we obtain from (1.79) 

QΔ ~ ld*A = (d*φ-γdj- 1 [a~ \QΔ ~ 2Q'*Γ 1Q'Δ ~ 2d*J - d*φ~ lQA "1 J] . (1.80) Substituting it in Eq. (1.78), we obtain finally (1.81) for J satisfying <( 1, J^> — 0. Then the solution A satisfies also < 1, A > = 0. The right-hand side of (1.81) defines the operator G on such functions J. For arbitrary J we take the decomposition J = J' + J 0, J0 constant, J' orthogonal to constant functions, and we put 

GJ = GJ' + a~ lJQ. (1.82) This gives the solution of Eq. (1.73), so G = Δ~ l. To investigate better the operator G we write it in momentum representation : 

+

# Σ[(Σ ί'.vL \ r 

v + n2 '"(»"' + r + ' ' ) 

A2(p' + l') 

Γ (/>' + /'), (1.83) 

for p # 0, λt(!} = ~J,<n, A,V>} = a-' J (0), where 32 T. Balaban 

We will prove that G is a bounded operator by transforming the formula (1.83) in a manner similar to that applied in the formula (1.63) for the operator Hk. Let us notice at first that the function has a limit as pf -> 0, lim ΔQ(p')φ (p') = α, and it is bounded from below and above 

> p'->0

by positve constants independent of fe and depending on d and a only. From this it follows that the function has the same property, hence also its inverse. Now we will analyze separately some groups of terms in (1.83). Let us start with the first two terms: 

# V,         

> •[u(p' +l')υ μ(p' + /') Jμ(p f+ /) -u(p'

0 3 0. (1.87) Owing to the cancellation of the terms with /' = /, the above expression can be extended by continuity to p' = 0. Using all the properties of the functions appearing above, e.g. the inequality (1.36), we can easily prove that this expression defines a bounded operator on L2(T η). It is bounded also when differentiated two times at most. To analyze the third term in (1.83) we will consider the expression in square bracket : 

# g,(p' + J 

V

\u(p' + Π 

Δ\p' + 1") 

u(p' + l)v u(p' + I) 

A(p' + I) (P >

# ' + 0 

# I2Λ(P') l)\ 2Δ0(p') 

Δ(p' + I) Δ(p' +1") 

(1.8 

Again taking into account the cancellation of the terms with /" = / the above expression is well defined by continuity for p' = 0, and we even get an additional factor A0(p r). Because there are two expressions in square brackets in the considered term, we get the additional factor Δ^(p'}. This factor multiplying the function between the square bracket expressions gives an inverse of the expression (1.86) which is also well defined. Thus the third term is well defined by continuity at 

p' = 0 and defines a bounded operator together with its derivatives up to the second Propagators for Lattice Gauge Theories. I 33 

order. It can be easily calculated that the values at p' = 0 agree with the second and third equalities in (1.83). We may conclude the above considerations in the following 

Proposition 1.1. The operator G is a symmetric operator on L 2(T ) and 

|| GJ ||, || VGJ ||, || GV*J ||, ||VGV*J ||, || VVGJ ||, || GV*V*J || ^ γ~ l \\ J ||, (1.89) 

with a positive constant y0 independent ofk, T , and depending on d only (if we put a — 1). This implies the bound from below: Aa = G~ l^y 0(A+I). (1.90) Let us now come back to the integral (1.68) and to a calculation of HkB. It is defined as a minimum of the form ^<Λ AaAy — a(B, By under the conditions 

QA = B, Rd*A = 0. We introduce the function 

h(A 9 ω, λ) = ±(A, Δ aAy + <ω, QA-By + <A, Rd*A) 9 Rλ = λ, (1.91) ω and λ are Lagrange multipliers, and we solve the equations 

δh _

~δA~ « +ΰ ω+ ,

δh δh 

— =QA-B = Q, — = Rd*A = 0. (1.92) 

oω oλ 

We get 

A = - Gβ*ω - Gdλ, Rd*A = - Rd*GQ*ω - Rd*Gdλ = 0. (1.93) Let us calculate the operators Rd*GQ* and Rd*Gd. The operator d*Gβ* acting on a constant configuration gives 0, so we have to calculate it on configurations orthogonal to constant configurations, β* transforms them into configurations on the ^/-lattice and orthogonal to constant configurations. On such configurations G is given by the formula (1.81), and we have d*Gβ* = d*A ~ 1Q* — ad* A ~ 1Q*φ~ 1QA ~ 1β* 

+ [A-1Q'*(Q'Δ-2Q'*Γ l-= A-1Q'*(Q>A-2Q'*Γ 1a~ 1(3*φ-ldlΓld*φ-1. (1.94) The operator R is given by the formula R = I - P = I - A~ ίQf* (QΆ~ 2Qf*)~ l

Q'Δ~ ί, so RΔ~ 1Q'* = Q and we have 

Rd*GQ* = 0, QGdR = 0. (1.95) Calculating d*Gd we get the formula 

d*Gd = I + Δ~^Q* [(Q'Δ -2Q'*Γ 1 a~ \d*φ ~ ^J" 1 (Q'Δ ~ 2Q'*Γ l

-2Q'*Γ i~]Q'Δ-L, (1.96) 34 T. Balaban 

and from this it follows that 

Rd*Gd = d*GdR = R. (1.97) The equalities (1.95), (1.97) imply that the second equation in (1.93) has the form Rλ = λ = 0. Thus we have 

A = - Gβ*ω, (1.98) and the condition Rd*A = 0 is satisfied automatically. We have to satisfy yet the condition QA = B, so we have to investigate the operator βGg*. It is given by the formula 

> 1

φ-i+a-lφ-id1(d*φ-ίdίΓίd*φ-i, (1.99) and can be bounded as follows 

^a~ lL (1.100) The operator a~ i (φ — \)/φ has the momentum representation 

> μ

# (p') Λ ( , } .o(P) 

> 1 10

nj

from which it follows that it is bounded from below and above by positive constants dependent on d only (for a = 1). The same property holds for QGQ*. The condition 

QA = B gives the equation - QGQ*ω = B,-ω = (QGQ*Γ 1B, (1.102) so finally we get the representation 

HkB = GQ*(QGQ*Γ 1B. (1.103) This representation allows us to reduce a proof of properties of Hk to the corres-ponding properties of G. In a similar way we can construct another important operator with the help of G, namely an orthogonal projection in the metric {A, A aAy on the subspace of A

satisfying the conditions QA = 0, Rd*A = 0. This projection can be found as a minimum of the form {A — AQ, Δ a (A — AQ)y on the subspace of AQ satisfying the conditions QA Q = 0, Rd*A Q = 0. We consider the function 

g(A 0, ω, λ) = ^<A Q - A, Δ a(A Q - A)y + <ω, QA oy + U RSM 0>, Rλ = λ, 

(1.104) and the equations 

(U05) Propagators for Lattice Gauge Theories. I 35 

The first equation gives A0 = A - Gβ*ω - Gdλ, and 

Rd*A 0 = Rd*A - Rd*GQ*ω - Rd*Gdλ = Rd*A - λ = 0, so AQ = A — GdRd*A — GQ*ω. The second equation gives 

QA 0 = QA- QGdRd*A - QGQ*ω = QA- QGQ*ω = 0, so we get the following formula for the projection 

A0 = PA = A- GdRd*A - Gβ*(βGβ*)~ *βΛ (1.106) 

or 

P = I - GdRd* - Gβ*(βGβ*Γ *β (1.107) Thus all the important operators we will work with in the future are expressed in terms of the operators Gk and G' k. The operators G' k were investigated in paper [2]. In the next section we will use those results and the methods of that paper to prove the corresponding properties of Gk .

F. Regularity and Decay Properties of G

We want to prove that the operators G fc have properties similar to those of the operators investigated in paper [2]. To formulate them we have to introduce several norms. The most fundamental are the supremum norm 

A =maxsup|A μ (x)|, \VA\ = maxsup|(δ μ Λv )(x)|, (1.108) 

> μ

and the Holder norm 

sup             

> μx,x': \χ —χ' \^ 1
> μ,\ x,x': \χ —x'\ 1Ξ

x — x , \ ( d μ A v ) ( x ) - ( d μ A v ) ( x ' ) \ . 

(1.109) Besides these we use also L 2-norms. To describe decay properties we use two families of cubes, both parametrized by points of the unit lattice T(£\ Cubes Δ(y) are simply unit cubes of Tη, or A(y) = B\y\ ye T (£\ Cubes 2(y} are sums of 2 d unit cubes having the point y as a corner, thus they are cubes of size 2 and with a center at y. 

Let us omit the indices k and η in the following. We can formulate the basic result of this section. 

Proposition 1.2. There exists a positive constant δQ depending on d only, such that 

- y / « | J | (1.110) 

for xeΔ(y\ supp J c Δ(y'\ with the constant 0(1) depending on d only, 

||CVGJ|| α , ||CGV*J|| α ^θ(l)^^-^'(||C|| α + | C | ) J| ( l . l i i ) 

for 0 rg α < 1, ζeC™(Δ(y)) 9 supp J c: Δ(y'\ with the constant O(l) depending on d 36 T. Balaban 

and α(O(l) -» oo ι/α -> 1), |(VGV*J)(x)|^0(l)β-^-^(||J|| e + | j | ) (1.112) 

for 0 < ε < 1, xeΔ(y\ supp J c zϊ(/), with the constant 0(1) depending on d and ε(0(1) -> oo jfβ -><)), /or 0 ^ α < l , ε > 0 , α + ε < l , CeC^(zϊ(j;)), supp J c zί(j/), wzί/z fλe constant 0(1) 

depending on d, α fl«d ε(O(l) -> oo z/α -» 1 or ε -> 0). 

Finally there exists a constant 0(1) SMC/Z that 

## || CGJ II, II ζVGJ II, II CGV*J II, II CVGV*J II, II CVVGJ II, 

l (1.114) 

for supp ζ <=. Δ(y\ supp J

Let us remark that in the inequalities (1.112), (1.113) the choice of derivatives VGV* is accidental; we can take arbitrary derivatives, like d μGδ v, <3*Gd v, d*Gd*. The localized inequalities (1.110)-(1.114) imply immediately the following global inequalities |GJ|,|VGJ|,|GV*J|,|zlGJ|, ||VGJ|| α , ||GV*/|| α ^ 0(1)|J|, (1.115) VGV*J ^0(l)(||J|| ε + |j|), (1.116) 

||VGV*J|| α ^0(l)(||J|| α + ε + |J|), (1.117) 

and (1.89), with the same dependence of the constants 0(1). A proof of Proposition 1.2 will be given in several steps. In the first step we will show that the inequalities (1.115)-(1.117), (1.89) imply the proposition. Probably the simplest proof of the exponential decay properties can be obtained by relating G on the torus to G on the whole lattice ηZ d in the usual way, and then proving that the operator e~ <q 'xy A ae<q 'xy — Aa is a small perturbation of Δa for vectors 

qeR d sufficiently small. Instead we construct a random walk representation of the kind described in [2]. Such representations will be our basic tool in investigation of more complicated operators. We consider the lattice of cubes of size M 0, M 0 =Lm°, defined by the lattice T(^m°\ and cubes Π z of size 2M 0 and with a center at the point ze T^ m°\ These cubes cover the lattice T . We construct a partition of unity taking the functions 

h(t) = 1 for te [ — ^, ^], h is chosen in such a way that 

Σh 2(t-n)=l, hence £/z z 2 (x)=l. (1.118)  

> «z

We define an operator C 0 by the formula Propagators for Lattice Gauge Theories. I 37 

We will prove that C 0 is a good approximation of G. We will be very sketchy with arguments because they are almost the same as in [2]. At first we calculate 

Ah A. We have 

(ΔhA) μ(x)=h(x)(ΔA μ)(x)- Σ

> best(x)

(QhA)(y) = μ

Σ l" Σ 

> eB k(y) xιe[x,x

= <QhA μ - S(dh)A μ,

so 

β*/zω μ = Λβ* ωίi - S*(dh)ω μ,

and 

β*βAX μ = Q*hQA μ + Q*S(dh)A μ = hQ*QA μ - S*(dh)QA μ + Q*S(dh)A μ,(dPd*hA(x) = Σ 1d(dPd*) v(x, x')h(x')A v(x') = h(x)(dPd*A\(x)- Σ ηd(dh)(Γ XtX ,)(dPd*) μv (x,x')A v(x') = h(x)(dPd*A) μ(x} - (Ptfh)A\(x). (1.120) These equalities imply 

ΔhA = (Δ~ dPd* + aQ*Q)hA = hΔ aA ~ Σ (dh)(b)(dA)(b) - (Δh)A + S*(dh)QA - Q*S(dh)A + P^ 

> L&esί( )

= hΔ aA-K(h)A 9 (1.121) 

hz = I-R, (1.122) and we get the desired representation V A GA K(A )GA ..... h K(h )Gh , (1.123) ί—t ωo ωo v ωι y α>ι ω n - ι v ωn^ ωn ' ^ '

> ω = (ωo>ωι,...,ω n)

where the summation is over all finite sequences ω with ω.e T(^+m °\ Of course the sum is convergent only if R is small in a proper sense. This holds if M 0 is sufficiently large. For example let us prove the inequality (1.113) assuming the inequalities 38 T. Balaban 

(1.115)-(1.117). Let us consider (VGV*J. We represent G by the sum in (1.123) and we estimate the norm || £VGV* J \\ a by the sum of norms. To estimate terms in this sum we have to understand properties of factors in each term. There are two types of factors, with the operator G and with the operator K(h). The factors with G are estimated by using (1.115). For the first factor we have Next we have to estimate \h z K(h z )A \. The operator K(h) is a simple, shortranged, first order differential operator, except the term P^dhJ. Let us write bounds for theoperator <9P<3*. They follow from the representation P = G'Q f*(Q'G f2 Q'*)~ lQG, 

from Lemma 2.4 of [2], and the representation (1.45) and the analyticity method of proving an exponential decay (see the proof of Lemma 2.4 in [2] ). We obtain 

> χ

-χ\ (1.126) 

\(dPd*) μtV (x 9 x") - (dPd*) μtV (x' 9 x")\ ^ 0(l)e-δ'^-χ"\ 

f o r x , x ; ' : | x - x ' | ^ l , α < 1. (1.127) The constant 0(1) in (1.126) depends on d only, and in (1.127) it depends on α also (O(l)-» oo if α -> 1). This implies a bound on the operator hzK(h z ). We have to consider separately the cases when Πz , D Z2 are disjoint, and when they are overlapping. In the first case we have only the operator hz^P l(dh z^} and (1.126) gives a bound with a small factor O(M^ 1) and the exponential factor 

exp(-±δ' Q z1 -z ? |)-exp(-^ / 0 M0 |z / 1 - z' 2\\ where z' vz' 2 are points z 1 ? z 2

rescaled to the unit scale, i.e., z\ , z' 2e T (1/c+mo) . In the second case we have the small factor 0(M~ l) only, but we may include the factor exp( — \z\ — z' 2 |) because 

\z\ — z2 1 ^ 2d. Defining 2δ Q = mm {^δ' G, M' 1}, we obtain 

+ \ A \ ) . (1.128) The last factor in each term is estimated by using (1.1 15), (1.1 16) (1.129) There is one possibility left yet, namely that of the terms with one factor. Then we apply the inequality (1.117) together with ( 1 . 1 1 5), ( 1 . 1 1 6) and we get 

# (1.130) 

Gathering together all these estimates we obtain 

# II CVGV*J || β 5Ξ o(i)( || clL + 1 c I ) Σ o(i) 2"M 0- α,=(ωo>ωι ,... J; eDωo ,yeDω         

> n = 0
> .g-2<5o|cΰ 0-coι| ..... e~2δ 0\ω n_1- ω n\/ II j II _j_ I j| \

# -^(\\ζl+ C|)(||J|U. + |J|) 

0(\) 2n M~ n( Σ e -a oMowV (1.131)   

> \XeZ dJPropagators for Lattice Gauge Theories. I 39

Let us notice that the constant O(l) under the sum above is an absolute constant depending on d only, hence we can fix M 0 depending on d only, such that the series is convergent. This M 0 is approximately equal to the norm 0(1) in the inequalities (1.115), (1.128), thus the exponential decay we get is practically the same as in the first mentioned method. The proofs of the other inequalities are exactly the same, but in the estimates of GV*J we have to take a representation of G adjoint to (1.123), with the operators 

K(h) acting on the right. Thus we have to prove inequalities (1.115)-(1.117). Let us notice that the proof of inequalities (1.114), describing the decay in L 2-norms, is completed because we have proved inequalities (1.89). This may serve as a basis of another proof of the exponential decay properties. This proof, and also a proof of (1.115)-( 1.117), makes use of the identity G - G0 + G0dPd*G, (1.132) where G 0 = (A +aQ*Q)~ 1. This operator is similar to G', but with the different averaging operator. We will prove (1.115)-( 1.117), and in fact the whole Proposition 1.2, for the operator G 0 . This together with the properties (1.126), (1.127) of dPd* 

and (1.89), or (1.114) for the operator G implies immediately (1.115)-(1.117), or Proposition 1.2 for G. Properties of the operator G0 can be easily reduced to the corresponding properties of the operator G' by the equality G0 = G' + G'(a kQ'*Q' - aQ*Q)G 0. (1.133) We only have to know some weak bounds for G 0, for example bounds in the L2-norm (1.89), or (1.114). This operator is given by the formula G0J = A~ 1J -aA~ lQ*φ~ lQA-lJ (1.134) for J orthogonal to constant functions, and G 0J = a~ 1J for J constant, hence by the first two terms in the representation (1.81). Thus its momentum representation is given by (1.87) and we have Proposition 1.1 for G 0 . This leads also to (1.114) by the same reasoning with a random walk expansion as for G. In paper [2] we have proved all the necessary properties of G', except the second order inequalities (1.112), (1.113). Let us prove for example (1.112). We use Lemma 2.4 of that paper and the equality (2.34) with Π replaced by the whole torus. Let us write this equality again,    

> / c - l
> G' k= C (0) '^ + £ a2.(Uη}-*GJQ*C (^LJ «Q f.GJ, (1.135)
> 7 = 1

where we have written explicitly indices and scales. We have   

> x—x\

40 T. Balaban 

*? Σ

(1.136) and applying the estimates (2.35)-(2.37) of Lemma 2.4 in [2] we obtain for xe3(y), 

supp/ c J(/) 

> (L137)

i.e., the inequality (1.112) with δ0 = 2<5' 0 The proof of (1.113) is similar. Thus we have finished the proof of Proposition 1.2. 

References 

1. Balaban, T.: (Higgs) 2 3 quantum fields in a finite volume. I. A lower bound. Commun. Math. Phys. 85, 603-636 (1982), and references therein 2. Balaban, T. : Regularity and decay of lattice Green's functions. Commun. Math. Phys. 89, 571-597 (1983) 3. Balaban, T. : Renormalization group methods in non-Abelian gauge theories. Harvard preprint HUTMPB134 4. Brydges, D. C., Federbush, P. : A lower bound for the mass of a random Gaussian lattice. Commun. Math. Phys. 62, 79-82 (1978) 5. Brydges, D. C., Frόhlich, J., Seiler, E. : On the construction of quantized gauge fields. I. General results. Ann. Phys. 121, 227-284 (1979) 6. Brydges, D. C., Frόhlich, J., Seiler, E. : Construction of quantised gauge fields. II. Convergence of the lattice approximation. Commun. Math. Phys. 71, 159-205 (1980). 7. Wilson, K. G., Bell, T. L. : Finite-lattice approximations to renormalization groups. Phys. Rev. 

Bll, 3431-3445 (1975) 8. Wilson, K. G. : Quantum chromodynamics on a lattice. In: Quantum Field Theory and Statistical Mechanics, Cargese 1976, M. Levy and P. Mitter (eds.). New York: Plenom Press, 1977, pp. 143-172 Communicated by A. Jaffe Received November 21, 1983; in revised form April 2, 1984
