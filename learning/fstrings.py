number = 3.14159265359
print(f'{number:.2f}')  # Output: 3.14

number = 3.14159265359
print(f'{number:10.2f}')  # Output:      3.14 (10 char wide, 3.14 gets 4, so 6 spaces left)

number = 3.14159265359
print(f'{number:.24f}')  # Output: 3.141592653590000061569754

fraction = 0.75
print(f'{fraction:.0%} of the time, it works every time.')
# Output: 75% of the time, it works every time. .1%, +1 float

x = 3
y = 4
print(f'The sum of {x} and {y} is {x + y}')
# Output: The sum of 3 and 4 is 7

print(f'The sum of {x} and {y} is {(((x + y) * 7) // 7) - 7}')
# Output: The sum of 3 and 4 is 0. / ---> division (float 0.0) // ---> floor div ( 5 // 2 ) ---> 2

x = 42 # -42
print(f'Binary: {x:b}, Octal: {x:o}, Hexadecimal: {x:x}')
# Output: Binary: 101010, Octal: 52, Hexadecimal: 2a (only int or neg int, not floats/str)

message = 'Hello, world!'
print(f'{message:^20}')
# Output:   Hello, world! (3 spaces and 3 spaces)
#Centered 20 spaces

name = 'Alice'
age = 30
print(f'{name:<10} is {age} years old')
# Output: Alice      is 30 years old (< space to the right)

num = 1234
print(f'{num:>10}')  # output: '      1234'

print(f"{10:5}") #   10
print(f"{5:10}") #         5 

print(f'{7.6*0.25:.2f}') # 1.90

long_string = 'abcdefg'
print(f'{long_string[:5]}...')
# abcde...

print(f'{10000000000:,}')
# 10,000,000,000

print(f'{10000000000*32:,}')
# 320,000,000,000

# Dictionaries

name = 'John'
info = {'age': 25, 'gender': 'male'}
print(f'{name} is {info["age"]} years old and is {info["gender"]}')
# John is 25 years old and is male (refers to key to get to value)

# Functions

def multiply(x, y = 3):
    return x * y

print(f'The result of 2 x 3 is {multiply(2,)}')
# The result of 2 x 3 is 6 (sends and receives values from the function through f-string)

# Conditional statements 

name = 'Lucy'
age = 21
print(f'{name} is {age} years old {"and is an adult" if age >= 18 else "and is a minor"}')
# Lucy is 21 years old and is an adult

name = 'Alice'
age = 25
city = 'New York'
country = 'USA'
print(f'{name} is {age} years old and lives in {"New York" if city == "New York" else "another city"} {"in the USA" if country == "USA" else "abroad"}')
# Alice is 25 years old and lives in New York in the USA (2 conditionals , 2 {})

# Loops

numbers = [1, 2, 3, 4, 5]
print(f'{", ".join(str(num) for num in numbers)}')
# 1, 2, 3, 4, 5 (makes each number str and append , in the end, if no str: TypeError)

# Booleans

result = True
print(f'The result is {"True" if result else "False"}')
# The result is True

result = 0
print(f'The result is {"True" if result else "False"}')
# The result is False

name = 'John'
job = 'Developer'

print("{} is a {}".format(name, job)) # John is a Developer. Takes name in the first {} then job all inside the print

# Time formatting 

import datetime

#        module . class  . method (gets real time)
today = datetime.datetime.today()
print(f'Today is {today:%B %d, %Y}')
# Today is April 24, 2023 (month (str)), day(num), years (full ---> 2023))

# %B ---> Month as locale’s full name. ---> January, February, …, December (en_US)
# %d ---> Day of the month as a zero-padded decimal number. ---> 01, 02, …, 31
# %Y ---> Year with century as a decimal number ---> 1970, 1988, 2001, 2013
# %% ---> Literal '%'

# We can separate with ,/./-/_(literal [WILL BE PRINTED]) or no, depends in what we want, result will have , or no (12, AM or 12 AM)

today = datetime.datetime.today()
print(f'Today is {today:%H/A,,%%., %p,- %A*5, %B,_ %Y}') # It is possible to put any symbol's / chars as wanted
# Today is 11/A,,%., AM,- Monday*5, April,_ 2023

today = datetime.datetime.today()
print(f'Today is {today:%H %p, %A, %B %Y}')
# Today is 11 AM, Monday, April 2023

today = datetime.datetime.today()
print(f'{today:%f %Z, %j, %W %x}')
# 917976 , 114, 17 04/24/23

# https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior