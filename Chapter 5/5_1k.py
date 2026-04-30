"""
Mutable property of lists leads to interesting phenomena.
In the code below, first and second are aliases (i.e., they refer
to the same list)
"""

first = [10, 20, 30]
second = first
print(first)
print(second)
# Returns the list [10, 20, 30] twice.

first[1] = 99   # Replaces position 1 (20) with 99
print(first)
print(second)
# Returns [10, 99, 30] twice
# Both variables (first and second) refer to the same list.

# To prevent aliasing, create a new object and 
# copy the contents of the original to it
third = []
for element in first:           # the for loop adds each element in the list to the empty list third
    third.append(element)
print(first)
print(third)
# Returns two identical lists [10, 99, 30]

first[1] = 100
print(first)
print(second)
print(third)
# Returns [10, 100, 30] for first and second
# Returns [10, 99, 30] for third because we avoided aliasing third to first and second


