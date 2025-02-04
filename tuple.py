# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Allow duplicate values: Since tuples are indexed, they can have items with the same value:
# Tuple Length: To determine how many items a tuple has, use the len() method:
# Create Tuple With One Item: To create a tuple with only one item, you have to add a comma after the item, unless Python will not recognize it as a tuple.
# Tuple Items - Data Types: Tuple items can be of any data type:

# a = ("apple", "banana", "cherry")
# print(a)
# def main():
#     # Creating a tuple
#     tuple_example = ("apple", "banana", "cherry")
#     print(tuple_example)
    
    
# main()


# unpack tuple 
# a = ("apple", "banana", "cherry")
# (green, yellow, red) = a
# print(green)


# Using Asterisk
# a = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = a
# print(green)
# print(yellow)
# print(red)


# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.
# Using a for loop we can iterate through each item in a tuple.
# a = ("apple", "banana", "cherry")
# for x in a:
#     print(x)


# Join Two Tuples
# To join two or more tuples you can use the + operator:
# a = ("apple", "banana", "cherry")
# b = (1, 2, 3)
# c = a + b
# print(c)


# Check if Item Exists in a Tuple
# To determine if a specified item is present in a tuple use the in keyword:
# a = ("apple", "banana", "cherry")
# if "apple" in a:
#     print("Yes, 'apple' is in the fruits tuple")
# else: 
#     print("No, 'apple' is not in the fruits tuple")


# Tuple Methods
# Python has two built-in methods that you can use on tuples.
# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
    # index()    Returns the index of the first occurrence of a specified value in a tuple
# a = ("apple", "banana", "cherry")
# print(a.count("apple"))

# a = ("apple", "banana", "cherry")
# print(a.index("cherry"))


