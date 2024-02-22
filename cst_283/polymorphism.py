class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("bow")
class Cat(Animal):
    def make_sound(self):
        print("weow")
c = Cat()
d = Dog()
c.make_sound()
d.make_sound()