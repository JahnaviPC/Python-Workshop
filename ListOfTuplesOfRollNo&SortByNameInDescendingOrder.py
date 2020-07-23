Write python program to get a list of tuples of Rollno,Name for 5 students through keyboard and sort them by Name wise descending order


a = []
for lam in range (5):
  name = input("Enter name:")
  roll = int(input("Enter roll no:"))
  a.append((roll,str(name)))
a.sort(key = lambda x:x[1], reverse = True)
print (a)

Enter name:a
Enter roll no:2
Enter name:f
Enter roll no:2
[(2, 'f'), (2, 'a')]
