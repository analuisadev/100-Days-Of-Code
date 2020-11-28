print ('\033[33m -=-\033[m' *7)
#unity1 is having a problem with the terminal spacing, just enter it back to the place
unity1 = float(input('\033[1;37mYour note from first unity: \033[m'))
unity2 = float(input('\033[1;37mYour note from second unity: \033[m '))
unity3 = float(input('\033[1;37mYour note from third unity: \033[m '))
unity4 = float(input('\033[1;37mYour note from fourth unity: \033[m'))
average = (unity1 + unity2 + unity3 + unity4) /4
print ('\033[33m -=-\033[m' * 7)
print ('\033[1;37mCalculating your average...\033[m')
print ('\033[33m -=-\033[m' * 7)
sleep(1)
if average >= 5:

    print ('\033[1;33m      AMAZING! Your PASSED!\033[m')
else:
    print ('\033[1;31m      WHAT A PITY! Your not PASSED!\033[m')