from time import sleep
import sys
nome = str(input('\033[1mDigite o seu nome: [Até 3 caracteres] '))
idade = int(input('Digite a sua idade: [De 0 até 150] '))
salario = float(input('Digite o valor do seu salario: R$'))
sexo = str(input('Informe o seu sexo: F/M ')).upper().strip()[0]
print ('''Informe o seu estado civil:
Solteiro(a): S
Casado(a): C
Viuvo(a): V
Divorciado(a): D
União estavél: U\033[m''')
sleep(1)
estciv = str(input('\033[1mInforme o seu Estado Civil:\033[m ')).upper().strip()[0]
if len(nome) > 3: 
    print ('\033[1mO nome digitado é maior do que 3 caracteres')
    print ('Renicie o programa e tente novamente\033[m')
    sys.exit()
if (idade < 0) or (idade > 150): 
    print ('\033[1mA idade foi digitada fora dos caracteres permitidos\033[m')
print ('\033[1mO nome foi digitado dentro dos caracteres permitidos\033[m')
print ('\033[1mA idade foi digitada dentro dos caracteres permitidos\033[m')
if (salario < 0):
    print ('\033[1mO salário foi digitado fora dos caracteres permitidos\033[m')
print (f'\033[1mO seu salário é R${salario} e foi informado corretamente.\033[m')
if (sexo != 'F') and (sexo != 'M'): 
    print ('\033[1mO sexo foi digitado fora dos caracteres permitidos\033[m')
print (f'\033[1mO seu sexo é {sexo} e foi digitado corretamente.\033[m')
while (estciv != 'S') and (estciv != 'C') and (estciv != 'V') and (estciv != 'D') and (estciv != 'U'):
    print ('\033[1mO Estado Civil informado não corresponde ao indicado, informe novamente: ')
    estciv = str(input('\033[1mInforme o seu Estado Civil: S/C/V/D/U \033[m ')).upper().strip()[0]
    if (estciv == 'S') and (estciv == 'C') and (estciv == 'V') and (estciv == 'D') and (estciv == 'U'): 
        print ('\033[1mO seu Estado Civil foi digitado dentro dos caracteres permitidos\033[m')
print ('\033[1;32mFim do programa\033[m')
