import numpy as np

A = np.zeros((3,3))
B = np.ones((3,3))

C = np.zeros((10,10))
D = np.ones((10,10))

s = 0
for i in range(A.shape[0]):
	for j in range(A.shape[1]):
		s = s + (A[i,j] - B[i,j]) ** 2
s = s / float(A.shape[0]*A.shape[1])

print s

print ((C-D)**2).mean()


