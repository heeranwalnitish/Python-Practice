# Write a program to find the volume of the cylinder. Also find the cost when, when the cost of 1 litre of milk is 40Rs

r = float(input("Enter the radius : "))
h = float(input("Enter the height : "))
pie = 22/7
v = pie *r*r*h
print(f"The volume of the cylinder is  {v}")
print(f"The cost is {40 *v/1000}Rs")
