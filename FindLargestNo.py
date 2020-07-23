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

    
x=0
print('The greatest no is',max([int(input(x)) for _ in range(int(input("Enter no")))]))

OUTPUT:
Enter no5
2
3
1
6
2
The greatest no is 6
