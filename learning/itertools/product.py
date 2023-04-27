from itertools import product # product always method creates a new list and method.

a = [1,2] # 1,1 1,2 2,1 2,2 ---> 4 appearances each (CARTESIAN PRODUCT)
#   |\ /|
b = [3,4]

c = product(a,b)
print(list(c)) # [(1, 3), (1, 4), (2, 3), (2, 4)]. All possible unique combinations. no 'list' will print map '<itertools.product object at 0x000001FC531AE240>' 

from itertools import product # product always method creates a new list and method.

a = [1,2] # 1,1 1,2 2,1 2,2 ---> 4 appearances each (CARTESIAN PRODUCT)
#   |\ /|
b = [3,4] # if it this was [3] only it would be 8 possible outputs (4 * 2)

c = product(a,b, repeat=2) # Same process as above but making tuples x2 larger and doing it twice.  the product(a, b, repeat=2) call creates a new iterable that contains all possible combinations of two elements from a and b, where each element can be repeated once (due to the repeat=2 argument). The resulting iterable contains tuples with four elements, representing two pairs of elements from a and b. 16 possible tuples. 4 ** (repeat)2
print(list(c)) # [(1, 3, 1, 3), (1, 3, 1, 4), (1, 3, 2, 3), (1, 3, 2, 4), (1, 4, 1, 3), (1, 4, 1, 4), (1, 4, 2, 3), (1, 4, 2, 4), (2, 3, 1, 3), (2, 3, 1, 4), (2, 3, 2, 3), (2, 3, 2, 4), (2, 4, 1, 3), (2, 4, 1, 4), (2, 4, 2, 3), (2, 4, 2, 4)]. All possible unique combinations. no 'list' will print map '<itertools.product object at 0x000001FC531AE240>' 