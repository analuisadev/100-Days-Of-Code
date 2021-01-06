from time import sleep 
numlist = []
for n in range(1, 5):
    numlist.append(int(input('\033[1mEnter a number:\033[m ')))
numlist.sort()
print (f'\033[1mThe order of the numbers entered were: {numlist}')
sleep(1)
numlist.sort(reverse=True)
print (f'The order of the numbers entered is: {numlist}')
sleep(1)
numlist.pop( )
print (f'A number has been removed from your list, can you find it?\033[m {numlist}')
