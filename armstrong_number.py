n = int(input("enter the number: "))
def is_armstrong(n):
    sum = 0
    length = len(str(n))
    for digit in str(n):
        sum += int(digit)**length
    if sum == n:
        return True
    else:
        return False
if is_armstrong(n):
    print("The number is armstrong number")
else:
    print("The number is not armstrong")