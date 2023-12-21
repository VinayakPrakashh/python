print("enter coordinates for first line")
x1=float(input("Enter x1: "))
y1=float(input("enter y1: "))
x2=float(input("Enter x2: "))
y2=float(input("e nter y2: "))
print("enter coordinates for second line")
x3=float(input("Enter x1: "))
y3=float(input("enter y1: "))
x4=float(input("Enter x2: "))
y4=float(input("enter y2: "))
 
t1=(x1,y1,x2,y2)
t2=(x3,y3,x4,y4)

def euclidean_distance(p):
  x1, y1,x2 , y2 = p
  return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

distance1 = euclidean_distance(t1)
distance2 = euclidean_distance(t2)
print("Length of the first line: ",distance1)
print("Length of the second line: ",distance2)
if distance1 > distance2:
  print("The first line is longer.")
elif distance1 < distance2:
  print("The second line is longer.")
else:
  print("The two lines are equal in length.")

