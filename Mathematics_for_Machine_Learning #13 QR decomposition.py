import numpy as np

def proj(a,b):
    result = np.matmul(a,b)/np.matmul(a,a) * a
    return result

A = np.array([ [2,0,0],[1,2,1],[-1,0,1] ])
#벡터 뜯기
a1 = A[:,0]
a2 = A[:,1]
a3 = A[:,2]

#gram schmidt
u1 = a1
u2 = a2 - proj(u1,a2)
u3 = a3 - proj(u1,a3) - proj(u2,a3)

#orthonomal basis로 변환
e1 = u1/(np.linalg.norm(u1,2))
e2 = u2/(np.linalg.norm(u2,2))
e3 = u3/(np.linalg.norm(u3,2))

Q = np.vstack((e1,e2,e3))
Q = Q.T

print(np.round(np.matmul(Q,Q.T)))

# R
R = np.zeros([3,3])

R[0,0] = np.dot(a1,e1)
R[0,1] = np.dot(a2,e1)
R[0,2] = np.dot(a3,e1)
R[1,0] = np.dot(a1,e2)
R[1,1] = np.dot(a2,e2)
R[2,2] = np.dot(a3,e3)

ret = np.matmul(Q,R)
print(A)
print(np.round(ret))