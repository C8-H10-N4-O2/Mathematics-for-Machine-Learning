import numpy as np
import random

"""A = 1/5 * (np.array([ [4,3],[-3,4] ]))
print(A)

res = np.matmul(A,A.T)
res = np.round(res,2)

print(res)

x = np.zeros([2,1])

for i in range(0,2):
    #compute Ax
    chk = np.matmul(A,x)
    #|Ax|
    n1 = np.round(np.linalg.norm(chk,2),2)

    n2 = np.round(np.linalg.norm(x,2),2)

    if n1!=n2 :
        print("different")
        flag = 1

if flag == 0:
    print("CORRECT")
print(n2)"""


print("------------------------------------------------")

A = np.array([ [3,2,2],[2,3,-2] ])

#1. A^T*A
ATA = np.matmul(A.T,A)
val, vec = np.linalg.eig(ATA)
val = np.round(val,2)
print(val)

S = np.zeros([2,3])
cnt = 0
for i in range(0,len(val)):
    if val[i] != 0 :
        S[cnt,cnt] = val[i]
        cnt= cnt+1
S = S**(1/2)
print(S)

#Step 3
print(val,"\n",vec)


#step 4
V = np.hstack((vec[:,0],vec[:,2],vec[:,1]))
print(vec)
print(V)


u1 = (1/S[0,0]) * np.matmul(A,V[:,[0]])
u2 = (1/S[1,1]) * np.matmul(A,V[:,[1]])
U = np.hstack((u1,u2))
print(U)

#step 5
chk = np.matmul(U,S)
chk = np.matmul(chk,V.T)
print(chk)

