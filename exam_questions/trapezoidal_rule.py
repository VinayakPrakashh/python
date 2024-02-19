def f(x):
    return 1/(1+x**2)
a = 0
b = 1
n= 4
h = (b-a)/n
k = 1
sum = 0
while k<n:
    t = a+(k*h)
    sum +=f(t) 
    k = k+1
int_a = (h/2)*(f(a)+f(b)+2*sum)
print(int_a)