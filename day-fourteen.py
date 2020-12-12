from time import sleep
player = 10
sleep(1)
#Welcome
print ('=' *35)
print ('Welcome to game I ALREADY and I NEVER!')
print ('=' *35)
sleep(2)
#Rules
print ('''Rules:
       1 ° For every question you ask you lose 1 POINT
       2 ° For every question you have never asked you will not receive any points
       3 ° The goal is not to reach 0, if you do you LOSE
       4 ° (OBS) The questions will not be of low slang or low level''')
print ('Are you ready? HAHA :D')
#Iniciation
q1 = int(input('I was never expelled from the room: 1 - Already / 2 - Never '))
if q1 == 1:
    player - 1
elif q1 == 3:
    print ('Invalid answer, Choose between 1 (already) and 2 (NEVER)')
else: 
    player == 0 
q2 = int(input('I never broke a bone in my body: 1 - Already 2 - Never'))
if q2 == 1:
    player - 1
elif q2 == 3:
    print ('Invalid answer, Choose between 1 (already) and 2 (NEVER)')
else: 
    player == 0
q3 = int(input('I never tried to cut my own hair: 1 - Already 2 - Never'))
if q3 == 1:
    player -1
elif q3 == 3:
    print ('Invalid answer, Choose between 1 (already) and 2 (NEVER)')
else:
    player == 0
q4 = int(input('I"ve never been to an amusement park: 1- Already 2 - Never'))
if q4 == 1:
    player - 1 
elif q4 == 3:
    print ('Invalid answer, Choose between 1 (already) and 2 (NEVER)')
else:
    player == 0
q5 = int(input('I was never fired: 1- Already 2 - Never'))
if q5 == 1:
    player - 1
elif q5 == 3:
    print ('Invalid answer, Choose between 1 (already) and 2 (NEVER)')
else:
    player == 0
q6 = int(input('I"ve never been mugged: 1 - Already 2 - Never'))
if q6 == 1:
    player - 1
elif q6 == 3:
    print ('Invalid answer, Choose between 1 (already) and 2 (NEVER)')
else:
    player == 0
q7 = int(input('I never laughed so much that I took a little pee: 1 - Now 2 - Never'))
if q7 == 1:
    player -1
elif q7 == 3:
    print ('Invalid answer, Choose between 1 (already) and 2 (NEVER)')
else:
    player == 0
q8 = int(input('I never missed a bus: 1 - Already 2 - Never'))
if q6 == 1:
    player - 1
elif q8 == 3:
    print ('Invalid answer, Choose between 1 (already) and 2 (NEVER)')
else:
    player == 0
q9 = int(input('I never immediately regretted having sent a message: 1 - Already 2 - Never'))
if q9 == 1:
    player - 1
elif q9 == 3:
    print ('Invalid answer, Choose between 1 (already) and 2 (NEVER)')
else:
    player == 0
q10 = int(input('I was never stopped by police: 1 - Already 2 - Never'))
if q10 == 1:
    player - 1
elif q10 == 3:
    print ('Invalid answer, Choose between 1 (already) and 2 (NEVER)')
else:
    player == 0
#This variable is in error, I'll fix it.
total = (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10) - 10
print ('{}'.format(total))
