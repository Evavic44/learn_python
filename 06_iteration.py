# Iteration is the ability to perform a task multiple times. It gives us the ability to run
# a block of statements repeatedly.

# Python supports variable re-assignments.
x = 5
print(x)  # x is 5
x = 7
print(x)  # x is 7

# Updating variables
# A common kind of reassignment is an update, where the new value of the variable depends on the old.
x = x + 1
# This expression is known as an increment. Subtracting 1 is called decrement.

# This above statement means the current value of x is added to 1 and the new value of x is updated.
# Updates only work on already initialized variable. If you try to update a non-existent variable,
# Python will throw an error:

# y = y + 1
# NameError: name 'y' is not defined.

# While Loop
# Repeats a statement or group of statements while a given condition is TRUE. It tests the
# condition before executing the loop body.

# Syntax of while loop

# while (condition):
#   statements(s)

# Example 1
print('\nWhile Loop (Countdown Function)')
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')

countdown(10)

# The flow of execution for a while statement:
# 1. Determine whether the condition is true or false.
# 2. If false, exit the while statement and continue execution at the next statement.
# 3. If the condition is true, run the body and then go back to step 1.

# Exercise:
print('\nPrint N Loop')
def print_n(string, n):
    con = 0
    while n > 0:
        con += 1
        print(f'{string} x {con}')
        n = n - 1

print_n('Hello World', 10)

# Example 2
num = 2
count = 1

print('\nWhile Loop')
while count <= 10:
    print(f'{num} x {count} = {num * count}')
    count = count + 1

# Result will be
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20

# Break Statement
# This is a statement that is used to break out of a loop.
num = 3
count = 1

print('\nBreak Statement')
while count <= 10:
    print(f'{num} x {count} = {num * count}')
    count += 1  # Same as count = count + 1
    if count == 6:
        break  # Loops stops when count

# Continue Statement
# The continue statement is used to skip the current iteration of the loop and the
# control flow of the program goes to the next iteration.

# This example counts from 0 to 10 and skips the iteration when the number is an even number.
print('\nContinue Statement')
num = 0
while num <= 10:
    num += 1
    if num % 2 == 0:
        continue
    print(f'Current Number is ODD {num}')

# The opposite example for odd numbers
a = 1
while a <= 100:
    a += 1
    if a % 2 != 0:
        continue
    print(a)

# Infinite Loop
# Infinite loops are essentially loops that lack a functional exit or break statement, thereby, executing infinitely
# This usually happens when the condition to continue running the loop will always be true.
# It is similar to not including to a 'base case' in recursive functions.

# count = 0
# while count < 10:
#     print('∞')

# Exercise 1.0
# Write a loop that prompts a user to enter a series of Pizza toppings.
# As they enter each topping, print a message that says you'll add that topping to their Pizza.

print('\nExercise')
while True:
    toppings = input('Enter a pizza topping \n')
    if toppings == 'Pineapple':
        print("Pineapple is not a valid topping")
        break
    else:
        print(f'{toppings} will be added to Pizza')

# Exercise 2.0
# A movie theatre charges different ticket prices depending on a person's age. If a person is under the age of 3,
# the ticket is free, if they are between 3 and 12, the ticket is $10, and if they are over 12, the ticket is $15
# Write a loop in which the age of the user is received and the cost is given according to their age.

while True:
    age = int(input('What is your age?'))
    if age > 1 and age <= 3:
        print('The ticket is free...')
    elif 3 <= age <= 12:
        print('The ticket is $10')
    elif age > 12:
        print('The ticket is $15')
    else:
        print('Value not allowed')
        break

# For Loop
# Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.
# It has the ability to iterate over the items of any sequence, such as a list or a string.
# If a sequence contains an expression list, it is evaluated first. Then the first item in the sequence is assigned
# to the iterating variable; iterating_var
# Next the statement block is executed. Each item in the list is assigned to iterating_var, and the statement(s) block
# is executed until the entire sequence is exhausted.

university = 'University of the People'
for letters in university:
    print(letters)


# Nested Loops
# Use one or more loops inside any while, or for loop.

# Nested While Loop Syntax
# while expression:
#   while expression
#       statements(s):
#   statements(s)

# Nested For Loop Syntax
# for expression:
#   for expression
#       statements(s):
#   statements(s)

# Example nested loop program that shows a right angle triangle using an asterix.

x = 0
y = 0
counter = ""
while x < 20:
    while y <= x:
        counter += "*"
        y += 1
    print(counter)
    x += 1

# Algorithm: an algorithm is a step-by-step procedure or a set of rules for performing a specific task
# or solving a particular problem.

# Algorithms do not require writing in a specific programming language. You can write an algorithm in any one you prefer
# Although best practices require your algorithm is written in the language closest to the one the code will be written.

# Sample Algorithm to find the biggest value of two numbers.

# Step 0 - START
# Step 1 - Input x, y
# Step 2 - if x > y then max = x else max = y
# Step 3 - Print max
# Step 4 - STOP

def largest_num(num1, num2):
    if num1 > num2:
        max_num = num1
    else:
        max_num = num2
    print(f'The max number is {max_num}')

largest_num(int(input('Enter first number')), int(input('Enter second number')))

# References:
# Python Loops while and for (2021). ITiNstructor Channel. https://youtu.be/j_BcMeqAz4I?si=8wEQqXFDJcFebXED
