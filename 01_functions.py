import math

# Functions
# A function is a named sequence of statements that performs a computation.
# Example: type(42) type is a function that takes in the argument: 42
# The return value of type is <class 'int'>

# Another example of a function is the int function. This takes any value and tries to convert it into an integer.
int('32')
# >>> 32
# int can convert floating point numbers to integers. But it doesn't round the numbers, but truncates the fraction
int(3.33)
# >>> 3

# Inversely, floats can convert integers to floating point numbers.
float(32)
# >>> 32.0

# str converts its argument into a string
str(22)
print(str(22))
# >>> '22'

# Math functions
# Python has a built-in math module that provides most of the mathematical functions.
# A module is a file that contains a collection of related functions.
# To use a module, you have to import it at the top of your script file. (import math)

# To use the module, you specify the name of the module, followed by a period and the function you want to access.
print(math)  # returns <module 'math' (built-in)>
print(math.pi)  # returns 3.14...
radians = 0.7
height = math.sin(radians)
print(height)


# Adding new functions
def print_twice():
    print('Come on' * 2)
    print('Get the radio on..')


print_twice()


def repeat_twice():
    print_twice()
    print_twice()
    # print(cat)


repeat_twice()


# Local parameters and function
# When you create a variable inside a function, it is local, which means it can only be accessed inside the function.


def get_name(name):
    title = "Mr "
    print(title + name)


get_name('Victor Eke')


# print(title) throws an error because title is local variable that is only available within the get_name function.
# When get_name runs and terminates, the variable; 'title' is destroyed and if you try to print it, you'll get an error
# parameters are also local. For example name is not accessible outside the get_name function.

# Stack Diagrams
# like state diagrams, stack diagrams shows the value of each variable and the function each variable belongs to.
# each function is represented by a frame that indicates which function called which.


def print_twice(params):
    print(params, params)


lyrics1 = "Rudiger"
lyrics2 = "Rudiger..."


def print_lyrics(part1, part2):
    lyrics = part1 + ' ' + part2
    print_twice(lyrics)


print_lyrics(lyrics1, lyrics2)

# Fruitful and void functions
# fruitful functions are essentially functions that returns a result, such as the math() function.
print('return value')
x = math.cos(22)
sqrt = math.sqrt(5)
# void functions are functions that perform and action but don't return any value.
result = print_twice(22)  # does not print anything.
print(result)
print(type(None))  # Special value with its own type.
# They might display something on the screen or have some other effect, but they don't have a return value.
# Another example of a void function is a function that calls other functions.

print((1, 000, 000))  # returns 1,0,0

# Marking a variable with the global flag.

count = 0


def mark_global():
    global count
    count = 44
    print(count)


mark_global()
print(count)

num4 = 11


def select_params(num1, num2, num3):
    print(num1 + num2 + num3 + num4)


select_params(1, 2, 6)