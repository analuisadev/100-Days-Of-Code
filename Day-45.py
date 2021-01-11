people = []
data = []
bigger = smaller = 0
while True:
    people.append(str(input('Name: ')))
    people.append(float(input('Weight: ')))
    if len(data) == 0:
        bigger = smaller = people[1]
    else:
        if people[1] > bigger:
            bigger = people[1] 
        if people[1] < smaller:
            smaller = people[1]
    data.append(people[:])
    people.clear()
    answer = str(input('Do you want to continue? [Y/N] ')).upper().strip()[0]
    if answer in 'N':
        break
print ('-=' * 30)
print(f'You registered {len(data)} people')
print (f'The bigger weight reported was {bigger}Kg. The weight of ', end='')
for weight in data:
    if weight[1] == bigger:
        print(f'{weight[0]}', end='')
print ()
print (f'The lowest reported weight was {smaller}Kg. The weight is', end='')
for weight in data:
    if weight[1] == smaller:
        print(f'{weight[0]}', end='')
