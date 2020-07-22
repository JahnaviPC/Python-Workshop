Python Program to detect if two strings are anagrams

s1=input("Enter first string:")
s2=input("Enter second string:")
if(sorted(s1)==sorted(s2)):
      print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")
      
OUTPUT:
Enter first string:abc
Enter second string:lkj
The strings aren't anagrams.
