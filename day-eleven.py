p = 0
print ('''\033[1;33mWelcome to the test of traffic laws
       RULES:

1 - You will have to accumulate a total of 7 points to pass the test

2 - If you take less than 7 in the test you will have to retake

3 - Do not steal

4 - Read and respond calmly\033[m''')
q1 = int(input('\033[1;36m1) What to do when the light turns red? 1- Stop / 2 - Walk\033[m '))
if  q1 == 2:
    (p+1)
else:
    p=0
q2 = int(input('''\033[1;36m2) The minimum category of the National Drivers License (CNH) for a motor vehicle driver used in cargo transportation, whose total gross weight exceeds three thousand five hundred kilograms, will be
1) "A" and "B".
2) "B" only.
3) "B" and "C".
4) "A" and "C".
5) "C" only.
Your answer:\033[m '''))
if q1 == 5:
    (p+1)
else: 
    p=0
q3 = int(input('''\033[1;36m3) How many negative points does the driver who drives with the CNH - National Driver's License expired twenty days ago receive in his medical record?
1) Nenhum.
2) 4.
3) 5.
4) 7.
Your answer:\033[m '''))
if q3 == 1:
    (p+2)
else:
    p=0
q4 = int(input('''\033[1;36m4) What is the meaning of the traffic sign represented by an inverted (upside down) red triangle?
1)Customs.
2)Works on the track.
3)Give preference.
4)Reduce the speed for inspection.
5)Lane narrowing.
Your answer:\033[m '''))
if q4 == 3:
    (p+1)
else:
    p=0
q5 = int(input('''\033[1;36m5) Pedestrians crossing the road over the bounded lanes (pedestrian crossings), when there are no traffic lights, have priority for crossing and crossing.
1) True
2) False
Your answer:\033[m '''))
if q5 == 2:
    (p+1)
else:
    p=0
q6 = int(input('''\033[1;36m6) Which of the violations below is considered very serious with a loss of 7 points in the portfolio?
1) Do not wear a seat belt.
2) Cross with red beacon.
3) Driving with headphones or cell phone.
4) Travel on the exclusive bus lane.
5) Stop using windshield wipers in the rain
Your answer:\033[m '''))
if q6 == 2:
    (p+2)
else: 
    p=0
q7 = int(input('''\033[1;36m7) Up to what age should children be transported in the rear seat of the vehicle?
1) 2 years
2) 5 years
3) 10 years
4) 15 years
5) There is no determination in this regard.
Your answer:\033[m '''))
if q7 == 3:
    (p+2)
else:
    p=0
q8 = int(input('''\033[1;36m8) What is the minimum speed limit on a road, respecting the operational traffic conditions:
1) It will always be 20 km / h.
2) It will be 20% with respect to the maximum speed.
3) It will be 50% with respect to the maximum speed.
4) There is no defined lower limit.
5) It will be 70% with respect to the maximum speed.
Your answer:\033[m '''))
if q8 == 3:
    (p+1)
else: 
    p=0
q9 = int(input('''\033[1;36m9) When a traffic agent makes a sound signal through your whistle to you, with two short hisses, he wants to inform you that:
1) You must stop.
2) You must slow down the vehicle.
3) It is releasing traffic in the direction / direction indicated by the agent.
4) You must accelerate as quickly as possible.
5) Does not mean anything.
Your answer:\033[m '''))
if q9 == 1:
    (p+1)
else:
    p=0
q10 = int(input('''\033[1;36m10) Currently, several cities have adopted bike lanes and bike lanes. In the signaling of ground, what should be the color of the strip that delimits the cycle path or the cycle lane?
1) Red
2) Blue
3) Yellow
4) Green
5) White
Your answer:\033[m '''))
if q10 == 1:
    (p+1)
else:
    p=0
total =  (q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10)/2
if total >=7:
    print ('\033[1;32mCongratulations, you passed the test. Your score was {} :D.\033[m'.format(total))
else: 
    print('''\033[1;31mToo bad, you didn't pass the test. your score was {}\033[m'''.format(total))