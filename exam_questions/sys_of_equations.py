from numpy import *
#using inbuilt function 
#8x+3y-2z = 9
#-4x+7y+5z = 15
#3x+4y-12z = 35
A = array([[8,3,-2],[-4,7,5],[3,4,-12]])
A_tmp = array([[8,3,-2],[-4,7,5],[3,4,-12]])
B = array([9,15,35])
x = linalg.solve(A,B)
print(f"X:{x[0]} Y ={x[1]} Z={x[2]} ")
#without any inbuilt function
det = linalg.det(A)
A[:,0] = B
X = linalg.det(A)/det
A = A_tmp
A[:,1]=B
Y = linalg.det(A)/det
A = A_tmp
A[:,2]=B
Z = linalg.det(A)/det
print(X,Y,Z)
