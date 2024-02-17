def f(x):
    return 1/(1+(x**2))
a = float(input("Lower limit"))
b = float(input("Upper limit"))
n = int(input("number of Strips"))
h = (b-a)/n
sum = 0
k=1
while k<n:
    t = a+(k*h)
    sum = sum+f(t)
    k=k+1
    
int_a = (h/2)*((f(a)+f(b))+(2*sum))
print(int_a)