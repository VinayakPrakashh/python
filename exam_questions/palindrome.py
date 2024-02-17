def is_palindrome(number):
  return str(number)[::-1] == str(number)
if is_palindrome(12321):
  print("Number is palindrome number")
else: print("Number is n0t a palindrome number")