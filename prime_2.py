def is_prime(j):
    cnt = 0
    for i in range(2,j):
        if j%i==0:
            cnt+=1
    if cnt==0:
        return True
    else: 
        return False
for j in range(2,10):
    if is_prime(j):
        print(j)