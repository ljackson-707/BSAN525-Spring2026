"""
All of the functions and methods examined in the previous chapters return
a value that the caller can then use to complete its work.
Mutator methods (e.g., insert, append, extend, pop, sort) usually
return no value of interest to the caller.
The caller is whoever is calling the method.
"""
# Example of previous chapter methods
# age = input("What is your age?")    # returns a value, assigned back to age

# This doesn't work on lists!
aList = [4, 2, 10, 8]
aList = aList.sort()
print(aList)
# Returns None
# This string method works for strings, but NOT on lists!
# You're assigning aList to nothing and get None back

