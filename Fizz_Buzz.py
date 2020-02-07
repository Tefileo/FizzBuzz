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

