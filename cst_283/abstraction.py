from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Car is being driven"

class Motorcycle(Vehicle):
    def drive(self):
        return "Motorcycle is being driven"

# Creating objects of Car and Motorcycle
car = Car()
motorcycle = Motorcycle()

# Calling drive method on objects
print(car.drive())         # Output: Car is being driven
print(motorcycle.drive())  # Output: Motorcycle is being driven
