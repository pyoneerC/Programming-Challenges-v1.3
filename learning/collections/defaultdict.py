from collections import defaultdict

d = defaultdict(int) # If we put (float), the default value would be 0.0. If we put nothing between () [or d =  {} (empty dict) with no defaults], there will not be any default value, so ['c'] will throw 'KeyError'
d['a'] = 1
d['b'] = 2
print(d)

# defaultdict(<class 'int'>, {'a': 1, 'b': 2})

# we create a defaultdict object d with the default value of int, and then we assign the values 1 and 2 to keys 'a' and 'b', respectively. When we print d, we see that it contains the expected key-value pairs as a dictionary-like object with the int default value type.

print(d['a']) # 1. Accessing index 'a', this should give us the int corresponding to it
# If the key didn't exist, the defaultdict would create a new key {with} the default value of int, which is 0, and return it.

print(d['c']) # As the key is invalid, it prints the default dict value, and as we didn't specified it, it will associate 0 to the key 'c', creating a ket value pair.