# Write a program that will give you 3 digit
num = input(" Enter a three digit no : ")
sum = 0
for i in num:
    sum = sum + int(i)

print(f"The sum of 3 digit number is {sum}")