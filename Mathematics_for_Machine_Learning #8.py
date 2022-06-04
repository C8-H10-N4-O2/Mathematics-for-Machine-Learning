import sympy as sp
import numpy as np
import math

#문제 1번
A = np.array([  [1,2,3],[4,5,6],[7,8,9]  ])
B = np.array([  [-1,0,1,3,2],[1,1,6,11,-5],[3,-10,2,3,5]  ])
C = np.array([  [-1,0,1],[2,3,10],[-7,3,2]  ])
D = np.empty([5,15])
E = np.empty([15,5])
#D2 = np.array([  3*i-4*j+5 for i in range(0,5) for j in range(0,15)  ])

for i in range(0,5):
    for j in range(0,15):
        D[i][j] = 3*i-4*j+5

for i in range(0,15):
    for j in range(0,5):
        E[i][j] = (-1)**(i+j)

print('1\n',A+C)
print('2\n',np.matmul(D,E))
print('3\n',np.matmul(np.matmul(B,D),E))
print('4\n',A*C)


#문제 2번
def Hadamard_matrix(a):
    count = 0
    while (1):
        if a % 2 != 0 :
            return print('odd number')
        elif a == 2 : break
        else :
            a = int(a / 2)
            count += 1

    H = np.zeros([a,a], int)

    for i in range(0,a):
        for j in range(0,a):
            if i == 0 or j == 0 : H[i][j] = 1
            else : H[i][j] = -1

    rc = 4 #rope_count
    brc = 2 #before_rope_count

    if count != 0 : 
        for i in range(0,count):
            A = np.hstack((H,H))
            H = np.vstack((A,A))

            for x in range(brc,rc):
                for y in range(brc,rc):
                    H[x][y] = -H[x][y]
            brc = rc
            rc += 4

        return H
    else : return H

n = int(input("input:"))
print(Hadamard_matrix(n))