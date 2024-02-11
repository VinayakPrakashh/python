
from numpy import *
from matplotlib.pyplot import *

# a = [23,24,56,78,34,45,67,56,43,36,23,67,79]

# hist(a,bins = [20,25,30,40,45,80],edgecolor = 'black')
# show()
# realizing the function
# t = arange(-5, 5, 0.01); #assigning the vector t
# ans = (4*t**2)+3
# plot(t,ans)
# title("function f(t)=4t^2 + 3")
# xlabel("vector t")
# ylabel("function f(t)")
# show()
# from scipy.integrate import quad

# def integrand(t):
#     return 4*t**2+3
# ans,err = quad(integrand,-2,2)
# print(ans)
N = [50,100,500,1000]
fn = 0
error = zeros(N[0])
for i in range(0,N[0]):
    fn += (-1)**i*((1/((3**i)*(2*i+1))))
    res = sqrt(12)*fn
    
    abserror = abs(3.14-res)
    error[i] = abserror
t = arange(1,51,1)
plot(t,error)
show()