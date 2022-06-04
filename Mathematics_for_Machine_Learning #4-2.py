import math
import numpy as np

T_main = np.empty((3,3))

e1 = np.array([1,0,0])
e2 = np.array([0,1,0])
e3 = np.array([0,0,1])

v3 = np.array([1,2,3])
v10 = np.array([2,4,6,8,10,12,14,16,18,20])

def T(E,n):
    T = np.empty((n),int)
    for i in range(0,n):
        if i == (n-1) : T[n-1] = E[n-1]+E[0]
        else : T[i] = E[i]+E[i+1]
    return T

#n = int(input("n을 입력: "))
n = 3
T_main = np.column_stack([T(e1,n),T(e2,n),T(e3,n)])

V_main = v3.reshape((3,1))
Main_Array = np.matmul(T_main,V_main)

print(Main_Array)

