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
# print(a)
# print(a["brand"])
# print(a.keys())
# print(a.values())

# Adding Items
a["color"] = "red"
# print(a)
# adding item with update method
a.update({"text": "blue"})
# print(a)

# Removing Items
a.pop("model")
# print(a)
# The popitem() method removes the last inserted item
a.popitem()
# The del keyword removes the item with the specified key name:
del a["brand"]
# print(a)


# Python - Loop Dictionaries
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary,
# but there are methods to return the values as well.
# b = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# for x in b:
#     print(x)

# values loopg
# for x in b:
#     print(b[x])

# values loop
# for x in b.values():
#     print(x)

# keys loop
# for x in b.keys():
#     print(x)

# items loop
# for x, y in b.items():
#     print(x, y)

# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1,
# and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
# c = b.copy()
# print(c)

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
d = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",

        "year": 2011
    }

}
# print(d)

# Accessing Items in Nested Dictionaries
# print(d["child1"]["name"])

# Adding Nested Items
# d["child4"] = {
#     "name": "Sally",
#     "year": 2014
# }
# print(d)

# Removing Nested Items
# d.pop("child3")
# print(d)

# Python - Loop Nested Dictionaries
# You can loop through a nested dictionary by using a for loop.
for x in d:
    print(x)
    for y in d[x]:
        print(d[x][y])