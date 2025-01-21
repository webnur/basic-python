# Description: This file contains the strings used in the program.
# strings loop

# a = "Hello"
# for x in a :
#     print(x)

# strings length
a = "Hello"
print(len(a))

# strings check string
txt = "The best things in life are free!"
print("free" in txt)
if "free" in txt:
    print("Yes, 'free' is present.")

# strings check string not in method
txt1 = "The best things in life are !"
print('free' not in txt1)
if 'free' not in txt1:
    print("Yes, 'free' is not present.")

# strings slicing
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[5])
print(b[5:])
print(b[-5:-2])

# strings upper case
a = "Hello, World!"
print(a.upper())

# strings lower case
a = "Hello, World!"
print(a.lower())

# strings remove whitespace
a = " Hello, World! "
print(a.strip())

# strings replace string
a = "Hello, World!"
print(a.replace("H", "J"))

# strings split string
a = "Hello, World!"
print(a.split(","))