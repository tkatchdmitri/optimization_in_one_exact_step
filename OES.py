

def mult(X,Y): # MATRIX MULTIPLICATION
    return [[X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][0]+X[0][1]*Y[1][0]],[X[0][0]*Y[0][0]+X[0][1]*Y[1][0],X[0][0]*Y[0][0]+X[0][1]*Y[1][0]]]

def sub(R,G): # MATRIX SUBTRACTION
    # print(ROMAN)
    return [[R[0][0]-G[0][0],R[1][0]-G[1][0]],[R[0][1]-G[0][1],R[1][1]-G[1][1]]]


def add(X,Y): # MATRIX ADDITION
    return [[X[0][0]+Y[0][0],X[1][0]+Y[1][0]],[X[0][1]+Y[0][1],X[1][1]+Y[1][1]]]

def over(X,Y):
    return [[X[0][0]/Y[0][0],X[1][0]/Y[1][0]],[X[0][1]/Y[0][1],X[1][1]/Y[1][1]]]

A,B,C,D,Z=[[1.0,1.0],[0.0,0.0]],[[0.1,0.1],[0.1,0.1]],[[0.1,0.1],[0.1,0.1]],[[0.0,0.0],[0.0,0.0]],[[0.001,0.001],[0.001,0.001]] # ESTABLISH MATRIX
for U in range(1): # ONE EXACT STEP
    # print("U",U)
    D=mult(mult(A,B),C) # FORWARD
    for S in range(1000000): # ONE MILLION DERIVATIVES
        # print("S",S)
        DD=over(sub(mult(mult(add(A,Z),add(B,Z)),C),mult(mult(sub(A,Z),sub(B,Z)),C)),add(Z,Z)) # PARTIAL
        B,C=B+DD,C+DD # APPLY PARTIAL
