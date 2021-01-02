listnum = []
bigger = 0
smaller = 0
for c in range(0, 5):
    listnum.append(int(input(f'Enter a value for the position {c}: ')))
    if c == 0:
        bigger = smaller = listnum[c]
    else: 
        if listnum[c] > bigger:
            bigger = listnum[c]
        if listnum[c] < smaller: 
            menor = listnum[c]
print(f'You entered the values {listnum}')
print (f'The highest value entered was {bigger} in the position', end=' ')
for index, value in enumerate(listnum):
    if value == bigger: 
        print (f'{index}... ', end='')
print()
print (f'The lowest value entered was {smaller} in the position', end=' ')
for index, value in enumerate(listnum):
    if value == smaller: 
        print (f'{index}... ', end='')
print()
