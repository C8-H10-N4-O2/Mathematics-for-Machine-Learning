import numpy as np
import sympy as sp
import math

# 실습 1-1 Gram-Schmidt process 를 이용해서 orthonomal basis를 구하는 함수를 만들어 봅시다.

N = np.array([[2,0,0],[1,2,1],[-1,0,1]])
#N = np.array([[1,5,0],[1,2,0],[0,1,2]])
#N = np.array([[1,5],[1,0]])

def proj(a,b):
    result = np.matmul(a,b)/np.matmul(a,a) * a
    return result

def orthogonal_vstack(num):
    #input : v_column

    global imsi

    if num == 2: 
        imsi = np.vstack((  eval('e{}'.format(1)),eval('e{}'.format(2))  ))
        return imsi

    else : 
        imsi = np.vstack((  orthogonal_vstack(num-1),eval('e{}'.format(num))  ))

    return imsi

def proj_repeat(num):
    tmp = 0 # 초기화를 생활화 합시다.
    for i in range(1,num):
        tmp += proj( eval('r{}'.format(i)),eval('v{}'.format(num)) )

    return ( eval('v{}'.format(num)) - tmp )

def function(v):

    # 입력받은 행렬의 행과 열의 크기를 변수에 저장한다. 
    # 대각행렬만을 다룰 예정이므로 열의 값을 저장한다.
    _, v_column = np.shape(v)
    
    # 입력받은 행렬 v를 v1,v2,...,vn으로 열벡터로 나누어준다.
    for i in range(1,v_column+1):
        globals()["v{}".format(i)] = v[:,i-1]

    #gram schmidt 과정
    for i in range(1,v_column+1):
        globals()["r{}".format(i)] = proj_repeat(i)

    #orthogonal -> orthonomal basis   e{i} = r{i}/(np.linalg.norm(r{i},2))
    for i in range(1,v_column+1):
       globals()["e{}".format(i)] = eval('r{}'.format(i)) / (np.linalg.norm(eval('r{}'.format(i)),2))
    
    orthogonal_vstack(v_column)

    result = np.round(np.matmul(imsi,imsi.T))

    return result

print("orthonomal basis\n",function(N))
