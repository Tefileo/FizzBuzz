# The game Fizz AND Buzz!
# multiple of 3 are POP
# multiple of 5 are TOC
# multiples of 3 and 5 are FizzBuzz
# as a user I should be ask for a number,
# so that I can play the game with my input
# As a player, I should see the game counting up to my number and
# substituting the multiples of 3 and 5 with the appropriate values,
# So that I can see if it is working
## EXTRA TASK!
# As a player, I should be able to exit the game using a key word,
# so that I can stop playing

import time
program = 'GO'

def three_mod(num1):
    return x % 3 == 0

def five_mod(num2):
    return x%5 == 0

while program != 'stop':
    x = int(input('Input a number to check if it is fizz or buzz: '))

    for x in range(0,x+1):

        if three_mod(x) and five_mod(x) and x != 0:
            print('FizzBuzz')
            time.sleep(0.1)
        elif three_mod(x) and x != 0:
            print('POP')
            time.sleep(0.1)

        elif five_mod(x) and x != 0:
            print('TOC')
            time.sleep(0.1)

        else:
            print(x)
            time.sleep(0.1)

    program = input('To stop game enter "STOP", otherwise hit "ENTER"').lower()

