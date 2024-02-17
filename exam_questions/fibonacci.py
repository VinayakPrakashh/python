x = int(input("Enter the number of terms: "))
def gen_fib(x):
    n0 = 0
    n1 = 1

    for i in range(x):
        print(n0)
        nth = n0+n1
        n0 = n1
        n1 = nth
gen_fib(x)