# Python Sets
# Set
# A set is a collection which is both unordered and unindexed.
# Sets are written with curly brackets.
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Set items are unordered, so you cannot be sure in which order the items will appear.
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can add new items.
# Duplicates Not Allowed: Sets cannot have two items with the same value.
# Set Length: To determine how many items a set has, use the len() method.
# Set Items - Data Types: Set items can be of any data type.

# Creating a Set
# a = {"apple", "banana", "cherry"}
# print(a)


# Add Items
# To add one item to a set use the add() method.
# a = {"apple", "banana", "cherry"}
# a.add("orange")
# print(a)

# Add Multiple Items
# To add more than one item to a set use the update() method.
# a = {"apple", "banana", "cherry"}
# a.update(["orange", "mango", "grapes"])
# print(a)

# a = {"apple", "banana", "cherry"} 
# b = {"google", "microsoft", "apple"}
# a.update(b)
# print(a)

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
# a = {"apple", "banana", "cherry"}
# a.remove("banana")
# print(a)

# clear method
# a = {"apple", "banana", "cherry"}
# a.clear()
# print(a)

# del method
# a = {"apple", "banana", "cherry"}
# del a
# print(a)

# Loop Through a Set
# You can loop through the set items by using a for loop.
# a = {"apple", "banana", "cherry"}
# for x in a:
#     print(x)


# join set 
# a = {"apple", "banana", "cherry"}
# b = {"google", "microsoft", "apple"}
# c = a.union(b)
# print(c)

# set constructor
# this is another way to create a set
# this is also called set constructor
# a = set(("apple", "banana", "cherry"))
# print(a)

# Update set 
# a = {"apple", "banana", "cherry"}
# b = {"google", "microsoft", "apple"}
# a.update(b)
# print(a)

