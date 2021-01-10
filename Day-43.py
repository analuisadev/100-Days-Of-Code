listanumerica = list()
pares = list ()
impares = list()
while True: 
    listanumerica.append(int(input('Digite um valor inteiro: ')))
    resposta = str(input('Deseja continuar a informar outros valores? S/N ')).upper().strip()[0]
    if resposta in 'N': 
        break
    for i, v in enumerate(listanumerica):
        if v % 2 == 0:
            pares.append(v)
        elif v % 2 == 1:
            impares.append(v) 
print ('-=' * 18)
print (f'Os valores informados foram {listanumerica}')
print (f'Os valores pares informados foram {pares}')
print (f'E os valores ímpares informados foram {impares}')
