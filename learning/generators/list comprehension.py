from sys import getsizeof

generator = (i for i in range(10) if i % 2 == 0)
# print(generator) # <generator object <genexpr> at 0x0000018DFE93C380> ---> 0x0000018DFE93C380 is the memory address (unique ID) for that generator (hex). genexpr ---> 'Generator expression'
# print(list(generator)) # Transforms the generator into a list [0, 2, 4, 6, 8]
print(getsizeof(generator)) # 208 bytes in memory

# All even numbers 0-9 in list comprehension

list1 = [i for i in range(10) if i % 2 == 0]
# print(list1) # [0, 2, 4, 6, 8]
print(getsizeof(list1)) # 120 bytes in memory (list are better for smaller datasets). 

# When lists become larger, like this example but with range(10000) the difference is crazy: 208 generator vs. 41880 for the list comprehension!!!!

# "Lists are better for smaller datasets, but for bigger, choose generators"