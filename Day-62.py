#importação
from Viagem import Viagem
#inicio do programa
print ('{:=^40}'.format(' CADASTRO DE VIAGEM '))
nome = input('Digite o seu nome: ')
print ('{:=^40}'.format(' OPÇÕES DE DESTINO '))
opcao = int(input('''1) Bahia
2) São Paulo
3) Estados Unidos
4) Portugal 
5) Canadá
6) África do Sul
7) Rússia 
Selecione a colocação correspondente a sua viagem: '''))
if opcao > 7: 
    print ('Sua opção de viagem está invalida, por favor digite o número correspondente ao destino corretamente...')
else:
    print (f'Você escolheu o {opcao}° destino, tenha uma ótima viagem :)')
