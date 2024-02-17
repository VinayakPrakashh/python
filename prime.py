X = int(input("enter the range: "))
def is_prime(a):
    for i in range(2,(a/2)+1):
        if a%i==0:
            return False
        else:
            return True
          
for j in range(0,X):
    if is_prime(j):
        print(j)