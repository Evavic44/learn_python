# Dictionary
# A dictionary is also a sequence of mutable values, but they are more general.
# In a list, the indices have to be integers; in a dictionary they can be almost any type.

# A dictionary contains a collection of indices, which are called keys, and a collection of values.
# Each key is associated with a single values. The association of a key and a value is
# called a key-value pair.

# Creating a dictionary
a = dict()
print(a)

# The squiggly-brackets, {} represents an empty dictionary.
# To add items to the dictionary, you can use square brackets:

a['john'] = 22
a['ben'] = 40
print(a)  # {'john': 22, 'ben': 40}

my_dict = {'name': 'John Doe', 'age': 22, 'fav_color': 'blue'}

# A dictionary is not ordered like indices, the order is unpredictable.
# To access the values of an object, you can use the keys instead.

john_name = my_dict['name']
print(john_name)  # John Doe

# The key 'name' always maps to 'John Doe'.
# If the key isn't in the dictionary, you get an exception error.
# print(my_dict['test'])  # KeyError: 'test'

# The len function works on dictionaries; it returns the number of key-value pairs:
print(len(my_dict))  # 3

# To see whether something appears as a key in a dictionary, we use the 'in' keyword.
check_age = 'age' in my_dict
print(check_age)

# To see whether something appears as a value in a dictionary, you can use the values method,
# which returns a collection of values and then use the in operator on the collection.
my_dict_values = my_dict.values()
chec_name = 'John Doe' in my_dict_values
print(chec_name)
print(my_dict_values)  # ['John Doe', 22, 'blue']


# The in operator uses a different algorithm for lists and dictionaries.
# For lists, the search is done in chronological order. This may take longer depending on how long the list is.
# For dictionaries, Python uses an algorithm called a hashtable that makes searching take up
# the same time no matter how long the object is.

# Suppose you are given a string, and you want to count how many times each letter appears.
# There are several ways you could implement it. Some implementations are better than others.

# And advantage of the dictionary implementation is that we don't have to know ahead of time
# which letters appear in the string, we only have to make room for the letters that do appear

def historgram(dicts):
    d = dict()
    for c in dicts:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


print(historgram('extravagant'))
# The name of the function is histogram, which is a statistical term for a collection of counters
# (or frequencies)
# The first line of the function creates an empty dictionary. The for loop traverses the string.
# Each time through the loop, if the current character 'c' is not in the dictionary,
# we create a new item with key c and the initial value 1 (since we have seen this letter once).
# If c is already in the dictionary we increment d[c] by 1.

# {'e': 1, 'x': 1, 't': 2, 'r': 1, 'a': 3, 'v': 1, 'g': 1, 'n': 1}

# Dictionaries have a method called 'get' that takes a key and default value.
# If the key appears in the dictionary, get returns the corresponding value;
# otherwise it returns the default value. Example.

# Check s in brontosaurus
h = historgram('brontosaurus')
check_g = h.get('s', 0)
print(check_g)  # Returns 2 because there are 2 s's in brontosaurus.


# As an exercise, use get to write histogram more concisely. You should be able to eliminate
# the if statement.

def histogram2(s):
    d = dict()
    for i in s:
        d[i] = d.get(i, 0) + 1
    return d


print(histogram2('Benevolent'))


# In this refactored example, the 'get' method retrieves the value of the current key (i)
# from the dictionary 'd', and adds it to the object using the current character of the string.
# 'get' returns 0 as the default value which we added + 1 to signify the character is present.

# Looping and Dictionaries
# Looping a dictionary using the for statement traverses the keys of the dictionary:
# For example:

def dict_keys(h):
    for i in h:
        print(i, h[i])  # i points to the key, while h[i] points to the value.


my_dict2 = {'b': 1, 'a': 2, 'r': 3, 'd': 4}
dict_keys(my_dict2)  # This will return an unsorted list of keys and their values.

