#Importações
from random import randint 
from time import sleep
from operator import itemgetter
#Dicionários para armazenar os valores
game = {'Player1': randint(1, 100),
        'Player2': randint(1, 100),
        'Player3': randint(1, 100),
        'Player4': randint(1, 100)}
ranking = dict()
#Seção que pega o nome e o valor que o jogador tirou
for name, value in game.items():
    print (f'{name} took the value {value}')
    sleep(1)
#Seção para mostrar os ranking´s dos jogadores
ranking= sorted(game.items(), key=itemgetter(1), reverse=True)
print ('{:=^40}'.format(' PLAYER RANKING '))
for indice, value in enumerate(ranking):
    print (f'{indice+1}° place: {value[0]} with {value[1]}')
    sleep(1)
print ('{:=^40}'.format(' END '))
