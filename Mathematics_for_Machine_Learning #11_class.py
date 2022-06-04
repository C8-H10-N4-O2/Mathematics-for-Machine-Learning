import numpy as np
import time

A = np.array([ [1,-1],[-1,1] ])

value, vectors = np.linalg.eig(A)

print(value, vectors)

D = np.diag(value)
print(D)

P = vectors
Pinv = np.linalg.inv(P)

res = np.matmul(P,D)
res = np.matmul(res,Pinv)
print(res)

#ㅇㅣㄹㅂㅏㄴㅈㅓㄱㅇㅣㄴ
ret = np.identity(2)
tic = time.perf_counter()
for i in range(0,200):
    ret = np.matmul(ret, A)
toc = time.perf_counter()

print(f"Standard mul in {toc-tic:0.4f} sec")
print(res)

#Diag

tic = time.perf_counter()
dd = value**200
D = np.diag(dd) 
res = np.matmul(P,D)
res = np.matmul(res,Pinv)
toc = time.perf_counter()

print(f"Standard mul in {toc-tic:0.4f} sec")
print(res)
