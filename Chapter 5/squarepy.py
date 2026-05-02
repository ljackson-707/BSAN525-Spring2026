# This is the same code from 5_2d.py

def square(x):
    return x * x

def main():     # main typically doesn't take arguments, but can
    number = float(input("Enter a number: "))
    result = square(number)
    print("The square of", number, "is", result)

if __name__ == "__main__":
    main()  # This called the function main
