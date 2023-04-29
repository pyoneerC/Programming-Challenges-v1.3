# yield return and pauses function till its called again next

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

# Giving int 4 to the function
cd = (countdown(4)) # Prints 'starting'

value = next(cd) # Error as the while is over.
print(value)

# Printing the yield
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))

# We define a generator function countdown(num) that takes a number num and uses a while loop to yield a sequence of numbers from num down to 1. The yield statement pauses the function and returns the current value of num, and then resumes the function on the next line when the generator is called again.
# We create a generator object cd by calling countdown(4).
# We call next(cd) to get the next value from the generator, which is the starting value of num (4) in this case. This value is stored in the variable value.
# We print value (which is 4).
# We call next(cd) four more times to get the remaining values from the generator, which are 3, 2, 1, and then the generator stops and raises a StopIteration exception.