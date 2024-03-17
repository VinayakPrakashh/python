class InvalidName(Exception):
    def display(self):
        print("invalid name")
class AgeError(Exception):
    def display(self):
        print("Age cannot be less than 18")
try:
    x = input("Enter the name:")
    y = int(input("enter age :"))
    if len(x)==0:
        raise InvalidName()
    if y<18:
        raise AgeError()
except InvalidName as n:
    n.display()
except AgeError as a:
    a.display()