# Python Learning Guide

This guide is for continuing to build basic proficiency with Python after beginning coursework in BSAN525. It is written for a beginning programmer and is meant to be a practical reference you can return to as you learn.

The main goal is to move from:

> "I can follow examples"

closer to:

> "I can build small programs on my own."

You do not need to know everything to become proficient. Even experienced programmers look things up constantly. The important thing is to keep practicing, understand the basics well, and gradually build confidence.

---

## 1. Where You Are Now

Based on the files in this project, you have already started working with many important Python concepts:

- Printing output with `print()`
- Getting user input with `input()`
- Variables
- Strings
- Integers and floating-point numbers
- Conditional statements with `if`, `elif`, and `else`
- Loops with `for` and `while`
- Lists
- Dictionaries
- Functions
- Reading and writing text files
- Importing libraries
- Basic pandas, NumPy, and matplotlib usage

That is a very good start. These are the foundations of Python programming.

---

## 2. What "Basically Proficient" Means

You are becoming basically proficient with Python when you can:

- Read and understand beginner/intermediate Python scripts
- Write small programs from scratch
- Use variables, strings, numbers, loops, and conditionals confidently
- Use lists and dictionaries to store and organize information
- Create and call your own functions
- Read from and write to files
- Understand common error messages
- Debug simple problems
- Import and use basic libraries
- Use pandas for simple data tasks
- Explain what your code does line by line

Basic proficiency does **not** mean memorizing every Python command. It means knowing enough to solve small problems and knowing how to look up what you do not remember.

---

## 3. Strengthen the Fundamentals

Before moving into advanced topics, become comfortable with these core skills.

### Core Python Skills

Practice using:

```python
print()
input()
int()
float()
str()
len()
range()
```

Practice writing code with:

```python
if
elif
else
for
while
break
```

Practice using these data types:

```python
string
integer
float
list
dictionary
```

A good benchmark is this:

> Can you write a small program from scratch without copying a full example?

Good beginner practice programs include:

- A tip calculator
- A grade average calculator
- A number guessing game
- A simple quiz game
- A grocery list manager
- A text-file agenda generator
- A temperature converter
- A password strength checker

---

## 4. Practice Functions More

Functions are one of the biggest next steps after learning basic syntax.

Beginner code often starts as one long script:

```python
name = input("Enter your name: ")
print("Hello", name)
```

As you improve, you want to organize code into reusable pieces:

```python
def get_name():
    return input("Enter your name: ")


def greet_user(name):
    print("Hello", name)


def main():
    name = get_name()
    greet_user(name)


main()
```

Functions help you:

- Organize your program
- Avoid repeating code
- Test smaller pieces
- Make your code easier to read
- Make your code easier to fix later

### Practice Exercise

Take a program you already wrote and divide it into functions.

For example, your `Assignment 2/activityrandomizer.py` could eventually be organized like this:

```python
def get_user_inputs():
    pass


def load_activities(file_name):
    pass


def choose_random_activities(dataframe, activity_number):
    pass


def write_agenda(output_name, today_date, activity_list):
    pass


def main():
    pass


main()
```

Do not worry about doing this perfectly at first. The goal is to start thinking in smaller pieces.

---

## 5. Learn How to Debug

Debugging is the process of finding and fixing problems in your code.

Programming is not just writing code. A lot of programming is figuring out why code does not work yet.

### Read Error Messages Carefully

Python error messages usually tell you:

- What type of error happened
- Which file it happened in
- Which line it happened on

For example:

```text
ValueError: invalid literal for int()
```

This often means Python tried to convert something into an integer, but the value was not a valid number.

### Use Temporary Print Statements

A simple debugging method is to print values while the program runs:

```python
print("activity_number is:", activity_number)
print("activity_list is:", activity_list)
```

This helps you see what your program is actually doing.

### Test One Piece at a Time

Instead of writing 80 lines and then running the whole program, write a few lines, run them, and then continue.

A good habit:

1. Write a small piece.
2. Run it.
3. Fix errors.
4. Add the next small piece.
5. Repeat.

---

## 6. Learn Data Structures Better

Data structures help you organize information.

### Lists

Lists store ordered collections of values:

```python
activities = ["walk", "read", "cook"]
activities.append("study")
print(activities)
```

Common list skills:

```python
activities[0]
activities.append("new item")
len(activities)
for activity in activities:
    print(activity)
```

### Dictionaries

Dictionaries store key/value pairs:

