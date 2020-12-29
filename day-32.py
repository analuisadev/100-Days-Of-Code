counter = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
number = int(input('Escola um número de 0 a 20: '))
while number not in range(0, 21): 
    number = int(input('Você digitou o número errado.Escola um número de 0 a 20: '))
print (f'Você escolheu o número {counter[number]}')
