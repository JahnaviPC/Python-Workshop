Python Program to form a string where the first character and the last character have been exchanged.

def change(string):
      return string[-1:] + string[1:-1] + string[:1]
string=input("Enter string:")
print("Modified string:")
print(change(string))

OUTPUT:
Enter string:jahnavi
Modified string:
ivanhaj
