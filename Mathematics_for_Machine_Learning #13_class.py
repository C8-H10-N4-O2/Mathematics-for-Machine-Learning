import numpy as np

#세로로 긴 행렬에 대한 식 (12주차는 가로에 대한 식)

A = np.array([ [3,2],[2,3],[2,-2] ])
B = A.T

#step 1 : B^T.B
BtB = np.matmul(B.T,B)
print(BtB)

val,vec = np.linalg.eig(BtB)
val = np.round(val,2)
print(val)

#step 2 : Sigma => B
S = np.zeros([2,3])
count = 0 #S index
for i in range(0,len(val)):
    if val[i] != 0:
        S[count,count] = val[i]
        count =+ 1
S = S**(1/2)

V = np.hstack((  vec[:,[0]], vec[:,[2]], vec[:,[1]] )) #자리바꾸기

#Last step : U
#U[:,i] = 1/S[i,i] * B * V[:,[i]]

u1 = (1/S[0,0]) * np.matmul(B,V[:,[0]])
u2 = (1/S[1,1]) * np.matmul(B,V[:,[1]])

U = np.hstack((u1,u2))
print(U)

#B = U*S*V^T
ret = np.matmul(U,S)
ret = np.matmul(ret,V.T)
print(ret)

#A = V*S^T*U*T
Ub = V
S = S.T
V = U
#A = Ub*S*V^T
chk = np.matmul(Ub,S)
chk = np.matmul(chk,V.T)
print(chk)
