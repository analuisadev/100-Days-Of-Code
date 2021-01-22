#importação do sleep
from time import sleep
#criação da agenda junto com seus elementos
agenda = dict()
agenda['Nome'] = str(input('Nome do contato: '))
agenda['Telefone: '] = str(input('Telefone do contato: '))
agenda['Endereço'] = str(input('Endereço do contato: '))
sleep(1)
#Resultado dos elementos
print ('{:=^40}'.format(' SUA AGENDA '))
for key, value in agenda.items():
    print (f'{key}: {value}')
excluir = str(input('Deseja excluir algum item da lista? S/N ' )).upper().strip()[0]
#A escolha do usuário
while excluir == 'N':
    print ('A sua agenda continuará salva a partir da última alteração')
    break
sleep(1)
if excluir == 'S':
    esc = int(input('''Escolha uma seção para ser excluida
0) Nome
1) Telefone
2) Endereço 
Sua escolha: '''))
#Excluindo itens do dicionário (com erro)
    sleep(1)
    if esc == 0:
        print ('O nome do seu contato está sendo excluido...')
        agenda.pop(0)
    elif esc == 1:
        print ('O Telefone do seu contato está sendo excluido...')
    agenda.pop(1)
elif esc == 2: 
    print ('O Endereço do seu contato está sendo excluido...')
    agenda.pop(2)
else: 
    print ('Opção invalida...')
