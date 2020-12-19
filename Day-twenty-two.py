print ('\033[1;33m{:=^40}\033[m'.format(' PROGRESSÃO ARITMÉTICA 2.0 '))
first = int(input('\033[1mEnter the first term: '))
reason = int(input('Reason:\033[m '))
term = first
cont = 1 
total = 0
bigger = 10
while bigger != 0:
    total = total + bigger
    while cont <= total: 
        print ('\033[1m{} ->\033[m' .format(term), end = '\033[1m \033[m')
        term += reason
        cont += 1
    print ('\033[1;31mBREAK\033[m')
    bigger = int(input('\033[1;32mHow many terms do you want to put the most?\033[m '))
print ('\033[1;36mOperation ended with\033[m \033[1;33m{}\033[m \033[1;36mterms shown.\033[m'.format(total))
    
