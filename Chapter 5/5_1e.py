# A list is mutable - Elements can be inserted, removed, or replaced
example = [1, 2, 3, 4]

example[3] = 0
print(example)  # Replaces index 3 in list (4) with 0
# Returns [1, 2, 3, 0]

# List processing example that shows how to replace 
# each number in a list with its square
numbers = [2, 3, 4, 5]

# not looping through the list, looping through index of list
for index in range(len(numbers)):
    numbers[index] = numbers[index] ** 2
print(numbers)
# Returns [4, 9, 16, 25]

# When we call a method on the list, it changes the list.
# We do not have to assign it back to itself after
# changing it like we do with strings.