# Write a program that will take three digits from the user and add the sequence

num = input("Enter a 3 digit number")

if len(num) == 3:

    a= int(num[0])
    b = int(num[1])
    c = int(num[2])

    sum = a**2 + b**2 + c**2
    print(sum)

else:
    print("Please enter a 3 digit number")