oddoreven = [[], []]
value = 0
for num in range(1, 8):
    value = int(input(f'Enter a {num}° value: '))
    if value % 2 == 0:
        oddoreven[0].append(value)
    else: 
        oddoreven[1].append(value)
print ('-=' * 30)
print (f'The value entered were {oddoreven}')
oddoreven[0].sort()
oddoreven[1].sort()
print (f'The PAIRS values entered were {oddoreven[0]}')
print (f'The ODD values entered were{oddoreven[1]}')
