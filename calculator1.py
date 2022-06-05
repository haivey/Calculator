# To add two numbers
def add (x, y):
    return x + y

# To subtract two numbers
def subtract (x, y):
    return x - y

# To multiply two numbers
def multiply (x, y):
    return x * y

# To divide two numbers
def divide (x, y):
    return x / y

print('Select Operation')
print('A.Add')
print('S.Subtract')
print('M.Multiply')
print('D.Divide')

while True:
    # take input from user
    choice = input('Enter choice(A/S/M/D): ')

    # check if choice is one of the 4 options
    if choice in ('A', 'S', 'M', 'D'):
        number1 = int(input('Enter first number: '))
        number2 = int(input('Enter second number:  '))

        if choice == 'A':
            print(number1, '+', number2, '=', add(number1, number2))
        
        elif choice == 'S':
            print(number1, '-', number2, '=', subtract(number1, number2))
        
        elif choice == "M":
            print(number1, '*', number2, '=', multiply(number1, number2))
        
        elif choice == "D":
            print(number1, '/', number2, '=', divide(number1, number2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else: 
        print("Invalid Input")