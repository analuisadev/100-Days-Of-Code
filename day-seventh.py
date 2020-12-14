from time import sleep
print ('\033[1;36m{:=^40}\033[m'.format(' MULTIPLICATION TABLE '))  
num = int(input('\033[1mChoose a number:\033[m '))
print ('''\033[1m{:=^40}\033[m
\033[1;33m[1] Sum
[2] Subtraction
[3] Multiplication
[4] Addition\033[m'''.format(' Which multiplication table do you choose? '))
option = int(input('\033[1mYour choice:\033[m '))
if option == 1: 
    for c in range(1, 11):
        print ('\033[1m{} + {} = {}\033[m'.format(num, c, num+c))
elif option == 2:
    for c in range(1, 11):
        print ('\033[1m{} - {} = {}\033[m'.format(num, c, num-c))
elif option == 3:
    for c in range(1, 11):
        print ('\033[1m{} x {} = {}\033[m'.format(num, c, num*c))
else:
    for c in range(1, 11):
        print ('\033[1m{} ÷ {} = {:.2f}\033[m'.format(num, c, num/c))
