expr = str(input('\033[1mEnter a expression:\033[m '))
battery = []
for simb in expr:
    if simb == '(':
        battery.append('(')    
    elif simb == ')':
        if len(battery) > 0:
            battery.pop()
    else:
        battery.append(')')
        break
if len(battery) == 0:
    print ('\033[1;32mYour expression is valid\033[m')
else:
    print ('\033[1;31mYour expression is invalid.\033[m')
