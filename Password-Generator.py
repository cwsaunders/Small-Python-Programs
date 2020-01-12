#!/usr/bin/env python3

import random
import string

# Generates password from recieved inputs
def generate(length):
    char = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(char) for x in range(length))
def generateWithSpecial(length):
    char = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    return ''.join(random.choice(char) for x in range(length))


        
        




print('Welcome to "Ye Olde Password Generator!"\n\n')

# Length of password
while True:
    try:
        length = int(input('How long would you like your password to be?'))
        if length < 36 and length > 8:
            break
        else:
            print('Whoops! Entry must be between 36 and 8 characters')
    except (TypeError):
        print('Whoops! That does not fit the proper criteria!')
# Special Characters question
while True:
    try:
        special = str(input('Would you like special characters in your password? (Y/N)'))
        if special == 'Y' or 'y':
            break
        if special == 'N' or 'n':
            break
        else:
            print('Whoops! Please select Y or N')
    except (TypeError):
        print('Whoops! That does not fit the proper criteria!')


# Calls generate password function with or without special characters
if special == 'y':
    print(generateWithSpecial(length))
elif special == 'Y':
    print(generateWithSpecial(length))
elif special == 'n':
    print(generate(length))
elif special == 'N':
    print(generate(length))



