mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat2 = [*zip(*mat[::-1])]
print(mat2)

# This code takes a matrix (`mat`), rotates it 90 degrees counterclockwise and stores it in `mat2`. Here's how it works:

# - `mat[::-1]` reverses the order of the rows in the matrix, so the last row becomes the first row, the second-to-last row becomes the second row, and so on.
# - `zip(*mat[::-1])` transposes the reversed matrix by unpacking each row into its own tuple, and then aggregating those tuples by position (i.e., grouping all the first elements together, all the second elements together, and so on).
# - `[*zip(*mat[::-1])]` unpacks the resulting tuples into a list, effectively reconstituting the matrix in its rotated state.

# Here's an example to illustrate the process:

# Original matrix:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

# Reversed matrix:
# [[7, 8, 9],
#  [4, 5, 6],
#  [1, 2, 3]]

# Transposed matrix:
# [(7, 4, 1),
#  (8, 5, 2),
#  (9, 6, 3)]

# Final rotated matrix:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

x = "tell"
x = print(x) # outputs 'tell' and then the print transforms into a None, which is assigned to x
print(x) # None ---> printing doesn't return a value, it just prints something
type = type(x) # type (built-in function) displays the type of certain value if printed in the console. No imports or modules required.
print(type) # <class 'NoneType'>. As type represents the type of x = print(x) it will be None, and for it, it will be NoneType (absence of value).


def square(x):
  return x ** 2


x_sq = square(2) # x_sq = 2 ** 2 ---> 4 
y = print(x_sq) # Output: 4 (y = None (assigned to print, that doesn't return anything))
# print(f'type(y): {type(y)}') # y = None ---> NoneType
# print(f'{type(y) = }')
# print(f'{y = }')

# x_sq ---> 4
# y ---> None (NoneType)

print(bool([])) # False because list is empty. When lists are converted to bool, empty list are 0 and non-empty lists 1.

print(bool([False])) # True because list is non empty, despite the confusing 'False'
print(bool([True])) # True because the list is non empty, despite the 'True' values
print(bool(['sa'])) # True because list isn't empty.

# bool(l) same as len(l) > 0


# Copies

# .copy ---> shallow copy 1 layered ---> changes will be effective to the copy but no in complex structures.
# .deepcopy ---> fully independent copy

print('apple', 'banana', 'orange', sep=', ') # SEP IN THE END OF () OF PRINT SEPARATED BY , (IS LIKE OTHER ARG), it takes place when there's a ' ', as the default sep(arator) is ' '. Not counted in the output.

# apple, banana, orange

print('apple', 'banana', 'orange', sep='-_as1*¨?0q ') # Anything can be a separator: ' ' ; ', ' ; '122' ; ')& ' ; etc. Takes place when it detects an ' ' space and replace it with what we attributed to the sep (in this case '-_as1*¨?0q ')
# apple-_as1*¨?0q banana-_as1*¨?0q orange

def gal():
  return print('hey!')

a = gal() # hey!. a turns into None because the function has already returned so takes the value of None, and we essentially giving assigning it to a print (NoneType)
print(a) # None
print(f'{a is None=}') # 'a is None=True'. We making a bool thanks to the is and expecting the value after the =. We making a question: {a is None=(???)}


def add_numbers(a, b):
  if isinstance(a, int) and isinstance(b, int): # Checks if both numbers are in and if they are it return the sum of them, if not, returns 'None'
    return a + b
  else:
    return None

result = add_numbers(10, 20) # Output: 30
print(result)

result = add_numbers(10, "20") # Output: None
print(result)
