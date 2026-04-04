# Alternative: Use a Boolean variabe to control loop

# Boolean variable done helps us keep track of if the user put an invalid input.

done = False
while not done:
    number = int(input("Enter a numeric grade: "))
    if number >= 0 and number <= 100:
        if number > 89:
            letter = "A"
        elif number > 79:
            letter = "B"
        elif number > 69:
            letter = "C"
        else:
            letter = "F"
        done = True
    else:
        print("Error: grade must be between 0 and 100")
print("The letter grade is", letter)