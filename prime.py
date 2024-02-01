def is_prime(a):
    for i in range(2,a):
        if a%i==0:
            return False
        else:
            return True
   
for j in range(0,101):
    if is_prime(j):
        print(j)