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
7. while True - conditional iteration loop to repeat the prompt until the user enters Y or N to break the loop (3.4 Conditional Iteraion: The while Loop)
8. if, elif, else - selection statement to perform different functions based on user input and respond with error message if needed (Y/N/other) (3.3 Selection: if and if-else Statements)
9. for index in range - Loop that repeatedly calls the functions assigned to the loop over the specified range (3.1 Definite Iteration: The for Loop)
10. range() - used in a count-controlled loop to specify the range is the length of the loop is the length of the activityList (3.1 Definite Iteration: The for Loop)
11. len() - returns the integer value of a string's length, used in determining the range of the for loop in this case (4.1 Accessing Characters and Substrings in Strings)
12. str() - Converts an int to a string so it may be concatenated with other strings (2.2 Strings, Assignment, and Comments)
13. outputFile.write() - accepts a single string argument (the numbered activity list) and writes the string to a file object (4.5 Text Files)
14. outputFile.close() - closes the output file to avoid data being lost and free up memory (4.5 Text Files)
15. break - break statement that stops the iteration of the while True loop, in this case if the user enters Y or N for input, the loop breaks (3.4 Conditional Iteration: The while Loop)
16. \n - newline character that starts a new line in the string (2.2 Strings, Assignment, and Comments)
"""

# Import pandas library as pd abbreviation to use pandas functionality (Section 11.3)
import pandas as pd

fileName = input("Enter the Excel file name: ")
todayDate = input("Enter today's date: ")
activityNumber = int(input("Enter the number of activities: "))
outputName = input("Enter the output text file name: ")

df = pd.read_excel(fileName)
randomdf = df.sample(n = activityNumber)  
activityList = list(randomdf["Name"])
print(list(randomdf["Name"]))

# Using a while True loop to ensure the user enters a valid Y or N to approve or disapprove of the activity list, or is re-prompted to do so (Section 3.4)
# Using an if, elif, else multiway if statement to generate different outputs depending on whether the user inputs Y, N, or something else (Section 3.3)
while True:
    approve = input("Approve activity list and generate file? (Y/N): ")
    if approve == "Y":
        outputFile = open(outputName, "w")
        outputFile.write("Agenda for " + todayDate + "\n\n")
        for index in range(len(activityList)):     
            lineNumber = index + 1      
            activity = activityList[index]
            line = str(lineNumber) + ". " + activity + "\n"     
            outputFile.write(line)
        outputFile.close()
        print("The agenda has been created in the output text file.")
        break
    elif approve == "N":
        print("The program is closed. No file will be generated.")
        break
    else:
        print("Invalid input. Please enter Y for Yes or N for No.")