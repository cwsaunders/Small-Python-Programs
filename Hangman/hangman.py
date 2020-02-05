#!/usr/bin/env python3

# NOTE: HANGMAN GAME NOT COMPLETE
#
#
#
#
#
#
#
#
#
#
#
#
#

import random
import string
import os

# Returns random word from text file
def getword():
    abs_dir = os.path.dirname(__file__)
    rel_path = "words.txt"
    abs_file_path = os.path.join(abs_dir, rel_path)
    return random.choice(open(abs_file_path).readline().split())


# Introduction
print('Welcome to the hangman game of your dreams!\n')


word = getword()

# This below list is to iterate through with guesses
wordlist = list(word)

# List to show player unguessed and guessed letters
for x in range(wordlist):
    hiddenlist[x] = '*'

# Initial game information
print(f'Your word is {len(word)} characters long')
print('You have 5 body parts to spare')
print(*hiddenlist, end=" ")
print('is your word!')

# Guess counter
counter = 0

# Checks to see if entire word is guessed or game over
finished = False

while not finished:
    # Error checking for user guess
    while True:
        try:
            userguess = str(input('Enter your guess!'))
            if len(userguess) is 1 and userguess.isalpha():
                break
            else:
                print('Error! Your input must be a letter, and only 1 digit in length')
        except TypeError:
            print('Error! Your input must be a letter, and only 1 digit in length')
    # Edits user-shown list when letter guessed
    # Shortenes list of letters to guess when correct letter guessed
    # Increases counter if a 'life' is lost
    for x in range(wordlist):
        if userguess is wordlist[x]:
            hiddenlist[x] = userguess
            worldlist.remove(f'{userguess}')
            print(f'Your guess ({userguess}), was correct!')
            break
        elif userguess not any(wordlist):
            counter += 1
            print(f'Your letter was not in the word! You have {5-counter} attempts left')
            break
    # Checks if attempts out or word guessed
    if len(wordlist) is 0 or counter > 5:
        finished = True
    print('Word: ', end='')
    print(*hiddenlist)

    # Checks if win vs loss
    if counter > 5:
        print('Game over! You lose')
    elif len(wordlist) is 0:
        print('You win! Congratulations!') 