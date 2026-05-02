# To delete an entry from a dictionary, remove its key
# using the method pop.
# pop expects a key and an optional default value as arguments.

info = {"name":"Sandy", "occupation":"manager"}
print(info.pop("job", None))
# pop returns key error without second argument "None"
print(info.pop("occupation", None)) # This deletes the occupation key/value pair
print(info)