from time import sleep
#Asks user height and weight
height = float(input('\033[1mEnter your height in meters: '))
weight = float(input('Enter your weight in Kg:?\033[m '))
imc = weight / (height ** 2)
sleep(1)
print ('\033[1;33mPROCESSING...\033[m')
sleep(1)
print ('\033[1mYour BMI is {:.1f}\033[m'.format(imc))
sleep(2)
print ('\033[1;36mPROCESSING RESULTS...\033[m')
sleep(2)
#Starts the BMI calculation program
if imc <= 18.5:
    print ('\033[1;36mUnder weight\033[m')
elif 18.5 <= imc < 25:
        print ('\033[1;32mNormal weight\033[m')
elif 25 <= imc <30:
    print ('\033[1;31mObesity degree I: Overweight\033[m')
elif 30 <= imc <40:
    print ('\033[1;31mObesity degree II: Obesity\033[m')
elif imc >=40:
    print ('\033[1;31mObesity degree III: Morbid obesity\033[m')
