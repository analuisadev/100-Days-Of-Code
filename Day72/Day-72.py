#Importação do Sleep para um descanso de uma mensagem para a outra
from time import sleep
from Functions import ReadInt, ReadFloat   
#Programa Principal
numInt = ReadInt('Digite um número inteiro: ')
numFloat = ReadFloat('Digite um número real: ')
sleep(1)
print (f'\033[1;32mParabéns! Você digitou o número: {numInt} como inteiro e {numFloat} como real! :)\033[m')