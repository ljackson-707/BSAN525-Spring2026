"""
In scripts that include the definitions of several
cooperating functions, it is often useful to define
a special function named main that serves as the entry
point for the script. 
"""

def square(x):
    return x * x

def main():     # main typically doesn't take arguments, but can
    number = float(input("Enter a number: "))
    result = square(number)
    print("The square of", number, "is", result)

# This is the entry point for program execution.
# Must be called at the end of the script
if __name__ == "__main__":  # if running as a standalone program, call main
    main()  # This called the function main

# __name__ is environment variable