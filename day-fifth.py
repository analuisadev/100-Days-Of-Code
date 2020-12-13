import sys
from time import sleep
import pygame
pygame.mixer.init()
pygame.mixer.music.load('Lullabyes_50k.mp3')
pygame.mixer.music.play()
#Init
print ('''\033[1;36m
██████╗░░█████╗░███╗░░██╗██╗░░██╗  ░█████╗░███████╗
██╔══██╗██╔══██╗████╗░██║██║░██╔╝  ██╔══██╗██╔════╝
██████╦╝███████║██╔██╗██║█████═╝░  ██║░░██║█████╗░░
██╔══██╗██╔══██║██║╚████║██╔═██╗░  ██║░░██║██╔══╝░░
██████╦╝██║░░██║██║░╚███║██║░╚██╗  ╚█████╔╝██║░░░░░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░╚════╝░╚═╝░░░░░

██████╗░██████╗░░█████╗░███████╗██╗██╗░░░░░
██╔══██╗██╔══██╗██╔══██╗╚════██║██║██║░░░░░
██████╦╝██████╔╝███████║░░███╔═╝██║██║░░░░░
██╔══██╗██╔══██╗██╔══██║██╔══╝░░██║██║░░░░░
██████╦╝██║░░██║██║░░██║███████╗██║███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝╚══════╝\033[m''')

sleep(2)
choice = int(input('''\033[1m[1] Loan
[2] Deposit
Your choice:\033[m '''))
sleep(1)
#Some conditions and variables are giving error, I will fix them
if choice == 1:
    vLoan = float(input('What is the loan amount? R$ '))
    vMouthly = float(input('What is the value of your MONTHLY income? '))
    years = int(input('How many years to repay the loan? '))
    mouthly = years * 12
    loan = vMouthly / mouthly
    total = (vMouthly / 100) * 30
    sleep(1)
    if loan <= total:
        print ('\033[1;31mLoan not approved!\033[m') 
        sys.exit()
    else:
        print ('\033[1;32mR${} loan approved\033[m'.format(vLoan))
        sys.exit()
#Sending the deposit
    if choice == 2: 
        v = float(input('\033[1;33mWhat is the amount of your deposit? R$ ' ))
    nameS = str(input('\033[1;32mEnter the name of the account holder: '))
    accountNum = float(input('Enter account number: '))
    agenNum = int(input('Enter the agency number: '))
    cpf = str(input('Enter the CPF number:\033[m '))
    print ('''The amount of R$ {} was successfully deposited into the account of:
Name: {}
Number Acconunt: {}
Agency: {} 
CPF: {}\033[m'''.format(v, nameS, accountNum, agenNum, cpf))

