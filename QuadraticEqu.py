Python Program to Solve Quadratic Equation

# Solve the quadratic equation ax**2 + bx + c = 0
# importing  complex math module
import cmath

 # To take coefficient input from the users
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


OUTPUT:
Enter a: 2
Enter b: 4
Enter c: 6
The solution are (-1-1.4142135623730951j) and (-1+1.4142135623730951j)
