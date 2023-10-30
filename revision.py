a = dict()
b = {}
print(a, b)

a['name'] = 'John'
print(a)

my_dict = {'name': 'John Doe', 'age': 22, 'fav_color': 'blue'}
print(my_dict['fav_color'])

print(22 in my_dict.values())
print(my_dict.values())
print(my_dict.keys())
print(my_dict.items())

def histogram(dicts):
    dx = dict()
    for i in dicts:
        if i not in dx:
            dx[i] = 1
        else:
            dx[i] += 1
    return dx

val = histogram('extravagant')
print(val.get('a', 0))

def histogram2(dictx):
    dxa = dict()
    for x in dictx:
        dxa[x] = dxa.get(x, 0) + 1
    return dxa

print(histogram2('welcome'))

# Looping a dictionary
for xl in my_dict:
    print(xl)

for values in my_dict.values():
    print(values)

for values in my_dict.keys():
    print(values)

for key_val in my_dict.items():
    # print(key_val)
    print(list(key_val))

# Lookup
v = my_dict['age']
print(v)

# Given a dictionary 'dict2' and a key 'd', find the corresponding value:
dict2 = {'a': 94, 'b': 2, 'c': 10}
val2 = dict2['a']
print(val2)

# Reverse Lookup
# This operation involves searching through a dictionary using the value to find the corresponding key or keys.
# There is no simple syntax to handle this operation, you have to search manually:

def reverse_lookup(d, string):
    for el in d:
        if d[el] == string:
            print(d[el])
            return el
    raise LookupError()

print(reverse_lookup(dict2, 2))

