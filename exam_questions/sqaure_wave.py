from matplotlib.pyplot import *
from numpy import *
t=linspace(1,10,1000)
sum = 0

n = 100000
for i in range(n):
    sum += sin(((2*i)+1)*t)/(2*i+1)
plot(t,sum)
show()