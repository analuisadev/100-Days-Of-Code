num = []
for position in range(1, 11):
    num.append(int(input(f'Enter a {position}° number: ')))
print (f'The numbers entered were {num}')
num.sort(reverse=True)
print (f'The inverted order is {num}')
