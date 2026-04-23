# Python's subscript operator can be used to obtain a substring through 
# a process called slicing by placing a colon (:) in the subcript.

name = "myfile.txt"

print(name[0:])             # This returns the entire string.
print(name[0:1])            # The first character
print(name[0:2])            # The first two characters
print(name[:len(name)])     # The entire string
print(name[-3:])            # The last three characters
print(name[2:6])            # Drill to extract characters 'file' (characters 2 to 5)

name = "Alan Turing"
print(name[name.find(" ")+1:len(name)])  # This returns the last name Turing