import numpy as np

A = np.array([ [4,11,14],[8,7,-2] ])

print(A)

#정사각행렬로 만들기
ATA = np.matmul(A.T,A)
print(ATA)

val, vec = np.linalg.eig(ATA)
val = np.round(val,2)
print(val)

S = np.zeros([2,3])
cnt = 0
for i in range(0,len(val)):
    if val[i] != 0:
        S[cnt,cnt] = val[i]
        cnt+=1
print(S)

S = S**(1/2)

print(vec)

V = np.hstack((vec[:,0],vec[:,2],vec[:,1]))
print(V)

#U[:[i]] = (1/sigma(i))*A*V[:[i]]
u1 = (1/S[0,0]) * np.matmul(A,V[:,[0]])
u2 = (1/S[1,1]) * np.matmul(A,V[:,[1]])
U = np.hstack((u1,u2))
print(U)


chk = np.matmul(U,S)
chk = np.matmul(chk,V.T)

print