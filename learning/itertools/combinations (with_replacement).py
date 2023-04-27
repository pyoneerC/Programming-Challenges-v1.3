from itertools import combinations, combinations_with_replacement # 2 arguments required in both: iterable and length

# Define a list of numbers
a = [1, 2, 3, 4]

# Use the combinations function to compute all possible pairs of numbers from the list, without repetition
comb = combinations(a, 2) 
print("Combinations of 2 from", a, "without replacement:")
print(list(comb)) # Output: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# Use the combinations_with_replacement function to compute all possible pairs of numbers from the list, with repetition (we will encounter repeated pairs like (1,1), (2,2) etc... (with 2 length)
combwrep = combinations_with_replacement(a, 2)
print("\nCombinations of 2 from", a, "with replacement:")
print(list(combwrep)) # Output: [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
