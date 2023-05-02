def foo(a, b, c):
    print(a,b,c)

mylist = {0,1,2} # Also works with: dicts, lists, tuples and sets.
foo(*mylist)

mydict = {'a': 0, 'b':1, 'c':2}
foo(**mydict) # 1 * only prints keys 'a b c'. ** sends values, printing 0,1,2

numbers = {1,2,3,4,5,6} # Works with [] and () too.
*beginning, last = numbers # * = [] except last.

print(beginning) # [1, 2, 3, 4, 5]
print(last) # 6 (no *, lonely item)

numbers2 = {1,2,3,4,5,6}
asias, *middle, almostlast, last = numbers # We can put any names here. Each name will take a value if it's not packed (*) asias ---> 1. *middle ----> [2,3,4]. almostlast ---> 5. last ---> 6 
print(asias) # 1 (unpacked, no *)
print(middle) # [2, 3, 4] (packed *) Only [2, 3, 4] because 1 is already unpacked, same as last 2 numbers.
print(almostlast) # 5
print(last) # 6

# * is for UNPACKING, and only one is allowed per unpacking. ex. We can't put *beginning and *last, only one, if no, we'll encounter an error.

# Only middle is packed by using *

# Merge *

mytuple = (1,2,3)
mylist1 = {4,5,6}

# We can do it with [], if wanted.

newlist = (*mytuple, *mylist1)
print(newlist) # Unpacks all and put it inside a tuple ---> (1, 2, 3, 4, 5, 6). First mytuple then mylist1. We merging a tuple and a list by unpacking * method.

dicta = {'a' : 1, 'b' : 2}
dictb = {'c' : 3, 'd' : 4}
dictc = {'e' : 5, 'f' : 6}

newdict = {**dicta, **dictb, **dictc} # We can merge as many dicts we want, no limit.

# If we try to put a single *, it won't allow us, that in the prevois example it did allow us, but printing literal keys. Now * = error in merging dicts

print(newdict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Note that order is key. If we merge **dict1 then 2 and 3 that will be the order: the 1 first, then the other 2. This can be changed freely if needed.