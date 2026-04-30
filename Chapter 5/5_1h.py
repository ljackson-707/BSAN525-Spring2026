# extend performs a similar operation, but adds the
# elements of its list argument to the end of the list.
# puts the two lists together and replaces the list with
# the extended list.
# it's like append but a bunch of additional elements
example = [1, 2, 3]
example.extend([11, 12, 13])
print(example)
# Returns [1, 2, 3, 11, 12, 13]

# The method pop is used to remove an element at a given position
example.pop()   # Remove the last element
print(example)
# Returns [1, 2, 3, 11, 12]
example.pop(0)  # Remove the first element
print(example)
# Returns [2, 3, 11, 12]

# To use pop, you need to know the element's index or position in the list
# To remove an element whose position you don't know, use remove method

example.remove(11)  # This removes 11 from the list
print(example)
# Returns [2, 3, 12]