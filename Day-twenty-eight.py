print ('{:=^40}'.format(' BANCO DO BRASIL '))
while True: 
    print ('''Escolha uma das opções disponíveis:
[1] Crie uma nova conta
[2] Deposito
[3] Empréstimo
[4] Cancelamento de conta
[5] Sair do programa''')
    opção = int(input('Qual é a opção escolhida? '))
    if opção == 1: 
        nome = str(input('Digite o seu nome completo: '))
        datanasc = str(input('Digite a sua data de nascimento: '))
        cpf = str(input('Digite o seu CPF: '))
        end = str(input('Qual é o seu endereço? '))
        print ('{:=^40}'.format(' Conta criada com Sucesso! '))
        print (f'''Nome do títular {nome}
Data de Nascimento {datanasc}
CPF {cpf}
Endereço {end}''')
    elif opção == 2: 
        valor = float(input('Qual é o valor do seu deposito? '))
        remet = str(input('Nome do destinátario: '))
        print ('{:=^40}'.format(' Deposito concluido com Sucesso '))
        print (f'O valor de {valor} foi enviado com sucesso para {remet}')
    elif opção == 3: 
        valorempret = float(input('Qual é o valor do empréstimo? '))
        valormens = float(input('Qual é o valor da sua renda mensal? '))
        aprov = 
