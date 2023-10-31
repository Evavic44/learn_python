# This chapter introduces the idea of 'persistent' programs that keep data in permanent storage
# Most of the programs we have seen so far are transient in the sense that they run for a short time
# and produce some output, but when they end, their data disappears.
import builtins
# HEAD:
#  Creating Text Files
#  Reading Text Files
#  Writing Text Files
#  Looping Operations with Text Files

import locale
import os
import sys
import dbm

# Other programs are persistent: they run for a long time (or all time).
# In persistent programs, data is stored in a permanent storage (a hard drive for example).

# Examples of persistent programs are operating systems which runs everytime a computer is turned on,
# or web servers which run all the time waiting for requests to come.

# One of the simplest ways for programs to maintain their data is by reading and writing text files.
# An alternative is to store the data or state of the program in a database.

# Text Files
# A text file is a sequence of characters stored on a permanent medium like a hard drive,
# flash memory, or CD-ROM.

# There are lots of word lists available but the most suitable for the purpose of this exercise,
# is one of the word list contributed to the public domain by Grady Ward as part of the Moby
# Lexicon project. This word list is known as the 'Moby Hyphenator II' (https://en.wikipedia.org/wiki/Moby_Project)
# It is a list of 113,809 official crosswords; words considered valid in
# crossword puzzles and other word games.

# This file is a plain text, so you can open it with a text editor.
# The 'Mphy' file uses the Mac Roman character encoding;
# an encoding created by apple to be used in the Macintosh computers.
# Hyphenation in this file is indicated by a bullet.

# Since windows uses mostly the 'UTF-8' encoding, you may need to change it when you load the
# file in your editor.

# Opening a Text File
# To open a file in Python, the built-in function 'open' takes the name of the file as a parameter
# and returns a file object you can use to read the file.

fin = open('words.txt')
print(fin)

# Note: fin is a common name for a file object denoting file input.

# The open() function in Python uses a platform dependent encoding to read text files.
# For example, Python 3.0+ in windows uses the 8-bit Windows-1252 character set,
# otherwise known as 'cp1252' in Python.

# To get the encoding type for your machine, import the locale module,
# and call the module with the 'getpreferredencoding()' method:
print(locale.getpreferredencoding())  # Returns cp1252
print(sys.getfilesystemencoding())  # Returns utf-8

# There is an ongoing request to change this default encoding to UTF-8 for global consistency:
# This update should reflect from Python 3.15. Reference: https://peps.python.org/pep-0686/

# The file object provides several metods for reading, writing, appending text files.
# For example: 'readline' reads characters from a file until it gets to a newline.

# HEAD: Creating Text Files
# To create a new file in Python, we pass in a file name with the extension attached to it,
# and pass in a second parameter 'x' inside the open() function.

# open('file.txt', 'x')

# This command will create a new empty file; newfile.txt in the project directory if the file does not
# already exist. If it does exist, the intepreter will throw an error alerting the file already
# exists.

# Note: This command will run eveyrtime the intepreter is executed.
# Note: You can also create other files and not just text files.

# There are other commands used for creating text files with different features.
# Some of them includes:

# 'w': Create a new file whether it exists or not. Will replace the file if it already exists.
# 'r+': Creates a file with both read and write access.
# 'w': Creates a read-only file
# 'a': Creates a write-only file


# HEAD: Reading Text Files:
# In order to read a word or character set of a text file, we use the readline() method.
# This method is called on the open method to return the first line of the word file.
# When you read the first line of the file in a Windows machine, you get 'a cap¥pel¥la'
line1 = fin.readline()
print(line1)

# This is because the Python Hyphenator II is encoded with the x-MacRoman encoder.

# Luckily, the open() method also takes in an optional property; encoding=""
# to set the preferred encoding to use in reading the file passed into the open method:

fin = open('words.txt', encoding='MacRoman')
l1 = fin.readline()
print(l1)

# The file object keeps track of the position of the current expression.
# So reading the file again with the readline method, should return the next line:

