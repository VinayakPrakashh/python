class car:
  def __init__(g,base,height):
    g.base=base
    g.height=height
       
  @classmethod
  def area(self,base,height):
        z=0.5*base*height
        return z
  @classmethod
  def peri(self,base,height):
     p=2*(base+height)
     return p
     
area = car.area(2,5)
print(area)

c=car.peri(2,3)
print(c)
