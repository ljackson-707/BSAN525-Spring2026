# Note that the code uses a for loop over an index rather than
# a for loop over the list of elements, because the index is needed
# to access the positions for the replacements.

# sentence.split() splits by the space character 
# unless you include something in the parentheses,
# then it will split by that character, and it 
# removes the character by which it splits.

sentence = "This example has five words."
words = sentence.split()        # Creates a list from a string
print(words)
# Returns ['This', 'example', 'has', 'five', 'words.']

# words = sentence.split("i")
# print(words)

for index in range(len(words)):
    words[index] = words [index].upper()

print(words)
# Returns ['THIS', 'EXAMPLE', 'HAS', 'FIVE', 'WORDS.']
# Converts all letters to uppercase in the list that was created from a string.