# Python includes a set of string operations called methods that 
# make tasks like coutning the words in a single sentence easy.

sentence = input("Enter a sentence: ")
listOfWords = sentence.split()  # breaks sentence into list of words
print(listOfWords)              # every time it sees a space it counts it as the next word
print("There are", len(listOfWords), "words.")

sum = 0
for word in listOfWords:
    sum += len(word)
print("The average word length is", sum / len(listOfWords))
