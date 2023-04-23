word = input('Enter word to encrypt: ')

encrypted = word.encode('utf-8')
decoded = encrypted.decode('utf-8')

print(f'Encoded word: {encrypted}')
print(f'Decoded word: {decoded}')