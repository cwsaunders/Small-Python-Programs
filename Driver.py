#!/usr/bin/env python3

import random

# Functions

def checkwinner(usertrans, computer):
    if usertrans == 0 and computer == 0:
        print('Tie!')
    elif usertrans == 0 and computer == 1:
        print('Victory!')
    elif usertrans == 0 and computer == 2:
        print('Epic failure! - You lose!')
    elif usertrans == 1 and computer == 0:
        print('Epic failure! - You lose!')
    elif usertrans == 1 and computer == 1:
        print('Tie!')
    elif usertrans == 1 and computer == 2:
        print('Victory!')
    elif usertrans == 2 and computer == 0:
        print('Victory!')
    elif usertrans == 2 and computer == 1:
        print('Epic failure! - You lose!')
    elif usertrans == 2 and computer == 2:
        print('Tie!')
    else:
        print('You entered the wrong input!')



print('Welcome to the ultimate game - Rock, Paper, Scissors')

usertrans = int(0)
userinput = input('\n\nPick your poison: R, P, S\n')


computer = random.randint(0, 2)

 # 0 = Rock
 # 1 = Scissors
 # 2 = Paper

if userinput == 'R' or userinput == 'r':
    usertrans += 0
elif userinput == 'S' or userinput == 's':
    usertrans += 1
elif userinput == 'P' or userinput == 'p':
    usertrans += 2
else:
    print('Incorrect entry!')

print(usertrans)
print(computer)

checkwinner(usertrans, computer)















