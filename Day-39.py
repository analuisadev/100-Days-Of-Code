numbers = list()
while True: 
    number = int(input('\033[1mEnter a number:\033[m '))
    if number not in numbers:
        numbers.append(number) 
        print ('\033[1;32mAdded value successfully!\033[m')
    else:
        print ('\033[1;31mDuplicate value! Re-enter another value\033[m')
    answer = str(input('\033[1mDo you want to continue? Yes / No\033[m ')).upper().strip()[0]
    if answer in 'N':
        break
numbers.sort()
print (f'\033[1;33mThe increasing order of the numbers entered was:\033[m \033[1;36m{numbers}\033[m')
