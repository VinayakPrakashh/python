def is_prime(a):
    cnt = 0
    for i in range(2,a):
      
        if a%i==0:
            cnt+=1
    if cnt==0:
        return True

   
for j in range(2,1001):
    if is_prime(j):
        print(j)