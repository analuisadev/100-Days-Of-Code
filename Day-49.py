from random import randint
from time import sleep
lista = list()
jogos = list()
print ('{:=^40}'.format(' MEGA SENA '))
quantnum = int(input('Quantos números serão sorteados? '))
total = 1
while total <= quantnum:
    contador = 0
    while True:
        num = randint (1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print ('-=' * 3, f'SORTEANDO {quantnum} JOGOS','-=' * 3)
for indice, lista in enumerate(jogos):
    print (f'Jogo {indice+1}: {lista}')
    sleep(1)
print ('Boa sorte')
