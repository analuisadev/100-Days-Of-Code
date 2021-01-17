info = dict()
finalização = list()
for cont in range (1, 4):
    info['Nome'] = str(input(f'Digite o {cont}° nome: '))
    info['Idade: '] = int(input('Digite a idade: '))
    finalização.append(info.copy())
print ('As informações informadas foram:')
for i in finalização:
    for v in i.values():
        print(v, end=' ')
        print ()
