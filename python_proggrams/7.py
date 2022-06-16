# Write a program that will tell whether the given year is a leap year or not.

year = int(input("Enter the year : "))

if ((year % 4 == 0) and (year % 100 != 0)) or  (year % 400 == 0) :
    print("Leap year")

else:
    print("Not a Leap year")
