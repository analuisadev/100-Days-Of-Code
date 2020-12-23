#Iniciação da estrutura de repetição infinita
print ('\033[1;32m{:=^40}\033[m'.format(' TABUADA 3.0'))
while True: 
    num = int(input('\033[1mInsira um número:\033[m '))
#O programa vai exibir essa mgs caso o número digitado seja negativo (ex: -1, -2, ,-1234..)
    if num < 0:
        print ('\033[1;33mNão é permitido números negativos nesta Operação! Finalizando...\033[m')
        break
#Escolha de opções
    print ('''\033[1mEscolha uma opção:\033[m     
\033[1;36m[1] Soma
\033[1;36m[2] Subtração
\033[1;36m[3] Divisão
\033[1;36m[4] Multiplicação
\033[1;36m[5] Cancelar/Sair do programa\033[m''')
#Estrutura de condição feito para cada uma das opções escolhidas
    opção = int(input('\033[1mQual opção você escolhe? '))
    if opção == 1: 
        for c in range(1, 11):
            print (f'{num} + {c} = {num+c}')
    elif opção == 2:
        for c in range(1, 11):
            print (f'{num} - {c} = {num+c}')
    elif opção == 3: 
#Irei alterar essa parte pois a divisão não está formatada corretamente.
        for c in range(1, 11):
            print (f'{num} ÷ {c} = {num/c:.1f}')
    elif opção == 4:
        for c in range (1, 11):
            print (f'{num} x {c} = {num*c}')
#Se o usuário digitar 5 o programa encerra como dito
    else: 
        print ('\033[1;35mPrograma encerrado!\033[m')
        break 
