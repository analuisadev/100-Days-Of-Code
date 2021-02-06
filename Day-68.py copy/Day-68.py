from Moeda import aumentar, diminuir, metade, dobro, resumo
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
Moeda.resumo(num, 10, 12 )