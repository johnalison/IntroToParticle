def printM(inputm):
    for r in range(4):
        for c in range(4):
            print inputm[(r,c)],"  ",
        print

def getTiTj(Ti, Tj):
    m = {}
    m[(0,0)] = Ti[0]*Tj[0]+Ti[1]*Tj[1]+Ti[2]*Tj[2]
    m[(0,1)] = 0
    m[(0,2)] = 0
    m[(0,3)] = 0

    m[(1,0)] = 0
    m[(1,1)] = Ti[0]*Tj[0]
    m[(1,2)] = Ti[0]*Tj[1]
    m[(1,3)] = Ti[0]*Tj[2]


    m[(2,0)] = 0
    m[(2,1)] = Ti[1]*Tj[0]
    m[(2,2)] = Ti[1]*Tj[1]
    m[(2,3)] = Ti[1]*Tj[2]

    m[(3,0)] = 0
    m[(3,1)] = Ti[2]*Tj[0]
    m[(3,2)] = Ti[2]*Tj[1]
    m[(3,3)] = Ti[2]*Tj[2]
    return m

# T x J
# 0 a b c        0 0   0  0    0  (-bA - cB)   (aA - cC)   (aB+bC)
# a 0 0 0        0 0   A  B
# b 0 0 0        0 -A  0  C
# c 0 0 0        0 -B -C  0


def getTiJj(T, J):
    m = {}
    m[(0,0)] = 0
    m[(0,1)] = (-T[1]*J[0] - T[2]*J[1])
    m[(0,2)] = ( T[0]*J[0] - T[2]*J[2])
    m[(0,3)] = ( T[0]*J[1] + T[1]*J[2])

    m[(1,0)] = 0
    m[(1,1)] = 0
    m[(1,2)] = 0
    m[(1,3)] = 0


    m[(2,0)] = 0
    m[(2,1)] = 0
    m[(2,2)] = 0
    m[(2,3)] = 0

    m[(3,0)] = 0
    m[(3,1)] = 0
    m[(3,2)] = 0
    m[(3,3)] = 0
    return m

# J x T
# 0 0   0  0       0 a b c     0          0    0    0 
# 0 0   A  B       a 0 0 0     Ab + Bc    0   0   0 
# 0 -A  0  C       b 0 0 0    -Aa+cC      0   0   0 
# 0 -B -C  0       c 0 0 0    -Ba - Cb

def getJiTj(J, T):
    m = {}
    m[(0,0)] = 0
    m[(0,1)] = 0
    m[(0,2)] = 0
    m[(0,3)] = 0

    m[(1,0)] = ( J[0]*T[1] + J[1]*T[2])
    m[(1,1)] = 0
    m[(1,2)] = 0
    m[(1,3)] = 0


    m[(2,0)] = (-J[0]*T[0] + J[2]*T[2])
    m[(2,1)] = 0
    m[(2,2)] = 0
    m[(2,3)] = 0

    m[(3,0)] = (-J[1]*T[0] - J[2]*T[1])
    m[(3,1)] = 0
    m[(3,2)] = 0
    m[(3,3)] = 0
    return m

 
# 0  0    0   0          0  0    0   0            0                0               0             0 
# 0  0   A1  B1          0  0   A2  B2            0  (-A1 A2 - B1 B2)          -B1 C2        A1 C2
# 0 -A1   0  C1          0 -A2   0  C2            0           -C1 B2   -A1 A2 - C1 C2       -A1 B2
# 0 -B1 -C1   0          0 -B2 -C2   0            0            C1 A2          -B1 A2     -B1 B2 - C1 C2


def getJiJj(Ji, Jj):
    m = {}
    m[(0,0)] = 0
    m[(0,1)] = 0
    m[(0,2)] = 0
    m[(0,3)] = 0

    m[(1,0)] = 0
    m[(1,1)] = (-Ji[0]*Jj[0] - Ji[1]*Jj[1])
    m[(1,2)] = -Ji[1]*Jj[2]
    m[(1,3)] = Ji[0]*Jj[2]


    m[(2,0)] = 0
    m[(2,1)] = -Ji[2]*Jj[1]
    m[(2,2)] = (-Ji[0]*Jj[0] - Ji[2]*Jj[2])
    m[(2,3)] = -Ji[0]*Jj[1]

    m[(3,0)] = 0
    m[(3,1)] = Ji[2]*Jj[0]
    m[(3,2)] = -Ji[0]*Jj[1]
    m[(3,3)]  =(-Ji[1]*Jj[1] - Ji[2]*Jj[2])
    return m



        
def subtract(Ti,Tj):
    m = {}
    for r in range(4):
        for c in range(4):
            m[(r,c)] = (Ti[(r,c)] - Tj[(r,c)])

    return m

def commTiTj(Ti,Tj):
    TiTj = getTiTj(Ti,Tj)
    TjTi = getTiTj(Tj,Ti)
    print 
    printM(subtract(TiTj,TjTi))
    print

def commTiJj(T,J):
    TJ = getTiJj(T,J)
    JT = getJiTj(J,T)
    print 
    printM(subtract(TJ,JT))
    print

def commJiJj(Ji,Jj):
    JiJj = getJiJj(Ji,Jj)
    JjJi = getJiJj(Jj,Ji)

    print 
    printM(subtract(JiJj,JjJi))
    print



#TiTj(1,0,0, 0,1,0)


#commTiTj( (1,0,0),(1,0,0))
#commTiTj( (0,1,0),(0,1,0))
#commTiTj( (0,0,1),(0,0,1))

#print "[T1,T2]"
#commTiTj( (1,0,0),(0,1,0))
#print "[T1,T3]"
#commTiTj( (1,0,0),(0,0,1))
#print "[T2,T3]"
#commTiTj( (0,1,0),(0,0,1))

#  1 -> 2 -> 3 -> 1
#
#
#
print "[T1,J1]"
commTiJj( (1,0,0),(0,0,1))
print "[T1,J2]"
commTiJj( (1,0,0),(0,1,0))
print "[T1,J3]"
commTiJj( (1,0,0),(1,0,0))


print "[T2,J2]"
commTiJj( (0,1,0),(0,1,0))
print "[T2,J3]"
commTiJj( (0,1,0),(1,0,0))


print "[T3,J3]"
commTiJj( (0,0,1),(1,0,0))


#print "[J1,J1]"
#commJiJj( (0,0,1),(0,0,1))
#
#print "[J1,J2]"
#commJiJj( (0,0,1),(0,1,0))
#
#print "[J1,J3]"
#commJiJj( (0,0,1),(1,0,0))
#
#
#print "[J2,J2]"
#commJiJj( (0,1,0),(0,1,0))
#
#print "[J2,J3]"
#commJiJj( (0,1,0),(1,0,0))
#
#print "[J3,J3]"
#commJiJj( (1,0,0),(1,0,0))
