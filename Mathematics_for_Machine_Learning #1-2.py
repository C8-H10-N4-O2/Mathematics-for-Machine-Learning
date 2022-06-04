import numpy as np

#A 정의
A = np.empty([15,22])
for i in range(0,15):
    for j in range(0,22):
        A[i][j] = 5*(i+1) - 4*(j+1)

#B 정의
B = np.empty((22,15))
for i in range(0,22):
    for j in range(0,15):
        B[i][j] = -7*(i+1) + 8*(j+1)

#C = AB, C의 합
C = np.matmul(A,B)
sum_C = np.sum(C)

#C의 대각행렬과 합
C_diag = np.diag(C)
sum_C_diag = sum(C_diag)

print('C의 모든 성분의 합 : ', sum_C)
print('C의 모든 대각 성분의 합 : ', sum_C_diag)