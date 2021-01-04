note = []
for contador in range(1, 5): 
    note.append(float(input(f'Digite sua {contador}° nota: ')))
average = sum(note)/4
print ('{:=^40}'.format(' RESULT '))
print (f'The number of notes read was {contador}')
print (f'The notes reported were: {note}')
print (f'Your average is {average:.1f}')
note.sort(reverse=True)
print(f'Reverse order is {note}')
sums = sum(note)
print (f'Total sum is{sums}')
