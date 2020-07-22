Write a program for finding surface areas of cylinder and cone using function.

#(2*PI*r*r*h, 1/3*PI*r*r*h)
def surfcyl (r,h):
  print("The surface area of the cylinder is:", 2*3.142*r*r*h)
def surfcon (r,h):
  print("The surface area of the cone is:", (1/3)*3.142*r*r*h)

r = int(input("enter the radius:"))
h = int(input("enter the height:"))

surfcyl(r,h)
surfcon(r,h)