# To traverse the keys in a sorted order, you can use the built-in sorted function.
print('')


def dict_sorted(h):
    for key in sorted(h):
        print(key, h[key])


dict_sorted(my_dict2)

# Reverse Lookup
# This is an operation that involves looking for the value of a key in a dictionary.
# Given a dictionary 'my_dict2' and a key 'd', it is easy to find the corresponding value:

v = my_dict2['d']
print(v)  # Returns the value of 'd' which is 4.


# There is no simple syntax to do a reverse lookup, you have to search.

def reverse_lookup(d, val):
    for i in d:
        if d[i] == val:
            return i
    raise LookupError()


print(reverse_lookup(my_dict, 'blue'))

# Dictionary Methods
# The dictionary data structure also supports most of the built-in methods like lists.
# You can view them using the dir function

dict1 = {'a': 'Red', 'b': 'Green', 'c': 'Blue', 'd': 'Alpha'}
print(dict1)
print(dir(dict1))  # Returns all the supported methods of a dictionary.

# get method: retrieves the value of the current key in a dictionary.
# This method takes in two arguments: The key, and a default value that is replaced when the value is found.
get_a = dict1.get('a', 0)  # Returns Red
print(get_a)

# keys method: return a list of all the keys in a dictionary
keys = dict1.keys()
print(keys)  # Returns ['a', 'b', 'c', 'd']

# values method: returns a list of all the values in a dictionary
values = dict1.values()
print(values)  # Returns ['Red', 'Green', 'Blue', 'Alpha']

# items method: Returns both lists and values in a dictionary.
items = dict1.items()
for keys, values in items:
    print(f'{keys}: {values}')

# Dictionary also contains other important methods like pop, copy, clear, ETC.

# Dictionaries and Lists
# List can appear as values in a dictionary.

# Here is a function that inverts a dictionary:
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


print(invert_dict(my_dict2))

# Each time through the loop, key gets a key from d and val gets the corresponding value.
# If val is not in inverse, that means we haven’t seen it before, so we create a new item and
# initialize it with a singleton (a list that contains a single element).

# Lists can be values in a dictionary, but they cannot be keys.
# Here's what happens when you try:

my_list = [1, 2, 3]
m = dict()
# m[my_list] = 'oops'  # TypeError: list objects are un-hashable.

# The dictionary is implemented using an algorithm called a hashtable.
# This means that the keys have to be hashable.

# A hash is a function that takes a value (of any kind) and returns an integer.
# Dictionaries use these integers, called hash values to store and look-up key-value pairs.

# This system works fine if the keys are immutable. Mutable keys like lists can have multiple
# locations when their keys are modified and hashed, and as such makes it hard to find a key.

# That is why keys have to be hashable and why mutable lists aren't.
# The solution is by using another data structure called tupules.

# Memos
# They are previously computed values that are stored for later use.

known = {0:0, 1:1}
def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

# Known is a dictionary that keeps track of the Fibonacci numbers already known.
# It starts with two items: 0 maps to 0 and 1 maps to 1.
# Whenever fibonacci is called, it checks known.
# If the result is already there, it can return immediately.
# Otherwise, it has to compute the new value, add it to the dictionary, and return it.

# Global Variables
# They are called global variables because they can be accessed from any function.
# Unlike local variables that disappear when their function ends.

# If you try to reassign a global variable from within a function, it won't work
# because the local variable creates a new local variable which goes away after the function is done executing.

verbose = True
def example():
    verbose = False  # WRONG

# To reassign a global variable inside a function,
# you have to declare the variable with the global flag before you use it.

def example2():
    global verbose
    verbose = False

# This tells the interpreter to refer to the global variable not create a new one.
# If a global variable refers to a mutable value, you don't need to declare it to mofify the value:

known2 = {0:0, 1:1}
def example3():
    known2[2] = 2

#  you can add, remove and replace elements of a global list or dictionary, but if you want
# to reassign the variable, you have to declare it:
