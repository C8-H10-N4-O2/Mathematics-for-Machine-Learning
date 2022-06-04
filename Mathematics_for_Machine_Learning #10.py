import numpy as np

#실습 1-1
A = np.array([ [-1,2,1,3,4],[0,0,2,-1,0] ])

v_1 = np.array([ [1],[2],[3],[4],[5] ])
v_2 = np.array([ [1],[0],[1],[0],[1] ])
v_3 = np.array([ [1],[-1],[1],[-1],[1] ])

print(A)
print(np.matmul(A,v_1))
print(np.matmul(A,v_2))
print(np.matmul(A,v_3))

A = np.array( [ [1,-1],[-1,1] ] )
values, vectors = np.linalg.eig(A)

#실습 2-1

def check_eigen(A,v):
    nrow, _ = A.shape
    res = np.matmul(A,v)
    k=(res[0]/v[0])
    chk = k*v

    ret = 0
    for i in range(0,nrow):
        if chk[i] != res[i]: ret = 1

    return ret

def check_eigen2(A,v):
    res = np.matmul(A,v)
    res = res/v
    nrow, _ = res.shape
    print(res)

    c = res[0]
    ret = 0
    for i in range(1,nrow):
        if c != res[i]:
            ret = 1
        return ret;

print("check eigenvector")
r = check_eigen(A,vectors[:,[0]])
v2 = np.array([ [2],[1] ])
r2 = check_eigen2(A,v2)

if (r2 == 0):
    print("eigenvector")
else : 
    print("Not eigenvecter")

A = np.array([ [-3,1,-3],[20,3,10],[2,-2,4] ])
B = np.array([ [7,4,6],[-3,-1,-8],[0,0,1] ])

valA, vecA = np.linalg.eig(A)
valB, vecB = np.linalg.eig(B)

def look_good(a):
    row, column = a.shape
    for i in range(0,row):
        for j in range(0,column):
            a[i,j] = round(a[i,j])
    return a

print("\n A eigenvalue & eigenvector")
print(np.round(valA,0),'\n',np.round(vecA,0))

print("\n B eigenvalue & eigenvector")
print(np.round(valB,0),'\n',np.round(vecB,0))
