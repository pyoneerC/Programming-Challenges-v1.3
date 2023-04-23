import random as rd
import time as t

print('LOVE CALCULATOR')
t.sleep(.5)
p1 = input('Please enter the name of the first person: ')
t.sleep(.5)
p2 = input('Please enter the name of the second person: ')

calc = rd.randint(1, 100)
t.sleep(.5)
print('Calculating...')
t.sleep(3)

print(f'According to my calculations, "{p1}" and "{p2}" are {calc} % compatible.')