# Aside from being a series of characters, strings are also sequences; an ordered collection of other values.

fruit = 'banana'
letter = fruit[1]

print(letter)   # returns 'a' which is the second character in 'banana'.
# The expression in bracket is called an 'Index'. This indicates which character in the sequence you want.
# The index of a string is zero-based, which means it starts counting from 0. Which is why fruit[1] = 'a' not 'b'

# fruit[1.5]
# The index must be an integer else it will throw: TypeError: string indices must be integers, not 'float'.

# Len: Returns the number of characters in a string.
fruit = 'apple'
length = len(fruit)
print(length)  # Returns 5

last = fruit[length - 1]  # Returns last letter, 'e'
print(last)
print(fruit[-1])  # Returns last letter, 'e'
print(fruit[-2])  # Returns second to last letter, 'l'

# Traversal with a for Loop
# A lot of computations involve processing a string one character at a time. Often they start
# at the beginning, select each character in turn, do something to it, and continue until the
# end. This pattern of processing is called a traversal

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1


# Exercise: Write a function that takes a string as an argument and displays the letters
# backwards, one per line.

def print_backwards(string):
    len_string = len(string)
    ind = len_string - 1

    while ind >= 0:
        print(string[ind])
        ind -= 1

print_backwards('racecar')
print_backwards('caput')  # prints 'tupac'


# You can also write a traversal with a for loop
for letter in fruit:
    print(letter)

# Each time through the loop, the next character in the string is assigned to the variable
# letter. The loop continues until no characters are left.

prefixes = "JKLMNOPQ"
suffix = 'ack'

for letter in prefixes:
    if letter[0] == 'Q' or letter[0] == 'O':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)


# A segment of a string is called a slice. Selecting a slice is similar to selecting a character.
s = 'Monty Python'
h = s[0:5]  # Prints from 0 to 5 = Monty
g = s[6:12]  # Prints from 6 to 12 = Python
print(h)
print(g)

# The [n:m] operator returns a portion of a string from the 'n-eth' to the 'm-eth' character.
# If the first index is greater than or equal to the second, the result is an empty string.

fruits = 'banana'
# fruits[3:3]  # Returns ''

# If you omit the 'n-eth' number, the result will start at the end of the string and vice versa.
name = 'John Doe'
print(name[1:])  # Returns 'ohn Doe'

# Strings are Immutable
# This means you can't change an already existing string.
greeting = 'Hello World'
# greeting[0] = 'J'  TypeError: 'str' object does not support item assignment

# Searching
# This is a pattern of traversing a sequence and returning a result.
def find(word, leta):
    i = 0
    while i < len(word):
        if word[i] == leta:
            return i
        i += 1
    return -1

def find_string_num(string, the_letter):
    i = 0
    for leta in string:
        if leta == the_letter:
            i += 1
    print(i)

find_string_num('Prestidigitation', 'i')

# String Methods
# This is similar to a function. It takes an argument and returns a value, but the syntax is different.
# A method call is  called an invocation; in this case, upper is invoking on 'title'.

# upper and lower methods
title = 'javascript'
title_u = title.upper()
title_l = title.lower()
print(title_u, title_l)


# Find method
index_js = title.find('a')
print(index_js)  # returns the position of the first occurrence of a sequence.

# By default, find starts at the beginning of the string, but it can take a second argument, the
# index where it should start and stop:
index_j = title.find('a', 5)

# The in operator
# This is a boolean operator that takes two strings and returns True if
# the first appears as a substring in the second.

check_a = 'a' in 'banana'
print(check_a)  # Returns True
check_c = 'c' in 'banana'
print(check_c)  # Returns False
