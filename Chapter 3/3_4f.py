# The random module supports several ways to 
# generate random numbers.

import random

for roll in range(10):
    print(random.randint(1, 6), end = " ") #randint returns random number 1,2,3,4,5, or 6
