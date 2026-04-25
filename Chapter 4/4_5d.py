# A for loop can be used to read 
# one line of a file at a time.

f = open("myfile.txt", "r")

for line in f:
    print(line)
f.close()
