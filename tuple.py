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
a = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = a
print(green)
print(yellow)
print(red)


# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.
# Using a for loop we can iterate through each item in a tuple.
a = ("apple", "banana", "cherry")
for x in a:
    print(x)
