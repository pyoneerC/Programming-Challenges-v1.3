
# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools # Provides several higher-order functions that can be used for functional programming. Higher-order functions are functions that can take other functions as arguments or return functions as values. The functools module contains functions that can be used to create new functions by combining or modifying existing functions. (partial, reduce, wraps, etc.)

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y,:x + y,letters) # reduce() is about summing x,y strings [0] [1] for the first iteration, then [0,1] + [2], etc.
print(word) # ---> 'HELLO'

factorial = [5,4,3,2,1] #  Works the same way for [1,2,3,4,5] or [2,4,3,5,1]
result = functools.reduce(lambda x, y,:x * y,factorial) # reducing() and specifying the reduce functionality (* all items taking only two at a time until the end is reached)
print(result) # 120 ---> !5

# Basically 5,4,3,2,1 lambda x,y: x * y, (in all) factorial (iterable)
# 5 * 4 (x * y) 20 then,
# 20*3 (x * y) 60 until the end is reached (whole 'factorial' list) then,
# 60*2 . 120 * 1 = 120

# 2 args per iteration since there's 2 vars