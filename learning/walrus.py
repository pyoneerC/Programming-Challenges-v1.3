list = 'abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd'

a = list.split()

if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")

    # Walrus saves lines of code, if not using it we'll need to do a line defining n = len(a))
    # print( happy := True) [:= inside () for assigning value tom something in a larger expression]

# := always surrounded by ()
# <= less or =. >= more or eq <: >:

# some_list = [2, 4, 6, 8, 10]

# Without walrus operator

# if len(some_list) > 0:
#     first_item = some_list[0]
# else:
#     first_item = None
    
# With walrus operator

# if len(some_list) > 0 and (first_item := some_list[0]) is not None:
#     do_something(first_item)

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#             break
# foods.append(food)

foods = []
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

print(list(range(1,10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]. Print list in ranges 0-9 (nice to know)


pi=[0,1,2]

l=pi[1] # 1
j=l+pi[2] # 1 + 2 = j
print(j) # 3