Python Program to Convert Kilometers to Miles

# To take kilometers from the user, uncomment the code below
kilometers = int(input("Enter value in kilometers"))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.3f kilometers is equal to %0.3f miles' %(kilometers,miles))


OUTPUT:
Enter value in kilometers20
20.000 kilometers is equal to 12.427 miles
