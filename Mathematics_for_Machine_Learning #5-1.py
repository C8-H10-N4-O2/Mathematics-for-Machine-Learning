import numpy as np
import sympy as sp
import math

A = np.empty([15,15], int)
B = np.empty([10,10], int)


for i in range(0,15):
    for j in range(0,15):
        if i+j % 2 == 0 : A[i][j] = 2
        else : A[i][j] = -1

b = np.array([1,2,0,-2,4,5,1,2,10,7])

for i in range(0,10):
    num = b[0]
    for j in range(0,10):
        if j == 9: b[9] = num
        else : b[j] = b[j+1]
    print(b)

