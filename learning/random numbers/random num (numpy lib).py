from numpy import random, array

# In numpy: array ---> TUPLES, LISTS INSIDE A LIST. LISTS AREN'T ARRAYS PER SE. ARRAY ---> ([[1,2,3], [4,5,6]]) (2D array that contains 3 elements per dimension)

# As all values are random their result changes in the console per every execution.

a = random.rand(3,3) # We generate a random numpy array with 3 lists inside, making it 3d. First 3 means amount of lists and second, dimensions. 
print(a)

# [[0.78611744 0.07698001 0.83002412]
#  [0.07441687 0.82436361 0.28588398]
#  [0.73489227 0.1884361  0.35399579]]

# In this case, the dimensions are 3x3, meaning that the resulting array has 3 rows and 3 columns. The array contains floating-point numbers between 0 and 1, which are randomly (random) generated.

b = random.randint(0, 8, 3) # Random list with 3 MEMBERS, which members go from 0 - 8 int values
print(b) # [4 1 5]

c = random.randint(0, 10, (3,4)) # In this case, we generate a 3(height) x 4(length) dimensional array, filled with values from 0 - 10 (inclusive as it's randINT)
print(c)

# [[3 7 4 1]
#  [7 3 8 9]
#  [1 1 5 5]]

arr = array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)

# Prints like a matrix, not like an inline array
      
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

random.shuffle(arr) # Remember that shuffle returns none, so if we assign this a variable 'a' and print(a) it will print 'None' in console, we got to do it this way. We random'd shuffled the array, now we print the original array as its changed, we do not print the shuffled(arr)
print(arr)

# Shuffled array (in this case: first row go to second, this to last and last to first). No shuffle between specific [] (lines), only shuffling different rows. As it is random, changes with every execution. 

# [[7 8 9]
#  [1 2 3]
#  [4 5 6]]

random.seed(1)
print(random.rand(3,3))
random.seed(1)
print(random.rand(3,3))

# Same results in both (as seeds are equal): 

# [[4.17022005e-01 7.20324493e-01 1.14374817e-04]
#  [3.02332573e-01 1.46755891e-01 9.23385948e-02]
#  [1.86260211e-01 3.45560727e-01 3.96767474e-01]]
# [[4.17022005e-01 7.20324493e-01 1.14374817e-04]
#  [3.02332573e-01 1.46755891e-01 9.23385948e-02]
#  [1.86260211e-01 3.45560727e-01 3.96767474e-01]]

random.seed(2)
print(random.rand(3,3))

# Different seed, different number, like minecraft seeds

# [[0.4359949  0.02592623 0.54966248]
#  [0.43532239 0.4203678  0.33033482]
#  [0.20464863 0.61927097 0.29965467]]


# Why we should use numpy seeds rather than python default random seed? 

# When we call numpy.random.seed, it sets the internal state of NumPy's random number generator, which determines how random numbers are generated. This ensures that the same sequence of random numbers will be generated each time we run the code, which is useful for testing and debugging purposes.
# On the other hand, Python's random.seed function sets the seed for Python's built-in Mersenne Twister pseudo-random number generator. This generator is sufficient for generating random numbers for most applications, but it is not designed to generate high-dimensional arrays of random numbers like NumPy's random number generator.
# So, we should use NumPy's random number generator with its seed function to generate arrays of random numbers and ensure reproducibility of results.