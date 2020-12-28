print ('=' * 31)
numInt = int(input('\033[1;32mEnter an integer of your choice:\033[m '))
print ('=' * 31)
print ('''\033[1;33mChoose one of the options for conversion
[1] Binary
[2] Octal
[3] Hexadecimal\033[m''')
option = int(input('\033[1mYour option:\033[m '))
if option == 1:
    print ('\033[1;36mYour number chosen is {} and converting it to BINARY is {}'.format(numInt, bin(numInt)[2:]))
elif option == 2:
    print('Your number chosen is {} and converting it to OCTAL is {}'.format(numInt, oct(numInt)[2:]))
elif option == 3:
    print ('Your number chosen is {} and converting it to HEXADECIMAL is {}\033[m'.format(numInt, hex(numInt)[2:]))
else:
    print ('\033[1;31mOption Invalid, TRY AGAIN\033[m')
    
