import numpy as np
import sympy as sp
import math

tv = np.array([1,2,3,4,5])
tv2 = np.array([4,-7,2,4,1])
tv3 = np.array([1,-1,2,8,3,-1922,5,2,8,1,7,435,23])

#1번

def max_num(v):
    vlen = len(v)
    Max = v[0]
    for i in range(1,vlen):
        if abs(Max) < abs(v[i]): 
            Max = v[i]
    return Max

print(max_num(tv3))

#2번

def fibo(v,n):
    
    for i in range(0,n):
        if i == 0 : v[i] = 0
        elif i == 1 : v[i] = 1
        else : v[i] = v[i-1]+v[i-2]

    return print(v)

k = int(input('k:'))
V = np.empty([k],int)

fibo(V,k)