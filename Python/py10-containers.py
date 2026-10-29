# lists [] = used to store multiple items in a single variable
# tuples () = used to store multiple items in a single variable
# sets {} = used to store multiple items in a single variable

# ===========================

# Lists : mutable, most flexible, allows duplicates
print("LISTS")
fruit = ["apple", "banana", "cherry"]

fruit.append("orange") # add an item to the list
fruit.remove("banana") # remove an item from the list
# fruit.pop(1) # remove an item at a specific index
# fruit.clear() # remove all items from the list

for item in fruit:
    print(item, end=" ")

print("\n")
# ===========================

print("TUPLES")
# tuples : immutable, faster, allows duplicates
cars = ("tesla", "bmw", "mercedes")

print(cars.count("bmw")) # count the number of occurrences of an item
print(cars[1]) # access an item by index
for car in cars:
    print(car, end=" ")

print("\n")
# ===========================

print("SETS")
# sets : mutable, no duplicates, unordered
# can't access items in a set by index, but can iterate through them

colors = {"red", "blue", "green", "green", "green"}

colors.add("yellow") # add an item to the set
colors.remove("blue") # remove an item from the set
print(colors)