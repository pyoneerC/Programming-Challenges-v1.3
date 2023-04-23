import random
import time

number = int(input("Enter a number between 1-10 "))

random = random.randint(1, 10)

if number == random:
    print(f'You guessed it! random number was {random}.')

elif number < random:
    print(f'Too bad, the number was {random}.')
    
elif number > random:
    print(f'Incorrect, the number was {random}.')

time.sleep(.8)
print('Thanks for playing!')