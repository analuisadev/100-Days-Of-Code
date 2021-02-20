from time import sleep #Importação do sleep para um descanso do aviso inicial e a seção de perguntas
print('{:=^40}'.format(' INVESTIGAÇÃO CRIMINAL ')) #Título informativo
while True: #Looping infinito para iniciar as perguntas
    try:
        print('AVISO: Você terá que responder um total de 5 perguntas, responda 1 - Para Sim e 0 - Para não.')
        sleep(1)
        question1 = int(input('Você telefonou para a vítima? '))
        question2 = int(input('Você esteve no local do crime? '))
        question3 = int(input('Você mora perto da vitima? '))
        question4 = int(input('Você devia para a vitima? '))
        question5 = int(input('Você trabalhava com a vitima? '))
        sum_questions = (question1 + question2 + question3 + question4 + question5)
    except (KeyboardInterrupt):
        print('\033[1;31mERRO: Você não deve ficar sem responder as questões! \nRetone ao inicio do programa novamente.')
        break
    else:
        if (sum_questions == 2):
            print('Indivíduo classificado(a) como suspeito(a)')
        elif (sum_questions < 2):
            print('Indivíduo classificado(a) como inocente')
        elif ( 3 <= sum_questions <= 4):
            print('Indivíduo classificado(a) como cúmplice')
        elif (sum_questions == 5):
            print('Indivíduo classificado(a) como assasino(a)')
    break