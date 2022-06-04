import math
import numpy as np

v = np.array([2,4,6,8,10,12,14,16,18,20])
V = v.reshape((10,1))

def function(n):
    T = np.zeros((n,n),int)
    for i in range(0,n):
        T[i][i] = 1
        if i == (n-1) : T[i][0] = 1
        else : T[i][i+1] = 1
    return T

#2-(2)
A = np.matmul(function(10),V)
print(A)

#2-(3)
for i in range(3,11):
    print('n = ',i,'-----',np.linalg.det(function(i)))
