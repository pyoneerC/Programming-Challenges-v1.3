import timeit as ti
import sys

# Define a function to measure
def my_function():
    my_list = [i**2 for i in range(1000)]

# Measure the execution time
execution_time = ti.timeit(my_function, number=1000)

# Print the result
print(f"List() time: {execution_time:.6f} seconds")

list_test = [i for i in range(1000)]
tuple_test = tuple(list_test)
set_test = set(list_test)

# timeit for sum() function on a list
list_time = ti.timeit('sum(list_test)', globals=globals(), number=10000)
print(f"List sum() time: {list_time:.6f} seconds")

# timeit for sum() function on a tuple
tuple_time = ti.timeit('sum(tuple_test)', globals=globals(), number=10000)
print(f"Tuple sum() time: {tuple_time:.6f} seconds")

# timeit for sum() function on a set
set_time = ti.timeit('sum(set_test)', globals=globals(), number=10000)
print(f"Set sum() time: {set_time:.6f} seconds")

# List() time: 0.038768 seconds
# List sum() time: 0.063741 seconds
# Tuple sum() time: 0.049201 seconds
# Set sum() time: 0.091800 seconds

# Sets are faster than tuples and lists when it comes to searching for elements.

# Print the size of the function in bytes
print(f"Function size: {sys.getsizeof(my_function)} bytes")

# Create a list of integers
my_list = [i for i in range(1000)]

# Print the size of the list in bytes
print(f"List size: {sys.getsizeof(my_list)} bytes")

# Create a tuple of integers
my_tuple = tuple(my_list)

# Print the size of the tuple in bytes
print(f"Tuple size: {sys.getsizeof(my_tuple)} bytes")

# Create a set of integers
my_set = set(my_list)

# Print the size of the set in bytes
print(f"Set size: {sys.getsizeof(my_set)} bytes")

# Create a dictionary with integers as keys and values
my_dict = {i: i**2 for i in range(1000)}

# Print the size of the dictionary in bytes
print(f"Dictionary size: {sys.getsizeof(my_dict)} bytes")

# Function size: 152 bytes
# List size: 9024 bytes
# Tuple size: 8040 bytes
# Set size: 32792 bytes
# Dictionary size: 36952 bytes