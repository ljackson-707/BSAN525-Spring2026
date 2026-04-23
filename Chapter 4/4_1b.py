# The subscript operator [] allows access to a single character 
# in a string at a given position

name = "Alan Turing"
print(name[0])              # Examine the first character
print(name[3])              # Examine the fourth character (count starts at 0)
# print(name[len(name)])      # Oops! An index error! You're asking for index 11 even though there are only 10
print(name[len(name) - 1])  # Examine the last character
print(name[-1])             # Shorthand for the last character
print(name[-2])             # Shorthand for next to last character

# The string is an immutable data structure - the characters can be
# accessed but they cannot be replaced, inserted, or removed

# name[0] = "a"   # Oops! A type error!