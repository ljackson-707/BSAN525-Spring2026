"""
The list type includes several methods for
inserting and removing elements.
The method insert expects an integer index
and the new element as arguments.
"""

example = [1, 2]
example.insert(1, 10)    # insert 10 at position 1
print(example)
# This returns [1, 10, 2]

example.insert(3, 25)
print(example)      # inserts 25 at position 3
# Returns [1, 10, 2, 25]
# This is the same as appending a number at the end of the list

# append expects a new element as an argument and
# adds it to the end of the list
example = [1, 2]
example.append(3)
print(example)
# Returns [1, 2, 3]

