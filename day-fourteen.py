import sys
from time import sleep
player = 10
sleep(1)
#Welcome
print ('=' *38)
print ('\033[1;33mWelcome to game I ALREADY and I NEVER!\033[m')
print ('=' *38)
sleep(2)
#Rules
print ('''\033[1;33mRules:
       1 ° For every question you ask you lose 1 POINT
       2 ° For every question you have never asked you will not receive any points
       3 ° (OBS) The questions will not be of low slang or low level''')
print ('Are you ready? HAHA :D\033[1m')
#Iniciation
q1 = int(input('\033[1;36mI was never expelled from the room: 1 - Already / 2 - Never\033[m '))
if q1 == 1:
    player = player - 1
elif q1 == 2:
    pass
else: 
    print ('\033[1;31mInvalid answer, Choose between 1 (already) and 2 (NEVER)\033[m ')
    sys.exit()
q2 = int(input('\033[1;36mI never broke a bone in my body: 1 - Already 2 - Never\033[m '))
if q2 == 1:
    player = player - 1
elif q2 == 2:
    pass
else: 
    print ('\033[1;31mInvalid answer, Choose between 1 (already) and 2 (NEVER)\033[m ')
    sys.exit()
q3 = int(input('\033[1;36mI never tried to cut my own hair: 1 - Already 2 - Never\033[m '))
if q3 == 1:
    player = player -1
elif q3 == 2:
    pass
else:
    print ('\033[1;31mInvalid answer, Choose between 1 (already) and 2 (NEVER)\033[m ')
    sys.exit()
q4 = int(input('\033[1;36mI"ve never been to an amusement park: 1- Already 2 - Never\033[m '))
if q4 == 1:
    player = player - 1 
elif q4 == 2:
    pass
else:
    print ('\033[1;31mInvalid answer, Choose between 1 (already) and 2 (NEVER)\033[m ')
    sys.exit()
q5 = int(input('\033[1;36mI was never fired: 1- Already 2 - Never\033[m '))
if q5 == 1:
    player = player - 1
elif q5 == 2:
    pass
else:
    print ('\033[1;31mInvalid answer, Choose between 1 (already) and 2 (NEVER)\033[m ')
    sys.exit()
q6 = int(input('\033[1;36mI"ve never been mugged: 1 - Already 2 - Never\033[m '))
if q6 == 1:
   player = player - 1
elif q6 == 2:
    pass
else:
    print ('\033[1;31mInvalid answer, Choose between 1 (already) and 2 (NEVER)\033[m ')
    sys.exit()
q7 = int(input('\033[1;36mI never laughed so much that I took a little pee: 1 - Now 2 - Never\033[m '))
if q7 == 1:
    player = player -1
elif q7 == 2:
    pass
else:
    print ('\033[1;31mInvalid answer, Choose between 1 (already) and 2 (NEVER)\033[m ')
    sys.exit()
q8 = int(input('\033[1;36mI never missed a bus: 1 - Already 2 - Never\033[m '))
if q8 == 1:
    player = player - 1
elif q8 == 2:
    pass
else:
    print ('\033[1;31mInvalid answer, Choose between 1 (already) and 2 (NEVER)\033[m ')
    sys.exit()
q9 = int(input('\033[1;36mI never immediately regretted having sent a message: 1 - Already 2 - Never\033[m '))
if q9 == 1:
    player = player - 1
elif q9 == 2:
    pass
else:
    print ('\033[1;31mInvalid answer, Choose between 1 (already) and 2 (NEVER)\033[m ')
    sys.exit()
q10 = int(input('\033[1;36mI was never stopped by police: 1 - Already 2 - Never\033[m '))
if q10 == 1:
    player = player - 1
elif q10 == 2:
   pass
else:
    print ('\033[1;31mInvalid answer, Choose between 1 (already) and 2 (NEVER)\033[m')
    sys.exit()
print ('\033[1;32mYour pontuation is {}\033[m'.format(player))

