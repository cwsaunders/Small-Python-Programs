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

# Returns random word from text file
def getword():
    return random.choice(open("words.txt").readline().split())


# Introduction
print('Welcome to the hangman game of your dreams!\n')


word = getword()
print(f'Your word is {len(word)} characters long')
print('You have 5 body parts to spare')

while True:
    try:
        userguess = str(input('Enter your guess!'))
        if userguess == len(1) and userguess == string.ascii_letters():
            break
        else:
            print('Error! Your input must be a letter, and only 1 digit in length')
    except TypeError:
        print('Error! Your input must be a letter, and only 1 digit in length')
