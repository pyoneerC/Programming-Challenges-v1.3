from sys import getsizeof # For measuring size in bits, along other functions.

# APPEND VALUES TO A LIST, NOT A GENERATOR

def a(n):
    nums = [] # All nums will go here, in a list.
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
    
# GENERATOR

def b(n):
    num = 0
    while num < n:
        yield num # Returns 1 value at a time, without remembering previous (list remembers all numbers, and that's why it make them ineffective against generators)
        num += 1

print(getsizeof(a(10_000))) # 85176 bytes in memory (precomputes all nums before action) (even though they are effective for smallest data sets)
print(getsizeof(b(10_000))) # 200 bytes in memory (yield numbers and print on-the-fly without remembering)

# saves a lot of memory as it size in bits is much more lower
# {The code is comparing the memory usage of a list created by a function that appends values to it versus a generator that yields values one at a time. The `sys.getsizeof()` function is used to measure the size of the resulting object in bytes.

# The `a()` function creates an empty list called `nums`, then loops through values from 0 up to `n`, appending each value to the list. Finally, the list is returned. This function uses memory to store the entire list in memory at once.

# The `b()` function uses a generator to yield values one at a time as requested. It starts at 0 and loops up to `n`, yielding each value one at a time. This function uses memory only to store the current value of `num`.

# The output of the `sys.getsizeof()` function shows that the list created by the `a()` function uses much more memory than the generator created by the `b()` function. This is because the list stores all the values in memory }at once, while the generator only stores one value at a time.

# Generators are effective for LARGER DATA SETS