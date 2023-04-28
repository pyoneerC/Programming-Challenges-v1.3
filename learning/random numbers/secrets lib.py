from secrets import randbelow, randbits, choice, token_bytes, token_hex, SystemRandom, token_urlsafe, compare_digest # secret has 7 functions total, all listed here.
# secret lib for passwords, secrets, security, but takes more time than random numbers (for generating them)

# The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

# In particular, secrets should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling and simulation, not security or cryptography.
    
a = randbelow(10) # Accepts 1 argument, from 0 to x. 'RandBELOW' as it doesn't include the upper bound (10 in this case)
print(a) # 6

b = randbits(4) # Random number with 4 bits (binary) ---> 0 0 0 0 ---> 8 4 2 1 ---> Number between 0 - 15 in this case (both inclusive)
print(b) # 9 (0 - 15)

c = 'abcdefghi'

d = choice(c) # Random char from the string, changes with every execution. Can do it the same with lists and tuples. It also becomes handy when we have something like ['asa', 'as', 'dsf'] for selecting a random choice.
print(d) # i


# Token_bytes. Return a random byte string containing *nbytes* bytes.

# >>> token_bytes(16) # 16 bytes
# b'\xebr\x17D*t\xae\xd4\xe3S\xb6\xe2\xebP1\x8b'
# 'b' for binary at the beginning of every random byte string.

f = token_bytes() # Default is 32 bytes long (below example)

print(f) # b'l\x19^\xb2<\x9e\xea\x87\xba\rJ\x9f\x0b\xb9\x01\xdb\xf9\xec\xce/\xd3W4\xac\x99\x9d\xd3\xe41I_\xb3'.

# If *nbytes* is None or not supplied, a reasonable default is used, that changes with every execution (example above)

g = token_bytes(2) # Contains 2 bytes ( example below)

print(g) # b'\x8e\xd3'


# Return a random text string, in hexadecimal.

# The string has *nbytes* random bytes, each byte converted to two hex digits. 
# If *nbytes* is None or not supplied, a reasonable default is used.

# >>> token_hex(16)  
# 'f9bf78b9a18ce6d46a0cd2b0b86df9da'

h = token_hex() # 16 bytes default
print(h) # '56f39a715cef0ae1acf4acffb4ce03c51b6207ea95cd122b25edd74d3b192cd7' ---> The length of the string is 32 bytes since it is a hexadecimal string (each hexadecimal digit represents 4 bits). Therefore, 32 hexadecimal digits represent 32*4=128 bits or 16 bytes.

i = token_hex(2) # 2 bytes ---> The string generated with token_hex(2) has a length of 4 characters, because it contains 2 bytes, and each byte is represented by 2 hex digits.
print(i) # 'f79c'


# SystemRandom

# Create a SystemRandom instance
rng = SystemRandom()

# Generate a random integer between 1 and 10 (inclusive)
rand_int = rng.randint(1, 10)

print(rand_int) # 8

# This code creates a `SystemRandom` instance and uses its `randint` method to generate a random integer between 1 and 10 (inclusive). 
# Because `SystemRandom` uses the system's cryptographic random number generator, the random integer is highly unpredictable and can be used for secure applications such as generating passwords or encryption keys.


# token_urlsafe

# Return a random URL-safe text string, in Base64 encoding.

# The string has *nbytes* random bytes. If *nbytes* is None or not supplied, a reasonable default is used.

# >>> token_urlsafe(16) 
# 'Drmhze6EPcv0fN_81Bj-nA'

k = token_urlsafe() # 44 random characters by default.
print(k) # IlLOW4pdorO0nQ7q6qTR4Et0JGytOXw8Z4oVF_3RaoU

j = token_urlsafe(2)
print(j) # z_k


# compare_digest ---> compares two STRINGS (NOT INT, FLOAT, ETC.) for equality. It is designed to mitigate timing attacks that could occur when using regular string comparison.

# In the example you provided, compare_digest is used to compare the strings 'a' and 'a'. Since they are equal, the function returns True.

l = compare_digest('a', 'a')
print(l) # True (equal strings)

m = compare_digest('csd', 'gsw')
print(m) # False (not equal strings)