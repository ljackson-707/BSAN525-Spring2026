# When a for loop is used with a dictionary, the loop's variable is
# bound to each key in an unspecified order.

# To print all of the keys and their values:
info = {"name":"Sandy", "occupation":"manager"}

for key in info:
    print(key, info[key])   

# Alternative: Use the dictionary method items()
# Returns the dictionary as a list of key/value couples
print(list(info.items()))   
# Returns list of tuples that contain key and value

# Access the key and value of each entry in the list within a for loop:
for (key, value) in info.items():
    print(key, value)
# Returns the same thing as the first for loop