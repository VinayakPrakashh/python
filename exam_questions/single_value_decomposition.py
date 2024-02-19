from numpy import *
from scipy.linalg import svd
x = [[1,2],[2,4]]
u,s,vt = svd(x)
sg = diag(s)
result = u.dot(sg.dot(vt))
print(result)