# Create a class car with attributes model, year and price and a method cost() for displaying the prize. Create two instance of the class and call the method for each instance.(university question)
class car:
    def __init__(self,model,year,price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        print(self.price)

c1 = car("maruthi",2002,48000)
c2 = car("rollce",2003,45000)
c1.cost()
c2.cost()
