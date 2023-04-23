import random as rd
import time as t

list = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ñ', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J','K','L','M','N','S','O','P','Q','R','S','T','W','X','Y','Z', 'Ñ', '}', '{', '?', '¡', '|', '/', '=', ')', '(', '.','%','!','"','#','$','&', '_', '-', '[', ']', '^', '*')

print('Password generator')
print('-----------------------------------------')
t.sleep(1)

num =int(input('How many chars you want in the password? '))

password = ''

for i in range(num):
    password += rd.choice(list)

print(f'Your password is "{password}"')
