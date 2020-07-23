Write python program to get a list of tuples of Rollno,Name for 5 students through keyboard and sort them by Rollno wise descending order

a = []
for lam in range (5):
  name = input("Enter name:")
  roll = int(input("Enter roll no:"))
  a.append((roll,str(name)))
a.sort(reverse = True)
print (a)


Enter name:k
Enter roll no:2
Enter name:l
Enter roll no:3
[(3, 'l'), (2, 'k')]
