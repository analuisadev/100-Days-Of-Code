def ReadInt(msg):
    while True:
        try:
            number = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: Digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;31O usuário preferiu não informar esse número.\033[m')
            return 0
        else:
            return number


#formatação do texto
def linha(tam=42):
    return '=' * tam

#Cabeçalho
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'{c} - {item}')
        cont += 1
        print(linha())
        option = int(input('Sua opção: '))
        return option