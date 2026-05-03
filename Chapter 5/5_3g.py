# Example: Finding the mode of a list of values.
# The mode of a list of values is the value that appears most frequently.
# The following script inputs a list of words from a text file and prints their mode.

fileName = input("Enter the file name: ")
f = open(fileName, "r")

# Input the text, convert its words to uppercase, and add the words to a list
words = []  # defines empty list for words to go into.
for line in f: 
    for word in line.split():
        words.append(word.upper())  # converts words to uppercase and appends to words list

# Obtain unique words and frequencies, saving these in a dictionary
# Each key will be the word, each value will be number of times word appears in file
theDictionary = {}  # create empty dictionary
for word in words:
    number = theDictionary.get(word, None) # want to get the value associated with the key word
    if number == None:                     # word encountered for the first time 
        theDictionary[word] = 1          #adds the word to the dictionary and its value is 1
    else:   # word was already seen, increment its number
        theDictionary[word] = number + 1
print(theDictionary)

# Returns: 
# Enter the file name: sentence.txt
# {'THE': 2, 'QUICK': 1, 'BROWN': 1, 'FOX': 1, 'JUMPS': 1, 'OVER': 1, 'LAZY': 1, 'DOG': 1}

# Find the mode by obtaining the max value in dictionary and determining its key
theMaximum = max(theDictionary.values())    
for key in theDictionary:
    if theDictionary[key] == theMaximum:
        print("The mode is", key)
        break
# Returns The mode is THE