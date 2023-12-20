from numpy import *
from matplotlib.pyplot import *
N = 1000
n = 0
t =arange(0,1000,1)
error = []
fun = 0
while(n<N):
    fun +=4*(((-1)**n)*(1/((2*n)+1)))
    pi_fun = pi - fun
    error.append(pi_fun)
    n += 1
plot(t,error)
show()