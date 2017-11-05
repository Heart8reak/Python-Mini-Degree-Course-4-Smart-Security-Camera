import numpy as np 

A = np.array([[0,230,75],[0,210,60],[0,200,50]])
B = np.array([[0,225,70],[0,210,65],[0,200,55]])

'''
s = 0
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        s = s + abs(A[i,j] - B[i,j])

print s 
'''
# numpy one line code to get the same answer as above
print abs(A-B).sum()

