import sympy as sp
import numpy as np
from math import *

A = np.array([ [1,2,3],[4,5,6] ])

#문제 1-1
def Trs(a):
    vlen, clen = np.shape(a)
    At=np.zeros([clen, vlen],int)

    for i in range(0,vlen):
        for j in range(0,clen):
            At[j][i] = a[i][j]

    return At

print('A :',A)
print('(A^t)^t :',Trs(Trs(A)))

#문제 1-2

V = np.array([  [1,2,3,4],[4,5,6,7],[7,8,9,9],[1,2,3,4]  ])
W = np.array([  [1,2,3],[4,5,6],[7,8,9]  ])

def tri_upper(v):
    vlen, clen = np.shape(v)

    if vlen != clen : return print("plz input square matrix")

    output = np.zeros([vlen, clen], int)

    for i in range(0,vlen):
        for j in range(0,vlen):
            if i > j : 
                output[i,j] = 0
            else : output[i,j] = v[i,j]
    return output

def tri_lower(v):
    vlen, clen = np.shape(v)

    if vlen != clen : return print("plz input square matrix")

    output = np.zeros([vlen, clen], int)

    for i in range(0,vlen):
        for j in range(0,vlen):
            if i < j : 
                output[i,j] = 0
            else : output[i,j] = v[i,j]
    return output

print("my triu :",tri_upper(V))
print("numpy triu :",np.triu(V))

print("my tril :",tri_lower(V))
print("numpy tril :",np.tril(V))
