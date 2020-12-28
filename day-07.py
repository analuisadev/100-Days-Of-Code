from random import randint 
from time import sleep
print ('=' * 18)
print ('\033[1mSTONE PAPER AND SCISSORS\033[m')
print ('=' * 18)
print ('I already chose mine now missing you')
sleep (1)
computer = randint (1, 3)
player = int(input('\033[1mChoose between\033[m \033[1;33m1) Stone 2) Paper  and 3) Scissors\033[m : '))
sleep(1)
if (player < computer):
    print ('\033[1;33mThought about {}\033[m'.format(computer))
    print ('\033[1;32mI WIN HEHE :D\033[m')
elif (player == computer):
    print ('\033[1;33mThought about {}\033[m'.format(computer))
    print ('\033[1;31mTIE, LET´S GO AGAIN\033[m')
else:
    print ('\033[1;33mThought about {}\033[m'.format(computer))
    print ('\033[1;36mYOUR LOST HAHAHA:D\033[m ')
