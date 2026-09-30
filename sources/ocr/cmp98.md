Title: 1103942283.pdf

URL Source: http://projecteuclid.org/journals/communications-in-mathematical-physics/volume-98/issue-1/Averaging-operations-for-lattice-gauge-theories/cmp/1103942283.pdf

Number of Pages: 36

Markdown Content:
Communications in  

> Commun. Math. Phys. 98, 17-51 (1985) Mathematical

## Physics 

> © Springer-Verlag 1985

# Averaging Operations for Lattice Gauge Theories* 

T. Bafaban 

> Department of Physics, Harvard University, Cambridge, MA 02138, USA

Abstract. Usually renormalization group transformations are defined by some averaging operations. In this paper we study such operations for lattice gauge fields and for gauge transformations. We are interested especially in character-izing some classes of field configurations on which the averaging operations are regular (e.g., analytic). These results will be used in subsequent papers on the renormalization group method in lattice gauge theories. 

Introduction 

In Wilson's approach to renormalization group transformations [9,10] for lattice gauge systems, it is necessary to define an operation of taking an average of field configurations over subdomains of a lattice. These subdomains are usually some simple subsets, for example cubes of a fixed size, or sums of several such cubes. In this paper we will study one such definition of an averaging operation. This operation will be used in other papers on gauge field theories. Let us introduce some definitions and notations. We will be very sketchy because these definitions have already appeared several times in the earlier papers [1, 2] of the author and we refer the reader to these papers, especially to [2], for more detailed explanations. We consider a subdomain Ω of the lattice ηZ d with alattice spacing η. A sequence of sets Ω{j) is defined as the intersections 

ΩU) = ΩnL jηZ d, (1) where L is a fixed integer, L > 1. For a point y e UηZ d (or any lattice δZ d), we define a block of an order j as the cube 

B\y) = {xeL-JL"ηZ d:y μ^x μ<y μ + L%μ=l,...,d} (2) (or the corresponding cube with Πη replaced by δ). We will omit the subscript; if 

j= 1. For a subset ΛcL nηZ d (or CδZ d), we define 

B\Λ)= U B^QL-^ηZ 0 (or CL-JδZ"). (3)    

> yeΛ
> Research supported in part by the National Science Foundation under Grant PHY-82-03669 18 T. Baϊaban

We assume that 

Bj(Ω U) ) = Ω for 7=1,..., k (4) for some k. In fact, we will assume that η = L~ k. Thus Ω is a sum of blocks of the order k. 

Besides the blocks of different orders, there are two other geometric objects important for us. Bonds of the lattice Ω are ordered pairs <x, x'> of nearest neighbor points x, x' of Ω. We identify them with the corresponding oriented intervals with endpoints x, x'. We will denote them also by the letters b, b\ c, etc. For example, b denotes a bond (b_, b + } with an initial point b_ and a final point 

b+; fc_, b+ are nearest neighbors. Plaquettes are oriented elementary squares of the lattice Ω and are denoted by p, p\ etc. A boundary of a plaquette p is a sum of four bonds, and an orientation of the plaquette may be indicated by an orientation of the bonds. A plaquette p may be identified also with an ordered quadruple <x, y, z, w> of corners x, y, z, w of the elementary square p; the ordering indicates the orientations of bonds <x, y}, <j, z>, <z, vv>, <w, x> forming the boundary dp. 

Speaking precisely, the symbol <x, y, z, vv> indicates not only the oriented square, but also the initial point x of its boundary. In this paper we will consider positively oriented plaquettes and such a plaquette p C Ω is represented as 

p = (x,x + ηe μ,x + ηe μ + ηe v,x + ηe v}, μ<v. (5) The above definitions of bonds and plaquettes may be applied to an arbitrary lattice, e.g., to Ωu\

Gauge field configurations U are defined on a set of bonds in Ω, and with values in a Lie subgroup G of a unitary group U(N). A value of U at a bond b = <x, x'> is denoted by (6) and we assume that U satisfies the condition t/(χ, xθ = [/" V , x) - U*(x\ x). (7) In the sequel, we will consider quantities which are invariant with respect to some important transformations in the space of gauge field configurations, the so-called gauge transformations. They are determined by gauge functions u:Ω-+G, and are given by 

Uu(x, xθ - u(x) U(x, xθ M" V ) , O ? O C Ω. (8) 

> w - l

# (J l

For an oriented contour Γ = (J <x ί ? xί + 1 > we define  

> i
> ^ + i ) , (9)
> ί = 0

where the order of factors in the product is the same as the order of bonds in Γ. This definition will be applied also to contours on arbitrary lattices. For a plaquette p = <x, y, z, w> we define dp as the oriented contour δp = <x, y>u<y, z>u<z, w> u<w,x>, and U(dp) is defined by (9). Averaging Operations for Lattice Gauge Theories 19 

The renormalization group transformations are integral operators transform-ing functions defined on gauge field configurations on a lattice, into functions defined on configurations on the lattice of blocks. We will consider transform-ations of the form 

ρ\V)=idUδ(VU-1)ρ(U) 9 (10) where, for example, U is a gauge field configuration on the lattice Ωij \ V is a configuration on the lattice Ωu+1) and dU is a product of Haar measures of the group G. The most important part of the above definition is an averaging operation Ό. It transforms a configuration U defined on Ω{j) into a configuration Ό

defined on Ωu+ υ . In fact, Ωω may be replaced by any other lattice. We will demand that this averaging operation has to satisfy some important and natural conditions. A first condition is connected with the fact that we consider gauge-invariant quantities, so we demand that the averaging preserves gauge transfor-mations, i.e., 

U~ U')u-1(y'), or Ό* = (ϋ)\ (11) This property implies that the renormalization transformation (10) transforms gauge-invariant functions ρ into gauge-invariant ρ'. Indeed, if v is a gauge function on a new lattice, then 

ρ'(V ϋ) = \dUδ{V vΌ-1)ρ{U)= ί dUδ(V Ό(U s)-1)ρ(U u)

(12) where we have used the gauge-invariance of the Haar measure dU and the function ρ, besides the condition (11). Now if we choose u coinciding with v at points of the new lattice, then we get 

ρ'(V). (13) We have used also the invariance of the ^-function concentrated at the identity of the group G with respect to transformations U^vUv^ 1. A second condition on averages Ό is formulated in the following way. We consider configurations U with values in a small neighborhood of the identity of G, hence U = e iA and A is a Lie algebra valued configuration with values in a small neighborhood of 0. For such configurations we demand that τlogf7 is well approximated by the linear averaging operation (1.8) defined in [2]. Let us write this operation 

J iU + )). (14) 

> xefl(c-)

We refer the reader to paper [2] for explanations of symbols used above. Let us notice that Γ c_)Jc u[x,x(c)]uΓ x(c))C+ is an oriented contour with c_ as an initial point and c+ as a final point. We denote it by Γc x.

There are many ways of implementing these two conditions. We will write now a definition of an average which satisfies these conditions and which has some other advantages. We define 

# ^ ] ^ ) (15) 20 T. Balaban 

It is easy to see that taking U = e ιA with A small and expanding the logarithm of the expression on the right-hand side above in powers of A, we get the expression (14) as a linear term in the expansion. In this paper we will study properties of this and other averaging operations, and especially their compositions. In the future we will need many properties of these compositions. For example, it will be necessary to know that a composition of many averaging operations applied to a regular or small gauge field configuration gives a regular or small configuration also, the notions of regularity or smallness being related to scales on which the gauge field configurations are considered. This is the basic property of averagings we would like to understand. Another important property is an analyticity of a result of the averaging operation with respect to an averaged field. The analysis and the propositions we prove in this paper can be easily extended to other definitions of averaging operations satisfying the requirements postulated in this introduction. The definitions we have used in this paper were chosen for their simplicity but in some future papers we will need somewhat more complicated definitions. We will discuss them at the proper time when they appear. 

A. Norms, Important Inequalities, and Functions 

We consider a Lie subgroup G of a unitary group U(JV). Its Lie algebra g is a subalgebra of the algebra of hermitian matrices. Because of analyticity properties we are looking for, we will consider complexified algebras and groups. The complexification of the algebra of hermitian matrices is the algebra of all complex 

NxN matrices, and the complexification of U(iV) is the general linear complex group GL(C,JV). The complexification g c is a subalgebra of the algebra of all complex matrices. It may be defined in the following way: we take a basis {t a} of the algebra g, then all elements A e g can be written as linear combinations A — Σ A ata, where Aa are 

> a

