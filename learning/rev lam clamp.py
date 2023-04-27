x = 5
y = 10
z = "Both x and y are positive" if x > 0 and y > 0 else "At least one of x and y is non-positive" # Conditional in a single line!!!! do:if...:else format.
print(z) # Both x and y are positive


# Clamp

import math

def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))

# We have to do the above function for setting a max and a min and clamping because clamp() itself don't exist in python (yet)

# Define a variable
x = 15

# Use clamp to set a minimum and maximum value. We deliver the values to the function.
x = clamp(x, 10, 20) # value, max, min

# The value of x will be 15, which is within the range of 10 to 20. We print what the function is returning.
print(x)

# Now set a new value for x
x = 5

# Use clamp again, but this time x is below the minimum value of 10. We deliver the values to the function.
x = clamp(x, 10, 20)

# The value of x will now be 10, which is the minimum allowed value.  We print what the function is returning.
print(x)

# Finally, set another new value for x
x = 30

# Use clamp one more time, but this time x is above the maximum value of 20. We deliver the values to the function.
y = clamp(x, 10, 20)

# The value of x will now be 20, which is the maximum allowed value.  We print what the function is returning (20).
print(y)


my_lambda = lambda a, b: a + b
result = my_lambda(3, 4)

print(result) # ANONYMOUS FUNCTION ---> 7

# lambda arguments (x): expression (x ** 2) (return)


# reverse=False parameter to the sort() method to sort the numbers in ascending order. 
# If we wanted to sort them in descending order, we would pass reverse=True instead. 

# numbers.sort(reverse=False) // (reverse=True)

# rev= True (ex. output: [8, 7, 5, 3, 2])
# rev = False (ex. output: [2, 3, 5, 7, 8])