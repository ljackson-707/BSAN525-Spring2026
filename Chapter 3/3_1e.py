# Example: bound-delimited summation 
# Adds the numbers together from a lower to an upper bound
# ask the user to define the upper and lower bounds

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
theSum = 0

for number in range(lower, upper + 1):
    theSum = theSum + number

print(theSum)
