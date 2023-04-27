from itertools import groupby # custom grouped by

def smaller_than_3(x): # Defining the function in which we will take base for grouping by.
    return x < 3 # The condition itself, which will return all elements < 3

lst = [1,2,3,4]

group_obj = groupby(lst, key=smaller_than_3) # we take the list and give the appropriate key, in this case, our function.

for key, value in group_obj: # Iterate over all the key and values of group_obj
    print(key, list(value)) # Prints the conditions next to the lists in fact

# True [1, 2] ---> < 3
# False [3, 4] ---> > 3

# groupby function groups the input list into two groups - one for elements less than 3 and one for elements greater than or equal to 3. The output shows the key (True/False) and the list of elements that belong to that key.

group_obj = groupby(lst, key=lambda x:x<3) # We can do the same as above but with a lambda (anonymous function) whose action is x < 3 instead of defining a function we'll use once.

for key, value in group_obj:
    print(key, list(value))

# True [1, 2] 
# False [3, 4] 

# Defining 'persons' as a list with dicts inside

persons = [{'name': 'Tim', 'age' : 25}, {'name':'Dan', 'age': 25},
           {'name': 'Lisa', 'age' : 27}, {'name': 'Claire', 'age' : 28}]

## Defining they key, in this case, a function that sorts (groupby) age.

group_object = groupby(persons, key=lambda x:x['age']) 

# The key function used for grouping is a lambda function that returns the age value for each dictionary.

# The groupby() function returns an iterator of pairs where the first element is the key (age in this case) and the second element is another iterator containing the values (dictionaries) that belong to that group.

# The code then iterates over the pairs and prints the age key and the list of people belonging to that group using the list() function to convert the iterator to a list.

# Iterating over the values. It will gives us the key (=lambda x:x['age']) and the values of form of list next to them.
for key, value in group_object:
    print(key, list(value))

# 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
# 27 [{'name': 'Lisa', 'age': 27}]
# 28 [{'name': 'Claire', 'age': 28}]