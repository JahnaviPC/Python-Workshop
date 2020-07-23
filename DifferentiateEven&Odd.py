Python Program to put the even and odd elements in a list into two different lists.

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)

INPUT:
Enter number of elements:4
Enter element:1
Enter element:2
Enter element:3
Enter element:4
The even list [2, 4]
The odd list [1, 3]

x=0
l=[int(input(x)) for _ in range(int(input("Enter n")))]
print('even list is',[ i for i in l if i%2])
print('odd list is',[i for i in l if not i%2])

OUTPUT:
Enter n4
1
2
3
4
even list is [1, 3]
odd list is [2, 4]
