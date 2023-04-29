from collections import namedtuple

# Creates a named tuple called point with two fields: x and y.
# he namedtuple() function is used to create a new subclass of tuple with named fields. In this case, point is the name of the new subclass, and x and y are the field names.
point = namedtuple('point', 'x,y')

# An instance of point is created with values 1 and -4 for the x and y fields, respectively. 
pt = point(1, -4)

# Shows the named tuple with its field names and values.
print(pt)

# point(x=1, y=-4)

# Prints the individual values of x, y with no tuple or anything. We can access each field of the tuple using the dot notation, as in pt.x and pt.y.
print(pt.x, pt.y)

# 1 -4