from numpy import *
m = [[1,2,3],[1,2,3],[1,2,3]]
y = [[4,2,3],[1,0,3],[1,9,3]]
print(linalg.inv(y))
print(linalg.det(y))
print(transpose(y))
print(dot(m,y))
print(linalg.eig(y))
print(linalg.matrix_rank(y))
