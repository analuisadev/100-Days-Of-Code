print ('=' * 26)
print ('\033[1;33mCalculate your monthly fee\033[m')
print ('=' * 26)
salary = float(input('\033[1mWhats is value your salary? '))
user = int(input('\033[1mWhat is the total value of your account? '))
months = int(input('\033[1mHow many months did you pay in installments? '))
total = (salary - user) / months
print ('\033[32mYour salary is equal to {:.2f} and the total amount you will have to pay in {} months is R${}\033[m'.format(salary, months, total))
