from numpy import *
from matplotlib.pyplot import *
N = [50,100,500,1000]
cnt = 0
fun = 0
error = zeros(len(N))
for i in N:
    if i==0:
        fun=0
    else:
        fun==1
    for j in range(1,i):
        fun=fun+(-1)**j*(1/((2*j)+1))
    pifun = 4*fun
    error[cnt]=abs(pi-pifun)
    cnt+=1
plot(N,error)
show()
