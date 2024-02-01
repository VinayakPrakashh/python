from numpy import *
from scipy import *
from pylab import *
val = array([[1,1,0],
       [1,-1,1],
       [1,1,-1]])
solu = array([2,4,6])
val2 = array([[1,1,0],
       [1,-1,1],
       [1,1,-1]])
val3 = array([[1,1,0],
       [1,-1,1],
       [1,1,-1]])
def solution(array1,array2,x):
    val_det = linalg.det(array1)
    array1[:,x] = array2

    solut = linalg.det(array1)/val_det
    return solut
X = solution(val,solu,0)
print(val)
Y = solution(val2,solu,1)
Z = solution(val3,solu,2)
print(X,Y,Z)