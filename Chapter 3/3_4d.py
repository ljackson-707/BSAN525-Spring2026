# This example modifies the grade-conversion program from 3_3d.py

while True:
    number = int(input("Enter the numeric grade: "))
    if number >= 0 and number <= 100:
        if number > 89:
            letter = "A"
        elif number > 79:
            letter = "B"
        elif number > 69:
            letter = "C"
        else:
            letter = "F"
        break
    else:
        print("Error: grade must be between 0 and 100")
print("The letter grade is", letter)

# If a valid grade is input, the loop breaks and the letter grade is printed.
# If an invalid grade is input, the loop continues to show the error message.