import random

options = ['rock', 'paper', 'scissors']
outcomes = ['win', 'lose', 'tie']

# make 5 random selections from the options list
choices = random.choices(options, k=5) # k = 5 (5 choices)

# print the choices and their corresponding outcomes
for choice in choices:
    outcome = random.choice(outcomes)
    print(f"{choice} -> {outcome}")

# paper -> tie
# rock -> win
# rock -> win
# scissors -> win
# paper -> tie

from random import choices

options = ['a', 'b', 'c', 'd']
weights = [1, 2, 3, 4] # Higher weight, higher possibilities of being selected

results = choices(options, weights, k=5) # 5 choices of option based in weights, without weights, 5 random choices.

print(results)

# ['c', 'c', 'b', 'b', 'b']