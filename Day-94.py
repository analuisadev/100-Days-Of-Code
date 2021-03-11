"""
Exercício Data por extenso:
    Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso
"""
#Lista para transformar o número do mês por extenso
months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

datenasc = input('Digite a data de nascimento (dd/mm/aaaa) ')

print (datenasc.split("/")[0],
       "de",
       months[(int(datenasc.split("/")[1])-1)],
       "de",
       datenasc.split("/")[2])