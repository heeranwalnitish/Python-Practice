# Write a program to find the simple interest when the value of principle, rate of interest and time period is given.

p = float(input("Enter the Principle : "))
r = float(input("Enter the Rate of interest : "))
t = float(input("Enter the time : "))

si = (p * r * t)/100

print(f"The Simple Interest is {si}")