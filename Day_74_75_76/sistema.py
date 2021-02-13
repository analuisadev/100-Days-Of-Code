from Day_74_75_76.lib.interface import *
from Day_74_75_76.lib.arquivo import *
from time import sleep

arquivo = 'ExercicioCursoEmVideo.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)
else:
    print ('O Arquivo não foi encontrado')
    criarArquivo
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resp == 1:
        #opção para listar o conteúdo de um arquivo
        lerArquivo(arquivo)
    elif resp == 2:
        cabeçalho('Opção 2')
    elif resp == 3:
        cabeçalho('Saindo do sistema... \nVolte sempre! :)')
        break
    else:
        print('\033[1;31mATENÇÃO: Digite uma opção válida!\033[m')
        sleep(2)
