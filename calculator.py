operation = input('''
Please key in the math operation:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input('Enter your first number:'))
number_2 = int(input('Enter your second number:'))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('You have not keyed in a valid operator, please try again')
    


