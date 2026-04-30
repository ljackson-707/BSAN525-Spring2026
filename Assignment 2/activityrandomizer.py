"""
Program: activityrandomizer.py
Author: Leigh Jackson

Generates a random list of activities from multiple categories.

Functions used:
1. 
2.
3.
"""

# Import the random module and pandas as pd (pd is the abbreviation for pandas)
import random   # may not need this library if using pandas functions
import pandas as pd

# Ask the user to enter today's date for logging and output
todayDate = input("Enter today's date: ")
# Ask the user to enter the number of random activities to generate
activityNumber = int(input("Enter the number of activities: "))

# df stands for DataFrame, a pandas function to work with spreadsheets
# pd.read_excel is pandas function to read from Excel file.
df = pd.read_excel("activities.xlsx")
randomdf = df.sample(n = activityNumber)  
print(list(randomdf["Name"]))

# Open/initialize output file in write mode. This will be used
# to write the agenda using the randomized activity list.
outputFile = open("agenda.txt", "w")
