def name(a, b = 2):
    return a * b 

print(name(1))
print(name('a', 8))

def greet(name, greeting = 'Hello'):
        print(f"{greeting}, {name}!")

greet("John")
greet("Mary", "Hi")