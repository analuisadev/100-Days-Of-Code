#Importação de todos os arquivos referentes a pasta Day_82
from Day_82.funcoes import fahr_cel, cel_fahr
#looping infinito para o sistema principal
while True:
    option = int(input(""" 1 - Celsius - Fahrenheit
2 - Fahrenheit  - Celsius
3 - Sair do Programa
Sua Opção: """))
    if option == 1:
        cel_fahr()
