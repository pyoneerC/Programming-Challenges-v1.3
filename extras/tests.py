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

lista = [0] * 5
print(list) # [0, 0, 0, 0, 0]
list1 = [0,1] * 5 # 5 times [0,1]
print(list) # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

text = '123' * 5
print(text) # 123123123123123

# Only '*' supported in this kind of operations (operations with str's and int's)

biglist = lista + list1 # joins lists for order specified (first list then list1)
print(biglist) # [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

# # Only '+' supported in this kind of operations (operations with str's and int's)

# Tuples ( () are optional)

tup = 'Max', 28, 'New York' # () are optional
print(tup) # ('Max', 28, 'New York') ---> A tuple!

tuple1 = ('Max') 
print(tuple1) # Max ---> Not recognized as a tuple! (is a string)

mytuple = ('Max', ) # Type: String ---> ('Max',) is considered tuple. When defining a tuple with only one element, you need to add a comma after the element to indicate that it is a tuple, otherwise it will be considered a string.
# print(type(mytuple)) ---> class tuple, if no ', ' and only a str inside the tuple ---> class string

# if (x := 'Max' in tup):
#   print(x)

print(tup.count('a')) # 0 as it won't track individual characters like from 'Max', so it will never say 1 unless an item 'a' is in the tuple
print(tup.index(28)) # Index 1 as 28 is in index 1 in tup. If value not in tup, like str '28' or 'sxbd', we will get a valueError.

r = list(tup) # Converter: tup (tuple) into list
print(r) # ['Max', 28, 'New York']

o = tuple(r) # Converter: r (list) into tuple
print(o) # ('Max', 28, 'New York')

name, sdfsdf, city = tup # We assign as much variables as elements the tuple has for getting each item (unpack)

print(name) # Is equal to index 0 ---> 'Max9
print(sdfsdf) # Is equal to index 1 of the tup ---> 28
# print(city) # Is equal to index 2 (-1) of tup ---> 'New York'

# We can also unpack 3 but print whatever we want.

# Lists are larger in size (bytes) compared to a tuple with the exact same elements and composition.
# List take longer to make with the 'timeit' module compared with the same tuple, the same amount of repetitions.
# Tuples can be used as keys in dictionaries, while lists cannot. Tuples are immutable (more security).

# In conclusion, tuples are more powerful than lists.

dict1 = dict(name='max', age=28, city='Boston') # We can create a dictionary using the dict function() to avoid putting ' ' for each key and : . We just put key=value, ...
print(dict1) # {'name': 'max', 'age': 28, 'city': 'Boston'}

dict1['email'] = 'abcde@gmail.com' # Appending a key and an arg at the end of the dictionary
print(dict1) # {'name': 'max', 'age': 28, 'city': 'Boston', 'email': 'abcde@gmail.com'}

dict1['email'] = 'a@gmail.com' # Replacing/updating the value referring to the key 'email'
print(dict1) # {'name': 'max', 'age': 28, 'city': 'Boston', 'email': 'a@gmail.com'}

del dict1['name'] # deleting key 'name' and it corresponding value
dict1.pop('age') # Same as delete. We pop the key, and the value referred to it. NEEDS A VALUE BETWEEN ()
dict1.popitem() # Deletes the last key and value from the dictionary. Receives no arguments between () (email deleted)

print(dict1) # {'city': 'Boston'} (name, age and email were deleted using methods del, pop and popitem in order)

print(dict1['city']) # Boston. Accessing dict by indexing the name of the keys
# print(dict['Boston']) Error. Only keys can be obtained and referenced by this method, no values. 

for vals in dict1.values(): # Gets the values of the dictionary using this method
  print(vals) # Boston

for keys in dict1.keys(): # Gets the values of the dictionary using this method
  print(keys) # city

for key, value in dict1.items(): # Gets keys and values but without ':: ' '' ' or {}
  print(f'The key "{key}" corresponds to the value: "{value}"') # The key "city" corresponds to the value: "Boston". No matter if we put value before or after either way, it will always print the key and then the value

dictcopy = dict1.copy() # Independent copy using .copy
      #  = dict(dict) works the same way

dictcopy['email'] = 'emailcopy@gmail.com'
dictcopy['city'] = 'New York Copy'
dictcopy['name'] = 'Copy'

print(dict) # {'city': 'Boston'}
print(dictcopy) # {'city': 'New York Copy', 'email': 'emailcopy@gmail.com', 'name': 'Copy'}

dictionary = {'a' : 1, 'b' : 2, 'c':3, 'd':4}
dictionary2 = dict(a=121212, b=32323, c='This is an extra text from second dict', name='Max')

dictionary.update(dictionary2) # Dictionary got updated taking reference of dictionary2 (only 1 argument accepted)
print(dictionary) # {'a': 121212, 'b': 32323, 'c': 'This is an extra text from second dict', 'd': 4, 'name': 'Max'} merged two dictionaries, but giving priority to the 2nd one to overwrite things! Keys that aren't present in the two dictionaries at the same time conserve their state.

my_dict = {4: 'apple', 5: 'banana', 6: 'orange'}
print(my_dict[4]) # 'apple'
print(my_dict[5]) # 'banana'
print(my_dict[6]) # 'orange'

# We are accessing the dictionary values by using their corresponding keys (4, 5, 6). We cannot access the dictionary values using an index like my_dict[0] in this case where keys are ints.

my_dict = {}
my_dict[(1, 2)] = 'value1'
my_dict[(3, 4)] = 'value2'

print(my_dict[(1,2)])  # Output: 'value1'
print(my_dict[(3, 4)])  # Output: 'value2'

# Assigning two keys to a value using tuples(non-mutables as keys in a dictionary) (no lists because these are mutables). Note that we need these two keys for accessing the value, and therefore using 'my_dict[(1)] and not 1,2 will gib¿ve us an error.


# 'IS' keyword

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)  # False, a and b reference different objects in memory
print(a is c)  # True, a and c reference the same object in memory

a = 5
b = 5.0

print(f'{a == b = }')  # True - value comparison (checks if the objects have the same value). 'a == b = True'
print(f'{a is b = }')  # False - strict comparison (a IS int, b IS float). 'a is b = False'

# This way of formatting string allow us to enter certain words between {} and then showing up the bool value.

# The 'is' keyword in Python is used for object identity STRICT comparison. Checks if two objects are the same object in memory