l2 = fin.readline()
print(l2)  # Returns a for•ti•o•ri

# If you notice, each line creates a space gap between the previous character,
# This is due to the newline character; '\n' attached to each word in the text file.
# To see this newline character, try calling the open() method and the readline method on a word list
# inside the Python interpreter directly.

# >>> x = open('words.txt', encoding='MacRoman')
# >>> x.readline()  # Returns 'a cap•pel•la\n'

# The strip() method is used to remove the newline character

l3 = fin.readline().strip()
l4 = fin.readline()
print(l3)
print(l4)

# There should be no spacing between the character at line 3 and the one at line 4.

# HEAD: Looping Operations on Text Files
# We can use for loop to iterate words in a text file. For example:

# file = open('words.txt', encoding='MacRoman')
# for line in file:
#     word = line.strip()
#     print(word)

# NOTE: Exercise 9.1. Write a program that reads words.txt and prints
#  only the words with more than 20 characters (not counting whitespace).

file = open('words.txt', encoding="MacRoman")

print('__________Exercise___________')
for char in file:
    c = char.strip()
    if len(c) >= 20:
        print(c)

# First we loop through the elements in the list and then used the relational >= operator
# to check if the len of the current element (minus the whitespace) is greater than or equal to 20
# If true, the result is printed to the interpreter.

# HEAD: Writing Text Files
# To write to a file, you have to open it with mode 'w' as a second parameter

fout = open('output.txt', 'w')

# If the file already exists, opening it in write mode clears out the old data and starts fresh,
# so be careful! If the file doesn’t exist, a new one is created

# To add data into the writeable text file, we call the file object with the 'write' method:
line1 = 'Hello Word \n'
fout.write(line1)
# print(fout.write(line1))  # Returns 12
# Printing the file object with the write method will return
# the number of characters written (including whitespaces)

# Calling the write method again should write to the next line.
line2 = 'This is my first writeable text file \n'
fout.write(line2)

# When you are done writing, close the file using the close method.
# fout.close()
# The argument of write must be a string so if you want to put other values in a file,
# you must first convert them to strings.

line3 = 42
# fout.write(line3)  # Expected str
fout.write(str(line3))

# Format Operator
# The % symbol when used with integers is known as the modulus operator.
# When used with strings the % operator is a string formatting operator.
# It allows you to format strings by inserting values into a string
# with a specific format. This process is often referred to as string interpolation.

# Syntax
# formatted_string = "String with placeholders: %d" % string_variable
# In this syntax:
# - '%s' is a placeholder for a string
# - '%d' is a placeholder for an integer

# And other placeholders avaialable.
# - '%f' is a placeholder for a floating point number

num = 400
print('%d' % num)
print('Your balance is %d' % 16500)

# You can use multiple placeholders in a string, to do this,
# the values should be inserted into a tuple after the % operator.
my_float = 0.5
my_string = 'Sacramento'
my_integer = 22

interpolation = 'Float Value: %f, String Value: %s, Integer Value: %d' % (my_float, my_string, my_integer)
print(interpolation)

# Another more readable way is by using the formatted f string.
form_f = f'Float: {my_float}, String: {my_string}, Integer: {my_integer}'
print(form_f)

# Filenames and Paths
# Every running program has a NOTE: current working directory or 'cwd',
#  which is their default location. For example,
#  creating a new file using the open() function does this at the root directory.

# The 'os' module (operating system) provides functions for working with files and directories:
cwd = os.getcwd()  # Returns the current directory your project is running on.
print(cwd)

# The string like '/home/projects' that identifies a file or directory is called a path.
# A simple filename like file.txt is also considered a path,
# but it is a relative path because it relates to the current directory.

# A path that begins with / is called an absolute path, and it does not depend on the current dir.
file_path = os.path.abspath('3.14.py')
print(file_path)

# Other Path Functions
check_file = os.path.exists('exercise/3.14.py')
print(check_file)  # Returns True if exercise/3.14.py exists otherwise returns false.
check_dir = os.path.isdir('exercise')
print(check_dir)  # Returns true if 'exercise' directory is found or else false.

