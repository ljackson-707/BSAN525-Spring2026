# The file method write expects a string as an argument.
# Other types of data must first be converted to strings
# before being written to an output file (e.g. using str function)

import random 

f = open("integers.txt", "w")
for count in range(500):
    number = random.randint(1, 500)     # this is actually 1 to 499, doesn't include 500
    f.write(str(number) + "\n")         # it will write the number and go to the next line
f.close()                               # be sure to close outside of loop (unindent)