arbitrary real numbers, Aa e R, and we form a complexification g c taking Aa as arbitrary complex numbers, Aa e <C. It is easy to see that this complexification is independent of any particular basis {t a} chosen in the above definition. For a function F(A) defined on the complexified algebra, a notion of analyticity is well defined and means analyticity with respect to complex variables Aa. The unitary group U(JV) can be obtained by an application of the exponential mapping to the algebra of hermitian matrices. This exponential mapping is simply given by the exponential function eίΛ , where        

> oo vn
> ex=QχVX= Σ- Γ
> n= o nl

is defined for an arbitrary matrix X. The group G is obtained by applying the function eiA to A e g, and the complexified group Gc may be defined as an image of the exponential function applied to the complexified algebra g c. Of course, Gc is a subgroup of GL(C, N). We will need only a neighborhood of G in this subgroup. We introduce a scalar product in the algebra of all complex matrices Averaging Operations for Lattice Gauge Theories 21 

and a scalar product in spaces of matrix valued functions defined on subsets ΩCηZ dd , (18) 

> xeΩ

similarly for functions defined at bonds or plaquettes of Ω. The scalar products define the corresponding norms. They are L2 norms and are denoted by || ||, e.g., for a matrix X the norm is given by ||X|| 2 = trX*X. The IF norms, 1 ^ p ^ oo, are defined in an obvious way. In estimates we will use much more frequently another norm for matrices. It is the operator norm given by 

\X\ = sup \X\p\ = sup \φ Xψ\ , φ, ψ e C N ,

\φ\ = \ψ\ = l,\ψ\ 2= Σ J ψ / (19) 

We have the following inequalities for the norms introduced: 

(20) 

> \XY\^\X\\Y\ 9\\XY\\^\\X\\\\Y\\.

Now we will introduce several important functions on the matrix algebra. The first is a logarithmic function. It is an inverse to the exponential function and for matrices X satisfying \X — 11 < 1 it is given by  

> 1 V * + 1

(21) Of course, both functions are analytic functions of complex matrices X. For any branch logz of the ordinary logarithmic function, we may define logX for X

> r

defining a normal operator on <C N. If X is such a matrix, then X = Σ zjPp zje ^> 

{Pj} is a spectral family of orthogonal projections (i.e., Pf = P p PjPk = P kPj

= δjk Pj), and we define 

logX = Σ^ogZjPj. (22) We will use this definition for logz = log \z\ + i argz, where argz e ] — π, π], and for unitary matrices. Every unitary matrix U can be represented uniquely in the form 

> r

U = Σ eiλj Pp where the numbers λ} are different and satisfy λj e ] - π, π], and then 

> 7 = 1

we define r

A is a hermitian matrix, follow: — 1 | = m a x 1 

> j

| ^ π . From this definition the following inequalities —11= m a x sin-r 

^ f | ί / - l | , because 

2sinx 

x

^ - for xe[-f,f]. 

π

(24) (25) 22 T. Bataban 

We will need also inequalities of this type for arbitrary complex matrices X

instead of U. For matrices X satisfying \X— 1 | ^ , we have      

> —X,-\X — L \=-i —7T? —7T=2A — 1 , (26)
> n=in 1 - | X - 1 |

\χ - 11 = \e lo *x -1\S e{logX{ - 1 S ellogX{ |logX| ^ 2 | l o g X | . (27) Let us consider now the most important function for all future considerations, the function describing the group multiplication in terms of Lie algebra elements. Let us define 

Z(u,v) = \oge uX evY . (28) It is a well-defined and analytic function of uX, vY, for example, in the domain  

> | M X | < | ,

|ι>Y|<£. Its power series expansion is given by the Baker-Campbell-Haussdorf formula (see [7], Sect. 2.15) 

## Z = logΛ y= £ Σ ^ ^ 1 

> 1

Y

(29) where ad^7= [X, Y~\ = XY— YX, and the series is convergent in a neighborhood of 0: \X\, \Y\^c 0 for some positive c 0. From the structure of this power series expansion, we get easily the bound |2 ), (30) and this implies 

\Z-X-Y\^2\X\\Y\ for \X\,\Y\^ Cl , (31) where c1 is a sufficiently small positive constant, cί^c 0. We will treat the expression ad x Y for a fixed X as a linear operator on a space of matrices Y, and we will consider functions of this operator /(ad x ). For analytic functions / defined in a neighborhood of 0 and for X with a sufficiently small norm, the function /(ad x )can be defined by the power series expansion. We will be interested in calculating derivatives of the function Z(w, v) and some other functions of this type. Let us start with the following basic formula (see [7, Theorem 2.14.3])  

> Ai)Ait)

# J fe ^ά)nA\) ^ά ))A\t) , (32) 

where Λ(t) is a differentiable matrix-valued function of t. The function g(z) defined by the above formula is an entire function given by Averaging Operations for Lattice Gauge Theories 23 

hence the function g~ 1(z) = —— is an analytic function in a neighborhood of 0, more exactly for z + 2kπί, fc=± 1, ± 2 , . . . , and we have the identities 

g~\z)=-^-[9 g-1(-z) = g-1(z)-z 9g-1(z)=l+±z+.... (34) Defining f(z) = g~ 1(z) — \z, we have / ( — z)=f(z), so 

## /oo=i+ Σ fc 2^, fl f-i(^)=/ω+^ff" 1(-^)=/ω-έ^. (35) 

> P = l

Using (32) we can derive easily the following formulas: 

## ^ =g-K-*L^x, d~ψ±=g-K«^JY. (36) 

We apply them to derive the second-order Taylor expansion of Z(w, v) with respect to the variable w, for example:   

> (7W oOU

(37) 

> ϋ

) = ί ; 7 , - ^ ) = δ r - 1 ( - a d ι , r ) X = ί 7 - 1 ( - ! ; a d r ) X . From this we get 

\loge ix eiγ =Y + g-1(-iSid γ)X + &r(X;Y) 9

| ^ ( X ; 7 ) | ^ 0 ( l ) | X | 2 ( 3 8 )

