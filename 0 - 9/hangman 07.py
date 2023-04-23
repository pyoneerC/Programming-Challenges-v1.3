import random as r

words = ('python', 'pyoneerc', 'tomato', 'lettuce', 'computer')

word = r.choice(words)

print('Welcome to the hangman game!')

number = len(word)

print(f'The word has {number} characters.')

hidden = ['_'] * number

print(' '.join(hidden))

guesses = 0

while True:
    guess = input('Enter a character (a-z): ').lower()

    if guess in word:
        print(f'Correct! {guess} is in the word')

        for i in range(number):
            if word[i] == guess:
                hidden[i] = guess

        print(' '.join(hidden))
        
        if ''.join(hidden) == word:
            print('Congratulations, you have won!')
            break

    else:
        print(f'Incorrect! {guess} is not in the word')
        guesses += 1
        print(f'{guesses} / 6 guesses incorrect.')

        if guesses == 6:
            print(f'Too bad! You have lost the game. The word was "{word}".')
            quit()