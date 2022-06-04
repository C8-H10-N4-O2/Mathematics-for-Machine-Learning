import numpy as np
import sympy as sp
import math

C = np.array([  [1,2,3],[4,5,6],[7,8,9]  ])
index_shape = np.empty([2])
index_shape = np.shape(C)

def f(C,index):
    sum = 0
    for i in range(0,3):
        sum += C[index][i]
    return print('해당 행렬의 원소의 값: ',sum)

while(1):
    try:
        id = int(input("인덱스를 입력하세요. : "))
        if id > index_shape[0] or id < 0 :
            print('인덱스 범위를 벗어났습니다.')
        else : 
            f(C,id)
            break 
    except ValueError:
        print('정수를 입력해주세요.')

