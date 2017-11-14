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

#we declare a secretNumber variable and store the random number
secretNumber = random.randint(1,20)

#welcome message
print("WELCOME TO THE GUESSING GAME")
#we simulate an infinite loop

while True:
    print("Enter your guess number: ")

    # we give the user 6 chances
    for guessTime in range(1,7):

        # we grab whatever the user enters
        guess = int(input()) #input returns a string but we make it a number

        #here is the game logic

        if guess < secretNumber:
            print("Try something higher...")
        elif guess > secretNumber:
            print("Try something less...")
        else:
            # they found the answer!
            # why?
            # because this number is not less and not higher
            # so its equal :)

            break #we break out of the infinite loop
if guess == secretNumber:
    print("Wow you won afte {0} tries".format(guessTime))
else:
    print("Sorry but you lost i was looking for {0}".format(secretNumber))
