mensage = ('A great', 'year', 'for all', 'programmers', 'and', 'developers,', 'happy 2021!')
for position in mensage: 
    print (f'\nIn this word there are {position.upper()} terms ', end='')
    for letters in position:
        if letters.lower() in 'aeiou':
            print (letters, end=' ')
