""""
Python includes many usseful functions,
which are organized in libraries of code called modules.
Functions often require arguments,
referred to by names known as parameters.
"""

# The math module includes functions that
# perform basic mathematical operations.
# We have to import the module first
import math

print(math.pi)
print(math.sqrt(2))

"""
If you are going to use only a couple of a module's resources,
you can just import the individual resources,
which saves memory and makes your program run faster.
"""
from math import sqrt, pi 
# this says only give me these two functions and
# you no longer have to do math. for these
print(pi)
print(sqrt(2))