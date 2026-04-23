# The subscript operator is also useful in loops where you want
# to use the positions as well as the characters in a string.

data = "Hi there!"

for index in range(len(data)):
    print(index, data[index])

