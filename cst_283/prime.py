x = int(input("Enter the number range: "))
def is_prime(x):
    count = 0
    
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            count+=1
    if x<2:
        return False
    elif count == 0:
        return True
    else:
        return False
for i in range(x):
    if is_prime(i):
        print(i)
