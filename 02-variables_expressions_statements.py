type(1)
type(0.5)
type(5 > 3)
type("This is a string")

# print statement
print(3 + 7)
print(2 - 1)
print("This is a chunk of text")

# Variables
a = 10
b = a + 2
c = b + a
print(c)

# Conditionals
if a > 3:
    print("a is greater than 0")
    print(a)
else:
    print("a is not greater than 0")
    print(b)
print("We are done with this program")

# Variables and strings
a = "My first test string"
b = 'Another test string defined'
c = "This is Sal's string"
# d = 'This is John's string' Won't work because the second single quotes closes the string
d = 'My favorite food is "Papaya"'
math_string = "34 + 2"
expression_string = "a+' '+b+' tiger'"
print(a, b, c, d, math_string, expression_string)

# 1x = 'This is not a valid variable name' Not a valid variable name
# @email = 'Not a email'

# Keywords: Reserved words in Python you can't use as variable names
# False, class, finally, is, return, None, continue, for, lambda, try, True, def, from, nonlocal, while
# and, del, global, not, with, as, elif, if, or, yield, assert, else, import, pass, break, except, in, raise

# Calculate length of a string
len(a)
e = 'Hey'
print(len(e))

# Concatenate strings
f = "Hello "
g = "World"

fg = f + g
print(fg)

# String methods

# split (Returns a list of substrings of a string)
split_text = a.split(' ')
print(split_text)

# find (spaces are also valid positions)
find_text = math_string.find('2')
print(find_text)

find_text_space = "Hey 1"
print(find_text_space.find('1'))

# replace
replaced = d.replace('a', '1')
print(replaced)

Pi = '3.14'  # This is a comment
x = y = 1
print(x + y)

# String case (uppercase and lowercase)
uppercase = "Hello".upper()
print(uppercase)
lowercase = "WORLD".lower()
print(lowercase)

# Math calculation:
# Calculate volume of a sphere if r = 5. (4/3⊼r³)
r = 5
PI = 3.14

result = 4 / 3 * (PI * r ** 3)
print(result)

# Suppose the cover price of a book is $24.95, but at a 40% discount, Shipping costs $3 for the
# first copy and 75 cents for each additional copy. What is the total wholesale cost of 60 copies

cover_price = 24.95
cp_discount = 24.95 / 100 * 40
shipping = 3 + 0.75 * 60 - 0.75
print(cp_discount * 60 + shipping)

# Order of operations
# When an expression contains more than one operator, the order of evaluation depends on the order of operations:
# For mathematical operations, Python follows the PEMDAS convention, which is structured in precedence descending order
# PEMDAS: Parentheses - Exponentiation - Multiplication - Division - Addition - Subtraction
# P: highest
# E: Second highest
# M/D: Similar precedence
# A/S: Similar precedence
