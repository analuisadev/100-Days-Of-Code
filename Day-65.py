def token(player='<desconhecido>', ngoals=0): 
       print (f'O jogador {player} fez {ngoals} gol(s) em um campeonato')
       
       
#Programa Principal       
name = str(input('Nome do Jogador: '))
goals = str(input('Quantidades de Gols feitos: '))
if goals.isnumeric(): 
       goals= int(goals)
else: 
       goals = 0
if name.strip() == '':
       token(ngoals=goals)
else: 
       token(name, goals)
