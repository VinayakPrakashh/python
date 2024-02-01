from numpy import *
from matplotlib.pyplot import *
N = [50,100,500,1000]
fun = 0
a = arange(0,1000,1)
print(a)
error = zeros(N[3])
for i in range(0,N[3]):
    fun=fun+(-1)**i*(1/((2*i)+1))
    pi_fun = 4*fun
    error[i] = abs(pi-pi_fun)
print(error)
plot(a,error)
show()