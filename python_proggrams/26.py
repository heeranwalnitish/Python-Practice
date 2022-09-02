# Write a program to print whether a given number is prime number of not
from enum import Flag


def is_prime(n):
    flag = False

    if n > 1:
        for i in range(2, n):
            if (n % i ) == 0 :
                flag = True
                break

    if flag :
        print(f"{n} is not a prime number")

    else :
        print(f"{n} is a prime number")

def main():
    number = int(input("Enter the number : "))
    is_prime(number)

if __name__ == '__main__':
    main()

