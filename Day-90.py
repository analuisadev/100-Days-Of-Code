print('{:=^40}'.format(' SAIBA O SEU PESO IDEAL '))
while True:
    altura = float(input('Informe a sua altura (h): '))
    sexo = input('Informe o seu sexo: F/M  ').strip().upper()[0]
    if sexo == 'F':
        pesoFeminino = (72.7 * altura) - 58
        print('O seu peso ideal é %.2f Kg' %pesoFeminino)
    elif sexo == 'M':
        pesoMasculino = (62.1 * altura) - 44.7
        print('O seu peso ideal é %.2f Kg'%pesoMasculino)
    elif sexo != 'F' and sexo != 'M':
        print ('Sexo informado incorretamente! Escolha entre F(Feminino) e M(Masculino)')
        continue
