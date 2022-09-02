# Write a menu driven program - 1) cm to ft  2) km to miles  3) usd to inr  4) exit

from matplotlib.style import use


user_input = input("""
What would you like to do :

1) Convert cm to inches
2) Convert km to miles
3) Convert USD to INR
4) Exit
""")

if user_input == '1' :
    cm = float(input("Enter the value in cm "))
    inch = cm * 0.394
    print("The value in inches is ", inch)

elif user_input == '2' :
    km = float(input('Enter value in km '))
    mile = km * 0.621
    print('The value in miles is  ', mile)

elif user_input == '3':
    usd = float(input("Enter value in USD "))
    inr = usd * 76.63
    print('The value in INR is ', inr)

else:
    print("Exit")