# The if-else statement is the most common
# type of selection statement.
# Also called a two-way selection statement.

import math
# Want to avoid negative number for area

area = float(input("Enter the area: "))
if area > 0:
    radius = math.sqrt(area/math.pi)
    print("The radius is", radius)
else:
    print("Error: the area must be a positive number")

# a = pi * r ** 2
# r **2 = a/pi
# math.sqrt(a/pi) = r