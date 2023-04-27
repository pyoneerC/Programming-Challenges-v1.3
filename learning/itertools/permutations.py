# Import the permutations function from the itertools module
from itertools import permutations

# Define a list of numbers
a = [1, 2, 3]

# Generate all possible permutations of the list a
perm = permutations(a)
perm1 = permutations(a, 2) # If the number here is superior to the numbers of elements of the list (ex.4) it will return not an error but an empty list (default is max numbers of values per list per permutation, in this case 3). If ', 1' ---> [(1,), (2,), (3,)] (list with tuples insides due to list() max 1 length per pair (permutation))

# Convert the permutations object to a list and print it, if no it'll print the map.
print(list(perm)) 
# Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# This list contains all possible combinations of the numbers in a with different orders, without repeating any numbers.

print(list(perm1)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)] ---> prints unique sets and permutations but only 2 of LENGTH (like specified above(a,2))

