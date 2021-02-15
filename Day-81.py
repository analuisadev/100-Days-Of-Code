line = [1, 2 ,3 , 4, 5, 6, 7, 8, 9, 10]
matriz = []
for cont in range(10):
    matriz.append(line)
print (len(line))
number = int(input('Digite um número para ser buscado na matriz: \n '))
cont_line = 0
cont_column = 0

for cont in matriz:
    for column in cont: 
        if(column == number):
            print (f'O número digitado {column} foi encontrado na linha {cont_line} e na coluna {cont_column}')
            isencontrado = True
            cont_column += 1
            
            cont_line += 1
            cont_column = 0
