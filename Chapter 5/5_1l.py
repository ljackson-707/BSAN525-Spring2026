# Object identity - if two variables refer to the exact same object in 
# memory.
# Python's is operator can be used to test for object identity

first = [20, 30, 40]
second = first
third = list(first) # a simple way to create a copy of a list
# Uses the list function on first to put content of first in third
# this is the same as 5.1k append method for third, this is shorthand way

print(first == second)  # object identity (output: True)
print(first == third)   # structural equivalence (output: True)

print(first is second)  # output: True
print(first is third)   # output: False