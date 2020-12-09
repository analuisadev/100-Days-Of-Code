from time import sleep
import sys
name = str(input('\033[1;40mYour name\033[m: ')).strip()
sleep (1)
age = int(input('\033[1;40mYour age:\033[m '))
sleep(1)
if age >= 18:
    print ('''\033[1;33mOkay, you can go to college
           Take responsibility!\033[m''')
else:
    print ('''\033[1;32mYour not can go to college now
           Likewise, take responsibility\033[m''')
    sys.exit()
sleep(1)
college = str(input('\033[1;40mDo you want to go to college?\033[m \033[1mYes/No\033[m ')).lower()
sleep(1)
if college == 'yes':
    print ('\033[32mOOW, THAT GREAT!\033[m')
else: 
    print ('\033[1;34mAlright :D all in your time\033[m')
    print ('\033[1;36mUntil next opportunity XD\033[m')
    sys.exit()
pp = str(input('\033[1mPublic or private?\033[m ')).lower()
if college == 'yes' and pp == 'private':
    print ('\033[1;33mYou will have to separate your monthly fee\033[m')
elif college == 'yes' and pp == 'public':
    print ('\033[1;33mStudy hard to pass your college\033[m')
    sys.exit()
sleep(1)
mb = float(input('\033[1mWhat is your total monthly budget? '))
sleep(1)
collegePrice = int(input('What is the cost of your college course? '))
total = mb - collegePrice
print ('PROCESSING...\033[m')
sleep(1)
print ('\033[1mYour monthly income is R$ {} and the value of your college is {} soon you will have a total of {}'.format(mb, collegePrice, total))
sleep(1)
print ('PROCESSING...')
if total <= 900:
    print ('\033[1;32mYour monthly income may be short, look for a way to earn EXTRA INCOME!\033[m')
    print ('''\033[1;33mEXTRA INCOME IDEAS:
           1 - Copper to teach
           2 - Offer your services
           3 - Take a tour of your home and write down what you no longer use and sell
           4 - Sell ​​online or face-to-face courses 
           5 - Work as a street vendor
           6 - Search for a part-time job or internship\033[m''')
else: 
    print ('\033[1Okay, it looks like it will be financially stable :D\033[m')