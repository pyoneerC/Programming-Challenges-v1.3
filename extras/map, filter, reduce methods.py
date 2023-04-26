# sort

points2D = [(1, 2), (15, 1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1]) # [0] orders by 'x' values (default) ---> [(1, 2), (5, -1), (10, 4), (15, 1)] 

print(points2D) # [(1, 2), (15, 1), (5, -1), (10, 4)]. not sorted
print(points2D_sorted) # [(5, -1), (15, 1), (1, 2), (10, 4)]. SORTS BY [1] (Y) (-1 ,1 ,2,4)

points2D = [(1, 2), (15, 1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1], reverse=True) # Sorted by sum of pairs ---> bigger pair will be at the end, while the smallest will be at the begging. We can perform mathematical expression to sort lists like in here (* / - or importing math)!!!

print(points2D_sorted) # [(15, 1), (10, 4), (5, -1), (1, 2)]
                       #     16  ,     14   ,  4  ,     3    ----> order by sum of pairs (+ to -) (thanks to reverse)

points2D = [(1, 2), (15, 1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D, key=lambda x: x[0] * x[1]) # (reverse is false by default (that means - to +)). Sorted by multiplication of pairs ---> smallest numbers at the beginning

print(points2D_sorted) # [(5, -1), (1, 2), (15, 1), (10, 4)]


# map ---> Changes each value from the list that we specify to and in which way (ex. all numbers go ** 2)

# Long way

a = [1,2,3,4,5]
b = map(lambda x : x **2 , a) # a (list) contains the items to be squared, that's why we put it in here.
print(b) # <map object at 0x00000204BCA9BD90>. The map() function returns a map object which is an iterable, but not a list, so you can't directly print its contents.
print(list(b)) # [1, 4, 9, 16, 25] (all numbers go ** 2!!)

# Easy way

c = [x ** 2 for x in a] # COMPREHENSION LIST (METHOD) (for all items in a x ** 2 'em)
print(c) # [1, 4, 9, 16, 25] (all numbers go ** 2!!)


# Filtering (ex. even numbers from a list or tuple)

list = [1,2,3,4,4,4,4,4,5,6,7,8,8,8,8,8,9,10] # numoranychar = x ---> just demonstrating we can put anything in this spot.
d = [numoranychar for numoranychar in list if numoranychar%2==0] # if x is even ---> mod x is 0 (for can't go at the beginning lonely, there must be something before it (numoranychar in this case))
print(d) # [2, 4, 4, 4, 4, 4, 6, 8, 8, 8, 8, 8, 10] (filtered all even numbers in list! Can do the same with lambda but is way larger.)


# product (same as factorial) ---> grabs a list and * all of its members 

from functools import reduce # needed for reducing

list1 = (1,2,3,4)

product = reduce(lambda x,y: x*y, list1) # "I'll take  list1 and some x,y values and * 'em"
print(product) # 24 (multiples all the numbers in the tuple/list ---> its like doing a !4)