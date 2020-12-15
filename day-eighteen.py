from time import sleep
print ('\033[1m{:=^40}\033[m'.format(' PALINTHROME DETECTOR '))
phrase = str(input('\033[1mType a phrase:\033[m ')).strip().upper()
sleep(1)
p = phrase.split()
together = ''.join(p)
reverse = together[::-1]
print ('\033[1mThe reverse of\033[m \033[1;32m{}\033[m \033[1mis\033[m \033[1;32m{}\033[m'.format(together, reverse))
sleep(1)
if reverse == together: 
    print ('\033[1mThat phrase is a\033[m \033[1;33mPALINTHROME\033[m')
else: 
    print ('\033[1mThat phrase is not\033[m \033[1;31mPALINTHROME\033[m')