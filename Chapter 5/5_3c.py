# Use [] to obtain the value associated with a key.
info = {"name":"Sandy", "occupation":"manager"}
print(info["name"])
# Returns Sandy

# If key is not present in dictionary, an error is raised
# print(info["job"])
# Returns KeyError: 'job'

# An easier strategy is to use the method get.
# If the key is absent, the default value passed to get is returned
print(info.get("job", "Key does not exist"))
# If you don't put a second argument, it just prints None if key doesn't exist
