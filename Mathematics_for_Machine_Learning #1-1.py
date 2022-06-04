import numpy as np
import math

A = np.array([  [5,-4,-2],[5,-5,4],[2,5,-4],[-5,4,3],[3,-4,3]  ])
B = np.array([  [5],[-2],[-3]  ])
C = np.array([  [-5,6,7,3],[-5,0,4,2],[3,7,-7,-7],[3,5,2,3],[-6,6,3,-1]  ])
D = np.array([  [-5,5,1,7,1],[4,-7,7,-6,1],[-4,-7,-3,4,-1],[-6,1,5,-1,-4]  ])
E = np.array([  [-1],[0],[10],[2]  ])

ans_1 = np.matmul(A,B)
ans_2 = np.matmul(C,D)
ans_3 = np.matmul(np.matmul(np.matmul(C,D),A),B)
ans_4 = np.matmul(C,E)
ans_5 = ans_1+ans_4

print('AB','\n',ans_1)
print('CD','\n',ans_2)
print('CDAB','\n',ans_3)
print('CE','\n',ans_4)
print('AB+CE','\n',ans_5)