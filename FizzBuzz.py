#!/usr/bin/env python3

# Welcome to FizzBuzz!

fizzstring = ""

for i in range(100):
    if(i%3==0):
        fizzstring+='Fizz'
    if(i%5==0):
        fizzstring+='Buzz'
    if(i%3 != 0 and i%5 != 0):
        fizzstring+=str(i)
    print(fizzstring)
    fizzstring = ""
