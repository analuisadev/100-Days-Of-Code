option = 'Yy'
print ('\033[1;32m{:=^40}\033[m'.format(' ANNUAL STUDENT RESULT '))
while option == 'Yy': 
    nome = str(input('\033[1mType your name: '))
    n1 = float(input('\033[1;33m{}\033[m \033[1;32mType a first note:\033[m '.format(nome.lower().capitalize())))
    n2 = float(input('\033[1;33m{}\033[m \033[1;32mEnter your second note:\033[m '.format(nome.lower().capitalize())))
    n3 = float(input('\033[1;33m{}\033[m \033[1;32mEnter your second note:\033[m '.format(nome.lower().capitalize())))
    n4 = float(input('\033[1;33m{}\033[m \033[1;32mEnter your second note:\033[m '.format(nome.lower().capitalize())))
    média = (n1+n2+n3+n4)/4
    print ('\033[1m{} Your average is\033[m \033[1;36m{:.1f}\033[m'.format(nome.lower().capitalize(), média))
    option = str(input('\033[1mDo you wish to continue? [Yes/No]\033[m ')).upper().strip()[0]
    print ('\033[1;32m{:=^40}\033[m'.format(' RESULT '))
if média <= 4:
    print ('\033[1mVocê está\033[m \033[1;31mDISAPPROVED\033[m')
elif média == 5:
    print ('\033[1mVocê está em\033[m \033[1;33mRECOVERY\033[m')
else: 
    print ('\033[1mVocê foi\033[m \033[1;36mAAPPROVED\033[m')
print ('\033[1;35mOperation completed\033[m')
