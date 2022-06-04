import numpy as np
import sympy as sp
import math

#(1)번
A = np.full((10,10),-1)

for i in range(0,10):
    A[i][i] = 1
    
print(A)


#(2)번
B = np.empty([10,10])

for i in range(0,10):
    for j in range(0,10):
        if (i+j)%2 == 0 : B[i][j] = 1
        else : B[i][j] = 0

print(B)


#(3)번
C = np.empty([10,10])

for i in range(1,11):
    for j in range(0,10):
        C[i-1][j] = i+j

print(C)