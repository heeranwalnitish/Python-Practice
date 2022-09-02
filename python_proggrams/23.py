# Write a program that can multiply 2 numbers provided by the user without using the * operator.
def multiply_by_2(n):
    return (n + n)

def main():
    num = int(input("Enter the number : "))
    print(multiply_by_2(num))

if __name__ == '__main__':
    main()
