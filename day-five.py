from time import sleep
name = str(input('\033[1mUser, whats your name?\033[m ')).strip()
year = int(input('\033[1mWhat year were you born in?\033[m '))
curyear = int(input('\033[1mWhat year are you applying this application?\033[m '))
agecur = curyear - year
print ('{} will have {} years'.format(name, agecur))
sleep(1)
if agecur >= 18:
    print ('\033[1;32mYou are of legal age, do everything within the law :)\033[m')
else: 
    sleep(1)
    print ('\033[1;31mYou are still a minor, obey your parents! :)\033[m')