def fibionacci(limit):
    # 0 1 1 2 3 5 8 13 21 ... (sum of the last 2 numbers)
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b,a + b

fib = fibionacci(30)

# Iterating trough all the function
for i in fib:
    print(i)

# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21

# 34 was the next, but it was above the limit!