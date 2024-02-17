x = int(input("Enter the numbe to find the factorial: "))
def find_fact(x):
    if x == 0:
        return 1
    else:
        return x*find_fact(x-1)
fact = find_fact(x)
print(fact)