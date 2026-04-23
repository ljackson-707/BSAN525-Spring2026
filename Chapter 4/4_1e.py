"""
When it is used with strings, the left operand of in is a target
substring and the right operand is the string to be searched.

The left operand is the character that I'm looking for in a string.

Returns True if target string is somewhere in the search string,
or False otherwise.
"""

print("g" in "Alan Turing")     # Searches for g in Alan Turing and returns true
print("y" in "Alan Turing")     # Searches for y in Alan Turing and returns false

fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]

for fileName in fileList:
    if ".txt" in fileName:
        print(fileName)

# The "in" in magenta is the one we used for a "for" loop which means loop inside the list. 
# The "in" in violet is the in operator used to see if a substring is in a target string.
# Using in with if is different than using in with for.
