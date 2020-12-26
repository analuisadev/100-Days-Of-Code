from time import sleep
print ('\033[1;36m{:=^40}\033[m'.format(' Welcome to the covid-19 manual and prevention '))
sleep (1)
while True: 
    print ('''\033[1mOptions menu:
[1] Prevention alerts
[2] Symptoms 
[3] End the programa\033[m''')
    sleep(1)
    select = int(input('\033[1;32mChoose the option:\033[m '))
    sleep(1)
    if select == 1: 
        sleep(1)
        print ('\033[1;36m{:=^40}\033[m'.format(''' Prevention list 
\033[1;32m1°\033[m \033[1;33mKeep 1.5 meters away from people coughing or sneezing\033[m
\033[1;32m2°\033[m \033[1;33mAlways wash your hands or use alcohol gel\033[m
\033[1;32m3°\033[m \033[1;33mWear a mask when it is not possible to maintain physical distance.\033[m
\033[1;32m4°\033[m \033[1;33mSeek medical attention if you have a fever, cough and difficulty breathing.\033[m
\033[1;32m5°\033[m \033[1;33mDo not touch the eyes, nose or mouth.\033[m
\033[1;32m6°\033[m \033[1;33mStay home if you feel unwell.\033[m
\033[1;32m7°\033[m \033[1;33mCover your nose and mouth with your arm folded or a tissue when you cough or exhale\033[m'''))
    if select == 2:
        temperature = int(input('Whats your temeperature? '))
        if temperature >= 35 and temperature == 36 or 37: 
            print ('\033[1;33mYour temperature is adequate, keep prevention measures in place.\033[m')
        else:
            print ('\033[1;31mIts temperature is high, ALERT SIGN\033[m')
    if select == 3: 
        print ('\033[1;35mFinished programm\033[m')
        break
        
