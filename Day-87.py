from time import sleep
print('{:=^40}'.format(' NÚMEROS PRIMOS POSITIVOS '))
sleep(1)
while True:
    number = int(input('Por favor, informe um número inteiro positivo: '))
    if number > 0:
        if number%2 == 1:
            print('\033[1;32mPARABÉNS! O número informado é um número primo positivo\033[m')
    elif number < 0:
        print ('\033[1;31mERRO: Informe um número positivo!\033[m')
        continue
    else:
        print('\033[1;31mInfelizmente o número informado não é um número primo :(\033[m')