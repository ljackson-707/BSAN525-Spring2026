# Our next example function computes the average value in a list of  numbers
def average(lyst):      # list is a reserved word in Python
    theSum = 0
    for number in lyst: # loop through the list being passed in
        theSum += number
    return theSum / len(lyst)   # this gives the average

print(average([1, 3, 5, 7]))
# Returns 4.0 because we have division making it a float


