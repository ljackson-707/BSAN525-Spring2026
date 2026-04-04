# The process of testing several conditions and responding accordingly
# can be described in code by a multiway selection statement.

number = int(input("Enter the numeric grade: "))

if number > 89:
    letter = "A"
elif number > 79:
    letter = "B"
elif number > 69:
    letter = "C"
else:
    letter = "F"

print("The letter grade is", letter)
