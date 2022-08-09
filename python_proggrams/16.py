# Write a program that will check whether the number is armstrong number or not.

"""
    Armstrong number is a number that is equal to the sum of cubes of its digits.
"""
n = int(input("Enter the number :"))
digit = len(str(n))
sum = 0
number = n

while n > 0:
    d = n % 10
    sum = sum + d**digit
    n = n // 10


if sum == number :
    print(f"{number} is an Armstrong number ")

else :
    print(f"{number} is not an Armstrong number ") 