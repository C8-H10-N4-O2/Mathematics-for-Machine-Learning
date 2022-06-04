import numpy as np

#실습 1-1 (5)

A = np.array([ [3,2,4],[2,0,2],[4,2,3] ])
val, vec = np.linalg.eig(A)

Q = vec
D = np.diag(val)
print(D)

Qinv = np.linalg.inv(Q)
ret = np.matmul(Q,D)
ret = np.matmul(ret,Qinv)
print(ret)

I5 = np.identity(3)
I5 = 5*I5
print(I5)

Dp = D - I5

chk = np.matmul(Q,Dp)
chk = np.matmul(chk,Qinv)

B = A-I5
print(B)














