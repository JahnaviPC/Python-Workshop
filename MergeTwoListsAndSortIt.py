Python Program to merge two lists and sort it.

a=[]
c=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    a.append(b)
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    c.append(d)
new=a+c
new.sort()
print("Sorted list is:",new)




x=0
l=[int(input(x)) for _ in range(int(input("Enter how many elements")))]
m=[int(input(x)) for _ in range(int(input("Enter how many elements ")))]
new=l+m
new.sort()
print("Sorted list is:",new)
