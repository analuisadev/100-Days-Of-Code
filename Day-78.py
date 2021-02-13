from time import sleep
#Criando os dicts que vão armazenar os itens e as compras
Agenda_Itens = []
Agenda_Compras = []
option = ['1 - Incluir Itens',
          '2 - Lista de Itens',
          '3 - Realizar Compras',
          '4 - Listar compras']
#looping para solicitar uma escolha do usuário
while True: 
    print (option)
    opt = int(input('Escolha uma das opções: '))
    if opt == 1: 
        print ('{:=^40}'.format(' SEÇÃO PARA INCLUSÃO DE ITENS '))
        #variaveis para armazenar o que foi pedido na questão
        nameItem = input('Nome do Item: ')
        colorItem = input('Cor do item: ')
        valueItem = float(input('Preço do Item: R$'))
        ItensDict = {'Item': nameItem, 'Cor':colorItem, 'Valor':valueItem}
        Agenda_Itens.append(ItensDict)
        sleep(1)
        print ('Item Adicionado com sucesso!')
    if opt == 2:
        print ('{:=^40}'.format(' LISTA DE ITENS ADICIONADOS '))
        sleep(1)
        print (Agenda_Itens)
    if opt == 3:
        print ('{:=^40}'.format(' REALIZAÇÃO DE COMPRAS '))
        i = 0
        for item in Agenda_Itens:
            print (f'{i} - item')
            i = i + 1
        #seção do item a ser comprado 
        Select_Item = input('Escolha o item que deseja comprar: ')
        if Select_Item.isnumeric():
            converted = item(Select_Item)
            converted = int(Select_Item)
        if converted in range(0, i):
            #inserção das váriaveis na lista de compras
            shopping = {'Compra': Agenda_Itens[converted]}
            Agenda_Compras.append(shopping)
            sleep(1)
            print ('Sua compra foi realizada com sucesso!')
            #se o selected n for um valor numérico
        else: 
            print ('Opção invalida')
    if opt == 4:
        print ('{:=^40}'.format(' LISTA DE COMPRAS REALIZADAS '))
        print (Agenda_Compras)
    elif (opt < 1 and opt > 4): 
        print ('Opção invalida')
        