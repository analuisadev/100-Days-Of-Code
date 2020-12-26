from time import sleep 
print ('\033[1;36m{:=^40}\033[m'.format(' BANCO DO BRASIL '))
sleep (1)
while True: 
    print ('''\033[1mEscolha uma das opções disponíveis:
[1] Crie uma nova conta
[2] Deposito
[3] Cancelamento de conta
[4] Sair do programa\033[m''')
    opção = int(input('\033[1mQual é a opção escolhida?\033[m '))
    sleep (1)
    if opção == 1: 
        print ('\033[1;36m{:=^40}\033[m'.format(' CRIE UMA NOVA CONTA '))
        nome = str(input('\033[1mDigite o seu nome completo: '))
        datanasc = str(input('Digite a sua data de nascimento: '))
        cpf = str(input('Digite o seu CPF: '))
        end = str(input('Qual é o seu endereço?\033[m '))
        sleep (1)
        print ('\033[1;32m{:=^40}\033[m'.format(' Conta criada com Sucesso! '))
        sleep (1)
        print (f'''\033[1mNome do títular {nome}
Data de Nascimento {datanasc}
CPF {cpf}
Endereço {end}\033[m''')
        sleep (1)
    elif opção == 2: 
        print ('\033[1;36m{:=^40}\033[m'.format(' DEPOSITO '))
        sleep (1)
        valor = float(input('\033[1mQual é o valor do seu deposito? '))
        remet = str(input('Nome do destinátario:\033[m '))
        print ('\033[1;36m{:=^40}\033[m'.format(' Deposito concluido com Sucesso '))
        sleep (1)
        print (f'\033[1mO valor de {valor} foi enviado com sucesso para {remet}\033[m')
        sleep (1)
    elif opção == 3: 
        print ('\033[1;36m{:=^40}\033[m'.format('CANCELAMENTO DE CONTA '))
        sleep (1)
        resposta = str(input('\033[1mDeseja cancelar sua conta permanentemente? S/N\033[m ')).strip().upper()[0]
        if resposta == 'S':
            sleep (1)
            print ('\033[1;36m{:=^40}\033[m'.format(' CONTA CANCELADA COM SUCESSO '))
            break
        else: 
            sleep (1)
            print ('\033[1;33m{:=^40}\033[m'.format(' A CONTA PERMANECERÁ ATIVA '))
    elif opção == 4:
        sleep (1)
        sair = str(input('\033[1;36mDeseja encerrar o programa? S/N\033[m ')).upper().strip()[0]
        if sair == 'S':
            sleep (1)
            print ('\033[1;33mPrograma encerrado!\033[m')
            break
        else: 
            continue
