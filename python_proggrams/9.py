# Write a program that takes a user of three angles and will find out whether it can form a triangle or not.

a = float(input("Enter the first angle : "))
b = float(input("Enter the second angle : "))
c = float(input("Enter the third angle : "))

if a+b+c == 180:
    print("Triangle can be formed")

else:
    print("NO!!! Triangle can not be formed")