from itertools import cycle

list = [1,2,3,4]

for i in cycle(list): # prints [1,2,3,4] to infinity
    print(list)