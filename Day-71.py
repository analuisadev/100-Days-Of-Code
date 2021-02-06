#importanto o sleep para dar tempo de 1 segundo de uma seção para outra para melhorar a leitura
from time import sleep
#Criando lista para armazenar os agendamentos
Agenda_Contatos = []
#Criando lista para enviar as opções disponíveis
opcoes = ['1 - Criar um novo contato',
          '2-  Lista de contatos',
          '3 - Excluir contato']
#Looping infinito
while True: 
    print ('{:=^40}'.format(' AGENDA DE CONTATOS '))
    print ('Seleione uma das opções abaixo: ')
    sleep(1)
    option = int(input(f'{opcoes} '))
    #Se o usuário escolher criar um novo contato
    if option == 1:
        nome = str(input('Nome do contato: '))
        telefone = str(input('Telefone do contato: '))
        endereco = str(input('Endereço do contato: '))
        #Criação de variável para inserir os elementos dentro da lista de agendamento
        cont_Agenda = {'nome':nome, 'telefone': telefone, 'endereco': endereco}
        Agenda_Contatos.append(cont_Agenda)
    #Opção de impressão dos contatos
    elif option == 2:
        #impressão dos elementos dentro da lista
        print ('{:=^40}'.format(' IMPRESSÃO DOS CONTATOS '))
        print (Agenda_Contatos)
    #Opção de exclusão de contatos
    elif option == 3:
        #Criação da variavel para percorrer a lista
        indice = 0
        #Looping para percorrer a lista
        for item in Agenda_Contatos:
            print (f'{indice} - {item}')
            indice = indice + 1
        #Seção de escolha do elemento a ser excluido
        selector = input('Item a ser excluído: ')
        #Conferindo se o valor é númerico
        if selector.isnumeric():
            #'converted' recebe o valor da variavel e 'selector' se refere ao item que vai ser excluido
            converted = int(selector)
        if converted in range(0, indice):
            #ultimo item de range é removido
            selector = Agenda_Contatos.pop(converted)
            print ('O elemento {selector} foi excluído com sucesso')
        #Se o elemento digitado não for encontrado
        else: 
            print ('Opção invalida')
            break
        
    elif (option < 1 and option > 4): 
        print ('A opção digitada não existe! ')
        break