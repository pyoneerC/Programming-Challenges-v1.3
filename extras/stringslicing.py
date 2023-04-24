word = input('Enter word: ')

print(word[5:2:-1]) # 654
print(word[2:5:-1]) # Empty, in step -1 starting index must be bigger than second (switch position)
print(word[:3]) #First 3
print(word[3:]) #Strip first 3

while True:
    user_input = input("Enter a string (1-3 chars): ")
    if len(user_input) >= 1 and len(user_input) <= 3:
        break
    else:
        print("Please enter a string with 1-3 characters.")

print(f'The string you entered is: {user_input}')
