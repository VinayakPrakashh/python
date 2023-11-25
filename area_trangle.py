x = int(input("ENter a number"))
def find_fact(x):
    result = 1
    for i in range(1,x+1):
        result = result * i
    return result
factorial = find_fact(x)
print(factorial)