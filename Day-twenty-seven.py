score = 0
from random import randint
print ('\033[1;32m{:=^40}\033[m'.format(' EVEN OR ODD? '))
while True: 
    player = int(input('\033[1mType a value:\033[m '))
    computer = randint(0, 11)
    total = player + computer
    typ = ' '
    while typ not in 'EO':
        typ = str(input('\033[1;35mEven or Odd?\033[m ')).strip().upper()[0]
    print (f'\033[1;32mYour played\033[m \033[1;36m{player}\033[m \033[1;32mits the computer played\033[m\033[1;36m{computer}\033[m \033[1;32mand the total is\033[m \033[1;36m{typ}\033[m', end = ' ')
    print ('\033[1;36mHe gave even\033[m' if total % 2 == 0 else '\033[1;36mHe gave odd\033[m')
    if typ == 'E': 
        if total % 2 == 0:
            score += 1
            print ('\033[1;34mYou WON the game!\033[m')
        else: 
            print ('\033[1;31mYou LOST the game!\033[m')
            break 
    elif typ == 'O':
        if total % 2 == 1:
            print ('\033[1;34mYou WON the game!\033[m')
            score += 1
        else: 
            print ('\033[1;31mYou LOST the game!\033[m')
            break
    print ('\033[1mLets play again: D ....')
print (f'\033[1mYou won {score} times, congratulations\033[m')
