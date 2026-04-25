# You open a file for input in a manner 
# similar to opening a file for output

f = open("myfile.txt", "r")     #opens the file in reading mode
text = f.read()
print(text)
f.close()