# os.listdir() returns a list of the files (and other directories) in the given directory.
get_all = os.listdir(cwd)
print(get_all)


# To demonstrate these functions, the following example “walks” through a directory, prints
# the names of all the files, and calls itself recursively on all the directories.

def walk(dirname):
    for name in os.listdir(dirname):  # listdir returns all the relative paths in the passed-in dir
        pathname = os.path.join(dirname, name)
        if os.path.isfile(pathname):
            print(pathname)
        else:
            walk(pathname)


# walk(os.getcwd())
# os.path.join takes a directory and a file name and joins them into a complete path.

# Walk
# The os.walk() module provides a function called walk that returns a generator,
# which creates a tuple of values (path, directory, file),

def walk_builtin(dirname):
    for path, directory, filename in os.walk(dirname):
        print(os.path.join(path))


walk_builtin(os.getcwd())

# Catching Exceptions
# Exceptions are errors that happen during execution of the program.
# Python won’t tell you about errors like syntax errors (grammar faults),
# instead it will abruptly stop.
# With exceptions, we can handle common errors when trying to read, write or execute a file.

# Trying to open a file that does not exist.

# fin = open('fake_file.txt')
# This throws an error [Errno 2] No such file or directory: 'fake_file.txt'

# When you don't have permission to access a file:
# fout = open('/exercise/', 'w')
# open(os.getcwd(), 'w')

# And if you try to open a directory for reading
# open(os.getcwd()) IsADirectoryError: [Errno 21] Is a directory: '/home'

# To avoid these errors, you could use functions like os.path.exists and os.path.isfile,
# but it would take a lot of time and code to check all the possibilities.

# In this case, it is better to go ahead and try to deal with problems
# if they happen. The syntax is similar to an if...else statement.

try:
    fin = open('bad-file.txt')
except:
    print('Something went wrong.')

# Python starts by executing the try clause. If all goes well, it skips the except clause and
# proceeds. If an exception occurs, it jumps out of the try clause and runs the except clause.

# Handling an exception with a try statement is called 'catching' an exception.
# You can also specify the Exception afer the except keyword.
# Run the command below to see the list of supported exceptions

print(dir(builtins))

def open_file(dir1):
    try:
        open(dir1)
    except FileNotFoundError:
        print('Invalid file type')
    print('Moves to next code line')

open_file('welcome.txt')

# In this example, we try to read a file that does not exist in the directory.
# Running this command without a try...except block should terminate the program.
# Since we're manually introducing an exception; 'FileNotFoundError',
# This will not terminate the program, but rather execute the statement
# inside the except block and continue the program from there.

# The idea of the try-except block is to handle exception errors at runtime.
# You can also write multiple blocks of exception errors:

# try:
#     # Code statement
# except FileNotFoundError:
#     # Handle file not found error
# except PermissionError:
#     # Handle permission access error
# except:
#     # Handle other errors

# Databases
# A database is an organized file for storing data.
# Databases are usually organized as dictionaries in the sense that they map from keys to values.
# The difference between a database and a dictionary is that databases are either on a disk,
# or permanent storage like web servers, so they persist afer the program ends.

# To set up an interface for creating and updating database files, we use the dbm module:

# Opening a database is similar to opening other files. First you "import dbm"

db = dbm.open('captions', 'c')
# The mode 'c' means that the database should be created if it doesn't already exist.
# The result is a database object that can be used (for most operations) like a dictionary.

# When you create a new item, dbm updates the database file.

image = 'https://avatars.githubusercontent.com/u/62628408?v=4'
db[image] = 'Victor Eke'
print(db[image])

# The result is a bytes object, which is why it begins with b. A bytes object is similar to a
# string in many ways but not the same.

# Some dictionary methods, like keys and items, don’t work with database objects. But
# iteration with a for loop works:

for key in db:
    print(f'Name: {db[key]}, Photo: {key}')

# As other files, you should also close the database when you are done:
db.close()

# TODO: Continue from Pickling - Chapter 14: Files