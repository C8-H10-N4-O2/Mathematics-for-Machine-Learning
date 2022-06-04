from tkinter import Y
import numpy as np
import random

#실습 1-1 

A = (1/3) * np.array([ [1,-2,2],[2,-1,-2],[2,2,1] ])

def rand_num(nlen,n):
    v=[]
    for i in range(0,nlen):
        v.append(random.randint(0,n))
    return v

def function(n): 

    for i in range(0,n):
        x = np.array(rand_num(3,1000))
        y = np.array(rand_num(3,1000))
        xy = np.dot(x,y)

        Ax = np.matmul(A,x.T)
        Ay = np.matmul(A,y.T)

        AxAy = np.dot(Ax,Ay)

        if int(AxAy) == int(xy) : 
            print("equal :",xy)
        
        else : print("Different")

function(1000)

#실습 1-2

def make_Hilbert(n):
    H = np.zeros([n,n])

    for i in range(0,n):
        for j in range(0,n):
            H[i,j] = 1/(i+j+1)
    return H

H6 = make_Hilbert(6)
Ht = H6.T

print(H6,'\n',Ht)

A,_ = np.linalg.eig(H6)
print(A)

count = 0
for i in range(0,len(A)):
    if A[i] < 0 : count+=1

if count == 0 : print("Positive definite")
