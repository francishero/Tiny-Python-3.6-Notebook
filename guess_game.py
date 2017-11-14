"""
A python program for the guessing game
We generate a random number : secretNumber
We allow user to enter a guess: guess
We check if the guess is less or higher than the secretNUmber
WE do this while the user has 6 chances
Otherwise they guessed the number and won
"""

#we import from the python standard library some code
#this code allows us to generate a random number


import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
