# Exercise 01
# Write a function called nested_sum that takes a list of integers
# and adds up the element from all the nested lists. For example.

t = [[1, 2], [3], [4, 5, 6]]


def nested_sum(nums):
    count = 0  # Create counter variable for increment
    for num in nums:
        if isinstance(num, list):  # Checks if current element is a list
            count += nested_sum(num)  # Calls nested_sum recursively on current list
        else:
            count += num  # Increment count with sum of numbers
    return count


print(nested_sum(t))

# Exercise 02
# Write a function called cumsum that takes a list of numbers and returns the cumulative sum;
# this is, a new list where the ith element is the sum of the first i + 1 elements from the list.
# For example:

t = [1, 2, 3]


def cumsum(numbers):
    cum_sum = []
    count = 0
    for i in range(len(numbers)):
        count += numbers[i]  # Adds the current index to count.
        cum_sum.append(count)  # Appends each sum of count to the cum_sum list.
    return cum_sum


print(cumsum(t))

# Exercise 03
# Write a function called middle that takes a list and returns a new list that contains
# all but the first and last elements.

t = [1, 2, 3, 4]


def middle(items):
    return items[1:-1]


print(middle(t))


# Exercise 04
# Write a function called chop that takes a list, modifies it by
# removing the first and last elements, and returns None.

def chop(a):
    a.pop(0) + a.pop(-1)


print(chop(t))  # Returns None
print(t)  # Returns the list without first and last elements

# Exercise 05
# Write a function called is_sorted that takes a list as a parameter
# and returns True if the list is sorted in ascending order and False otherwise:

a = [1, 2, 2]
b = ['e', 'q', 'a']


def is_sorted(d_list):
    if sorted(d_list) == d_list:  # Checks if the sorted list is the same with the original list
        return True
    else:
        return False


print(is_sorted(a))  # Returns True
print(is_sorted(b))  # Returns False


# Exercise 06
# Write a function called is_anagram that takes two strings and returns True if they are anagrams.

def is_anagram(w1, w2):
    word1 = w1.replace(' ', '').lower()
    word2 = w2.replace(' ', '').lower()

    check_length = len(word1) == len(word2)
    check_sort = sorted(word1) == sorted(word2)
    print(sorted(word1))
    print(sorted(word2))

    if check_length and check_sort:
        return True
    else:
        return False

print(is_anagram('tupac', 'caput'))  # Returns True
print(is_anagram('letter', 'reel it'))  # Returns False