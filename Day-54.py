#importação
from datetime import datetime
dados = dict()
#definindo os elementos do dicionário
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc 
dados ['Carteira de Trabalho'] = int(input('Carteira de trabalho: (Digite 0 se não tiver) '))
#Seção para obter mais informações caso o usuário tenha carteira de trabalho
if dados['Carteira de Trabalho'] != 0:
    dados ['Contratação'] = int(input('Ano de contratação: '))
    dados ['Salario'] = float(input('Salário: R$'))
    dados ['Aposentadoria'] = dados['Idade'] = ((dados['Contratação'] + 35) - datetime.now().year)
print ()
print (dados)
#Aqui irá informar os valores
for key , value in dados.items():
    print (f'Os dados informados de {key} é {value}')
