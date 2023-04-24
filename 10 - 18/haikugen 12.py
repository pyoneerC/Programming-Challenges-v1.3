from random import choice

# separator = ' ,' (hidden)

print('Haiku', 'generator', sep='---') # changed str separator to '---' (can be anything ---> 1 , ---, ___, +, etc.)

line1 = ['A winter moon--', "In the cicada's cry--", 'The light of a candle']
line2 = ['the only thing left', 'no sign can foretell', 'is greeting the world']
line3 = ['to guide me', 'of an autumn evening', 'of dewdrops at dawn']

def haikugenerator():

    a = choice(line1)
    b = choice(line2)
    c = choice(line3)

    return f'{a}\n{b}\n{c}'

print(haikugenerator())