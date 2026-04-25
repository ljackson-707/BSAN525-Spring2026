# len and [] work on lists as they do for strings
first = [1, 2, 3, 4]
print(len(first))   # prints 4 because the list is 4 items long
print(first[0])     # prints 1 because it's first in the list
print(first[2:4])   # prints elements 2 to 4, not including 4, meaning 3 and 4 in this list

# Concatenation (+) and equality (==) also work as expected for lists.
first = [1, 2, 3, 4]
second = list(range(1, 5))
print(first + [5, 6])
print (first == second)     # tests to see if the lists are the same, returns True or False

# The in operator detects the presence of an element
print(3 in [1, 2, 3])       #returns True
print(0 in [1, 2, 3])       #returns False