# zip unpacks from lists, tuples, iterables, etc.

x = (1, 2, 3)
y = (4, 5, 6)

z = zip(x, y)

for i in z: # iterates 3 times
    print(i)
    
    # (1, 4)
    # (2, 5)
    # (3, 6)
    
for a, b in z: # iterates 6 times (1 per number)
    print(a, b)
    
    # 1 4
    # 2 5
    # 3 6

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}

for key1, key2 in zip(dict1, dict2): # iterates 3 times (2 keys values same time)
    print(key1, dict1[key1], key2, dict2[key2]) # 1. a (1) d (2) 2. b (3) e (4) 3. c (5) f (6) ---> key 1: a  dict[a] --> 1 ---> a 1
    
    # a 1 d 4
    # b 2 e 5
    # c 3 f 6


import time

num_dots = 0

while True:
    a = print(f'Loading{"." * num_dots}', end='\r') # end='\r' returns cursor to the beginning of the line, necessary for restarting the ...
    num_dots = (num_dots + 1) % 8 # num_dots keeps track of ... printed and the % 4 restarts to 0 (% 4 catches 3rd . , 8 catches 7th, 1 less.)
    time.sleep(1) # time between .'s