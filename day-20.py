from random import randint
computer  = randint(0, 10)
print ('-=' * 19)
print ('\033[1;32m{:^40}\033[m'.format(' GUESSING GAME 2.0 '))
print ('-=' * 19)
print ('\033[1mThe number I thought of is between 0 and 10...')
print ('Can you guess which one it was?\033[m')
hit = False
hunch = 0
while not hit: 
    player = int(input('What your guess? '))
    hunch += 1
    if player == computer:
        hit = True
    else:
        if player < computer:
            print ('\033[1;36mA little more ... Try one more time\033[m')
        elif player > computer:    
            print('\033[1;35mA little less ... Try one more time\033[m')
print ('-=' * 19)
print ('\033[1;33m{:^40}\033[m'.format(' Your HIT!'))
print ('\033[1;33m{:^40}\033[m'.format('The number of attempts was {}'.format(hunch)))
print ('-=' * 19)
