from itertools import accumulate # default accumulation method is '+' if not specified, in the second example we specify to '*' all numbers

# Define a list of numbers
numbers = [1, 2, 3, 4]

# Use the accumulate function to compute the running total of the numbers
running_total = accumulate(numbers)

# Convert the running total iterator to a list and print it
print(list(running_total)) # Output: [1, 3, 6, 10]
                           #             |  |  |
                           # Original :[1+2+3+4] 


# There's certainly a more effective method to show only the final number instead of the entire list:

numbers1 = [1,2,3,4,5]

total = list(accumulate(numbers1)) [-1] # We do the same as above but show only index -1 (last number), rather than the entire list summed.
print(total) # 15

# If we put index -2 (or 3) it will show the sum up to before last number (4) ---> total sum being 10 (1+2+3+4)
# Index 0/-5 (1) ---> 1
# Index out of bounds ---> IndexError: list index out of range

# We can perform variety of math expressions in here, not only sums, we can do * if wanted:

import operator 

ab = [1,2,3,4]

total1 = list(accumulate(ab, func=operator.mul)) # [-1] We import operators and define the function to MULTIPLY the values. (same logic as before, -1 will give us only the last computed and * number (24 in this case), because 1*2*3*4 = 24)
print(total1) # [1, 2, 6, 24] ---> Like a !4

# operator.eq will give the list '[1, False, False, False] because it makes all numbers bool except the first and compare it, if values are same, True. In this example [1,2,3,4] all numbers are different so it will be [1, False, False, False], if we set ab to [1,1,2,3] it will be [1, True, False, False] as index1 is the same as the first one.add()

# import operator

# a = 5
# b = 5

# print(operator.eq(a, b))  # Output: True

import operator

abc = [2, 1, 90, 4, 5]

# Compute a running (live) maximum using the max function from the operator module
total2 = list(accumulate(abc, func=max))

# Compute a running (live) minimum using the min function from the operator module
total3 = list(accumulate(abc, func=min))

# Print the results
             # Original: [2, 1, 90, 4, 5]
print(total2)  # Output: [2, 2, 90, 90, 90] (Checks one by one and print the highest number detected so far) Step by step: starts with 2, print, 2 still bigger compared 1, print 2, sees 90, 90 is bigger than the previous higher (2), so print it, then 4, 90 stills highest, print, and 5, 90 still highest so result is [2,2,90,90,90]
print(total3)  # Output: [2, 1, 1, 1, 1]    (Checks one by one and print the lowest number detected so far) Step by step: Starts with 2, prints, then sees a 1, its the lowest so far!!! (compared to 1 and 2), sees 90, 1 is minimum recorded yet, so prints 1, and same with 4 and 5. Same logic as the above comment but reversed (instead of max, min) Final result [2,1,1,1,1]
