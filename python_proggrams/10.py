# Write a program  that takes a user input of cost price and selling price and determines whether its a loss or a profit.

cp = float(input("Enter the Cost Price : "))
sp = float(input("Enter the Selling Price: "))

if sp < cp :
    print(f"LOSS ocurred {cp-sp}")

else :
    print(f"Profit gained {sp-cp}")