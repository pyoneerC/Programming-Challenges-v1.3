from collections import deque

# Creating the deque
d = deque()

# Appending values
d.append(1)
d.append(2)

print(d)

# deque([1, 2])

# Appending a value to the left
d.appendleft(3)
print(d)

# deque([3, 1, 2])

# Removing element from the left and printing the table, as well as the popped number. Pop pops value from right by default
a = d.popleft()
print(d) # deque([1, 2])
print(a) # 3 --> Popped num

# Clearing the deque
# d.clear()
# print(d)

# deque([])

# Extending the deque appending numbers at the left 
d.extend([3,4,5])
print(d)

# deque([1, 2, 3, 4, 5])

# Extends to the left (add items in the left). Always inside [( )] the values to append (this and before example)

d.extendleft([0])
print(d)

# deque([0, 1, 2, 3, 4, 5])
# Added  | num at the left!

# We move rotate the deque by 1, so the last element become first, moving the old 1st x(1 in this case) movements to the right
d.rotate(1) # Does not generate a new list, we are modifying the original with all these deque modifiers
print(d)

# Original: deque([0, 1, 2, 3, 4, 5])
# Rotated: deque([5, 0, 1, 2, 3, 4])

# Same with negative rotation. If it's -1, the first item will become last, and will move the previous last x ([-] 2 in this case) spots to the LEFT

d.rotate(-2) # -2 in this case as the matrix was already rotated +1
print(d)

# Original: deque([0, 1, 2, 3, 4, 5])
# Rotated: deque([1, 2, 3, 4, 5, 0])

# They follow the same logic but reversed. Note that no number got excluded, it's just a rotation.