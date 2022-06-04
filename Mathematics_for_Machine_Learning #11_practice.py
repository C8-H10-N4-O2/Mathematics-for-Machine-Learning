from optparse import Values
from turtle import shape
import numpy as np

A = np.array( [ [3,2,4],[2,0,2],[4,2,3] ] )

#고유값, 교유벡터 구하기
values, vectors = np.linalg.eig(A)

#D(고유값을 대각성분으로 하는 대각행렬)구하기
D = np.diag(values)

#고유벡터(P)의 역행렬 구하기
P = vectors
Pinv = np.linalg.inv(P)

#PDPinv = A 확인하기
res = np.matmul(P,D)
res = np.matmul(res,Pinv)

"""값 확인
print(res)
print("P \n",P)
print("D \n", D)
print("Pinv \n",Pinv)"""

#PDP^T 확인
P_T = np.transpose(P)

#PDPinv = A 확인하기
res = np.matmul(P,D)
res = np.matmul(res,P_T)

for i in range(0,3):
    for j in range(0,3):
        res[i,j] = round(res[i,j])

"""값 확인
print(res,"\n")
print(A)"""

#행렬과 값을 입력받아 주어진 값이 고유값인지 확인하는 함수

def function(V, value):
    values= np.linalg.eig(V)[0]
    
    #고유값 계산
    nrow, ncol = V.shape
    In = np.identity(nrow)
    In = value*In
    B = V-In

    if np.linalg.det(B) == 0: return print("This value is eigenvalue.")
    else : return print("This value is not eigenvalue.")

B = np.array([ [6,-1],[2,3] ])

for i in range(0,10):
    function(B,i)