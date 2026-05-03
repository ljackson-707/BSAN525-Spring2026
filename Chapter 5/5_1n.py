# A tuple resembles a list, but is immutable.
# If you wanted to create a list but not have methods
# work on the list, create a tuple.
# You indicate a tuple by enclosing its elements in ()

fruits = ("apple", "banana")
print(fruits)
meats = ("fish", "poultry")
print(meats)

food = meats + fruits
print(food)
# Food is now a tuple that combines the meats and fruits together.

veggies = ["celery", "beans"]
print(tuple(veggies))
# Converted the veggies list to a tuple

# Empty list would be myList = []
# Empty tuple would be myTuple = ()