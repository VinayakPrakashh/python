# class Employee:
#     def __init__(self, name, salary):
#         self._name = name
#         self._salary = salary

#     def get_name(self):
#         return self._name

#     def get_salary(self):
#         return self._salary

#     def set_salary(self, new_salary):
#         if new_salary > 0:
#             self._salary = new_salary
#         else:
#             print("Salary must be greater than 0.")

# # Creating an instance of Employee
# employee = Employee("Alice", 50000)

# # Accessing data using accessor methods
# print("Name:", employee.get_name())
# print("Salary:", employee.get_salary())

# # Attempting to directly access and modify data (not recommended)
# # This will not work due to encapsulation
# print(employee._name)
# employee._name = "Bob"

# # Changing data using mutator method
# employee.set_salary(55000)
# print("New salary:", employee.get_salary())

# # Trying to set a negative salary (will not change the salary)
# employee.set_salary(-5000)
# print("Salary after trying to set a negative value:", employee.get_salary())


#MRO
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        
        print("B method")
        super().method()

class C(A):
    def method(self):
        print("C method")
        super().method()

class D(B, C):
     def method(self):
        print("D method")
        super().method()

# Print the Method Resolution Order for class D

d = D()
print(d.method())