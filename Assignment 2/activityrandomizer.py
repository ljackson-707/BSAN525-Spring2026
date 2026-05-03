"""
Program: activityrandomizer.py
Author: Leigh Jackson

Generates a random list of activities from multiple categories.

Functions used:
1. 
2.
3.
"""

# Import pandas as pd (pd is the abbreviation for pandas)
import pandas as pd

fileName = input("Enter the file name: ")
# Ask the user to enter today's date for logging and output
todayDate = input("Enter today's date: ")
# Ask the user to enter the number of random activities to generate
activityNumber = int(input("Enter the number of activities: "))

# df stands for DataFrame, a pandas function to work with spreadsheets
# pd.read_excel is pandas function to read from Excel file.
df = pd.read_excel(fileName)
randomdf = df.sample(n = activityNumber)  
activityList = list(randomdf["Name"])
print(list(randomdf["Name"]))

approve = input("Approve activity list and generate file? (Y/N): ")
if approve == "Y":
# Open/initialize output file in write mode. This will be used
# to write the agenda using the randomized activity list.
    outputFile = open("agenda.txt", "w")
    outputFile.write("Agenda for " + todayDate + "\n\n")
    for index in range(len(activityList)):      # 4_1c.py example
        lineNumber = index + 1      # index is zero based, numbering needs to start at 1
        activity = activityList[index]
        line = str(lineNumber) + ". " + activity + "\n"     # similar to exercise 4.9
        outputFile.write(line)
    outputFile.close()
    print("The agenda has been created in the output file agenda.txt.")
elif approve == "N":
    print("The program is closed. No file will be generated.")
else:
    print("Invalid input. Please enter Y for Yes or N for No.")


# ** To write to an outputfile, outputFile.write(text)

# Close the file at the end of the program, frees up memory
