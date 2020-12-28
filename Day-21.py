import sys
from time import sleep 
n1 = int(input('\033[1mType a number: '))
n2 = int(input('Type a number:\033[m '))
option = 0
while option != 5:
    sleep(1)
    print ('''\033[1;33m{:=^40}\033[m 
       \033[1m[1] SUM
       [2] MULTIPLICATION
       [3] BIGGER 
       [4] NEW NUMBERS
       [5] LEAVE\033[m'''.format(' CHOOSE BETWEEN '))
    sleep(1)
    option = int(input('\033[1mYour option:\033[m '))
    if option == 1:
        sum = n1 + n2
        sleep(1)
        print ('\033[1;32mThe sum in between\033[m \033[1;36m{}\033[m \033[1;32mand\033[m \033[1;36m{}\033[m \033[1;32mit´s\033[m \033[1;36m{}\033[m\033[1;32m.\033[m'.format(n1, n2, sum))
    elif option == 2:
        mult = n1 * n2
        sleep(1)
        print ('\033[1;32mThe multiplication in between\033[m \033[1;36m{}\033[m \033[1;32mand\033[m \033[1;36m{}\033[m \033[1;32mit´s\033[m \033[1;36m{}\033[m\033[1;32m.\033[m'.format(n1, n2, mult))
    elif option == 3: 
        if  n1 > n2:
            big = n1
        else: 
            big = n2
        sleep(1)
        print ('\033[1;32mThe largest number between\033[m \033[1;36m{}\033[m \033[1;32mand\033[m \033[1;36m{}\033[m \033[1;32mis\033[m \033[1;36m{}\033[m\033[1;32m.\033[m'.format(n1, n2, big)) 
    elif option == 4: 
        print ('Enter new numbers')
        sleep(1)
        n1 = int(input('Enter a number: '))
        sleep(1)
        n2 = int(input('Enter another number: '))
    elif option == 5: 
        sleep(1)
        print ('\033[1;32mFinishing the operation...\033[m')
        sys.exit()
    else: 
        print ('\033[1;31mOPTION INVALID! TRY AGAIN...\033[m')
