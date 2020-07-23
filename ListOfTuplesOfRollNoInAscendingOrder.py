Write python program to get a list of tuples of Rollno,Name for 5 students through keyboard and sort them Rollno wise ascending order


a = []
for lam in range (5):
  name = input("Enter name:")
  roll = int(input("Enter roll no:"))
  a.append((roll,str(name)))
a.sort()
print (a)

INPUT:
Enter name:a
Enter roll no:5
Enter name:s
Enter roll no:1
[(1, 's'), (5, 'a')]
