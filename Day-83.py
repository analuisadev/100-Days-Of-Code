#Função que receberá a soma de A e B e irá mostrar se for verdadeiro ou falso
def sum_greater_than_limit(a = 0, b = 0, limit = 0):
    number = int(input('Digite um valor'))
    if a + b > limit:
        return True
    else:
        return False
    
