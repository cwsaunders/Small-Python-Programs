#!/usr/bin/env python3

import random
import string
import os

# Returns random word from text file
def getword():
    abs_dir = os.path.dirname(__file__)
    rel_path = "words.txt"
    abs_file_path = os.path.join(abs_dir, rel_path)
    lines = open(abs_file_path).read().splitlines()
    return random.choice(lines)


# Introduction
print('Welcome to the hangman game of your dreams!\n')


word = getword()

# This below list is to iterate through with guesses
wordlist = list(word)

# List to show player unguessed and guessed letters
hiddenlist = []
for x in range(len(wordlist)):
    hiddenlist.append('*')

# Initial game information
print(f'Your word is {len(word)} characters long')
print('You have 5 body parts to spare')
print(*hiddenlist, end=" ")
print('is your word!')

# Failed guess counter
counter = 0
counter2 = 0
# Checks to see if entire word is guessed or game over
finished = False

while (not finished and counter < 5):
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
    for i in range(len(wordlist)):
        if(userguess == wordlist[i]):
            hiddenlist[i] = wordlist[i]
            counter2 += 1
        elif(i == (len(wordlist)-1) and userguess != wordlist[i] and counter2 == 0):
            counter += 1
            print(f'Incorrect guess! You have {5-counter} body parts left!')
            print(*hiddenlist, end=" ")
            break
        
        if(i==(len(wordlist)-1) and counter2 > 0):
            while(counter2>0):
                counter2 -=1
            print(*hiddenlist, end=" ")
    for i in (range(len(hiddenlist))):
        anyasterisk = 0
        if(hiddenlist[i] == '*'):
            anyasterisk += 1
            break
    if(anyasterisk == 0):
        finished = True
    if(anyasterisk >= 1):
        anyasterisk = 0
if(finished == False):
    print('You lost!')
elif(finished == True):
    print('You won!!!!')

