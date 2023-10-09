num = int(input("Enter the number: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
result=factorial(num)

print(result)

