from time import sleep
values = []
while True: 
    values.append(int(input('\033[1mEnter a value: ')))
    answers = str(input('Do you want to continue? Y/N\033[m  ')).upper().strip()[0]
    if answers == 'N': 
        print ('\033[1mProgram closed...\033[m ')
        sleep(1)
        break
    else:
        continue
print (f'\033[1mYou entered {len (values)} values')
values.sort(reverse=True)
print (f'The descending order of the values ​​entered are: {values}\033[m ')
if 5 in values: 
    print('\033[1mThe value 5 is part of the list\033[m ')
else: 
    print ('\033[1mThe value 5 is not part of the list!\033[m ')
