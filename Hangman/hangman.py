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

for x in range(wordlist):
    hiddenlist[x] = '*'


print(f'Your word is {len(word)} characters long')
print('You have 5 body parts to spare')
print(*hiddenlist, end=" ")
print('is your word!')

finished = False

while not finished:
    while True:
        try:
            userguess = str(input('Enter your guess!'))
            if len(userguess) is 1 and userguess.isalpha():
                break
            else:
                print('Error! Your input must be a letter, and only 1 digit in length')
        except TypeError:
            print('Error! Your input must be a letter, and only 1 digit in length')
    for x in range(wordlist):
        if userguess is wordlist[x]:
            hiddenlist[x] = userguess
            worldlist.remove(f'{userguess}')
            print(f'Your guess ({userguess}), was correct!')
            
