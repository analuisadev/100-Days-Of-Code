nameandmean = dict()
nameandmean['Name'](str(input('Nome do aluno: ')))
nameandmean['Mean'](float(input(f'{nameandmean["Name"]} show your average ')))
if nameandmean['Média'] >= 7:
    student['Situation'] = 'Approved'
elif nameandmean['Média'] < 7:
    student['Situation'] = 'In recovery'
else:
    student['Situation'] = 'Disapproved'
print ('-=' * 30)
for keys, values in nameandmean.items():
    print (f'{keys} is the same as {values}')
print ('-=' * 30)
