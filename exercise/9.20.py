# NOTE: Exercise 9.1. Write a program that reads words.txt and prints
#  only the words with more than 20 characters (not counting whitespace).

file = open('words.txt', encoding="MacRoman")

print('__________Exercise___________')
for char in file:
    if len(char.strip()) >= 20:
        print(char)


# First we loop through the elements in the list and then used the relational >= operator
# to check if the len of the current element (minus the whitespace) is greater than or equal to 20
# If true, the result is printed to the interpreter.


# NOTE: Exercise 9.2. Write a function called has_no_e that returns
#  True if the given word doesn’t have the letter “e” in it

def has_no_e(word):
    if 'e' not in word:
        return True

def has_no_e2(word):
    for chars in word:
        if chars == 'e':
            return False
    return True

def has_no_e3(word):
    return 'e' not in word

print(has_no_e('hello'))  # None: has e
print(has_no_e('world'))  # True: has no e
print(has_no_e2('coding'))  # True: has no e
print(has_no_e3('hello'))  # False: has e
print(has_no_e3('world'))  # True: has no e
