# the in operator determines an element's presence or absence,
# but it does not return the position of the element (if found).
# in gives True if it's in there, False if it is not

aList = [34, 45, 67]
target = 45

if target in aList:
    print(aList.index(target))  # prints the index of target
else:
    print(-1)    # means it is not in the list
# Returns 1 because 45 is at index 1 in the list

# The method sort mutates a list by arranging its elements in
# ascending order
example = [4, 2, 10, 8]
example.sort()
print(example)