from random import randint
from time import sleep


def draw(lista):
    print ('Sorteando 5 valores: ', end='')
    for cont in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print (f'{num} ', end='', flush=True)
        sleep(0.4)
        print ('FIM!')


def somaPair(lista):
    sum = 0
    for value in lista:
        if value % 2 == 0:
            sum += value
    print (f'Somando todos os valores pares de {lista}, o seu resultado é {sum}')
     
     
numbers = list()   
draw(numbers)
somaPair(numbers)
