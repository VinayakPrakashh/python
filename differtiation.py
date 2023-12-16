from numpy import *
from scipy.integrate import odeint
from matplotlib.pyplot import *
def find_sol(x,t,k):
    dxdt = -2*(k*x)
    return dxdt
x0 = 5

t = arange(0,50)

k = 1

x1 = odeint(find_sol,x0,t,args=(k,))
k = 8
x2 = odeint(find_sol,x0,t,args=(k,))
k = 3
x3 = odeint(find_sol,x0,t,args=(k,))
plot(x1,t,label = 'k=1')
plot(x2,t,label = 'k=2')
plot(x3,t,label = 'k=3')
xlabel('Time')
ylabel('derivative')
legend()
show()