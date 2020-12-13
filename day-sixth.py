import sys
from time import sleep 
sleep(1)
print ('{:=^40}'.format(' \033[1;36mBEST BUY\033[m '))
sleep(1)
cost = float(input('\033[1mWhats is the cost of purchases? R$\033[m'))
sleep(1)
print ('''{:^40}
\033[1m[1] IN CASH OR CHECK
[2] THE VIEW ON THE CARD
[3] UP TO 2X ON CARD 
[4] UP TO 3X OR MORE ON THE CARD (20% INTEREST)\033[m '''.format(' \033[1;32mPAYMENT METHODS\033[m '))
option = int(input('\033[1mWhat will be your option?\033[m '))
if option == 1:
    total = cost - (cost * 10 / 100)
    print ('\033[1;32mPROCESSING...\033[m')
    sleep(2)
    print ('''\033[1;33m
The value of your purchase:\033[m \033[1;36mR${:.2f}\033[m.
\033[1;33mith the\033[m \033[1;36m10%\033[m \033[1;33mdiscount you will pay\033[m \033[1;36mR${:.2f}\033[m'''.format(cost,total))
elif option == 2:
    total = cost - (cost * 5 / 100)
    print ('\033[1;32mPROCESSING...\033[m')
    sleep(2)
    print ('''\033[1;33mThe value of your purchase:\033[m \033[1;36mR${:.2f}\033[m
\033[1;33mWith the\033[m \033[1;36m5%\033[m \033[1;33mdiscount you will pay\033[m R$\033[1;36m{:.2f}\033[m'''.format(cost, total))
elif option == 3:
    total = cost
    portion = total / 2
    print ('\033[1;32mPROCESSING...\033[m')
    sleep (2)
    print ('\033[1;33mYour purchase will be divided into\033[m \033[1;36m2x\033[m \033[1;33min the amount of\033[m \033[1;36mR${:.2f}\033[m \033[1;33mat the end INTEREST-FREE.\033[m'.format(portion))
elif option == 4:
    total = cost - (cost * 20 / 100)
    totP = int(input('\033[1;33mHow many installments will there be?\033[m '))
    portion = total / totP
    print ('\033[1;32mPROCESSING...\033[m')
    sleep(2)
    print ('\033[1;33mYour purchase will be divided into\033[m \033[1;36m{}x  R${:.2f}\033[m \033[1;33mWITH INTEREST\033[m'.format(totP, portion))
    print ('\033[1;33mYour purchase of\033[m \033[1;36mR${:.2f}\033[m \033[1;33min the end will cost\033[m \033[1;36mR$ {:.2f}\033[m.'.format(cost, total))
elif cost >= 5:
    total = 0
    print ('\033[1;31m{:^40}\033[m'.format(' OPTION INVALID '))
    sys.exit()
