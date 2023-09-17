# import math
#
#
# # 3.1 Write a function named right_justify that takes a string named 's' as a parameter and prints the string
# # —with enough leading spaces so that the letter of the string is in column 70 of the display.
#
# def right_justify(s):
#     string = ' ' * 70 + s
#     print(string)
#     print(len(string))
#
#
# right_justify('Hello World')
#
#
# # 3.2 A function object is a value you can assign to a variable or pass as an argument. For example,
# # do_twice is a function that takes a function object as an argument and calls it twice:
#
# def do_twice(f, val):
#     f(val)
#     f(val)
#
#
# # Here's an example that uses do_twice to call a function named print_spam twice.\
# # 1. Modify do_twice so that it takes two arguments, a function obj and a value, and calls the def twice.
# # passing the value as an argument.
# # 2. Copy the definition of print_twice from earlier in this chapter to your script.
#
# def print_twice(params):
#     print(params, params)
#
#
# # 3.
#
# def print_spam(x):
#     print(x)
#
#
# do_twice(print_spam, 'yet another spam!')
#
# # Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
# do_twice(print_twice, 'spam')
#
#
# # Define a new function called do_four that takes a function object and a value and calls the funtion four times
# # passing the value as a parameter. There should be only two statements in the body of this function, not four.
#
# def print_val(obj):
#     print(obj)
#     print(obj)
#
#
# def do_four(fn_obj, val_string):
#     fn_obj(val_string)
#     fn_obj(val_string)
#
#
# print('')  # empty line
# do_four(print_val, math.pi)
#
# # Write a function that draws a grid
#
# print('\n' + ' ' * 8 + 'Python Grid')
#
#
# def print_four(val):
#     print(val, val, val)
#     print(val, val, val)
#     print(val, val, val)
#     print(val, val, val)


# def draw_grid():
#     print('+' + ' — ' * 4, '+' + ' — ' * 4, '+')
#     print_four('|' + ' ' * 12)
#     print('+' + ' — ' * 4, '+' + ' — ' * 4, '+')
#     print_four('|' + ' ' * 12)
#     print('+' + ' — ' * 4, '+' + ' — ' * 4, '+')
#
#
# draw_grid()
#
#
# print('First Line', end=' ')   # end='' prints the two closest objs in one line
# print('Second Line')

# Write a function that draws a similar grid with four rows and four columns using only statements and features
# learned so far.

print('\n' + ' ' * 16 + 'Python Grid with Four Rows 🐍')


def print_four_grid():
    print('+' + ' — ' * 4, end=" ")
    print('+' + ' — ' * 4, end=" ")
    print('+' + ' — ' * 4, end=" ")
    print('+' + ' — ' * 4 + "+")
    print('|' + ' '*13 + '|' + ' '*13 + '|' + ' '*13 + '|' + ' '*12 + '|')
    print('|' + ' '*13 + '|' + ' '*13 + '|' + ' '*13 + '|' + ' '*12 + '|')
    print('|' + ' '*13 + '|' + ' '*13 + '|' + ' '*13 + '|' + ' '*12 + '|')
    print('|' + ' '*13 + '|' + ' '*13 + '|' + ' '*13 + '|' + ' '*12 + '|')
    print('+' + ' — ' * 4, end=" ")
    print('+' + ' — ' * 4, end=" ")
    print('+' + ' — ' * 4, end=" ")
    print('+' + ' — ' * 4 + "+")
    print('|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 12 + '|')
    print('|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 12 + '|')
    print('|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 12 + '|')
    print('|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 12 + '|')
    print('+' + ' — ' * 4, end=" ")
    print('+' + ' — ' * 4, end=" ")
    print('+' + ' — ' * 4, end=" ")
    print('+' + ' — ' * 4 + "+")
    print('|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 12 + '|')
    print('|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 12 + '|')
    print('|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 12 + '|')
    print('|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 12 + '|')
    print('+' + ' — ' * 4, end=" ")
    print('+' + ' — ' * 4, end=" ")
    print('+' + ' — ' * 4, end=" ")
    print('+' + ' — ' * 4 + "+")
    print('|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 12 + '|')
    print('|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 12 + '|')
    print('|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 12 + '|')
    print('|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 12 + '|')
    print('+' + ' — ' * 4, end=" ")
    print('+' + ' — ' * 4, end=" ")
    print('+' + ' — ' * 4, end=" ")
    print('+' + ' — ' * 4 + "+")

print_four_grid()
print("This code is a programmer's nightmare 🫠")
