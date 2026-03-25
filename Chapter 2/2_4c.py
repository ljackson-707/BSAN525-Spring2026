# You must use a type conversion function
# when working with the input of numbers.
print(int("33"))
print(float("3.14"))
print(float("33"))

# Note that the int function converts a float
# to an int by truncation, not by rounding.
print(int(6.75))

# To round a float to the nearest integer, use the round function.
print(round(6.75))

""""
You can convert a number to a string using the str function
Note that Python is a strongly typed programming language
which means the interpreter checks the types of values before
performing operations on them.
"""
profit = 1000.55
print("$", 1000.55) # <---this puts a space between $ and number
print("$" + str(1000.55)) # <---no space with concatenation