```python
student = {
    "name": "Leigh",
    "grade": 95,
    "course": "BSAN525"
}

print(student["name"])
```

Common dictionary skills:

```python
student["grade"]
student["major"] = "Business Analytics"
for key in student:
    print(key, student[key])
```

### Lists of Dictionaries

Lists of dictionaries are very useful in business and data programming:

```python
students = [
    {"name": "Maya", "grade": 90},
    {"name": "Chris", "grade": 85},
    {"name": "Jordan", "grade": 92}
]

for student in students:
    print(student["name"], student["grade"])
```

If you can comfortably work with lists of dictionaries, you will be much more capable in Python.

---

## 7. Keep Practicing With Small Projects

Do not try to build a huge application right away. Build small, finished programs.

Small completed programs are better than large unfinished ones.

### Beginner Project Ideas

- Tip calculator
- Temperature converter
- Number guessing game
- Simple calculator
- Password strength checker
- To-do list stored in a text file
- Grade average calculator
- Mad Libs story generator

### Slightly More Advanced Project Ideas

- Expense tracker
- CSV sales summary
- Random meal planner
- Contact book
- Agenda generator
- Flashcard quiz app
- File organizer
- Simple data analysis with pandas

Your `activityrandomizer.py` project is a good beginner project because it uses:

- User input
- Files
- pandas
- Lists
- Loops
- Conditionals
- Random selection
- Output generation

That is exactly the kind of program that builds practical skill.

---

## 8. Learn pandas Gradually

Since this project appears to be connected to business analytics coursework, pandas will likely be important.

Start with the basics.

### Import pandas

```python
import pandas as pd
```

### Read Files

```python
df = pd.read_excel("activities.xlsx")
df = pd.read_csv("sales.csv")
```

### View Data

```python
print(df.head())
print(df.info())
print(df.describe())
```

### Select Columns

```python
names = df["Name"]
print(names)
```

### Filter Rows

```python
high_sales = df[df["Sales"] > 1000]
print(high_sales)
```

### Group Data

```python
summary = df.groupby("Category")["Sales"].sum()
print(summary)
```

### Sort Data

```python
df = df.sort_values("Sales", ascending=False)
print(df)
```

### Write Output

```python
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
```

A useful pandas goal:

> Load data, inspect it, filter it, summarize it, and save a result file.

---

## 9. Start Using Good Coding Habits Early

Good habits matter. They make your code easier to understand and easier to fix.

### Use Meaningful Variable Names

Less clear:

```python
x = 5
y = ["Walk", "Read"]
```

More clear:

```python
activity_count = 5
activity_list = ["Walk", "Read"]
```

### Use Python Naming Style

Python usually uses lowercase words separated by underscores:

```python
activity_number
output_file
today_date
```

Instead of:

```python
activityNumber
outputFile
todayDate
```

Your current style is understandable, but learning standard Python style will help as you continue.

### Add Useful Comments

Good comment:

```python
# Choose a random sample of activities from the spreadsheet
random_activities = df.sample(n=activity_number)
```

Less useful comment:

```python
# Print the list
print(activity_list)
```

Comments should explain why something is being done, not just repeat what the code already says.

---

## 10. Learn Basic Error Handling

A major next step is learning `try` and `except`.

For example, this code can crash if the user types `five` instead of `5`:

```python
activity_number = int(input("Enter the number of activities: "))
```

You can improve it with error handling:

```python
try:
    activity_number = int(input("Enter the number of activities: "))
except ValueError:
    print("Please enter a valid number.")
```

Eventually, you can put this in a loop so the user is asked again until they enter a valid number.

```python
while True:
    try:
        activity_number = int(input("Enter the number of activities: "))
        break
    except ValueError:
        print("Please enter a valid number.")
```

Error handling makes your programs more user-friendly and more professional.

---

## 11. Learn Better File Handling

You have already used file writing like this:

```python
output_file = open("agenda.txt", "w")
output_file.write("Hello")
output_file.close()
```

A better Python habit is to use `with open(...)`:

```python
with open("agenda.txt", "w") as output_file:
    output_file.write("Hello")
```

This automatically closes the file when the indented block finishes.

Use this pattern for most file reading and writing.

---

## 12. Suggested Learning Path

### Stage 1: Beginner Comfort

Focus on:

- Variables
- Input/output
- Strings
- Numbers
- Conditionals
- Loops
- Lists
- Basic functions

Goal:

