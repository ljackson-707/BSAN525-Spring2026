# String methods (see Table 4-2)

s = "Hi there!"

print(s.center(11))
print(s.count("e"))
print(s.endswith("there!"))
print(s.startswith("Hi"))
print(s.find("the"))    # Returns the position before "the" starts
print(s.isalpha())      # Doesn't accept arguments. True if string is alphabetic, false if not.
#This one returns false because there is a space character and a ! character

print(s.isdigit())
print(s.lower())        # Returns the string in lower case, doesn't change the string itself
print(s)
s = s.lower()           # Changes the string to lower case
print(s)
print(s.upper())
print(s.replace("i", "ey"))

print(s.split())        # split takes a string and makes it a list. splits by whatever like a space or new line,
print(s.split("e"))     # unless you specify a character