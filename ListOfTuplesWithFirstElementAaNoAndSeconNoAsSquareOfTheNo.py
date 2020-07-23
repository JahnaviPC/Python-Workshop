Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number

urange = int(input("Enter the upper range:"))
lrange = int(input("Enter the lower range:"))
man = [(x,x**2) for x in range(urange,lrange)]
print (man)

OUTPUT:
Enter the upper range:2
Enter the lower range:5
[(2, 4), (3, 9), (4, 16)]
