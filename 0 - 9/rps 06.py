import time as t
import random as rd

options = ('rock', 'paper', 'scissors')

print('Welcome to RPS!')
t.sleep(.5)
print('You will be playing against me, pyoneerC!')
t.sleep(.5)
user_choice = input('Rock, paper or scissors?').lower().strip()

my_choice = rd.choice(options)

if user_choice == my_choice:
    print(f'It is a tie! We both selected {my_choice}.')

if user_choice == 'rock' and my_choice == "paper":
    print(f'You win! You selected {user_choice} and I chose {my_choice}.')

if user_choice == 'rock' and my_choice == "scissors":
    print(f'You win! You selected {user_choice} and I chose {my_choice}.')

if user_choice == 'scissors' and my_choice == "paper":
    print(f'You win! You selected {user_choice} and I chose {my_choice}.')

if user_choice == 'scissors' and my_choice == "rock":
    print(f'I win! You selected {user_choice} and I chose {my_choice}.')

if user_choice == 'paper' and my_choice == "rock":
    print(f'You win! You selected {user_choice} and I chose {my_choice}.')

if user_choice == 'paper' and my_choice == "scissors":
    print(f'I win! You selected {user_choice} and I chose {my_choice}.')