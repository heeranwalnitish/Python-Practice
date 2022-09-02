# write a program to find the sum of first n numbers, where n will be provided by the users.

import numbers


number = int(input("Enter the number : "))
sum = 0 

for i in range(number + 1):
    sum = sum + i
print(sum)