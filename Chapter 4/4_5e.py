# In cases where you might want to read a specified number
# of lines from a file, (say, first line only),
# you can use the file mthod readline
# readline() doesn’t take any arguments and reads each line one at a time

f = open("myfile.txt", "r")

while True:
    line = f.readline()
    if line == "":      # we reached the end of the file (use in 4.10)
        break
    print(line)
f.close()

# Tells the program to keep running the readline until you hit an empty string, meaning the end of the file
