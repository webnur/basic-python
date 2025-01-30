# python list 
# list is a collection which is ordered and changeable. Allows duplicate members.
# In Python lists are written with square brackets.
# For example:
# list
# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# Access Items
# You access the list items by referring to the index number:
# Example
# Get the second item of the list:
# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# Change Item Value
# To change the value of a specific item, refer to the index number:
# Example
# Change the second item:
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# Loop Through a List
# You can loop through the list items by using a for loop:
# Example
# Print all items in the list, one by one:
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
# Example
# Check if "apple" is present in the list:
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# List Length
# To determine how many items a list has, use the len() function:
# Example
# Print the number of items in the list:
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# Add Items
# To add an item to the end of the list, use the append() method:
# Example
# Using the append() method to append an item:
# thislist = ["apple", "banana", "cherry"]

# thislist.append("orange")
# print(thislist)

# To add an item at the specified index, use the insert() method:
# Example
# Insert an item as the second position:
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# Remove Items
# There are several methods to remove items from a list:
# Example
# The remove() method removes the specified item:
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified):
# Example
# Remove the second item:
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# The del keyword removes the specified index:
# Example
# Remove the first item:
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# The del keyword can also delete the list completely:
# Example
# Delete the entire list:
# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist) #this will cause an error because "thislist" no longer exists.

# The clear() method empties the list:
# Example
# Clear the list content:
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# There are ways to make a copy, one way is to use the built-in List method copy().
# Example
# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)



