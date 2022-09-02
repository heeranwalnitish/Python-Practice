# Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%)
# and tax (if salary is between 5-10 lakh - 10%), (11-20lakh - 20%), (more than 20lakh - 30%), (0-1lakh print k).

sal = int(input("Enter your Salary : "))
after_HRA = sal - (10/100 *sal)
after_DA = after_HRA - (5/100 * after_HRA)
after_PF = after_DA - (3/100 * after_DA)

if sal > 0 and sal <= 100000 :
    print(f"Your in-hand salary is {after_PF}")

elif sal > 500000  and sal <= 1000000 :
    after_tax = after_PF - (10/100 * after_PF)
    print(f"Your in-hand salary is {after_tax}")

elif sal > 1100000 and sal <=2000000 :
        after_tax = after_PF - (20/100 * after_PF)
        print(f"Your in-hand salary is {after_tax}")

elif sal > 2000000 :
        after_tax = after_PF - (20/100 * after_PF)
        print(f"Your in-hand salary is {after_tax}")
