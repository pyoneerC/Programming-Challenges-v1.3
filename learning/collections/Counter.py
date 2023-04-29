from collections import Counter

a = 'aaaabbbccd'
my_counter = Counter(a)
print(my_counter)

# Counter({'a': 4, 'b': 3, 'c': 2, 'd': 1})

# Divides the string into a dictionary which each unique letter is a unique key and the value the number of appearances.

print(my_counter.items())

# dict_items([('a', 4), ('b', 3), ('c', 2), ('d', 1)])

# Enumerates the keys and the values (number of appearances), but in a tuple inside a list, inside minor tuples (similar to a numpy array)

print(my_counter.keys())

# dict_keys(['a', 'b', 'c', 'd'])

# Enumerates all the unique keys without repetitions (like a set)

print(my_counter.values())

# dict_values([4, 3, 2, 1])

# Instead of the keys, enumerates the values corresponding to the dict (in this case its referring to number of appearances) 
# Sorted by highest to minimum

print(my_counter.most_common(1)) # 1 argument only

# [('a', 4)] Most common pair in the counter in the form of a tuple
# If I'd put most_common(2) the result would be: [('a', 4), ('b', 3)] (2 tuples)

# List the n most common elements and their counts from the most common to the least. If n is None, then list all element counts.

print(my_counter.most_common(1)[0][0]) 
# print(my_counter.most_common(2)[1][0])  # Output: b
# print(my_counter.most_common(2)[1][1])  # Output: 3

# 3

# This is a good way for filtering the most common numbers, for example, if you put (1) 0 0. It's the top 1 index 0 0, so it's a. If you put 1 0 1 ---> is top 1 (a) index 1, so 4.
# (2)[1][1]) will give us the most two common numbers, but we enter index 1 (b), and then again, so its the value of the 2nd most common --> 3

print(list(my_counter.elements()))

# Inside a list if no it'll give us a map (returns value as a list, also)
# .elements is an iterator over elements repeating each as many times as its count.

# ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd']

# Print every element of the counter (dict) but in a list

# This list contains all elements from the original counter, and each element is repeated as many times as it appeared in the counter.

