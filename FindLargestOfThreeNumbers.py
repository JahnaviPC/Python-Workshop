Program to find the largest of three numbers 

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

if (a>b and a>c):
  print("The first number is the largest of all")
elif (b>c):
  print("The second number is the larges of all")
else:
  print("The last number is the largest of all")
  
OUTPUT:
Enter the first number:3
Enter the second number:9
Enter the third number:0
The second number is the larges of all
