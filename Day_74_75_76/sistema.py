#Importação de todos os arquivos referentes as pastas criadas dentro do exercício
from Day_74_75_76.lib.interface import *
from Day_74_75_76.lib.arquivo import *
#Importação do sleep para dar um descanso
from time import sleep

arq = 'exerciciodocursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

#Looping infinito para o sistema principal
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção para listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção para cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = leiaInt(('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #Opção para sair do sistema
        cabeçalho('Encerrando o sistema, Volte sempre!')
        break
    else:
        #Digitou uma opção indisponível no menu
        print ('\033[1;31mERRO: Você digitou uma opção indisponível no menu!\033[m')
        sleep(2)