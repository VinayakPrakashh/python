#hcf and gcd are the same
def hcf_loop(a, b):
    for i in range(1,min(a,b)+1):
        
        if a%i==0 and b%i == 0:
           hcf = i
    return hcf
hcf = hcf_loop(2,8)
print(hcf)
