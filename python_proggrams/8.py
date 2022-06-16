# Write a program to find the euclidean distance between two coordinates.
x1, y1, x2, y2 = input().split()

e_distance = ((float(x2)-float(x1))**2 + (float(y2) - float(y1))**2)**0.5

print(f"Euclidean Distance is {e_distance}")