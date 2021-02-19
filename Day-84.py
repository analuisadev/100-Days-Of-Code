from time import sleep
while True:
    print ('{:=^40}'.format(' CONVERSOR DE TEMPERATURAS '))
    option = int(input('''1 - Celsius - Fahrenheit
2 - Fahrenheit - Celsius
3 - Sair do Sistema
Sua escolha: '''))
    if option == 1: 
        C = float(input('Temperatura em Celsius: '))
        F = C * (9 / 5) + 32
        print ('{:=^40}'.format(' CONVERTENDO... '))
        sleep(1)
        print ('{0:>20}F°'.format(F))
        print ('=' * 40)
        sleep(1)
    elif option == 2: 
        F = float(input('Temperatura em Fahrenheit: '))
        C = (F - 32) * (5 / 9)
        print ('{:=^40}'.format(' CONVERTENDO... '))
        sleep(1)
        print ('{0:>20}°C'.format(C))
        print ('=' * 40)
        sleep(1)
    elif option == 3: 
        print ('Saindo do sistema....\nVolte sempre :)')
        break 
    else: 
        print ('\033[1;31mERRO: Sua escolha não corresponde as opções existentes no sistema!\033[m')
        continue
