# A Boolean function usually tests its argument for the
# presence or absence of some property.

def odd(x):
    if x % 2 == 1:      # if when i divide x by 2, i get remainder 1
        return True     # that would mean it is odd
    else:
        return False

print(odd(5))
# Returns True
print(odd(6))
# Returns False