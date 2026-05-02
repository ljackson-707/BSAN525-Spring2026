"""
Defining our own functions allows us to organize our code
in existing scripts more effectively. 
Definition of a function consists of a header and a body.
"""

# First we need to define our function using def
# Then we name the function (anything you want)
# Inside parentheses, define a parameter of x, which
# represents the data being passed into this function

def square(x): 
    print(x * x)

square(4)
# Returns 16 because 4 * 4 = 16
# Functions can be called from another file/module/library.

# Place a return statement at each exit point of a function
# when the function should explicitly return a value.
def square(x):
    return x * x

square(4)
# You get no output in terminal because value is returned, not printed
s = square(4)
print(s)
# This prints to terminal 16
