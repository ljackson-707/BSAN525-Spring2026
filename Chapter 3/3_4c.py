# The while loop can be complicated to write correctly;
# It is possible to simplify its structure and improve its readability

theSum = 0.0

while True:
    data = input("Enter a number or just enter to quit: ")
    if data == "":  # user pressed enter?
        break
    number = float(data)
    theSum += number

print("The sum is", theSum)

# This if statement didn't need an else because if the condition is true,
# the loops breaks anyway. If it isn't true, lines 10 and 11 run.