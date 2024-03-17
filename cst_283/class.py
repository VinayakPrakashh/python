class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
person1 = Person('alice',70)
print(person1.name)
print(person1.age)

class A:
    pass

class B(A):
    pass

print(issubclass(B, A))  # Output: True, B is a subclass of A
print(issubclass(A, B))  # Output: False, A is not a subclass of B
class animal:
    def __init__(self,name):
        self.name = name
class dog(animal):
    def speak(self):
        return f"{self.name} says Woof!"
class cow(animal):
    def speak(self):
        return f"{self.name} says bhaaa"
    
class cat(animal):
    def speak(self):
        return f"{self.name} says weow"
Dog =dog("arjun") 
Cat = cat("henna")
print(Dog.speak())
print(Cat.speak())
class Point:
    '''representing a point in xy plane'''
    def __init__(self,x=0,y=0): 
        self.x=x
        self.y=y
    def printpoint(self):
        print("(",self.x,",",self.y,")")
    def __del__(self):
        print("Object deleted")
    def compare(P1,P2):
        return (P1.x==P2.x) and (P1.y==P2.y)
P1=Point()
P1.printpoint() # will print (0,0)
P2=Point(10,20)
P2.printpoint() # will print ( 10,20)
print(P1. __doc__) # will print docstring '''representing a point in xy plane'''
del P1 # will call the destructor and print Object deleted 
P1=Point(10,20)
P2=Point(10,20)
print(P1==P2)
print(P1 is P2)