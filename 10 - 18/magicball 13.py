from time import sleep
from random import choice

print("I'm the magic ball and I'll decide your fate!")
sleep(.5)
input('Enter your question: ')

answers = ['Maybe' , 'Never', 'Can be', "Don't event think about it", 'Of course' , 'Yes.', 'No.' , "I don't know", 'Possibly']

response = choice(answers)

sleep(1)
print('Processing...')
sleep(2)

print(f'{response}')