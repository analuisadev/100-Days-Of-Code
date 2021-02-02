#Função para validar o uso de números inteiros
def ReadInt(msg):
    validation = False
    value = 0
    while True:
        number = str(input(msg))
        if number.isnumeric():
            value = int(number)
            validation = True
        else: 
            print ('\033[1;31mERRO! Você não digitou um número válido!\033[m')
        if validation:
            break
    return value
#Programa Principal
number = ReadInt('\033[1mDigite um número:\033[m ')
print (f'\033[1;33mO número digitado foi\033[m \033[1;32m{number}\033[m')
