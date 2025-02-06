# Python Dictionaries
# Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values.

# Creating a Dictionary
a = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
a["model"] = "Fiesta"
print(a)
print(a["brand"])
print(a.keys())
print(a.values())

# Adding Items
a["color"] = "red"
print(a)
# adding item with update method
a.update({"text": "blue"})
print(a)

# Removing Items
a.pop("model")
print(a)
# The popitem() method removes the last inserted item
a.popitem()
# The del keyword removes the item with the specified key name:
del a["brand"]
print(a)