> Build small scripts without copying every line from an example.

Practice projects:

- Tip calculator
- Number guessing game
- Grade calculator
- Simple quiz

---

### Stage 2: Organized Programs

Focus on:

- Functions
- `main()`
- Splitting programs into logical pieces
- Avoiding repeated code
- Basic error handling

Goal:

> Take a messy script and organize it into readable functions.

Practice projects:

- Rewrite an old assignment using functions
- Create a menu-driven program
- Improve your activity randomizer

---

### Stage 3: Files and Data

Focus on:

- Reading text files
- Writing text files
- Reading CSV files
- Reading Excel files
- pandas basics
- Summarizing data

Goal:

> Load data, analyze it, and save useful output.

Practice projects:

- Expense tracker
- Sales summary
- Contact list
- Agenda generator

---

### Stage 4: Practical Projects

Focus on:

- Small complete programs
- Improving old assignments
- Making programs more robust
- Documenting your code

Goal:

> Build 3 to 5 small projects that you can explain clearly.

Possible projects:

- Personal budget analyzer
- Random meal planner
- Flashcard quiz app
- File organizer
- Basic data dashboard with pandas and matplotlib

---

## 13. Recommended Next Steps for This Project

A very good next learning task would be to improve:

```text
Assignment 2/activityrandomizer.py
```

Suggested improvement order:

1. Rename variables using Python style, such as `activity_number` instead of `activityNumber`.
2. Break the script into functions.
3. Add error handling for invalid number input.
4. Allow lowercase `y` and `n` as approval answers.
5. Check whether the Excel file exists before trying to read it.
6. Prevent the user from requesting more activities than exist in the spreadsheet.
7. Use `with open(...)` instead of manually closing files.
8. Clean up comments so they explain the purpose of the code.
9. Test the program with different inputs.

This would teach many important real-world skills while building on something you already understand.

---

## 14. A Possible Improved Structure for `activityrandomizer.py`

Here is a possible structure to work toward gradually:

```python
import pandas as pd


def get_user_inputs():
    file_name = input("Enter the Excel file name: ")
    today_date = input("Enter today's date: ")
    activity_number = int(input("Enter the number of activities: "))
    output_name = input("Enter the output text file name: ")
    return file_name, today_date, activity_number, output_name


def load_activities(file_name):
    return pd.read_excel(file_name)


def choose_random_activities(dataframe, activity_number):
    random_df = dataframe.sample(n=activity_number)
    return list(random_df["Name"])


def get_approval(activity_list):
    print(activity_list)

    while True:
        approve = input("Approve activity list and generate file? Enter Y for Yes or N for No: ")
        approve = approve.upper()

        if approve == "Y":
            return True
        elif approve == "N":
            return False
        else:
            print("Invalid input. Please enter Y for Yes or N for No.")


def write_agenda(output_name, today_date, activity_list):
    with open(output_name, "w") as output_file:
        output_file.write("Agenda for " + today_date + "\n\n")

        for index in range(len(activity_list)):
            line_number = index + 1
            activity = activity_list[index]
            line = str(line_number) + ". " + activity + "\n"
            output_file.write(line)


def main():
    file_name, today_date, activity_number, output_name = get_user_inputs()
    dataframe = load_activities(file_name)
    activity_list = choose_random_activities(dataframe, activity_number)

    if get_approval(activity_list):
        write_agenda(output_name, today_date, activity_list)
        print("The agenda has been created in the output text file.")
    else:
        print("The program is closed. No file will be generated.")


main()
```

This version is not the final perfect version. It is just a stepping stone toward better organization.

---

## 15. How to Ask for Help

When you ask for help, try to include:

1. What you are trying to do
2. What you expected to happen
3. What actually happened
4. Any error message you received
5. The file or section of code you are working on

For example:

> I am working on `Assignment 2/activityrandomizer.py`. I am trying to make it accept lowercase `y` and `n`. I expected `y` to approve the list, but it says invalid input. Can you help me understand why?

That kind of question makes it much easier to help you learn instead of just giving you an answer.

---

## 16. Encouragement

Learning programming can feel confusing at first because small details matter. That is normal.

You are not expected to remember everything. You are expected to practice, make mistakes, read errors, fix them, and gradually understand more.

The best way to learn Python is:

1. Read examples.
2. Type code yourself.
3. Change the code.
4. Break the code.
5. Fix the code.
6. Build small projects.
7. Repeat.

If you keep doing that, you will become proficient.
