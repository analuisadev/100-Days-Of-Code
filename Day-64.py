from time import sleep #importação do sleep
def vote(yearofb=0): #criação da função vote para dar inicio ao programa
       from datetime import date #importação local
       currentyear = date.today().year #variavel que irá receber o ano atual
       age = currentyear - yearofb #variavel que calcula a idade do usuário
       if age < 16: #seção de condicionais para imprimir 3 resultados diferentes de acordo com a idade informada
              return f'\033[1mPessoas com {age} anos terão o voto\33[m \033[1;31mNEGADO\033[m'
       elif 16 <= age < 18 or age > 65: 
              return f'\033[1mPessoas com {age} anos tem o voto\033[m \033[1;33mOPICIONAL\033[m'
       else: 
              return f'\033[1mPessoas com {age} tem o voto\033[m \033[1;32mOBRIGATÓRIO\033[m'
       
#Aqui o usuário irá informar o ano de nascimento e o resultado será impresso na tela através do print       
birth = int(input('\033[1mAno de Nascimento:\033[m '))
sleep(1)
print (vote(birth))
