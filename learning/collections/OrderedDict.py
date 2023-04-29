from collections import OrderedDict
o_dict = OrderedDict()
o_dict['a'] = 1
o_dict['b'] = 2
o_dict['c'] = 3
o_dict['d'] = 4
print(o_dict)

# Prints the ordered dict, by assigning the same order as received above. Yes, if we put 'a' : 1 at the end it will be at the end of the predict ---> OrderedDict([('d', 4), ('b', 2), ('c', 3), ('a', 1)])

# OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
# {'a': 1, 'b': 2, 'c': 3, 'd': 4} (if we put dict instead OrderedDict)