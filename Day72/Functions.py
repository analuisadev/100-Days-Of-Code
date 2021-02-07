#Função para ler um número inteiro usando tratamento de erros caso não seja digitado corretamente
def ReadInt(msg):
    while True: 
        try:
            number = int(input(msg))
        except (ValueError, TypeError):
            print ('\033[1;31mERRO: Digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print ('\n\033[1;31mO usuário preferiu não informar um número\033[m')
            return 0
        else: 
            return number
        
#Função para ler um número real usando tratamento de erros caso não seja digitado corretamente        
def ReadFloat(msg): 
    while True:
        try: 
            number = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: Digite um número real válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print ('\n\033[1;31mO usuário preferiu não informar não informar um número.\033[m')
            return 0
        else: 
            return number 