# String representations of integers and floating-point
# numbers can be converted to numbers by using  the 
# functions int and float.

f = open ("integers.txt", "r")

theSum = 0
for line in f: 
    line = line.strip()     # removes the \n at the end of the line (not necessary to use int)
    number = int(line)
    theSum += number
print("The sum is", theSum)
f.close()