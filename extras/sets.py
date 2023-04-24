# Sets characteristics:

# Sets are unordered, meaning that the elements in a set are not arranged in any particular order.
# Sets are mutable, which means you can add, remove or modify elements in a set.
# Sets can only contain unique elements. If you try to add an element that already exists in the set, it will not be added again.
# Sets use curly braces {} to enclose their elements, with elements separated by commas.
# Sets do not support indexing or slicing because they are unordered. However, you can loop over the elements of a set using a for loop.
# Sets can be created from other iterable objects such as lists, tuples, and strings using the set() function.
# Some common set operations include union, intersection, difference, and symmetric difference.


my_set = {1, 2, 3, 4, 5}
print(my_set) # {1, 2, 3, 4, 5}
my_set.add('a')
print(my_set) # {1, 2, 3, 4, 5, 'a'}
my_set.remove(3)
my_set.remove('a')

# Remove() catches 1 arg only. (3, 'a') won't work.

print(my_set) # {1, 2, 4, 5}


if 3 in my_set:
    print("3 is in my_set")
else:
    print("3 is not in my_set") 

# 3 is not in my_set

# UNION .union

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2) # set 1 union with set 2
print(union_set) # Union 2 sets ---> {1, 2, 3, 4, 5} (no numbers twice, like 3)

# INTERSECTION x.intersection(y)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2) # set 1 union with set 2
print(intersection_set) # What numbers are repeated? ---> {3}

# DIFFERENCE x.difference(y)

set1 = {'a', 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2) # All elements in set1 that aren't present in set2 (4,5 aren't even present in set1, so not printed)
print(difference_set) # {'a', 2} (exclusives to set1)

# DISJOINT x.isdisjoint(y) (checking if two sets have any common elements):

set1 = {1, 2, 3}
set2 = {3, 4, 5}
if set1.isdisjoint(set2):
    print("set1 and set2 have no common elements")
else:
    print("set1 and set2 have some common elements")

    # set1 and set2 have some common elements (it's 3)

my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set) # Output: set() (empty)


my_set = {x for x in range(10) if x % 2 == 0} # creates a set with even numbers from 0 (included) to 9 (10 not included). if x is divisible by 2 it prints it (even num)
print(my_set) # Output: {0, 2, 4, 6, 8}

my_set = {x for x in range(0, 10, 2)} # creates a set with even numbers from 0 (included) to 9 with step 2 (same as example before) (10 not inclusive)
print(my_set) # Output: {0, 2, 4, 6, 8}


my_list = [1, 2, 3, 3, 4, 4, 5, 6, 6, 6]
my_set = set(my_list) # makes list a set. sets are made for storing unique elements, automatically removes.
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
subset = set2.issubset(set1) # Does set1 'contains' set2?
print(subset)  # Output: True (bool)

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4}
print(set1.issuperset(set2)) # Does all set2 elements are in set1? (x.issuperset(y)) Report whether this set contains another set)
# Output: True

set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8}
disjoint = set1.isdisjoint(set2) # Does set1 and set 2 have completely different elements?
print(disjoint)  # Output: True

word = "hello world"
unique_chars = set(word) # transforms the string into a set, and sets only contains unique elements, deleting the duplicates automatically
print(unique_chars)
# Output: {'r', 'h', ' ', 'd', 'l', 'o', 'e', 'w'} (prints the set, only unique chars)

# Checking if a string contains all the letters of the alphabet:

s = "the quick brown fox jumps over the lazy dog"
alphabet = set("abcdefghijklmnopqrstuvwxyz")
print(alphabet.issubset(s)) # Does 's' contains ALL the chars from 'alphabet'?
# Output: True

# Finding the COMMON characters between two strings:

s1 = "hello"
s2 = "world"
common_chars = set(s1) & set(s2) # set1(s1) '&' set2(s2) gives us the chars that repeat within the 2 vars (because we are making those str ---> sets)

# {'h', 'e', 'l', 'o'} & {'w', 'o', 'r', 'l', 'd'} (Which are repeated between these 2 sets??)

print(common_chars)
# Output: {'l', 'o'}


# Finding the UNIQUE characters in two strings:

s1 = "hello"
s2 = "world"
unique_chars = set(s1) ^ set(s2) # non repeated chars.

# {'h', 'e', 'l', 'o'} ^ {'w', 'o', 'r', 'l', 'd'} (Which are unique between these 2 sets??)

print(unique_chars)
# Output: {'h', 'e', 'd', 'r', 'w'}


# Find union of sets: You can find the union of two or more sets using the `union()` method or the `|` operator. For example:

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6, 7}

set3 = {7, 8, 9}
print(set1 | set2 | set3)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9} UNION OF ALL USING |


# Find intersection of sets: You can find the intersection of two or more sets using the `intersection()` method or the `&` operator. For example:

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
print(set1.intersection(set2))  # Output: {4, 5} (Where do they met? Which numbers in common?)

set3 = {5, 6, 7}
set4 = {5, 9, 10}
print(set1 & set2 & set3 & set4)  # Output: {5} WHERE THE 4 SETS MET? (USING &)


# Find difference of sets: You can find the difference of two sets using the `difference()` method or the `-` operator. For example:

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
print(set1.difference(set2))  # Output: {1, 2, 3} (In what set1 differ compared to set2)

set3 = {3, 4, 5}
print(set1 - set2 - set3)  # Output: {1, 2} (- subtracts set 2 and 3 from set1) (It's all comparing 1 TO THE OTHERS, set1 has exclusive {1,2})

# Reversed set

print(set('hello')) # {'h', 'l', 'e', 'o'} (random orders cause the sets are unordered): next iteration output: {'e', 'h', 'o', 'l'}
print(set(reversed('hello'))) # It's not reversed (it's mixed) but rather CHANGES THE ORIGINAL SET {'h', 'e', 'o', 'l'}

# For example:

# print(set('hello')) ---> {'o', 'l', 'e', 'h'}
# print(set(reversed('hello'))) ---> {'h', 'o', 'e', 'l'} (not reversed but instead, changed, and changes every time we run the file.)