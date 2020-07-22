Python Program to reverse a number using loop

r=0
n=int(input("Enter a number: "))
while(n>0):
    dig=n%10
    r=r*10+dig
    n=n//10
print("The reversed no  is:")
print(r)

OUTPUT:
Enter a number: 3245
The reversed no  is:
5423
