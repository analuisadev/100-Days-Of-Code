sumage = 0
mAge = 0
bigageMan = 0
nameOld = 0
twoman20 = 0
print ('\033[1m{:=^40}\033[m'.format(' COMPLETE ANALYZER '))
for people in range(1, 5):
    print ('=-=-=-=--=-= {}ª PEOPLE -=-=-=-=-=-='.format(people))
    name = str(input('\033[1mName:\033[m ')).strip()
    age = int(input('\033[1mAge:\033[m '))
    sex = str(input('\033[1mSex M/F:\033[m ')).strip()
    sumage += age
    if people == 1 and sex in 'Mm':
        sumage = age
        nameOld = name 
    if sex in 'Mm' and age > bigageMan:
        bigageMan = age
        nameOld = name
    if sex in 'Ff' and age < 20 :
        twoman20 +=1
mAge = sumage / 4
print ('\033[1;32mThe average age of the group is {} years\033[m'.format(mAge))
print ('\033[1;32mThe oldest man is {} years old and is called {}\033[m'.format(bigageMan,nameOld))
print ('\033[1;32mThere are {} women under 20\033[m'.format(twoman20))