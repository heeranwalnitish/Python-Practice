# User will input (3 ages). Find the oldest one

a = int(input("Enter the first age : "))
b = int(input("Enter the second age : "))
c = int(input("Enter the third age : "))

max = a
if max < b:
    max = b
if max < c :
    max = c

print(f"{max} is the oldest one")