for \X\, \Y\ sufficiently small, where 0(1) is an absolute constant [e.g., we can take 0(1) = 24 for |X|:g 2Ό, | Γ | ^ χ £ | . Another important function we will need later is (39) Repeating the above calculations, we get 

> 1

Z(u) = ug( — 2iά γ)X + u 2\ dt(\ —ϊ)Z"(tύ), (40) oand      

> l.γ+. γ _.y

— \ o g e e —g{ — idiάγ)X + O{\X\). (41) 

i

B. Compositions of Averaging Operations 

Let us recall the basic definitions. Let U be a gauge field configuration with values in U(ΛΓ). The one-step averaging operation is defined by 

|i Σ L-d-\ogU(Γ cJU(c)-ι\    

> LxeB(c-) IJ
> c

= exp|i Σ L-d-\ogU(Γ cJU(c)-ι\U(c\cC& ι\ (42) 

L I J24 T. Balaban 

and if fe th order averaging Uk is defined at bonds of Ω{k \ then 

> xeB(c-)

where the contours Γc x are defined on the lattice Ω(k) .

Let us notice that this definition is local in the sense that Uk, c C Ω{k \ depends only on the bond variables Ub for b C Bk(c^)uB k(c+). This property will play a very important role in the future. Let us notice also that the property (11) is satisfied. Indeed, for an arbitrary gauge field configuration U and a gauge transformation u, 

we have U\Γ c%x )U\c)' 1=u{cJ)U{Γ Ct ^U{cY ιu^\cJ)\ thus the matrices 

U\Γ C x) JJ u{cY ι and U(Γ C x) U{c)~ ι are unitarily equivalent, their eigenvalues are equal, and by the definition (22) their logarithms are unitarily equivalent with the same unitary operator u(c_). Then from (42) we get (ΪF) c = w(c_)0 \u~ ι {c +). Now we would like to understand how regular the configuration Ό is, assuming some regularity of U. We will investigate carefully the one-step averaging operation from this point of view. We assume that a configuration V

defined on a unit lattice Ω' satisfies l | < α 0 , pCΩ', (44) and α 0 sufficiently small. We would like to get optimal bounds for \V(dp')- 1|, pf

Let us denote by y the upper right corner of the plaquette /?' and let us introduce locally the axial gauge with the initial point y. This means that we take the contours for x in some neighborhood of y containing 2d blocks having the point y as one of the corners, and we make a gauge transformation υ0 such that the gauge transformed configuration VO = V V° satisfies the conditions V0(Γ yx ) = l. Such a gauge transformation can be easily found because Vo(Γ ytX ) = VVo (Γ yiX ) 

> =v

o(y)V(Γ ytX )vό *0*0=1 implies vo(x) = v o(y)V(Γ ytX ); thus v0 is determined uniquely if vo(y) is given. Of course, we have 1|. (45) 

< Pr-

V0(Γ y x)=l imply V0(x,x + e 1)= 1, \V 0(x,x + e2)-l\<\x i-y 1\(x 0,\V( ) l | ( | lAveraging Operations for Lattice Gauge Theories 25 

+ \x μ _1 — y μ _! I) α 0, μ = 2,..., d, for x in the neighborhood of y. If we denote (46) then for bcAij)') we have |F O ί ,—l|<|fo_ — y | α o ^ ^ L α o , hence V0J} = e ιAb and |^4 fc | < 2 |b_ — y\ α0 ^ 2dLoc o. For c C δ//, the contours Γc x are contained in A(p') and we have 

> bCΓ CjX

\V 0(Γ cJ-\-iA(Γ cJ\Si(\A\(Γ cJ) 2<0(l)(L 2a0)2

so using the definition (21) of the logarithmic function, we have 1 <O(l)(L 2 α0 )2

for L 2α0 sufficiently small. From this and (31) we get 

\i Σ L

= expΓί Σ L 

> [_ xeB(c-)

hence         

> V—1 — f V)
> v0,c Lιί—i 1

Now we can estimate |F 0(δ//)— 1| We have o ( d j θ - l - i Σ Σ J 

> cCδp' xeB(c-)

<0(l)(L 2 α0 )2 .<0(l)(L 2 α0 )2 . (47) Denoting by (p') x a plaquette obtained by translation of the plaquette p' to the point x, we have the identity 

Σ Σ L-Ά(r ej= Σ L-"A(d(p%)  

> cCdp' xeB(c-) xeB(y 0)

= Σ IT" Σ >4(δp). (48)  

> XEB(yo) pC(p')x

Further, we have for pCΛ(p r)\V 0(dp)- 1 - W(3p)| <λ2(\A\(dp)) 2 <i(8dLα 0)2 = O(l)L 2α2. (49) Gathering together the above three inequalities, we obtain Σ IT* Σ \A(dp)\ + 0(l)(L 2oc 0)2 

> xeB(y 0)pC(p') x

Σ L~ d Σ | F 0 ( a P ) - l | + 0(l)(L 2 α0 )2 

> xeB(y 0)pC(p') x

α0 + 0(l)(L 2 α0 )2 . (50) This is the estimate we are looking for. Let us notice that it is a local result; the bound above depends on bounds for V(dp)—l on A(p r), i.e., for pCA(p'). We formulate the results in the following: 26 T. Bafeban 

Proposition 1. There exist positive constants Co , c2 such that for every configuration V satisfying (44) for pCΔ(p f) and for oc 0^c 2, we have 

L 2 α 0 ) 2 . (51) 

The constant C o depends on d and c 2 depends on d and L. 

Now it becomes obvious what assumption we have to make for a configuration 

U in order to get a bound on U\dp) - 1, p C Ω(k) . Each averaging operation rescales a bound on plaquette variables approximately by the factor L 2, hence k operations by the factor L2k . To get some small number yet, we have to assume that | l / ( 3 p ) - l | < α ( Λ 2 , η = L' k (52) on some set of plaquettes. If oc 0^c 2, then by the above Proposition, \Ό{dp /)— 1| < L2a0η2 + Co(L 20ί oη2). We take k ^ 1 so α ? L V + Co(oι oL2η2)2 <; α? + C oαg and we assume further that α 0 + Coal ^ c2. Applying the Proposition again, we get for p" 

I Ό2{df) -11 < α o l V + C0L2(L 2(x 0η2)2 + C0 (α 0 L4 ^2 + C0L2(L 2a0η2)2) 

> o

( o n ) IT 2 [ o o 7 ( 0 ^ ) ] ^ α 0 L V + C0(a 0Uη 2)2 [1 + L" 2 (1 + C 0 α 0 ) 2 ] . We make the following inductive assumption for j^k\ 

I ϋ\dp) - 11 < α 0 L2 V + C 0 ( α 0 L 2 ^ 2 ) 2

> o)

2O - D ] . (53) 

The right-hand side can be bounded by α 0 + Coal2 if L~ 2 (l + C 0 α 0 ) 2 < \. The last inequality holds if, e.g., C0oc 0Sh a n d then α o + C o αo2<2α o . We assume further that 2α o ^C2. Then fory</c, we can apply Proposition 1 to the configuration Uj

and we get for pQΩ u+1) 

+ C 0 ( α 0 L 2 ^ 1 V + C 0 L2 (α 0 L2 V ) 2 [1 + ] ) 2

Thus the inequality (53) is proved for all ^fc. Taking j = k, we get 

Proposition 2. 7/ [7 satisfies (52) vWί/z α 0 ^ c 2 = min < —— ,~c 2f, then 

(3C 0 2 J

-11 < α 0 + 2C 0 α2 < 2α 0 , p C &k) . (54) The result is local in the sense that if p = <x, y, z, w>, then it is enough to assume 

(52) for pCB\x)uB k(y)uB k(z)uB k(w). 

C. Other Averaging Operations 

In future analysis of variational problems we will have a situation, where the averaging operation will be composed with a change of gauge conditions, i.e., with Averaging Operations for Lattice Gauge Theories 27 

a gauge transformation. Let us recall that if we apply a gauge transformation v to aconfiguration V,V£ = υ{b_)V hv~\b+\bcΩ\ then(F) c = ϋ(c_)^~ 1 (c+),cCΩ / ( 1 ) .We will consider gauge field configurations V of the form V= V'V 0, where Vo is afixed configuration and F' may have values in the complexified group G c. We find easily that if we apply a gauge transformation v to V and we write Vv = F / y F0 , then  

> +

) = K6-)n /«o.^" 1(fe +)9 (55) 

where for arbitrary invertible matrix X the operator R(X) is given by the formula 

R(X)Y=XYX~ 1. (56) 

R(X) acts on the algebra of all matrices and has the following properties: 

R(X)f(Y) = f(R(X)Y) for analytic functions /, 

R(Xy 1=R(X~ 1)9 (57) In a one-step renormalization transformation we consider configurations V

satisfying axial gauge conditions in blocks: 

(R 0,yV')(Γ yJ= Π R(V 0(Γ ytb _))Vi;=l,xεB(y),xΦy. (58) 

> bCΓy^x

It will be convenient to change this gauge into another one. We apply a gauge transformation v~ 1 to V and we get a configuration Vu thus      

> V'=Vf and VC= (VΎ O)C= (V^V O)C=

We will consider this average for configurations V and V1 with values close to 1 and we will be interested in the expression ). (59) The gauge conditions (58) written in terms of the configurations Vx and v have the form and they imply 

(R 0,yv) (x) = v(y) (Λ Ofy ^i) (/\,*), x eB(y), x + y, y e Ω^ . (60) To determine the configuration v uniquely, we will impose on it an additional condition at each block. To find a form of this condition, let us recall the simplest case of one vector field considered in paper [1]. To change a gauge, we make a gauge transformation λ

satisfying {Q'λ) (y) = Σ L~ dλ(x) = 0. Such a transformation does not change the 

> xeB(y)

average given by (1.11) in [2], and this is very important because the explicit representations of propagators, and other formulas, hold for this specific form of the averaging operation. In the considered general case, we will also try tofindthe additional condition on gauge transformation requiring that the form of the 28 T. Baίaban 

averaging operation should be preserved. We will be able to obtain only an approximate invariance. Because of the axial gauge conditions (58), the average 

(7%) c depends on (K 0 ,c_n([*,*(c)])= Π Λ(7 0(Γ c_iX u[x,fc-]))7 6', 

> bC[x,x(c)]

xeβ(c_), and a good approximation of the function -log(VΎ 0)c(V 0)~* for 

V' = e iA , A small, is given by (Q 0A)(c)= Σ L~ d(Ro c >4)([x,x(c)]), where 

> xeB(c-)

ROtC _ A is defined as Ro C _V\ only the product over b is replaced by the sum. If we make a small gauge transformation v = e iλ , then a good approximation of this transformation acting on Lie algebra variables A is given by Ab = A b — (R Ob λ(b +)— λ(b_)) = A b — (D Vo λ) (b). Under such a transformation the average Q0A changes as follows: 

(Q 0Aλ)(c)= Σ L-d(R 0,c_λ)(x) + (Q 0A)(c) 

> xeB(c -)

- Σ L-\R 0,c_λ){x').   

> x'eB(c +)

If we define (Q' oλ) (y) = Σ L~ d(R 0 λ) (x), then the first term in the right-hand 

> xeB(y)

side above is equal to (Q' oλ) (c_). There are troubles with the second term because  

> x'eB{c + ) x'eB{c + )

= Σ L-dR(V 0(Γ c,M-c)))R(V 0(c))(R Q,c+ λ)(x'),   

> x'eB(c +)

and this expression is only approximately equal to R(V o(c))(Q' ol)(c +), because 

VO(Γ C>x u( — c)) are close to 1 for Vo regular, but not necessarily equal to 1. Now if we assume that λ satisfies the conditions QΌλ = O, then the form of Q0A is approximately preserved under such a gauge transformation. Finally, these conditions are approximations for λ small to the conditions 

# l ^ H ) ^ ) w l 1 (61) 

We assume that the gauge transformation v we have applied to the configuration 

V satisfies these conditions. The equality (60) and the condition (61) imply and (62)    

> |_ xeB{y) IJ

Thus the gauge transformation v is determined uniquely by the gauge conditions (58) and conditions (61). It is a function of the gauge transformed configuration Vλ.

From (59) and (62) we get 

- i Σ

> xeB(c-)

Σ L-4log(Ro.c + ^i)(^ + i X ol- (63)     

> x'eB(c +)IJ

Averaging Operations for Lattice Gauge Theories 29 

The same reasoning can be applied to a higher order average Uk, where 

U= U'U 0, UO is a fixed configuration and XJ f satisfies a sequence of axial gauge conditions in blocks of lattices Ω, Ω (1 \ . .., Ω{k ~1} . More precisely, we describe these conditions in the following way. For blocks of the lattice Ω, we assume 

(R 0,yU')(Γ yJ=lxeB(y), xΦy,yeΩ^\ (64) where Ro is defined by the configuration Uo. Next defining 

(U% = (UΊΓ O)C(U-Oχι, (65) 

we assume 

ϋ ( 2 (66) and Ro is defined by Uo. If an average U/j is defined on the lattice Ωu\j < k, then we assume 

(KiyU'J) (Γ yJ = 1, x G B(y), x + y,ye Ω^ + », (67) and we define 

## u[ j+ι =φW 0)c(ϋl); 1. (68) 

From this inductive definition of the average ΰ/j , it follows easily that 

ϋ'i = (U'U 0)ί(Ui) b- \ be β°>. (69) 

Now we would like to change these gauge conditions and we apply a gauge transformation M"" 1 to U'. We get some configuration Ux and U'=U". The/ h

order averages Ό' transform as follows, (70) and this implies a transformation law for U' j,

The gauge conditions (67) written in terms of Uί give us the following equations: 

(%,yO rl ){ΓjJ = u(y)(K 3o,>ϋ{)(ΓyJ (R~i yuΓ 1(x)= 1 (72) for xeB(y), x + y, yeΩ <J+1 \j<k. Solving these equations, we get 

(R 0,Xl u)(.x) = u(x 1)(R 0:Xi U1)(Γ XuX ) for xeB( Xl ), Xl e&», (73) 

(RΌ, X2 u)(x 1) = u(x 2)(Ro, X2 U1)(Γ X2 ,Xι ) for Xι EB(x 2),x 2eΩ^, (74) hence 

(R~o, X2 Ro, Xl «) W = u(x 2)fcA) (Γ X2 ,Xl )R~o, Xl (Ro, Xl Uΰ(Γ xux ), xeB\x 2),(75) and for arbitrary j < k we have 

(Ri Xj+ι u)(xj) = u(x j+1 )(Ri, Xj+ι ϋi)(Γ X] +uX ) for x,eB(x, + 1 ), xj+1 eΩ« +1 K

(76) Let us_ denote_ υQ(Γψ.J = Όi-\Γ Xh )•... 00(Γ X2iXl )U 0(Γ Xl J, then 

(Ri Xj + ^ C *o,»Λ>.χ, "> W = R(Uo( ΓXj ++ \]x»u(x), and we have the equality 30 T. Baiaban 

## . R(ϋi(r x)i u x ) ) (RC) ϋ{-') (r Xj ,Xj _,)-...  

> j

, j + ι ^ + \ ] j + 1 ) , (77) 

where the symbol (R 0,Xj + ^ i ) 0 ^ 1 ? * ) i s defined by the last equation. Taking (77) 

ϊorj = k-1, we may determine the gauge transformation u uniquely, given values 

u{y) at points y of the lattice Ω{k) . We calculate these values from additional conditions, as in (61) and (62).These conditions are straightforward generalizations of the conditions (61). At first we define inductively a fe th order averaging operation for gauge transformations. Generally a one-step averaging transformation defined by a field configuration Vo is given by 

(R ov) (y) = (R(V 0)v) (y) = {(R(V 0)v) (x)} xeBM 

= Φ)expΓi Σ L-d~\ogv^(y)R(V 0(Γ yJMx)\, (78) 

where v is defined on a lattice Ω', yeΩ' (ί) .

For a given configuration Uo we define inductively (79) (80) The additional conditions are 

(R^u k)(y)=U yeΩ {k \ (81) 

Now using the identities (76), (77) we will solve the equations (81) and we will determine u uniquely as a function of U1. We have 

## ZJΓ, (82) 

for xιeΩ m, where the expression -R 0,*i^i is defined by the last equation. Next from (74) we have 

= (R(U o)R ou)(x 2)

,) (Ro, X2 Ro,Xl 

= u(x 2) {{RO^UJ (Γ X2iXί )

(83) where the last equation defines the symbol ROx2 U1(2) . We easily find by induction that 

(R^)(xj) = u(x^R^ΊΓ^, XjeΩP, (84) where Ro xU^ is defined inductively as Averaging Operations for Lattice Gauge Theories 31 

(85) The formula (84) together with the conditions (81) give the equation 

^U[ w=l for yeΩ ( f e \ (86) hence 

W^Γ 1 . (87) 

Thus the gauge transformation is uniquely determined by all the conditions and is given by the formulas (77) for j = k— 1 and by (87). Similarly as in (63) we get (88) We may consider this expression as a new averaging operation of kih order acting on a configuration Uί defined at bonds of the lattice Ω. A result of the averaging is a configuration defined at bonds of the lattice Ωik) . Such an operation for k = 1 is given by the formula (63). Now we will prove the following fundamental fact: the new kth order averaging operation defined by the last expression in (88) is a composition of k averaging operations defined by (63) with properly chosen configurations Vo. More precisely, for a / h factor in this composition, we take Vo = U j0~1. Let us introduce some new notations. We denote the averaging operation in (63) by = (^Γ^)" 1^i*o,c^7^. (89) We define inductively a sequence of averaging operations of/ h order composing) operations defined above for Vo = U θ9 Uo,..., Uj0~x correspondingly. For j = 1 we define 

W^ (90) and if the operation ϋ{ is defined, then 

U{ +1 = R(Ui)Ό{, (91) i.e., it is a composition of the operation (89) for V0 = U j0 and of the / h order operation U{. 

Let us remark thatthese averages have the same locality properties as the averages £7\ namely (U k)c, cCΩ ik \ depends on the variables Ub for bcB k(c_) 

uB\c +). 

We are going to prove now the fundamental equality 

(R^U 1^r 1U\R kOtb R^U-1^ = (U\) b. (92) 

The proof will be by induction. For k = 1 the equality holds by the definitions (89), (90), and the Eq. (63). If we have a configuration V= V γ Vo on a lattice Ω\ then 32 T. Bahiban 

for an arbitrary gauge transformation υ we write V=(V v~1)v = (Yi~ 1V0)v and we have Let us consider the case k = 2, and let us start with an analysis of U\. We have by (68) E/ί = (l/i) and we apply the above identity with Vί = U u V0 = U 0, and 

> (1)

( l ^ l ^ (94) 

Further, by the definition (89), we have 

(Ur^iR^ΊΓ^'ΰ^Ro^R^^Γ^ϋ,, (95) 

hence 

•RΊΛR^Z^iΓ 1- (% )

The expression in the square bracket above is equal to Ό\. Let us make the following inductive hypothesis: 

φ[) b = vj{b-){Ό[) bWo,bvj\b +) = {Ό[)V, bzΩP,             

> vj(x) = ( R o . U J ( R o . x U J ••••• ( Λ Jo 7 χ VJΓ'), xεΩϋ)

We have proved it for j = 1,2. The definition (68) and the hypothesis imply 

# {+ ^Miuί)"' u{) e utf± e=»/c_              

> ^1<c1^1i(c+),( 9 8 )

where we have used the identity (93) again and the other definitions. Let us now consider the expressions RQ^U^, xeΩ U) . We will prove that 

^j j (99) For ;•= 1 it is the definition (97) of v}. For 7 + 1 we have by (85), (97), and (99) 

J (Ri yVj ) (x)} xmy) 

^ (100) hence the identity (99) is proved by induction. From (97), (99) for; = /c we get (92). Let us consider again the gauge transformation u calculated before in terms of 

U1 and given by the equalities (77) for j = k — _1, (87). In the future we will need this transformation expressed by the averagings D{. Let us write explicitly the formula Averaging Operations for Lattice Gauge Theories 33 

for u^ , . ^ ) , (loi) where xeB k(y), yeΩ ik \ xk = y, x o = x. 

We use the equalities (97) and we get for j > 0

(Ri. Xj +ι U[) (Γ Xj+uX ) = Vj(x J+ ,) (Ri Xj+1 ϋ{) (Γ XjtίιXj )•(Ri^^-'ixj). (102) If we take two neighboring factors for;, j — 1 in (101), then the last factor on the right-hand side above for) and the first factor for j — 1 give the product 

## ? Xj ff 'Ui-1) -1, (103) 

where we have used the second Eq. (97). We connect this expression with the factor corresponding to j — 1. We get such an expression for j —1=0 also. The first factor in (102) for j+l=k and the first factor on the right-hand side of (101) give 

> v

k1(y) vk-i(y) a n d ^is is equal to (103) for j = k. Thus we obtain the equality 

## R(u o(rf> x))u(x)= π  

> jk1

## i^M UM J. „,;]. (104) 

Let us recall that we have Σ g^,,^.^)^,,,,)]. (105) 

> xeB(x j+ί )I

The Eq. (104) can be written also in the following way: 

i this 

(1 

> 0

# .π 

gives 

## (i  

> \r\U )

the 

## (ϋo(r« ++!!J)) 

formulas  

> y

(χj)= Π ( 

> l = k-ί
> ••• +1 )R(U j0(Γ x

# -'mix,  

> +ίtX

))(Ri *ί+ βi)(Γ Xj+ 

(106) (107) (108) 

D. Properties of the Averages U\ 

We will now investigate the new averaging operations. Forthe averages Ok natural quantities to consider were plaquette variables. For U\ we expect that the configuration itself, i.e., bond variables, has good bounds in terms of bounds of U1.

We will prove to this effect propositions analogous to Propositions 1 and 2. 34 T. Bafeban 

Let us recall that the definition of φ\) c, cCΩ {k \ involves only the gauge fields 

Uuh9 UOib at bonds bcB k(c_)uB\c +). 

Let us start with a detailed analysis of the one-step averaging operation Vv We assume that the configurations Vo, V ι satisfy the conditions 

\V o(dp)-l\«x O9 Vltb = e iA »9\A b\«* l9 p9bcΩ' 9 (109) and Ab belong to the complexified Lie algebra g c.We would like to prove that for α 0 , aί sufficiently small the average (F x)c is an analytic function of the variables Ab,bC B(CJ)\JB{C +), C C Ω/(1 \ and to find bounds for (V ί)c— 1, or rather τ log(F 1 )c . We assume that α0 is so small that the Propositions 1 and 2 hold, i.e., α o ^ c 2 .At first let us consider the expressions 1

i Σ LΓ d-log(R 0fy V1)(Γ ytX )'], yeΩ /(1) . (110) We have 1-log(jR 0 v^i)(^v x) = (Ro VA)(Γ V X) + O(QA\(Γ V J ) 2 ) , (111)       

> i'y'yy'y'

hence (112) Next let us consider 

## Σ

> xeB(c-)

= expΓi Σ L-O-  

> LxeB(c_) I

- i Σ L-4logK 0 (Γ c > J C u(-c))   

> xeB(c~) I
> >

(113)   

> xeJ3(c-) IJ

and let us denote ^=jlog(Ro,c-^i)(Γ C i ,u(-c)), y x =jlog7 0 (Γ C i J C u(-c)). (114) As in (111) we have   

> ii

?). (115) A logarithm in the first exponential in (113) can be written as ~\oge ιAχ eιYχ .Averaging Operations for Lattice Gauge Theories 35 

Applying the results of Sect. A, more exactly (38), we have 

±loge tA *e tr *=Y x + g-1(-i*ΛγMχ + O(\A x\2). (116) All these formulas give us 

Σ L-'Y x + i Σ L-dg-\-iady x) 

> xeB(c-) xeB(c-)

i Σ L~ dYx\ (117) Denoting Σ L~ dYx= Y and using the formula (41), we have further  

> xeB(c-)
> χ
> *εB(c-)
> 2

α2 )where • exp[-iY] exp[iR(e iy ) (R O,C.A) (c) + 0(L 2 α2 )] = e x P r i 9 ( - i a d y ) Σ 

> LX6B(C-)

• exp[iΛ(e ir ) (R O,C.A) (c)  

> 2 2

) ] , (118) 

+ R(e iY )(R OtC _A)(c), (119) as it follows from (115). We can transform this linear expression using the identities R(e' Yχ ) = e' ady * and 

g ~ 1 (— i ad y J eιady * = g ~ ι (i ad y J . The last follows from the corresponding identity for functions of a complex variable: g~ i( — z)e z = g~ 1(z). We have also 

= R(e-iY )R((V 0)c)(R 0,c+ A)(Γ c+ ,x,) 

= e - i a d ^ 0 , c ( i ? 0 ,These identities imply the following formula: 

## Σ

> xeB(c-)

From (118) and (112) we get finally = expΓ-i Σ L-'(R o<  

> IXEB(C-)

+ i Σ L - ^ 0 , c ( ^ 0 , c + ^ ) ( Γ c + ? x O + 0(L 2α?)Ί. (120) 

' J36 T. Bafeban 

In all the estimates above, we have assumed that α 0, α x are sufficiently small so that the formulas and inequalities proved in Sect. A hold, and that \Y X\ = 0(L 2OL 0) are small. We restrict further a1 assuming that the norm of the element in the exponential above is small also; for example, it is enough that it is 5 Ξ \. Under these assumptions it is obvious that functions of the variables A involved in all the formulas until now are analytic functions of A. Let us define 

Q(V 0,A,c)=-.\og(V 1)c, (121) then <2(F 0, A, c) is an analytic function of A and from (120) it follows that its Taylor expansion begins with a first-order polynomial. Let us denote it by L(Q{V Q)A) C.

Thus we have 

A,c). (122) 

C(V 0) A,c) is an analytic function of A whose Taylor's expansion begins with a second-order polynomial (a quadratic form), and 

\C(V 0, A, c)\ S C,L 2\A\ 2 < C.iLa,) 2 . (123) The linear form Q(V 0)A is given by 

(Q(V O)A) C= Σ L^ d+1 \R Ot «

> xeB(c -)

## Σ

> xeB(c-)

## ) - Σ 

> xeB(c-)
> x

\ ^ (124)  

> xeB(c-) J

The first term on the right-hand side above is the main term in this linear form, and it resembles the definition of the averaging operation Q in [2]. The remaining terms are small because the functions g{ — z),g~ x(z), eiz are equal to 1 for z = 0, so the operators occurring in these terms can be estimated by O(L 2α0) and the terms can be estimated by 0(l)L 2oc 0L\A\ <O(l)L 2 α0 Lα 1 . We will denote the main term by Qv o> or Qo

(QoA) c = (Q Vo A)c= Σ L-« + '\R 0,c_A)([x,xy, (125)  

> XEB(C _)

and it has an estimate |(β o ;l)cl^μ4|<αi> so we have for the whole linear term | ( ρ ( F 0 ) ^ ) c | ^ μ | + 0 ( l ) L 2 α 0 μ | < ( l + 0 ( l ) L 2 α 0 ) α 1 < β O ( 1 ) L 2 α 0 α 1 . (126) Thus we have proved the following 

Proposition 3. There exist constants C l 5 c3 , c3^c 2, such that for α0 , oc ι^c 3 the function Q(V 0, A) = τ l o g Vί is an analytic function of A satisfying the equalities and bounds (122)—(124). The constant C x depends on d and c3 depends on d and L. Averaging Operations for Lattice Gauge Theories 37 

Now we will consider the kih order average TJ\. Its definition implies that 

-\ogU\ as a function of -\ogU x is a composition of the functions 

Q(U 0, -),Q(U 0, •),..., (127) 

We assume that Uo satisfies the assumptions of Proposition 2 and U1=e iηΛ ,

|^4|<α x . Then by this proposition the configurations Uj0 for j<k satisfy the assumptions of Proposition 3 for V0 = U j0 if ot 0L2j η2 + 2C 0(oc 0L2j η2)2

We will now investigate compositions of functions in the sequence (127). For the first function we have 

\Q(U 0, ηΛ)-LηQ(U 0)A\ £ < Cx (oc.Lη) 2 ,hence and 1

Lη < \Q(U 0)A\ + C.Lηa 2 < (1 + 0(1) L 2^)^ + C

<έ ,O(l)L 2η2x0

(128) Because e° il)L2η2ao oc ί + CγLηa\ ^ e0™* 0^ + C&\ ^ 2α x for α 0, oq sufficiently small ( O ( l ) α 0 ^ j , C i α ^ l ) , so | β ( ί 7 0 , η A ) \ < 2 a ι L η ^ 2 a ι ^ c 3 for α ^ ^ C g , and we can apply Proposition 3 to function Q(U 0, •) calculated at Q(U Q,ηA). For this composition we have 

Q(U 09 Q(U 09 ηA)) - L 2ηQ(U 0) ±- Q(U θ9 ηA) 

L,η i

1

Lη 

denoting 

Q(U 0, Q(U 0,ηA)) = Q 2(U 0, ηA), Q(Ό 0)Q(U 0) = Q 2 (l7 0 ), and using (128) we get  

> J-J ΫΊ
> ΎΓI

Q2(U 0,ηA)-Q 2(U 0)A 

> 2

)ηaj )ηaj, <έ 

<e O ( 1 »2 0 I O (l+8C 1 α1 )αi <2αj for α o ,α! sufficiently small [e.g., (129) 38 T. Bafeban 

Continuing these arguments, we arrive at the following inductive assumption for the composition Qj(U 0,ηA) of the first j functions (127) aad the composition 

Qj(U 0) of their linear parts: 1 

> Jη

/ ' (130) This implies (131) and for α t ^ j c 3 we can apply Proposition 3 to the function Q(O JO, ) calculated at 

Qj(U 0, ηA), and we get 

.-.,-. 1 

(132) Applying (130) and denoting we have 

jj+τ-Q j+1 (Uo,ηA)-Q j+ι (U o)A 

Thus the inductive hypothesis (130) is proved for j^k. For j = k, we have (133) We formulate the obtained results in 

Proposition 4. There exist constants C 2, c4 such that for α0, α x ίί c 4 ί/ιe function Qk(U 0,ηA,c)= -τlog(ί/i) c, cCi2 (k) , is α« analytic function of the variables A b, b CB k(c_)κjB k(c +). Further we have 

and 

\C k(U 0,A)\^C 2\A\ 2<C 2ai. 

(134) (135) Averaging Operations for Lattice Gauge Theories 39 

The constants C 2, c 4 are independent of k, C 2 depends on d and c 4 depends on d and L. The function Ck can be decomposed further into a sum of homogeneous polynomials, Ck(U 0, A) = C?\U θ9 A) + Cί 3\U 0, A) + .... (136) We will need some more precise information about the function Qk. This information is connected with a notion of the functional derivative. Let us recall this notion. If F{A) is a differentiable function defined at field configurations A on 

Ω, then the differential is a linear functional of the variable δA and can be represented as a scalar product of δA and some Lie algebra valued function. This function is called the functional derivative and is denoted by -z—F(A), thus we have 

oA d „, A , . _ „. δF(A) n . IδF(A) „ A (13δ) 

From this definition it follows easily that the functional derivative coincides with partial derivatives (gradient) of F(A) multiplied by η~ d.

We would like to prove that the functional derivative of Qk(U 0, ηA) is bounded by a constant independent oϊη. This property is not clear even for the linear part of 

Qk, so let us start with an analysis of this linear part. The linear part of the one-step renormalization transformation is given by the formula (124). It is a sum of the main term QVo A given by (125) and a remainder which we will denote by Q"{VQ)A. 

From (124) it is clear that we have the inequalities 

\Q Vo A\ZQ\A\, \Q"(V 0)A\^C\L 2*0Q"\A\, (139) where the operator Q is defined as in [2], and Q" is defined as 

(Q"A) C= Σ L-"A b. (140)  

> bCB(c-)uB(c + )

The constant C\ depends on d and L. A composition of k operators Q is the operator Qk. The operators Q" do not compose in a simple way, but if we introduce an operator Q' k by the formula (141)  

> bCB k(c-)vB k(c + )

then we have the inequality 

\Q"QjΛ\SQ"Qj\A\ύ2dQ'j +1 \A\. (142) Now we will prove by induction the bound (143) 40 T. Baίaban 

assuming that Uo satisfies the bound (52). Fory'= 1 it is a consequence of (139). We assume (143) for j<k and we have 

S Q(QM\ + 2C\ a o(tiη) 2 Q] \2z o(Ώη) 2

= Q J+1 \A\ + 2C; ao(LJη) 2 QQ'j\A\ + 2C\ a o(IJη) 2 Q"Q j\A\ + 4C' 12a20(lJη) 4Q"Q';\A\ (144) by (139) and Proposition 2. Further using the inequalities (142), QQ'j\A\ 

S2Qj +1 \A\, and Q"QJ\A\SQJ +1 \A\, we get 

Because 2L" 2 + L" 2 + 4ί/C; α 0 L - 4 ^ f + 4dCΊ L" 4oc 0 ^ 1 if 16ί/CΊL~ 4 α0 ^ 1, so the bound (143) is proved for all jfΞfc. For j = k we have 

\Q k(U 0)A\ίQ k\A\ + 2C' 1a0Ql\A\S(l+2C 1a0)Ql\A\, (146) and this bound implies the required property, namely 

oA b

> 0

;c,b), \Q k(U 0;c,b)\Sl+2C 1a0. (147) Now we will generalize it to the whole function Qk. It is enough to prove it for Ck.

For one-step renormalization transformation we have the bound 

# PΨ 1-" (148) following easily from general properties of the function C(V 0, A). The constant C\ 

depends on d and L. We will prove that a similar bound holds for the functional derivative of CfU Q,A) for arbitrary j ^ k. We will prove by induction that 

— Cj(U 0,A),δA (149) where the configurations A are considered on L •'-lattice and C 3 is a positive constant satisfying conditions which will be written later. From the definition of the functions Qj(U 0,ηA) we have /o, ηA) = Q(Ul, Qj(U 0, ηA)), 

hence 

= LQ(U j0)Qj(U 0, ηA) + C(W 0, β/l/ 0 , ηA)) = L J+ 'ηQiUti Qj(U 0)A + LQ(Ui) Cj(U 0, UηA) + C(Ui,Qj(U 0,ηA)) = L j+1 ηQ j+1 (U 0)A + Cj+ι (U 0,U +1 ηA), (151) Averaging Operations for Lattice Gauge Theories and 41 (152) 

A is a field configuration considered on 17 (jί+ 1 } Z d , \A\ < L j+ 1 ηoc 1. Differentiation of the above equality gives (153) Using (143), (148), (149) we obtain the following bound: 

δ

δA Cj+1 (U 0,A),δA ^QC 3L-1\A\Q" J\δA\ + C' ι2a 0(IJη) 2Q"C 3L-1\A\Q';\δA\ Q"  

> 1

(1 

'Mtiη) 2 Q]\δA\ + C,L~ x \A\ Q'-\δA\)  

> 1

α 1 ) 2 . (154) This bound implies the inequality (149) ioτj+ 1 if 

> 1

a1)2S^ (155) This inequality is satisfied if C3 > C'[ and α 0 , α x are sufficiently small, e.g., we may take C 3 = 6Cί and α 0 , α x satisfying 4dC' 1a0L~ 1 Si, (C 2Lr l+ \2dC'[L~ ί)<x ί^l. 

Thus we have proved 42 T. Baίaban 

Proposition 5. The functional derivative of Q k(U 0, ηΛ) is a bounded function for α0 ,

(X 1 sufficiently small, and we have the bounds δA -Q k(U 0,ηA,c) ; α 0 + C3\A\ δA •C k(U 09 A,c) 

(156) (157) E. Analyticity Properties of the Averaging Operations 

In this section we will prove some simple analyticity results for the averages. Let us begin with the average Uk. Formally, it is defined for all configurations, but we have good control over it for configurations U satisfying the regularity condition (52). We will prove that Uk is an analytic function of U on this domain. In fact, we will prove a little bit stronger result. Let us take a configuration Uo satisfying (52) and U=U'U 0, U' = e iηΛ ', \A'\ bounded by a small constant oc v Such configurations 

U do not necessarily satisfy (52), so we get a neighborhood of Uo which is larger than neighborhoods of Uo in the domain. This neighborhood may be also described by the conditions 

\U— U 0\ = \UUQ 1 — l\<octf, (158) 

oc 1 is a sufficiently small number. We will prove that Uk = U /Uok is an analytic function of A' and Όk{Ό k0)~ ι is close to 1; the difference may be estimated by a constant proportional to CL V We have (159) where 

vk(x) = (Ro,χUWo. xUΊ' ...'(R&U*-1), xeΩ*K (160) From Proposition 4, and especially from (131), we get 

τlog£/ /J (161) hence 1

i

and 

<8a, 1dL j+1 ηe 2ctldLJ+i 'i<O(l)a 1LJ+1 η, j = O,l,...,k-l ( 1 6 2 ) 

> k-l

(163) for (x ί sufficiently small. Moreover, Proposition 4 implies that the functions of A in (159) are analytic. We get the following Averaging Operations for Lattice Gauge Theories 43 

Proposition 6. If Uo satisfies (52), then U'U ok is an analytic function of A'= — log JJ r for A f with values in the complexified algebra, and satisfying \A'\ <cc 1.Moreover, we have a bound 

l E T T T ^ o Γ ' - l ^ C K l K . (164) Of course, we assume that α 0, a1 are sufficiently small. Another analyticity result we will need is an analyticity of Qk(U 0,ηA) with respect to Uo. We will understand it in a similar way as for Uk. We take U'U 0

instead of Uo, U' = e iηA \ \A'\ < αl 5 and we consider the function Qk(U'U 0, ηA). We want to prove that it is an analytic function of both variables Af and A, and that Proposition 4 holds uniformly with respect to A'. 

Let us analyze the proof of Proposition 3 first. The bounds depend on bounds of the quantities Yx= τ l o g F 0 ( Γ C ) X u ( - c ) ) . Previously we had \Y x\ = O(L 2(x 0), but now we allow complex perturbations V'V 0 of Vo, and for these we have I Yx\ = 0(L 2oc 0 + LαJ. Thus Proposition 3 holds unifirmly for V'V 0 instead of Vo and with the only change in the inequality (126), where the constant eO{1)L2cc ° on the right-hand side is replaced by gWM^o+Lαi) similarly we repeat the reasoning connected with Proposition 4, but with 0J0 replaced by U'U oj= U/j OJ0. Because of the bound (164), we have to replace the factors e0{1)L2(i+i)η2cxo by 

> e

o(i)(L^J+ί) η2ao+L j+i ηaι ^ b u t t h i s c h a n g e i s e a s i l y incorporated into the consider-ations and the estimates. We get the same results as before for α 0, oc 1 sufficiently small, uniformly in A\ and additionally, we get the analyticity of Qk with respect to 

A'. Let us formulate these results in 

Proposition 7. For Uo satisfying (52) and U' = e ιηA> , | ^ Ί < α 1 ? α0 , ax sufficiently small, the function Qk(U'U θ9 ηA) is analytic in complex variables A\ A, and Proposition 4 holds uniformly in A'. 

Similarly, Proposition 5 may be extended to include analyticity and uniformity statements. The formulations are obvious. F. Averaging Operations for Gauge Transformations 

In the last section of the paper we will study the averaging operations for gauge transformations, given by (61), (78)-{80). A natural analog of the regularity condition (52) would be the condition 

\(d Uo u)(b)\ = \R(U 0,b)u(b +)-u(b^\<ot 0η, bcΩ. (165) We will consider functions u satisfying this condition, but we have to consider also the functions u given by the formulas (104)-(106). They appear naturally in our considerations and generally they do not satisfy the regularity condition (165), but they satisfy other conditions following from (107), (108) if the configuration Uί is small, i.e., IL^ — 1|<α 1f7, α x small. We define: 44 T. Baίaban 

Λk(U θ9 α3) is a set of gauge transformations u defined on Ω, 

and satisfying the conditions 

(xj)-\\<a 3,XjeΩ u\ j = 0,1, ...,fc, (166)  

> j

x j e B ( x j + ι ) , j = 0,1, . . . , f e - l . (167) From this it is obvious that for u e Λk(U 0, α3) and α 3 small, all operations needed to define Rouk are done always in a case where proper expressions are small. More exactly, we have to calculate a logarithm of the expression in (167) and this expression is small. We need to consider a product of two gauge transformations satisfying (166), (167), so we would like to know that it also satisfies similar conditions. Let us consider at first the following situation: we have functions v9 vl9 v2 defined on a lattice Ω' and a gauge field configuration Vo, and we assume that 

v(x) = vi{x)v 2(x)e ir ^\ \r(x)\<c u \vri(yURo, yvd(?c)-_}\<c 2, i = l , 2 , x e B ( y ) , 

y G Ω /{1) . We will find relations between Rov and Rovi, R0v2, and bounds satisfied by Rov. We have = exp -ίr(y) + iR{v 2 \y)) jloguf hence 

L-d\ogυ~\y)(R 0>y v)(x)]=v i(y)v 2(y) 

) J

i Σ

i Σ L-ά-  

> xeB(y) IxeB(y)
> , , - 1 / =

vi(y)v 2(y)R(v 2 %y))eχp [-, 

•exp L' d-\ogv 2\y)(R v )(x) I

## 'y J

•exp i 2. *

> xeB(y)

e^\ \r[y)\<c 1+ O(( Cl + c2 )2 ). (169) Averaging Operations for Lattice Gauge Theories 45 

Let us denote the constant in the above bound by C 3, so we have 

c1+c 2)\ yeΩ™. (170) Now let us take two gauge transformations uu u2 satisfying (166), (167). Applying the above result to u = uγu2, we get 

(R^u) (x x) = f e ) (xθ (Ϊ^Γ 2) (x t) e»^\ ^(x^l < C 3(α 3Lf/) 2 (171) for Xi eΩ ( 1 ) . Next applying it to Rou, R ouu R0u2, we get 

(R^ύ 2) (χ 2) = (R^l 2) (x 2) ( K ^ 2 ) (x 2) eir ^,|r 2(x 2)| < C3(a 3Lη) 2 + C 3(C 3(α 3L>?) 2 + α 3L2^) 2

^C 3 (α 3 L2 ^) 2 [l+L-2 (l + C 3 α3 )2 ] (172) for x 2 E Ώ( 2 ) We can prove by an easy induction that 

(R-&) (xj) - (R^ΓΛ (xj) (R^Γ 2j) ( Xj ) e ir ^, Xj e Ω<» ,|r/x 7 OI<C 3 (α 3 L^) 2 [l+L-2 (l + C 3 α3 )2 + ...+(L-2 (l + ^ ^ ^ 

<2C 3(a 3IJη) 2 (173) for α 3 sufficiently small, i.e., such that L~ 2(1 + C 3 α3 )2 ^ ^. From this it follows that 1. (175) We can formulate these results in 

Proposition 8. // uuu2e Λk(U 0, α3 ) and α 3 is sufficiently small, i. e.,oc 3S c6 for some c6, then u = u 1u2eΛ k(U o,2a 3-\-2C 3a3ι) and we have (173). 

We will need to consider regular configurations vΐ in the sense that the following conditions are satisfied: | u ' ( x ) - l | < α 4 , x e Ω , (176) 

bcΩ. (177) We would like to know that if w' is such a configuration and uγ belongs to a class v4 k(α 3), then the product u/uί belongs to some class Λk(O(l) (α 3 + α 4)) also. Because we want some analyticity properties of -logRQu'u^, we will consider configu-rations vΐ with values in the complexified group G c, i. e., u' = eiλ and λ has values in the complexified algebra g c. We will consider the averages (178) As in the case of averages TJ'\ it can be easily seen that they may be defined inductively as  

> j

i ^ A ^ R ^ J r 1 (179) 46 T. Balaban 

We will prove that the configuration u' j for j^k satisfy the regularity conditions (176), (177) on proper scales and with different constants. As usual, we start with a careful analysis of a one-step operation. Let us assume that we have a gauge field configuration Vo satisfying the regularity condition \V 0(dp)— l|<α 0 , pCΩ\ and two gauge transformations v\ v x satisfying the conditions 

(loU) 

x G B(y), y e Ω/{i \ We assume that the constants are sufficiently small, so that we can apply proper theorems and estimates. We will find a bound for 

v'-\c_)R 0J'(c +)-l. We have 

•expΓΐ Σ L-d\log(υ'υ 1y1(yHRo,yV /v1)(x)\, (181) 

v'vj- \y) (Λ 0,,»'»i) W = RivT'iy)) [ Γ 1 ^ ) ( i ? 0 » (x)] ,, (182) and \v'-1(y)(R Oty v')(x)-\\<\r yJa' Ae\ r^a'* = O(La' ii ) by (180), hence 

o.yΌ'υJ (x) = R(v; x(y)){logt;'- ι(y) Λ, y g ; ( y ) ( 0 ^ 1 ) ( ) ( 3 4 ) (183) A constant in the bound above is an absolute constant. Using (41) and (181), (183) we get 

v'(y) = v'(y)v 1(y)exp\ i Σ L "R^ 

• (R 0,yv/) (x) + O(L 2α' 3α;) + (L 2 <2 ) wf ι(y) 

# Γ A

= ί/(j/)exp| i Σ L τ logί/ (y)(R Oyy v/)(x) 

(184) Let us denote 

η=v'-ι(b-)R Otb t/(b +), then \V;-l\<a' Ae«'\ 

Using this we can write 

v'-1(y)(R 0,yv')(x)= Π Λ(Ko(Γ,, 6.))ίς'=(Λ Oi ,n(Γ,,»), (186) Averaging Operations for Lattice Gauge Theories 47 

and we have 

g( 0ty ^( yJ ( 0 t y ) ( y J ( ( ^ ) 2 ) . (187) Now using this and the representation (184), we have 

> XGB(C-)

Let us recall that hence Similarly, 

(R 0,cR0,

Further we can write and this implies the following representation 

ff-\c.)R OtC ff(c +)-l = -i Σ L-"(R OtC _A)(Γ c_, x)

> xeB(c -)

+ i(R 0,c_A)(c) + ί %

•expΓi Σ L~ d(R Oc Ro   

> |_ x'eB(c +)

(188) 

i Σ

> κJ(c-)
> x'eB(c + )

. (189) We will transform the linear terms in A on the right-hand side of (189). Let us notice that by the definition (185) of A and by the identity logy" x = — logi; we have 48 T. Baίaban 

hence 

-A b = R Otb A. b. (190) For the term (R OtC _A)(c)> we have for x e £ ( c _ ) , 

(R OtC _A)(c)= Σ W P r Σ y o l J ) b 

> bQc bCc

= - Σ R{V 0(cυ(-Γ eJ))R(V 0(Γ e,xuίc +,b-J))A b

> bC-c

= - Σ K(F 0 (Γ C j X u[c + ,fe_]))Λ + O(L 2 α0 α;); (191) 

> bC-c

similarly for the third term on the right-hand side of (189). Taking this into account, we have 

ff-\c-)R OtC vr(c +)-l=i Σ L-'(K OiC _Λ)([x,x']) 

xeB(c-) 

-ί Σ L-\R OtC _A)(Γ C9 M-c)) 

xeB(c-) 

+ 0(L 2 (α 0 α4 + α 0 α4 + αr3α; + α^ 2)). (192) Let us now estimate the terms (R OtC _A) (Γ cx u( — c)). They almost vanish because by the definition (185) A is almost equal to the derivative of λ= τlogι/. We will prove in fact that they are small. Similarly, as in (187) we have  

> f

^ j i Λi) 2 ), (193) and (194) hence 

(R 0,c_A)(Γ c,M-c)) = 0(L 2(a 0a4 + a' 42)). (195) This gives us finally 

v'-1(c_)R 0J'(c +)-\=i d

> xeB(c)

+ 0(L 2 (α 0 α4 + α 0 α; + α' 3α4 + α4 2 )). (196) From this we easily get a bound if we notice that This implies | ^ | < α 4 + 0(α 4 2 ), and . (197) Averaging Operations for Lattice Gauge Theories 49 

From representation (184) we obtain also 

\v\y) - 11 < α 4 + 0(Lα 4 ) + O(L 2(α 3 + α 4 )α 4 ) ^ α 4 + 0 ( L α 4 ) . (198) Let us formulate these results in 

Proposition 9. There exist positive constants C4 , C" 5, c' 6 5wc/z ί/zαί /or arbitrary functions Fo , 1/, 1^ satisfying (180) w/ί/z α 0 , α 3 , α 3 , α 4 , α ^ C g , ί/ze following bounds 

hold: 

(199) (200) In these bounds we have assumed that α 4 = 0(α 4 ), which will always be true here and in forthcoming papers. Let us apply this result to configurations Uo, u\ u γ many times. We assume that 

Uo satisfies (52), u satisfies (176), (177), and u1 satisfies (166), (167). When we apply it the first time, we get bounds (201) (202) Let us denote /? = α 0 α4 + α 3 α4 + α 4, C 5 = 1+4C' 5 , C 4 = 8C 4 C5 . We will prove by induction that (203) 

\u' j(y) -11 < α 4 + 2C 5oc 4Lη + ... + 2C 5oc 4Ljη, y e Ω U) . (204) 

Let us notice that 

(x 4Ljη + CJ(L jη) 2 ^ α 4ίΛ/(l + C 4 (α 0 + α 3 + α 4)) ^ 2α 4 L^ ^ 2α 4

for α 0, α 3, α 4 sufficiently small, so the condition α 4 = 0(α 4 ) mentioned above is satisfied indeed. The inequalities (203), (204) hold for 7 = 0,1. We assume them for some) and we will prove them for7+ 1. We apply Proposition 9 with Vo= Uj0,v' = u\ v1 =R ouιj. We have α 0 replaced by 2<x o(L jη) 2, α3 replaced by a3Ljη, α4

replaced by the right-hand side of (204), which can be bounded by α4 (l +4C' 5) = C 5aί 4., and α 4 replaced by the right-hand side of (203), which can be bounded by 2α 4. The conditions of the proposition are satisfied if, e.g., 2α 0, α 3,C5 α4 , 2α 4rgc6, so we can apply it and we get + Q ( 2 α 0 C 5 α 4 + α 3 2α 4 + 4α 2) (L j+ ιη) 2

^ α 4 ί / + ιη + C4β(B + 'η) 2 , (205) 

Wj+ Ky) - 11 < α 4 + 2C 5oc 4Lη + ... + 2C 5ot 4Ljη + 2C 5oc 4Lj+ xη . (206) Thus we have proved the following 50 T. Baiaban 

Proposition 10. There exist positive constants C4 , C 5 , c6 such that for arbitrary configurations U o, u\ u x satisfying (52), (176), (177), (166), (167) with α0 , α 3 , α 4 ^ c 6

the bounds (203), (204) hold forj^k. 

This result implies in particular that the configuration u' belongs to the class /L fc (C 5α4). The assumptions (176), (177) can be reformulated in terms of the functions λ= -logu'. If we assume  

> α

4 , \λ(x)\<oc 4, λ

α4 sufficiently small, (207) then assumptions (176), (177) are satisfied with a constant 4α 4 instead of α 4. It is obvious from the definition of the averaging operations that ύ/j are analytic functions of λ, and 

Q'j(μ l9 λ)=^logu' J9 j^k, (208) are analytic functions of λ also. We want to calculate a linear term in an expansion of this function. In fact, we will be satisfied with a good approximation of this term. From (184), (187), we have for v' = e iλ 

(209) By definition of A, 

hence 1 ,

iAb=\loge-iλ(b -)eiRo -bλ(b +) 

1

i  

> xeB(y)
> Voλ)(ft) /2

(210)  

> 4 2

) . (211) By (179) the function Q](u u λ) is a composition of one-step functions and from the above formula we can easily see that 

Qj(Mi,λ,y)= Σ L-J dR(u 0(if x))λ(x)+ 1Σ   

> xeBJ(y) I=0

• 0(C 5oc 42a 4Lιη + «32a 4(L ιη) 2 + 4al(L ιη) 2), (212) hence 

Q' j(u uλ,y) = (Q' jλ)(y) + Cj(u ι,λ,y), (213) 

| q ( M l , λ, y)\ = O((α 3α4 + oftϋη). (214) Averaging Operations for Lattice Gauge Theories 51 

References 

1. Balaban, T.: (Higgs) 2; 3 quantum fields in a finite volume. I. A lower bound. Commun. Math. Phys. 85, 603-636(1982) 2. Balaban, T.: Propagators and renormalization transformations for lattice gauge theories. I. Commun. Math. Phys. 95, 17-40 (1984) 3. Brydges, D.C., Frόhlich, J., Seiler, E.: On the construction of quantized gauge fields. I. General results. Ann. Phys. 121, 227-284 (1979) 4. Kadanoίf, L.P.: Notes on Migdal's recursion formulas. Ann. Phys. 100, 359-394 (1976) 5. Kadanoff, L.P.: The application of renormalization group techniques to quarks and strings. Rev. Mod. Phys. 49, 267-296 (1977) 6. Osterwalder, K., Seiler, E.: Gauge field theories on a lattice. Ann. Phys. 110, 440-471 (1978) 7. Varadarajan, V.S.: Lie groups, Lie algebras and their representations. New York: Prentice-Hall 1974 8. Wilson, K.G.: Confinement of quarks. Phys. Rev. D10, 2445-2459 (1974) 9. Wilson, K.G.: Quantum chromodynamics on a lattice. In: Quantum field theory and statistical mechanics, Cargese 1976, pp. 143-172. Levy, M., Mitter, P., eds. New York: Plenum Press 1977 10. Wilson, K.G.: Monte Carlo calculations for the lattice gauge theory. In: Recent developments in gauge theories, pp. 363^02. 't Hooft, G., Itzykson, C, Jaffe, A., Lehmann, M., Mitter, P.K., Singer, I.M., Stora, R., eds. New York: Plenum Press 1980 Communicated by A. Jaffe Received January 12, 1984; in revised form September 4, 1984
