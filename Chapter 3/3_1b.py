# Loop to compute an exponentiation for a non-negative exponent
# 2**3 = 8

number = 2
exponent = 3
product = 1

for eachPass in range(exponent):
    product = product * number
    print(product, end = " ")
    