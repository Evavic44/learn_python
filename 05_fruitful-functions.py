import math


# Fruitful functions are essentially functions that return some form of value. The opposite is called a void function
# which performs a computation but does not return any value.


# Calling a function generates a return value, which is usually assigned to a variable or used as an expression

# Example: This function
def area(radius):
    a = math.pi * radius ** 2
    return a


# Sometimes it is useful to have multiple return statements, one in each branch of a conditional.'


def absolute(x):
    if x < 0:
        return -x
    else:
        return x


# As soon as a return statement runs, the function terminates, without expecting any subsequent statements.
# Any code that appears after a return statement will be unreachable. This term is called `dead code`


def compare_func(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0


print(compare_func(2, 2))


# Incremental Development: This is the process of testing a portion of a code to avoid long debugging sessions.
# 1. Start with a working program and make small incremental changes
# 2. Use variables to hold intermediate values, so you can display and check them.
# 3. Once the program is working, remove the scaffolding or consolidate multiple statements into compound expressions.


def hypotenuse(a, b):
    squared = a ** 2 + b ** 2
    return math.sqrt(squared)


print(hypotenuse(16, 18))


# Boolean functions are functions that returns a true or false value. It is common to give boolean functions names that
# sound like yes/no questions; is_divisible returns either T/F to indicate whether x is divisible by y


def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


is_divisible(4, 6)  # False
is_divisible(3, 3)  # True


def is_between(x, y, z):
    return x < y < z


print(is_between(2, 4, 6))


# More recursion


def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        return recurse * n


print(factorial(12))


def recursive_func(x):
    if x == 0:
        return 1
    else:
        return x * recursive_func(x - 1)

recursive_no = int(input('Enter a number \n'))
result = recursive_func(recursive_no)
print(f'The factorial of {recursive_no} is {result}')

# Fibonacci
# After factorial, the most common example of a recursively defined mathematical function is the fibonacci, which has
# the following definition:

# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(5)

# Checking types
# Make sure the type of recursive input is an integer to avoid missing the base case. For example if you call the
# fibonacci function with 1.5, you will get an error: 'Maximum recursion depth exceeded' because 1.5 is a floating
# point number not an integer, so it misses the base case and recurse forever.

# You can use the built-in isinstance function to verify the type of argument. For example:


def factorial_is(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorials is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial_is(n-1)

# The first base case handles non-integers; the second handles negative integers. In both
# cases, the program prints an error message and returns None to indicate that something
# went wrong
print(factorial_is(5))

# This demonstrates a pattern called guardian. The first two conditionals act as guardians protecting the code that
# follows from values that might cause an error.

# Debugging
# if a function is not working properly, there are three possibilities to consider:
# 1. A precondition is violated (There is something wrong with the arguments the function is getting)
# 2. A postcondition is violated. (There is something wrong with the function)
# 3. There is something wrong with the return value.

# Post Condition
# To rule out a precondition, you can do the following:
# a. Print the values of the parameter at the beginning of the function to display the values or type.
# b. Write code to check the precondition explicitly.

# Pre Condition
# If the parameter looks good,
# a. Add a print statement before each return statement and display the return value.
# b. If possible, check the result by hand.
# c. Consider calling the function with values that make it easy to check the results.

# Return Value
# If the function seems to be working, look at the function call to make sure the return value is being used correctly


def factorial_debug(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial_debug(n-1)
        res = n * recurse
        print(space, 'returning', res)
        return res

factorial_debug(4)


def divide_num(a, b):
    if b == 0:
        print('Division by zero not allowed')
    else:
        print(a / b)

divide_num(6, 3.2)


def get_initials(ini):
    if len(ini) == 2:
        print('Your initials is:', ini)
    else:
        raise ValueError('Please provide only two letters')

get_initials('VE')

# Incremental development is the process of breaking down code requirements into different stages or increments
# based on the user requirement. This process adopts an iterative approach in the development cycle of a program.
# And is usually implemented to catch errors early, and release the program in a short duration.

# Here's a program that calculates the area of a rectangle

# Increment 1
# a. Get width and height input from the user
# b. Test the result

# width = int(input('Enter width of Rectangle'))
# height = int(input('Enter height of Rectangle'))

# print('Width:', width)
# print('Height:', height)

# Increment 2
# a. Define a simple function without parameters to calculate the area
# b. Display the area of rectangle within function
# c. Test the result


# def area_rectangle():
#     width = int(input('Enter width of Rectangle >> '))
#     height = int(input('Enter height of Rectangle >> '))
#     area_rect = width * height
#     print(area_rect)

# area_rectangle()

# Increment 3
# a. Modify function and include two parameters
# b. Pass the arguments to the function
# c. Display answer through a return value outside the function
# d. Test the result

width = int(input('Enter width of Rectangle >> '))
height = int(input('Enter height of Rectangle >> '))


def area_rectangle(width, height):
    area_rect = width * height
    return area_rect

print('Area of rectangle is', area_rectangle(width, height))
