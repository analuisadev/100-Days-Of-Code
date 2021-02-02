def Notes(*notes, situation=False):
    """
    Função para analisar notas e situação de alunos
    """
    results = dict()
    results['Total'] = len(notes)
    results['Maior'] = max(notes)
    results['Menor'] = min(notes)
    results['Média'] = sum(notes)/len(notes)
    if situation:
        if results['Média'] >= 7:
            results['Situação'] = 'Ótima'
        elif results['Média'] >= 5:
            results['Situação'] = 'Regular'
        else:
            results['Situação'] = 'Péssima'
    return results

#programa principal
numbers = Notes(2.5, 2.7, 5.5, 7.0, 10, situation=True)
print (numbers)
