import numpy as np

def proj(a,b):
    result = np.matmul(a,b)/np.matmul(a,a) * a
    return result

v1 = np.array([1,0,1])
v2 = np.array([1,1,1])
v3 = np.array([0,1,1])
 
r1 = v1
r2 = v2-proj(r1,v2)
r3 = v3 - proj(r1,v3) - proj(r2,v3)

e1 = r1/(np.linalg.norm(r1,2))
e2 = r2/(np.linalg.norm(r2,2))
e3 = r3/(np.linalg.norm(r3,2))

A = np.vstack((e1,e2,e3))
ret = np.matmul(A,A.T)
print(np.round(ret))   #round() : int형으로 내보내는 함수인 듯?

