x =int(input("ENter the number "))


def is_armstrong(x):
    length  = len(str(x))
    sum = 0
    for digit in str(x):
        sum = sum+ (int(digit)**length)
    print(sum)
    if x==sum:
        return True
    else:
        return False

if is_armstrong(x):
    print("Number is armstrong")
else:
    print("number is not armstrong")