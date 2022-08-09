# Write a program that will take user input of 4 digit number and check whether the number is narcissist number or not.

"""
    Narcissist number  : An n-Digit number which is the Sum of the nth Powers of its
    Digits is called an n-narcissistic number, or sometimes an Armstrong Number
"""

n = int(input("Enter the number : "))
temp = n 
sum = 0
digit = len(str(n))

while temp > 0 :
    d = temp % 10
    sum += d ** digit
    temp = temp // 10

if n == sum:
    print(f"{n} is an Narcissist number ")

else :
    print(f"{n} is not an Narcissist number ")
