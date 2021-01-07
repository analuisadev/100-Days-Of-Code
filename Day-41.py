num5 = []
for c in range(0, 5): 
    n = int(input(f'Digite o {c}° número: '))
    if c == 0 or n > num5[-1]:
        num5.append(n)
        print ('Adicionado ao final da lista')
    else: 
        position = 0
        while position < len(num5):
            if n <= num5[position]:
                num5.insert(position, n)
                print ('Adicionado a posição {position} da lista ')
                break 
            position += 1
print (f'A ordem dos valores digitados foram {num5}')
