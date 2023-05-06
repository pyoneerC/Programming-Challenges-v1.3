# def foo(a,b,c):
#     print(a,b,c)

# foo(1, b=2, c=3) # 1 2 3

# Assigning values as keys 'defaults' (cannot put 1, b=2 , 3), an error happens if we conversely do: (1, b=2, a=3 since a is already 1, it isn't dynamic in this way)


# def fooo(a, b=2, c, d=4):
#                  ^
# SyntaxError: non-default argument follows default argument

def food(a, b, *args, **kwargs):
    print(a, b) # print a,b in the same line together
    for arg in args:
        print(arg)
    for key, value in kwargs.items(): # keys and values in items(food)
        print(key, value)

food(1, 2, 3, 4, 5, six=6, seven=7)

# In this code, *args is used to accept any number of positional arguments, and **kwargs is used to accept any number of keyword arguments. The function prints the values of a and b, and then iterates over args and kwargs to print their values.

# When you call the function with food(1, 2, 3, 4, 5, six=6, seven=7), a is set to 1, b is set to 2, and args is set to (3, 4, 5). kwargs is set to {'six': 6, 'seven': 7}.

# The first loop prints the values of args, which are 3, 4, and 5. The second loop iterates over the key-value pairs in kwargs and prints them. The output shows that six is associated with 6, and seven is associated with 7.

def fa(a,b,*,c,d):  # ALL keyword arguments after * (args), if ** ---> kwargs

# kwargs example:

# def fa(a, b, *, **kwargs):
#     c = kwargs.get('c')
#     d = kwargs.get('d')
#     print(a, b, c, d)
    
# fa(1, 2, c=3, d=4)  # Output: 1 2 3 4

    print(a,b,c,d,) # no problem if ',' alone 

fa(1,2,c=3,d=4) # 1 2 3 4 (calling the function with these values will gives this values and also enter the function: the print, in essence.)

def f(*args, last):
    for arg in args:
        print(arg)
    print(last)

f(1,2,3, last=100) # error if we put 'f(a=1,b=2,c=3, last=100)' here.

# 1
# 2
# 3
# 100

# globals = (outer functions)

def u():
    global a
    a = b
    print(a)

b = -1 # first
u()
print(b)

# -1
# -1

# step by step:

# b is assigned the value -1.
# The function u is called.
# The variable a is assigned the value of b, which is -1.
# The value of a is printed, which is -1.
# The program continues to the next line, which prints the value of b, which is also -1.

def g():
    
    number=3 # LOCAL AND UNUSED, THATS WHY THE VALUE IS 0 AT THE END

#     def g():
#     global number
#     number = 3

# number = 0
# g()
# print(number)

# 3

number = 0
g()
print(number)

# 0