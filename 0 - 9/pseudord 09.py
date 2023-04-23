import random as rd

articles = ['The', 'A', 'An']
nouns = ['dog', 'cat', 'car', 'tree', 'book', 'house', 'cat', 'turtle']
verbs = ['ran', 'jumped', 'ate', 'slept', 'read', 'walked', 'typed']
adverbs = ['quickly', 'slowly', 'eagerly', 'calmly', 'carefully', 'relaxed', 'wisely']

ar = rd.choice(articles)
no = rd.choice(nouns)
ve = rd.choice(verbs)
ad = rd.choice(adverbs)

print(f'{ar} {no} {ve} {ad}.')