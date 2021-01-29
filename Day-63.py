from time import sleep
#comando para cores
cor = ('\033[m' #sem cor
       '\033[0;30;41m' #vermelho
       '\033[0;30;42m' #verde
       '\033[0;30;43m' #amarelo
       '\033[0;30;44m' #azul
       '\033[0;30;45m' #roxo
       '\033[7;30m'    #branco
       );
#Função help
def ajuda(com):
       titulo(f'Acessando o manual do comando \'{com}\'',4)
       print (cor[6], end='')
       help(com)
       print(cor[0], end='')
       sleep(2)
       

#Função Titulo       
def titulo(mensagem, cores=0):
       tamanho = len(mensagem) + 4
       print(cor[cores], end='')
       print ('=' * tamanho)
       print (f'   {mensagem}')
       print ('=' * tamanho)
       print (cor[0], end='')
       sleep(1)
       
       
#Programa Principal
comando = ''
while True: 
       titulo('SISTEMA DE AJUDA PyHELP', 2)
       comando = str(input("Função ou Biblioteca >>> "))
       if comando.upper() == 'FIM':
              break
       else:
              ajuda(comando)
titulo('ATÉ A PRÓXIMA!', 1)
