# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic operators: +, -, *, /, %, **, //
# Assignment operators: =, +=, -=, *=, /=, %=, **=, //=
# Comparison operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not
# Identity operators: is, is not
# Membership operators: in, not in
# Bitwise operators: &, |, ^, ~, <<, >>

# Python Arithmetic Operators
# Operator	Name	Example
# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y

# Python Assignment Operators
# Operator	Example	Same As
# =	x = 5	x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# %=	x %= 3	x = x % 3
# //=	x //= 3	x = x // 3
# **=	x **= 3	x = x ** 3
# &=	x &= 3	x = x & 3
# |=	x |= 3	x = x | 3
# ^=	x ^= 3	x = x ^ 3
# >>=	x >>= 3	x = x >> 3
# <<=	x <<= 3	x = x << 3

# Python Comparison Operators
# Operator	Name	Example
# ==	Equal	x == y
# !=	Not equal	x != y
# >	Greater than	x > y
# <	Less than	x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	x <= y

# Python Logical Operators
# Operator	Description	Example
# and 	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

# Python Identity Operators
# Operator	Description	Example
 # is    Returns True if both variables are the same object    x is y
    # is not	Returns True if both variables are not the same object	x is not y

# Python Membership Operators
# Operator	Description	Example
 # in    Returns True if the value is found in the sequence    x in y
    # not in    Returns True if the value is not found in the sequence    x not in y

# Python Bitwise Operators
# Operator	Name	Description
# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
    # ^    XOR    Sets each bit to 1 if only one of two bits is 1
    # ~    NOT	Inverts all the bits
    # <<    LEFT SHIFT    Shifts the bits of the number to the left by the specified number of bits
    # >>    RIGHT SHIFT   Shifts the bits of the number to the right by the specified number of bits
# Example:

x = 10

# Bitwise AND operator

result = x & 3
print("Result of x & 3 is", result)

# Bitwise OR operator
result = x | 3
print("Result of x | 3 is", result)