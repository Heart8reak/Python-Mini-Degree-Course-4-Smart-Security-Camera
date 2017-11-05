import numpy as np 
#Python 2.7
A = np.ones((3,3))

'''
s = 0 
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        s = s + A[i,j]

print s 
'''

# one line code in numpy to do the same as above code
print A.sum()

