from random import random, uniform, choices, shuffle, seed, randint

a = random() # Generates a random float ranging 0 - 1 (excluding 1) ([a, b)). Receives no arguments.

print(a) # 0.20716740697585168

b = uniform(1, 10) # Generates a random float from 0 - 10 (excluding 10) ([a, b)). Receives two arguments

print(b) # 6.18946184274404

# These both are the same but in one we specify the range while in the first is a random float from 0 - 0.999

c = 'rock', 'paper', 'scissors' # (tuple). Note that the output of choices() is a list, not a tuple. The elements of the list are randomly selected from the given sequence (in this case the tuple c) with replacement. In this example, choices() returns a list of two elements randomly selected from c. Since the selection is done with replacement, an element can be selected multiple times.

d = choices(c, k=2) # Length of the samples returned. From c, select 2 samples. Generates new list, as it's value is assigned to a variable.

print(d) # ['paper', 'rock'], can generate same choices '['paper', 'paper']' since it's a tuple, not a list. List will select 2 random samples avoiding repetition

e = ['tomato', 'lettuce', 'aubergine', 'corn', 'pumpkin']

shuffle(e) # Mixes the content of the table as every execution takes place.
print(e) # ['aubergine', 'corn', 'tomato', 'pumpkin', 'lettuce']. This can't be done with tuples.

# f = shuffle(e) Shuffle doesn't return any value, so doing this is wrong.
# print(f) ---> NONE

seed(1)
print(random())
print(randint(1, 10)) # [a,b], both ends included.

# Seed 1: 
# 0.13436424411240122
# 2

seed(1)
print(random())
print(randint(1, 10)) 

# Seed 1: 
# 0.13436424411240122
# 2

seed(2)
print(random())
print(randint(1, 10)) 

# 0.9560342718892494
# 1

# We 'seed' the random values if we want to keep them and if we call the seed again it is likely to give the exact same result, like a minecraft seed.