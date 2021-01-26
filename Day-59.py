from time import sleep
import sys
print ('-=' * 20)
def contador(inicio, fim, pulo):
    if pulo < 0:
        pulo *= -1
    if pulo == 0:
        print ('O pulo não pode ser igual a ZERO!')
        sys.exit()
    print (f'A contagem será feita de {inicio}, {fim} de {pulo} em {pulo}.')
    sleep(0.4)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print (f'{cont}', end='',flush=True)
            sleep (0.4)
            cont += pulo
        print ('SEÇÃO FINALIZADA!')
    else: 
        cont = inicio
        while cont >= fim:
            print (f'{cont}', end='', flush=True)
            sleep(0.4)
        print ('SEÇÃO FINALIZADA!')
print ('-=' * 20)
contador (1, 10, 1)
contador (10, 0, 2)
print ('{:=^40}'.format(' CONTAGEM PERSONALIZADA '))
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
pulo = int(input('Pulo: '))
contador (inicio, fim, pulo)
