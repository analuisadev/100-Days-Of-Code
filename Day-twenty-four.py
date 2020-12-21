answer = 'Y'
sum = average = amount = bigger = smaller = 0
print ('\033[1;32m{:=^40}\033[m'.format(' BIGGER AND SMALLER VALUES '))
while answer in 'Yy':
    n = int(input('\033[1mType a number: \033[m'))
    sum += n
    amount += 1
    if amount == 1: 
        bigger = smaller = n
    else: 
        if n > bigger:
            bigger = n
        if n < smaller:
            smaller = n
    answer = str(input('\033[1;33mDo you wish to continue? [Yes / No]:\033[m ')).upper().strip()[0]
average = sum / amount
print ('\033[1;32m{:=^40}\033[m'.format(' RESULT '))
print ('\033[1mYou entered {} numbers and their average was {}'.format(amount, average))
print ('''The highest value entered was {}
The lowest value entered was {}\033[m'''.format(bigger, smaller))
