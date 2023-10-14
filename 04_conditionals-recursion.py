# Conditionals are simply expressions that are executed depending on the state of a program or expression.
import sys

# Floor Division
# The floor division operator '//', divides two numbers and rounds them down to an integer.
# Conventional division (/) returns a floating point number.

# float division
minutes = 105
time = minutes / 60
print(time)  # Result = 1.75

# floor division
mins = 105
hours = mins // 60
print(hours)  # Result = 1 (Rounds the value and returns an integer without a decimal point)
remainder = mins - hours * 60
print(remainder)

# Modulus Operator
# This operator divides two numbers and returns the remainder.
rem = mins % 60
print(rem)  # Result = 45

# The modulus operator can also be used to check if a number is divisible by another. Formula: if x % y = 0,
# x is divisible by 0.
x = 20
y = 2
print(x % y)  # Result = 0 because 20 divided by 2 produces 10 and 0 remainder.

# Boolean Expression
# A boolean expression is an expression that is either true or false. It uses the == relational operator (double equals)
# which compares two operands and produces 'True' if they are equal or the same, and 'False' otherwise.

print('5' == '5')  # True
print(5 == '5')  # False
print(True == True)  # True
print(True == False)  # False

# True and False are both special values that both have a type of '<class 'bool'>'
print(type(True))

# The == operator is one of the relational operators; others are:
print(x != y)  # True 20 is not equal to 2
print(x > y)  # True 20 is greater than 2
print(x < y)  # False 20 is not less than 2
print(x >= y)  # True 20 is greater than 2 but not equal to 2
print(x <= y)  # False 20 is not less than or equal to 2

# Logical Operators
# There are three logical operators: 'and', 'or', and 'not'
print(x % y == 0 or x % 3 == 0)  # The or operator is true if either one of its operations is true.
print(x % y == 0 and x % 3 == 0)  # The and operator is true if both operations and true and false otherwise.
print(not x < y)  # The not operator negates a boolean expression. In other words, it inverts is so true becomes false
# and false becomes true.
print(not 1 > 2)  # prints true because the expression 1 > 2 is false.

# Conditional Execution
# Conditional statements give us the ability to write useful programs based on certain conditions. The simplest forms
# is the if statement.

if x > y:
    print('x is greater than y')

# if statements have the same structure as function definitions. A header followed by an indented body. It can take any
# number of statements, but it requires at least 1.
# The if statement also contains a 'pass' statement that can be used in place of a condition. This is helpful when
# creating conditions to be used as placeholders.

if x <= y:
    pass  # TODO: will work on this.

# Alternative Execution
# The if statement also has an alternative execution in which there are two possibilities and the condition determines
# which one runs. Example:

a = 6
if a % 2 == 0:
    print('a is even')
else:
    print('a is odd')

# If the condition is false, the second set of statements run. Since the conditions must be true or false, one of the
# alternatives must run. The alternatives are called branches.

# Chained Conditionals
# This includes conditions that have more than two possibilities or alternatives. This condition uses a third statement
# called 'elif' which is an abbreviation of 'else if'.

if x > y:
    print('x is greater than y')
elif x < y:
    print('x is less than y')
else:
    print('x and y are equal')

# Nested Conditionals
# These are essentially conditions nested within another condition.

if x == y:
    print('x and y are equal')
else:
    if x != y:
        print('x is not equal to y')
    else:
        print('x is equal to y')

# The outer condition contains two branches, the first contains a simple statement and the second contains another if
# statement which has two branches on its own. Nested conditions may become difficult to read  very quickly, so it is a
# good idea to avoid them if possible.

# Logical operators often provide a way to simplify nested conditionals statements. For example, we can rewrite the
# following nested example like so:

if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')

if 0 < x and x < 10:
    print('x is a positive single-digit number.')

# Python even provides a more concise option
if 0 < x < 10:
    print('x is a positive single-digit number.')


# Recursion: A function defined in terms of itself via a self-referential expression.
# In other words, it is a function that calls itself and keeps executing until a condition is met.
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)

countdown(5)

# In the expression above, if n is 0 or a negative number, it prints the word 'Blastoff!', otherwise it prints 'n' and
# then calls itself with the argument of n - 1.

# Calling the countdown function with 5 will output 5 4 3 2 1 Blastoff!. Since n is greater than 0, the else branch is
# executed and the countdown starts from n = 5, since 5 > 0, it calls itself again producing n = 4 since 4 > 0, it
# calls itself again producing 3, and it keeps going until n = 0, then it executes the if branch which is 'Blastoff!'

# Infinite Recursion
# This is a recursion that never reaches a base case, it goes on making recursive calls forever,
# and the program never terminates.

def recursive():
    recursive()

recursive()

# What is a Base Case?


# Running the above recursive function will in most environments throw a runtime error:
# 'RuntimeError: Maximum recursion depth exceeded' when the maximum recursion depth is reached.

# You can check the recursion limit using the command:
print(sys.getrecursionlimit())

# If you encounter an infinite recursion by accident, review your function to confirm that there is a base
# case that does not make a recursive call. And if there is a base case, check whether you are guaranteed to reach it.

# Here's a recursive function example that introduces a base case


def recursion_func(year):
    if year == 2024:    # The base case
        print('I hereby terminate this recursion!')
    else:
        print(year)
        recursion_func(year + 1)

recursion_func(2020)

# In this scenario, the base case is the conditional statement: year == 2024.
# Since calling the function keeps adding 1 to the date, the base case will surely be reached
# and the date will be 2024, at that point, the recursive function terminates and the statement inside the condition is
# executed; in this case: 'I hereby terminate this recursion'.

# References:
# Python Software Foundation. (2023). System Specific Parameters and Functions.
# https://docs.python.org/2/library/sys.html#sys.getrecursionlimit

# Keyboard Input
# Python provides a built-in function called input that prompts a user to type in character or string of text.
# The input stops the program when active and continues the program after the user presses return or enter, and it
# returns whatever the user typed as a string. In python 2, it is called raw_input.

text = input()
print(f'You just inputted {text}')

# To pass a message into the print output, add a string of text inside the input function like so:

name = input('What is your name? \n')
print(f'Nice to meet you {name}')

# '\n' is a special character that represents a newline.
# If you want users to input integers you can try wrapping the response with an int.

question = 'What is the boiling point of water? \n'
answer = input(question)
print(f'Your answer is {int(answer)}')

con = 'a' < 'b'
print(con)

# Returns False because all characters actually have a Unicode value attached to them. When a comparison
# operator is used on two different strings, the Python interpreter compares the strings based on their Unicode value.
# which can be found on an ASCII table. In the ASCII table, a  = 97 and b =  98.
# Essentially 97 is less than 98 which is the reason why the comparison produces False.

ord('a')
