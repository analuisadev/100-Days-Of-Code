print('{:=^40}'.format(' DOWNLOAD DE ARQUIVOS '))
files = float(input('Informe o tamanho do arquivo para download (em MB): '))
velocity = float(input('Informe a velocidade da sua internet (em MBPS): '))
time = files / velocity
minutes = time / 60.0
print('O tempo aproximado para a conclusão do seu arquivo é de: %.2f minutos'%minutes)