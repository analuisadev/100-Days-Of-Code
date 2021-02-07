from Moeda import diminuir, aumentar, dobro, metade
from time import sleep
"""
    Programa para exercitar Módulos em Python
    Objetivo do programa: 
    - Receber um valor inteiro informado pelo usuário
    - Mostrar esse valor com: 
        Aumento de 10%
        Dobro do valor 
        Métade do valor 
"""
#Programa Principal
num  = float(input('Digite um valor: R$ '))
print ('PROCESSANDO...')
sleep(1)
print (f"O valor R${num} com 10% de aumento é {aumentar(num, 10)}")
print (f'O dobro do valor R${num} é {dobro(num)}')
print (f'A Métade do valor R${num} é {metade(num)}')
print (f"Reduzindo 13% do valor, temos {diminuir(num, 13)}")