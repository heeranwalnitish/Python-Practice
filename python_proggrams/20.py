# Write a program that will tell the number of dog and chicken are there when the user will provide the value of total heads and legs.

def counter(nLegs, nHeads):
    for nChicken in range(0, nHeads +1):
        nDogs = nHeads - nChicken
        total_legs = 4 * nDogs + 2 *nChicken
        if total_legs == nLegs :
            return [nDogs, nChicken]

    return[None, None]

def main():
    legs = int(input("Enter the no. of Legs :"))
    heads = int(input("Enter the no Heads :"))
    Dogs, Chickens = counter(legs,heads)
     
    if Dogs == None:
        print("There is no solution")

    else:
        print(f"{Dogs} Dogs and {Chickens} Chickens")


if __name__ == '__main__':
    main()



