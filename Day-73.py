#Importação para dar um tempo de 1 segundo para melhorar a impressão de resultados na tela do usuário
from time import sleep
#Dicionário que irá armazenar os agendamentos
Agendamento_Carros = []
#Lista com opções de serviço 
opcoes = ['1 - Agendar Revisão ',
          '2 - Listas de agendamentos', 
          '3 - Sair']
#Looping para apresentação das opções de escolha para o usuário
while True: 
    print (opcoes)
    sleep(1)
    option = int(input('Por favor, escolha uma opção: '))
#Seção de cada escolha
    if option == 1:
        print ('{:=^40}'.format(' AGENDAMENTO DE REVISÃO '))
        sleep(1)
        nomeCarro = input('Nome do carro: ')
        anoModel = int(input('Ano do carro: '))
        proprietario = input('Nome do(a) proprietário(a): ')
        dia = int(input('Dia do agendamento: '))
        hora = int(input('Horario para a revisão: '))
        sleep(1)
        #Inserção das variaveis para o dicionário feito para agendamento
        ListAgend = {'Proprietário': proprietario, 'Veículo': nomeCarro, 'Ano/Modelo': anoModel, 'Horario': hora, 'Data': dia}
        Agendamento_Carros.append(ListAgend)
        print ('Seu agendamento foi realizado com sucesso!')
        #Seção para imprimir a listas de agendamentos feitos
    elif option == 2:
        print ('{:=^40}'.format(' LISTAS DE AGENDAMENTOS '))
        sleep(1)
        print (Agendamento_Carros)
        #Saindo do programa
    elif option == 3:
        print ('Saindo do programa...\nVolte Sempre!')
        sleep(1)
        break
    #Se o usuário digitar valores maiores que 3
    else: 
        print ('Opção invalida!')
        sleep(1)
        continue