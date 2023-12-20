# Open a file and read its contents
try:
  with open("my_file.txt", "r") as f:
    data = f.read()
    print(data)
except FileNotFoundError:
  print("File not found!")
except PermissionError:
  print("You don't have permission to access the file.")
else:
  print("File read successfully!")
finally:
  print("Always executed, regardless of success or failure.")

# Another example with multiple exceptions
try:
  number = int(input("Enter a number: "))
  result = 10 / number
except ValueError:
  print("Please enter a valid number.")
except ZeroDivisionError:
  print("Division by zero is not allowed!")
else:
  print(f"The result is: {result}")
try:
  print("jj")
except:
  print("bbbbb")
else:
  print("no issues")