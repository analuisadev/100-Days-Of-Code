from random import randint
from time import sleep
computer = randint(0,100)
print ('=' * 28)
print ('\033[1;37;40mWelcome to the guessing game\033[m')
print ('=' * 28)
sleep(1)
print ('\033[1;32mI will think of a number from 0 to 100...\033[m')
player = int(input('What number did I think of? '))
sleep (1)
print ('\033[1;30mCHECKING...\033[m')
if player == computer:
    sleep (1)
    print ('Can you get it right :( \033[1;33mREMATCH\033[m')
else:
    sleep (1)
    print ('\033[1;31mYou didnt get it right HAHAHA, good luck next time\033[m')
