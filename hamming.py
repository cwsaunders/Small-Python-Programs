#!/usr/bin/env python3
#DNA Sequence Hamming Program

while True:
    try:
        sequenceone = input('Insert sequence 1')
        if(sequenceone.isalpha()):
            break
        else:
            print('Error! Input must be a string of letters!')
    except TypeError:
        print('Error! Input must be a string of letters!')

while True:
    try:
        sequencetwo = input('Insert sequence 2')
        if(sequencetwo.isalpha() and len(sequenceone) == len(sequencetwo)):
            break
        else:
            print('Error! Input must be a string of letters and the same length as seq1!')
    except TypeError:
        print('Error! Input must be a string of letters and the same length as seq1!')
counter=0
for i in range(len(sequenceone)):
    if(sequenceone[i] != sequencetwo[i]):
        counter +=1
print(f'Hamming difference is {counter}')
