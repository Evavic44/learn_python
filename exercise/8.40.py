# 1.
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


# The function 'any_lowercase1' takes in a string via the parameter, loops through each letter in the string,
# and stores the value of the current letter in a variable 'c'. It then proceeds to check if the current letter is a
# lowercase letter. Returning True if it is and False otherwise.

# This function does not work correctly because it terminates the loop after the first iteration.
# So it only checks the first character of the string.

# print(any_lowercase1('Hello'))  # Will return False because the first letter is an uppercase letter.
# print(any_lowercase1('hello'))  # Will return True because the first letter is lowercase


# Example 2
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

# The function 'any_lowercase2' takes in a string via the parameter, loops through each letter of the string,
# but it does not correctly check if there is a lowercase letter in the string.

# For example, if the function is called with any string whether lowercase or uppercase,
# the result will always be true:

print(any_lowercase2('ABC'))  # Returns true
print(any_lowercase2('abc'))  # Returns true

# Here are the reasons why this function does not work correctly:
# 1. The condition is not checking the looped variable from the input string,
# instead it checks for a hardcoded value: 'c'.
# This means the condition will always be true because 'c' is a lowercase letter.
# 2. The return 'True' and return 'False' statements will return a <class 'str'> and not
# a Boolean value because it is wrapped in quotes. This can be verified by checking the
# return type using the Python type function: return type('True'). (Python 2023)

# Example 3.
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

print(any_lowercase3('jOHN'))
# # The function 'any_lowercase3' takes in a string via the parameter, loops through each character to check,
# # if the current value is lowercase and stores the result of this condition in a variable; flag
# # The function then tries to return the variable flag, which is the result of checking if the current
# # letter is lowercase.
#
# # The issue with this function is that the flag variable is returned in the body of the function
# # and not inside the loop. This makes the flag variable unreachable,
# # and produce False when the function is called with any value; whether it is lowercase or uppercase.

# Example 4.
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

print(any_lowercase4('Week'))

# The function 'any_lowercase4' contains a variable; flag, which holds the value of False.
# It then loops through the string passed in as a parameter into the function,
# and updates the value of the flag variable using the logical OR operator that should result in either flag
# or the value of checking if the current letter of the variable is lowercase.

# Finally, the function returns the value of flag in the body of the function.

# This function is indeed accurate and should check if the string passed into the function
# contains a lowercase character:
print(any_lowercase4('World'))  # Will output True
print(any_lowercase4('UPPER'))  # Will output False
print(any_lowercase4('lower'))  # Will output True.

# Example 5
print('Example 5')
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print(any_lowercase5('hello'))

# The function 'any_lowercase5' takes in a string via the parameter, loops through each letter in the string,
# and stores the value of the current letter in a variable 'c'. It then proceeds to check if the current letter
# is not a lowercase letter using the Not operator in the conditional statement.

# Since the Not operator yields True if its argument is false, and False otherwise, (Python 2023)
# it will immediately return False if the current letter is not lowercase.
# And finally, if all the characters are lowercase, it will return True.

# This function will not work correctly because it only returns True when all the characters are lowercase.
# It returns False even if just one letter of the string is uppercase.

any_lowercase5('hello')  # Will return True because all characters are lowercase
any_lowercase5('WORLD')  # Will return False because all characters are uppercase
any_lowercase5('World')  # Will return False because one of the character is uppercase.

# Boolean operations. (2023). Python Software Foundation. https://docs.python.org/3/reference/expressions.html#not
