"""
Program: activityrandomizer.py
Author: Leigh Jackson

Generates a random list of activities from a pandas DataFrame created from an Excel spreadsheet.

Functions used:
1. input() - Accepts input file name, today's date, number of activities, output text file name, and Y/N confirmation from user input (1.4 Getting Started with Python Programming)
2. int() - Converts the user input to integers so that the variable can be used as sample size n (1.4 Getting Started with Python Programming)
3. pd.read_excel() - pandas library function that reads Excel file into a DataFrame (https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
4. df.sample() - pandas library function that takes a random sample of rows from the DataFrame (https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
5. list() - Converts the sample from the DataFrame into a list of strings with the activity names (5.1 Lists)
6. print() - Prints activity list for approval and confirmation prompts to the terminal for user feedback. (1.4 Getting Started with Python Programming)
7. while True - conditional iteration loop to repeat the prompt until the user enters Y or N to break the loop (3.4 Conditional Iteration: The while Loop)
8. if, elif, else - selection statement to perform different functions based on user input and respond with error message if needed (Y/N/other) (3.3 Selection: if and if-else Statements)
9. for index in range - Loop that repeatedly calls the functions assigned to the loop over the specified range (3.1 Definite Iteration: The for Loop)
10. range() - used in a count-controlled loop to specify the range is the length of the loop is the length of the activityList (3.1 Definite Iteration: The for Loop)
11. len() - returns the integer value of a string's length, used in determining the range of the for loop in this case (4.1 Accessing Characters and Substrings in Strings)
12. str() - Converts an int to a string so it may be concatenated with other strings (2.2 Strings, Assignment, and Comments)
13. outputFile.write() - accepts a single string argument (the numbered activity list) and writes the string to a file object (4.5 Text Files)
14. outputFile.close() - closes the output file to avoid data being lost and free up memory (4.5 Text Files)
15. break - break statement that stops the iteration of the while True loop, in this case if the user enters Y or N for input, the loop breaks (3.4 Conditional Iteration: The while Loop)
16. \n - newline character that starts a new line in the string (2.2 Strings, Assignment, and Comments)
17. open() - opens the output file in write mode so the string can be copied to the output file (4.5 Text Files)
"""

# Import pandas library as pd abbreviation to use pandas functionality (Section 11.3)
import pandas as pd

# Asks the user for the input Excel file name (Section 1.4)
fileName = input("Enter the Excel file name: ")
# Asks the user to input today's date, to be used in the output file (Section 1.4)
todayDate = input("Enter today's date: ")
# Asks the user to input the number of activities and converts it to an integer to be used as sample size (Section 1.4)
activityNumber = int(input("Enter the number of activities: "))
# Asks the user to input the name of the output file to be generated (Section 1.4)
outputName = input("Enter the output text file name: ")

# pandas function to read an Excel file into a Pandas DataFrame
df = pd.read_excel(fileName)
# pandas function to generate a random sample of rows from the DataFrame with size n.
randomdf = df.sample(n = activityNumber)
# Generates a list of items from the Name column in the randomdf sample (Section 5.1)
activityList = list(randomdf["Name"])
# Prints the generated activity list to the terminal for user review (Section 1.4)
print(list(randomdf["Name"]))

# Using a while True loop to ensure the user enters a valid Y or N to approve or disapprove 
# of the activity list, or is re-prompted to do so. If the user inputs Y or N, the loop will 
# break, or else if there is any other input, the loop continues. (Section 3.4)
while True:
# Asks the user to input Y to approve list or N if not (Section 1.4)
    approve = input("Approve activity list and generate file? Enter Y for Yes or N for No: ")
# Using an if, elif, else multiway if statement to generate different outputs depending on whether the user inputs Y, N, or something else (Section 3.3)
# Checks if user input for approve is equal to Y (Section 3.3)
    if approve == "Y":
# Opens an output file with the outputName in write mode (Section 4.5)
        outputFile = open(outputName, "w")
# Writes a concatenated string with input from todayDate to the output file (Section 4.5)
        outputFile.write("Agenda for " + todayDate + "\n\n")
# Using a for loop to loop through the range of items in activityList (Section 3.1)
        for index in range(len(activityList)):
# Sets lineNumber variable as index + 1 because indexes are zero-based, and the numbered list in the output file needs to start at 1 (Section 4.5)     
            lineNumber = index + 1
# Inspects the item in the activity list at the index in the subscript operator (Section 5.1)     
            activity = activityList[index]
# Creates a line for the output file from the lineNumber converted to a string so it can be concatenated with the activity and a newline, so that each activity is printed on a new line (Section 2.2)
            line = str(lineNumber) + ". " + activity + "\n"
# Writes the line to an output file (Section 4.5)    
            outputFile.write(line)
# The for loop has ended and the output file is no longer needed, so this function closes the file (Section 4.5)
        outputFile.close()
# Prints a confirmation that the output file has been created in the terminal (Section 1.4)
        print("The agenda has been created in the output text file.")
# Breaks the while True loop since the program has completed (Section 3.4)
        break
# Checks if user input for approve is equal to N, which means the user did not approve the activity list and program is terminated (Section 3.3)
    elif approve == "N":
# Prints confirmation to the terminal that the program has ended and no file is generated (Section 1.4)
        print("The program is closed. No file will be generated.")
# Breaks the while True loop since the program has completed (Section 3.4)        
        break
# Checks if anything else, other than Y or N was input into the approve prompt (Section 3.3)
    else:
# Prints an error message to terminal showing that the input was invalid, and asks for proper input (Section 1.4)
        print("Invalid input. Please enter Y for Yes or N for No.")
# If the while True loop was not broken by a Y or N input, the loop will repeat from the top. 