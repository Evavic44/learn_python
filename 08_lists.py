# Lists
# A list is a sequence of values. Unlike strings that the sequences are characters,
# in lists, they can be of any type (Bool, string, Int, Float, ETC).
# List values are called elements or items.

# Example:
numbers = [10, 20, 30, 40]  # A list of numbers (integers)
names = ['John', 'Benjamin', 'Victor']  # A list of strings
my_list = [1, 'Nigeria', names, True]  # List can contain multiple types and even other lists
empty = []
print(numbers, names, my_list, empty)

# When the bracket operator appears on the left side of an assignment,
# it identifies the element of the list that will be assigned.

numbers[0] = 15  # Reassigns the first element with 15
print(numbers)

# List indices that work the same as strings indices:
# - An integer expression can be used as an index.
# - If you try to read or write an element that does not exist, you get an IndexError.
# - If an index has a negative value, it counts backwards from the end of the list.

# The in operator also works on lists
check_john = 'John' in names
print(check_john)  # Returns true

# Traversing a list
# The most common way to traverse the elements of a list is with a for loop.

for name in names:
    print(name)

# To write or update the elements in the list, you need the indices.
# This can be done by combining the built-in function range and len.

for i in range(len(numbers)):
    calc = numbers[i] = numbers[i] + 2
    print(calc)


# List Operations
# The + operator concatenates lists:
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(a+b)

# List Slice
# The slice operator also works on lists.

alph = ['a', 'b', 'c', 'd', 'e', 'f']
alph[1:3]  # Returns from the second index to the 3 index. = ['b', 'c']
# Side note: Start index is zero-based, while end index is not-zero based (Not a verified fa).
alph[:4]  # Returns all elements from the start to the 4th element. (Not zero-based) = ['a', 'b', 'c', 'd']
alph[3:]  # Returns all elements from the third index to the end. (Zero-based) =  ['d', 'e', 'f']
alph[:]  # Returns all elements
alph[::-1]  # Returns all elements in reverse.

# Since lists are mutable, it is often useful to make ac copy before
# performing operations that modify the list

# A slice operator on the left side on assignment can update multiple elements:
updated_alph = alph[1:3] = ['x', 'y']
print(alph)  # Returns ['a', 'x', 'y', 'd', 'e', 'f']

# List Methods
# Python provides methods that operate on lists. For example,
# append adds a new element to the end of the list.

num = [1, 2, 3, 4]
num.append(5)
print(num)

# Extend takes a list as an argument and appends all the elements.
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']

t1.extend(t2)
print(t1)  # Returns ['a', 'b', 'c', 'd', 'e']

# Sort arranges the elements of the list from lowest to highest.
t = ['f', 'e', 'd', 'c', 'b', 'a']
t.sort()
print(t)

# Most list methods are void; they modify the list and return None.
t_sort = t.sort()  # Will print None

# Map, filter and reduce
# To add up all the numbers in a list, you can use a loop like this.

def add_numbers(x):
    count = 0
    for number in x:
        count += number
    return count

print(add_numbers(num))
# count keeps getting updated by adding the previous number from the list
# to produce the sum of all the numbers.
# Python also provides the sum built-in function for this operation.

x = [10, 20, 30]
sum_x = sum(x)
print(sum_x)

# This operation that reduces a sequence of elements into a single value is known as reduce.

# Map
# This is an operation that involves mapping a function onto each of the elements in a sequence.
# Here's an example operation that returns each string element in the list capitalized.
def capitalize_string(strings):
    res = []
    for string in strings:
        res.append(string.capitalize())
    return res

print(capitalize_string(['john', 'doe', 'ben', 'cold']))

# Filter
# This is an operation that involves selecting certain elements from a list
# and filter out the rest

# Here is an example operation that filters a list and returns only the uppercase strings.

items = ['GET', 'POST', 'put', 'fetch']
def only_upper(letters):
    lists = []
    for letter in letters:
        if letter.isupper():
            lists.append(letter)
    return lists

print(only_upper(items))

# Deleting Elements
# To delete elements from an array, we use a method called 'pop'.

m = ['a', 'b', 'c']
n = m.pop(1)
print(m)  # Returns ['b', 'c']
print(n)  # Returns the deleted element 'b' in this case

# pop mutates the list and returns the element that was removed.
# If an index is not provided, it deletes and returns the last element.

# If the removed value is not needed, the 'del' operator can be used.
del m[0]
print(m)

# If you know the element you want to remove (but not the index), you can use remove:
p = ['aa', 'bb', 'cc', 'dd']
p.remove('dd')
print(p)

# The return value of remove is None.
# To remove more than one element, you can use del with a slice index
q = ['a', 'b', 'c', 'd', 'e']
del q[1:5]  # Deletes the elements from the second index to the fifth index
print(q)  # Returns ['a']

# List and Strings
# To convert a string to a list, we use the list function.
s = 'spam'
t = list(s)
print(t)  # Returns ['s', 'p', 'a', 'm']

# You can also split words of a string into a list instead of individual strings.
q = 'Good morning, Nigeria'
r = q.split()
print(r)  # Returns ['Good', 'Morning,', 'Nigeria']
# The split method takes an optional argument called a delimiter which the string should be split by.
# For example: The example string is split by hyphens.

t = 'Oct/01/1960'
u = t.split('/')  # Separates the string based on the forward slash.
print(u)  # Returns ['Oct', '01', '1960']

# Join is the inverse of split, although it is still a string method.
# It takes a list of strings and concatenates the elements.
delimiter = ''
f = delimiter.join(t)
print(f)

# Strings with the same values creates only one string object in Python and both 'e' and 'f'
# refer to it.

e = 'banana'
f = 'banana'
print(e is f)  # Returns True

# Unlike strings, lists with the same values create a separate objects in Python.
g = [1, 2, 3, 4]
h = [1, 2, 3, 4]
print(g is h)  # False because both objects are equivalent but not identical.

# List Arguments
# The append method modifies a list, but the + operator creates a
# new list.

