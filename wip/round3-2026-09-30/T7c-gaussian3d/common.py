import numpy as np, itertools
PL = [(0,1),(0,2),(1,2)]          # plaquette orientations (mu,nu)
PERP = {(0,1):2,(0,2):1,(1,2):0}
SIG = {(0,1):1,(0,2):-1,(1,2):1}  # F_{mu nu} = SIG * B_perp

def site(x, s):
    x = [xi % s for xi in x]
    return x[0] + s*(x[1] + s*x[2])

def link(x, mu, s):
    return 3*site(x, s) + mu

def dmat(s):
    """fine exterior derivative 1-forms -> plaquettes on (Z/s)^3"""
    D = np.zeros((3*s**3, 3*s**3))
    for x in itertools.product(range(s), repeat=3):
        for o,(mu,nu) in enumerate(PL):
            r = 3*site(x,s)+o
            e = [0,0,0]; e[mu]=1; xm=[x[i]+e[i] for i in range(3)]
            e = [0,0,0]; e[nu]=1; xn=[x[i]+e[i] for i in range(3)]
            D[r, link(x,mu,s)] += 1; D[r, link(xm,nu,s)] += 1
            D[r, link(xn,mu,s)] -= 1; D[r, link(x,nu,s)] -= 1
    return D

def path_axis_ordered(Y, u, s):
    """row vector: A(Gamma_{Y,Y+u}), axis ordered 0 then 1 then 2"""
    v = np.zeros(3*s**3); x = list(Y)
    for ax in range(3):
        for j in range(u[ax]):
            v[link(x,ax,s)] += 1; x[ax] += 1
    return v

def Qmat(s, L, contour='axis'):
    """Balaban linear block average, research/10 (7.1)-(7.2): fine (Z/s)^3 -> coarse (Z/(s/L))^3"""
    sc = s//L; Q = np.zeros((3*sc**3, 3*s**3))
    U = list(itertools.product(range(L), repeat=3))
    def Lam(Y):
        v = np.zeros(3*s**3)
        for u in U:
            if contour=='axis':
                v += path_axis_ordered(Y,u,s)
            else:  # reverse axis order 2,1,0 (alternative contour family)
                x=list(Y)
                for ax in (2,1,0):
                    for j in range(u[ax]):
                        v[link(x,ax,s)] += 1; x[ax]+=1
        return v/L**3
    lam = {y: Lam([L*yi for yi in y]) for y in itertools.product(range(sc), repeat=3)}
    for y in itertools.product(range(sc), repeat=3):
        Y = [L*yi for yi in y]
        for mu in range(3):
            r = 3*site(y,sc)+mu
            S = np.zeros(3*s**3)
            for u in U:
                for j in range(L):
                    x = [Y[i]+u[i] for i in range(3)]; x[mu]+=j
                    S[link(x,mu,s)] += 1
            yp = list(y); yp[mu]+=1; yp=tuple(v%sc for v in yp)
            Q[r] = lam[y] + S/L**3 - lam[yp]
    return Q
