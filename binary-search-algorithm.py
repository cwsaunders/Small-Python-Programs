#!/usr/bin/env python3

# Basic binary search algorithm

import random

# Definitions

def binary_search(random_list, item):
    first = 0
    last = len(random_list)-1
    found = False
    while(first<=last and not found):
        mid = (first + last)//2
        if random_list[mid] is item:
            found = True
        else:
            if item < random_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

# Declarations
length = int(40)

#Fills list with pseudo-random numbers
numbers = [random.randint(0,100) for i in range(length)]

#Sorts pseudo-random numbers with Timsort
list.sort(numbers)

# User introduction
print('Binary Search Program\n\n')

# Input and exception handling
while True:
    try:
        userGuess = int(input('Guess an item between 0 and 100 from the list\n\n'))
    except ValueError:
        print('Invalid user input! Try again.')
    if(userGuess >= 0 and userGuess <= 100):
        break
    else:
        print('Input must be numbers between 0 and 100!\n')
   
# Tests user input against pseudo-random numbers and displays if the guess was within the list
if binary_search(numbers, userGuess) is True:
    print('Yes! You guessed correctly!')
else:
    print('No! No! Noooo! You have failed!')


