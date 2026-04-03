# range returns a list (sequence of numbers)

print(list(range(4)))    
print(list(range(1,5)))

# You can use for loops to visit each value in a list
for number in [0, 1, 2, 3]:
    print(number, end = " ")

# Strings are also sequences of characters
# in which values can be visited with a for loop
for character in "Hi there!":
    print(character, end = " ")