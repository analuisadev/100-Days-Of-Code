def cel_fahr():
    while True:
        try:
            C = float(input('Informe a temperatura em graus Celsius: '))
            F = C * (9 / 5) + 32
        except (KeyboardInterrupt):
            print('\033[1;31mERRO: Sem informar a o valor da temperatura é impossível realizar a conversão!\033[m')
            continue
        else:
            print('\033[1;33mConversão realizada com sucesso!\033[m')
            print('A conversão da temperatura em Celsius informada é:\n{0}°F'.format(F))


def fahr_cel():
    while True:
        try:
            F = float(input('Informe a temperatura em graus Fahrenheit: '))
            C = (F - 32) * (5 / 9)
        except (KeyboardInterrupt):
            print('\033[1;31mERRO: Sem informar a o valor da temperatura é impossível realizar a conversão!\033[m')
            continue
        else:
            print('\033[1;33mConversão realizada com sucesso!\033[m')
            print('A conversão da temperatura em Celsius informada é:\n{0}°F'.format(C))