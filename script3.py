import numpy as np 

A = np.array([[0,230,75],[0,210,60],[0,200,50]])
B = np.array([[0,225,70],[0,210,65],[0,200,55]])

'''
s = 0 
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        s = s + (A[i,j] - B[i,j]) ** 2

print s 
'''
# numpy one line code Sum Squared Errors
print ((A-B) ** 2).sum()
