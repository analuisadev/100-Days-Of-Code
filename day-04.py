from time import sleep
name = str(input('\033[1;37mWhats your name?\033[m ')).strip()
print ('=' * 30)
print ('\033[1;37;40m       Welcome {}\033[m'.format(name))
print ('=' * 30)
investiment = float(input('\033[1;37;40mWhats is your value initial for investiment? R$\033[m '))
i = float(input('Monthly profitability: R$ '))
i = i / 100
mouth = int(input('\033[1;37;40mHow many months do you want it to stay?\033[m '))
investiment = (i+1)**mouth
print ('\033[1;37;40mThe amount you will receive in {} months will be R${}\033[m'.format(mouth, i))
sleep(1)
print ('\033[1;32mThank you for using the aplication, BYE :)\033[m')
