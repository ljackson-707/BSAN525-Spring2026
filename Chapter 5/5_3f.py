# You can sort the list first then traverse it to print the
# entries of the dictionary in alphabetical order

info = {"occupation":"manager", "name":"Sandy"}

# .items returns key and value together
# .keys returns the keys in the dictionary
# .values returns the values in the dictionary
theKeys = list(info.keys())
theKeys. sort() # This sorts the list of keys in alphabetical order

for key in theKeys:
    print(key, info[key])
# Returns:
# name Sandy
# occupation manager