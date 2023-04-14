import numpy as np

# Quick Numpy tutorial
# https://numpy.org/doc/stable/user/quickstart.html

A = np.matrix('1,2,3;4,5,6;7,8,9')
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
eigen = np.linalg.eig(a[1])
print(max(eigen[0]))