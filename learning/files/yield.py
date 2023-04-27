def fetch_lines(filename):
    with open ('C:\\Users\\Users\\Desktop\\prog chall py\\learning\\files\\yield.txt') as file:
        for line in file:
            yield line # Returns one line at a time and forgets it without storing in memory and without returning the word list, saving resources.

lorem = fetch_lines('C:\\Users\\Users\\Desktop\\prog chall py\\learning\\files\\yield.txt')

print(next(lorem))
print(next(lorem))
print(next(lorem))
print(next(lorem))
print(next(lorem))

# Result;

# Lorem Ipsum is simply dummy text of the printing and typesetting industry. (line 8 .py, line 1 .txt)

# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, (line 9, line 2 .txt)

# when an unknown printer took a galley of type and scrambled it to make a type specimen book.

# It has survived not only five centuries, but also the leap into electronic typesetting,

# remaining essentially unchanged.