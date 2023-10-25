# Tuples is an immutable collection of objects.
# The values in tuples can be of any numerous types, and they are indexed by integers.

emp = tuple()
print(emp)

# Creating a tuple
city = 'Pune',  # Creates a tuple because of the trailing comma.
print(type(city))

my_tuple = ('a', 'b', 2, 3, True)
print(my_tuple)

# Although it is not necessary it is common to enclose tuples in parentheses.
tuple_1 = 1, 2, 3  # This syntax is similar to
tuple_2 = (1, 2, 3)  # this.
print(tuple_1, tuple_2)

# Tuples are immutable meaning their values can neither be removed nor updated.
# For example, you can't use the append method on tuples.

my_list = (1, 2, 3, 4)
# my_list.append(5)  Throw errors because tuples does not contain the append method.

# Tuples are indexed; You can access the elements using the index.
t1 = my_list[0]
print(t1)  # Returns the first element

t4 = my_list[-1]
print(t4)  # Returns the last element

# Tuples Operations
# Although tuples are immutable, there are still certain operations you can perform on them:
# Concatenation:

list1 = (1, 2, 3)
list2 = ('a', 'b', 'c')
add_list = list1 + list2
print(add_list)  # Concatenate both tuples

# Nesting
# You can nest tuples inside of other tuples
nest = (list1, list2)
print(nest)

# You can multipy the elements of a tuple:
rep = ("Python",) * 6
print(rep)

# Slicing Tuples
# All the slicing operation available on lists also works on tuples.
first_four = add_list[0:4]
print(first_four)

tuple_rev = add_list[::-1]
print(tuple_rev)

# Unpacking
# You can convert a string into a tuple using the tuple function
my_str = "Hello World"
str_to_tuple = tuple(my_str)
print(str_to_tuple)

# You can assign the elements of a tuple into variables:
(a, b, c) = list1
print(a, b, c)  # Returns the elements of the tuple.

# You can assign particular elements of a tuple to variables and
# add the rest of the elements into a list using the gathers (*) argument
# followed by the variable of the list.

(x, *y, z) = add_list
print(x, y)

# You cannot delete an element from a tuple, but you can delete the entire tuple using the del keyword:
del list1
# print(list1)  # Returns a NameError: 'list1' is not defined.

# Count element occurrence:
# To count the number of occurrence of an element in a tuple, we use the count function.

tuple_3 = (1, 2, 'a', 'b', 'a')
print(tuple_3.count('a'))  # Returns 2 because 'a' appears twice in the tuple.

# Find the sum of all elements in the tuple:
tuple_sum = sum(my_list)
print(tuple_sum)  # 4 + 3 + 2 + 1 = 10

# Get total number oƒ elements in the tuple:
tuple_len = len(tuple_3)
print(tuple_len)

# Find the min or max element in the tuple
min(my_list)
max(my_list)

# Convert list to a tuple
lst = ['x', 'y', 'z']
list_to_tuple = tuple(lst)
print(list_to_tuple, type(list_to_tuple))

# Exercise
tuple1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple1)

tuple2 = tuple1 + (10,)
print(tuple2)

tuple3 = tuple2 + tuple1[::-1]
print(tuple3)

# Tuples as return values
# The built-in function divmod() takes two arguments and returns a tuple of two values,
# the quotient and remainder.

t = divmod(21, 7)
print(t)  # Returns 3 as the quotient and 0 as the remainder.

# Lists and Tuples
# Zip Function
# zip is a built-in function that takes two or more sequences and returns a list of tuples
# where each tuple contains one element from each sequence.
# The name of the function refers to a zipper.

# This example zips a string and a list.
s = 'abc'
t = [0, 1, 2]
zip(s, t)
print(zip(s))

# The most common use of zip is in a for loop:
for pair in zip(s, t):
    print(pair)

# A zip object is a kind of iterator. They are similar to lists
# except you can't access an element using an index.

# You can use a zip object to make a list:
print(list(zip(s, t)))

# The zip() function will stop producing pairs when the shortest input iterable is exhausted.
# In this case, since ['a', 'b', 'c'] has only 3 items, the loop will iterate 3 times
zip_len = list(zip('1234', ['a', 'b', 'c']))
print(zip_len)  # Returns only 3 elements.

# If the sequences are not the same length, the result will return the length of the shorter one.

# You can loop through a list of tuples:
for numbers, value in zip_len:
    print(numbers, value)


# Each time through the loop, Python selects the next tuple in the list.
# If you combine zip, for and tuple assignment, you will get a useful idiom
# for traversing two or more sequences at the same time.

def has_match(t5, t6):
    for m, n in zip(t5, t6):
        if m == n:
            return True
    return False


print(has_match('123', ['1', '2', '3']))

# Enumerate Function
# If you need to traverse the elements of a sequences and their indices,
# you can use the built-in function enumerate:

for index, element in enumerate('xyz'):
    print(index, element)

# The result from enumerate is an enumerate object which iterates a sequence of pairs;
# each pair contains an index (starting from 0) and an element from the given sequence.
# In this example, the output is:
# 0 x
# 1 y
# 2 z

# Dictionaries and Tuples
# Dictionaries have a method called items that returns a sequence of tuples
# where each tuple is a key-value pair.

d = {'l': 1, 'm': 0, 'n': 2}
f = d.items()
print(f, type(f))

# The result is a dict_items object which is an iterator that iterates the key-value pairs.
# You can use it in a for loop like this:

for key, value in d.items():
    print(key, value)

# As expected from a dictionary, the result items are in no particular order.
# You can also use a list of tuples to initialize a new dictionary:

e = [('a', 0), ['b', 3], ['c', 1], ['d', 2]]
tuples_to_dict = dict(e)
print(tuples_to_dict)

# Combining dict with zip yields a concise way of creating a dictionary:
v = dict(zip('abc', range(3)))
print(v)

# In many contexts, the different sequences (strings, list and tuples) can be used interchangeably.
# So how do we choose one over the other?

# Strings are more limited that other sequences because the elements have to be characters,
# and they are immutable. If you need the ability to change a character,
# you might want to use a list of characters instead.

# Lists are more common that tuples because they are mutable.
# Here are the few cases where tuples might be more useful:

# 1. In contexts, like a return statement, it is syntactically simpler to create a tuple that a list.
# 2. If you want to use a sequence as a dictionary key, you have to use an immutable type like a tuple or string
# 3. If you are passing a sequence as an argument to a function, using tuples reduces the potential
# for unexpected behaviour due to aliasing.
