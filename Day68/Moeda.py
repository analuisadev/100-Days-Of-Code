#Função para aumentar o valor informado
def aumentar (valor, taxa): 
    total = valor + (valor * taxa/100)
    return total
#Função para diminuir o valor informado
def diminuir (valor, taxa): 
    total = valor - (valor * taxa/100)
    return total
#Função para dobrar o valor informado
def dobro(valor):
    total = valor  * 2
    return total 
#Função para importar a métade o valor informado
def metade (valor):
    total = valor / 2
    return total 

