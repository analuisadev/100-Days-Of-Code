def area(width, length):
    total = width * length
    print (f'A área do seu terreno de {width}x{length} é de {total}m²')
    

width = float(input('Digite a largura do terreno em metros: '))
leng = float(input('Digite o comprimento do terreno em metros: '))
area(width, leng)
