# Count-controlled loops: loops that count through a range of numbers
# Compute factorial
# 4! = 1 * 2 * 3 * 4 = 24

product = 1
for count in range(4):
    product = product * (count + 1)
print(product)

# To specify an explicit lower bound:
product = 1
for count in range(1,5):
    product = product * count
print(product)