Write python program to get a list of tuples of Rollno,Name for 5 students through keyboard and sort them by Name wise ascending order


a = []
for lam in range (5):
  name = input("Enter name:")
  roll = int(input("Enter roll no:"))
  a.append((roll,str(name)))
a.sort(key = lambda x:x[1])
print (a)


Enter name:hus
Enter roll no:5
Enter name:abs
Enter roll no:7
[(7, 'abs'), (5, 'hus')]
