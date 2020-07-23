Program to find the largest number in a list.

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[n-1])


OUTPUT:
Enter number of elements:5
Enter element:2
Enter element:3
Enter element:1
Enter element:6
Enter element:2
Largest element is: 6
