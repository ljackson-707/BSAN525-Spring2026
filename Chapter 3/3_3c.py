# Print the maximum and minimum of two input numbers.
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first > second:
    maximum = first
    minimum = second
else:
    maximum = second
    minimum = first
print("Maximum:", maximum)
print("Minimum:", minimum)

# Note: Python includes two built-in functions, max and min,
# that make the if-then statement above unnecessary
print("Maximum:", max(first, second))
print("Minimum:", min(first, second))
