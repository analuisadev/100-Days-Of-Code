print ('\033[1;32m{:=^40}\033[m'.format(' MULTIPLICATION TABLE 2.0 '))
while True: 
    num = int(input('\033[1mType a number:\033[m '))
    print ('''\033[1m
[1] SUM
[2] MULTIPLICATION
[3] SUBTRACTION
[4] ADITTION\033[m''')
    option = int(input('\033[1mYour choice:\033[m '))
    for c in range(1, 11):
        if option == 1:
            print (f'\033[1m{num} + {c} = {num+c}\033[m')
        elif option == 2:
            print (f'\033[1m{num} x {c} = {num*c}\033[m')
        elif option == 3:
            print (f'\033[1m{num} - {c} = {num-c}\033[m')
        elif option == 4: 
            print ('\033[1m{} ÷ {} = {:.2f}\033[m'.format(num, c, num/c))
        if num <= 0:
            break
    print ('\033[1;33m{:=^40}\033[m'.format(' PROGRAM CLOSED '))
