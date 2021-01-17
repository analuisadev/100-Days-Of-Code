boletim = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    escolha = str(input('Quer continuar? S/N')).upper().strip()[0]
    if escolha in 'N':
        print ('Programa encerrado')
        break
print ('-=' * 30)
print (f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print ('-=' * 30)
for i, a in enumerate(boletim):
    print (f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print ('-=' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 fecha o programa)'))
    if opc == 999:
        print ('Finalizando')
        break
    if opc <= len(boletim) -1:
        print (f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')
print ('<<< VOLTE SEMPRE >>>')
