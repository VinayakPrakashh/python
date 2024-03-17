# create class Arith to do arithmetic operation.It contains a member function read() to read the two numbers and add() method to find the sum. You can add more methods to the class to incorporate more functionality.
class Arith:
    def __init__(self,x1,x2):
        self.x1 = x1
        self.x2 = x2
    def __add__(self,other):
        return f"{self.x1+other.x1}+{other.x2+other.x2} i"
d1 = Arith(2,3)
d2 = Arith(4,5)
print(d1+d2)