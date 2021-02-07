#Função para aumentar o valor informado
def aumentar (valor = 0, taxa = 0, formato=False): 
    total = valor + (valor * taxa/100)
    return total if formato in False else moeda(total)
#Função para diminuir o valor informado
def diminuir (valor = 0, taxa = 0, formato=False): 
    total = valor - (valor * taxa/100)
    return total if formato in False else moeda(total)
#Função para dobrar o valor informado
def dobro(valor = 0, formato=False):
    total = valor  * 2
    return total if formato in False else moeda(total)
#Função para importar a métade o valor informado
def metade (valor = 0, formato=False):
    total = valor / 2
    return total  if formato in False else moeda(total)
def moeda (valor = 0, moeda='R$'):
    return  f'{moeda}{valor:>2.2f}'.replace('.', ',')
def resumo (valor=0, taxa=10, taxaa=5):
    print ('-=' * 30)
    print('RESUMO DO VALOR'.center(30))
    print ('-=' * 30)
    print(f'Preço analizado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Métade do preço: \t{metade(valor, True)}')
    print(f"Com {taxa}% de aumento: {aumentar(valor, taxa, True)}")
    print(f"{taxaa}% de redução: {diminuir(valor, taxaa, True)}")
    print ('-=' * 30)
    