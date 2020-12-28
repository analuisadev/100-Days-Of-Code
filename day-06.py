from time import sleep
print ('-=-' * 7) 
#Program Start
name = str(input('\033[1;37mWhats your name?\033[m ')).strip()
age = int(input('\033[1;37mWhats your age?\033[m '))
print ('-=-' * 7)
print ('Welcome to program Traffic rules')
#Initial Question 
sred = str(input('\033[1;33mIf the light turns \033[1;31mRed\033[m, what do you do?  Walk/Stop: \033[m'))
sleep(1)
#Initial Questions about traffic sign color
if sred.lower() == 'stop':
    print ('\033[4;32mCongratulations, so you avoid unnecessary accidents\033[m')
else: 
    print ('\033[4;31mWrong answer, you should always STOP\033[m')
sgreen = str(input('\033[1;33mIf the light turns \033[1;32mgreen\033[m, what do you do? Walk/Stop: \033[m'))
sleep(1)
if sgreen.lower() == 'walk':
    print ('\033[4;32mCool!\033[m')
else: 
    print ('\033[4;31mNo your WALK!\033')
syellow = str(input('\033[1mIf the light turns \033[1;33myellow\033[m, what do you do? \033[1mAttencion/Stop:\033[m '))
sleep(1)
if  syellow.lower() == 'attencion':
    print ('\033[1;32mCool, your passed the first basic driving test\033[m')
else:
    print ('\033[1;33mThe yellow sign indicates attention, showing the imminence of the mandatory stop. This means that when you see the traffic light changing to yellow, the driver must slow down and stop the vehicle.\033[m')
#Last test question (Typing part and emoji have a rhombus with question mark, I don't know how to solve it yet.)
Tplace = str(input('Tell me the name of ONE of those 3 traffic signs: \U0001F6B8 \U0001F6D1 \U0001F6A6: '))
sleep(1)
if Tplace.lower() == 'stop' and 'pedestrian traffic' 'traffic light':
    print ('\033[1mOkay, Contrats! Your\033[m \033[1;32mPASSED\033[m \033[1m the final stage of the rapid transit test\033[m')
else:
    print ('\033[1That sad! :( Your\033[m \033[1;31mNOT PASSED\033[m \033[1mthe final stage of the rapid transit test. Go back and repeat again!\033[m')
#Finished
