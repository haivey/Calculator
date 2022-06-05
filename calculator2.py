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

numList=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

while True:
    # take input from user
    choice = input('Enter choice(A/S/M/D): ')

    # check if choice is one of the 4 options
    if choice in ('A', 'S', 'M', 'D'):
        numbers = []
        while True:
            inputNumber = input('Enter the number: ')
            if inputNumber == "=":
                break
            elif inputNumber in numList:
                numbers.append(int(inputNumber))
            else:
                print("Invalid Input")


        if choice == 'A':
            print(numbers)
            print(f"The sum of all numbers is {sum(numbers)}")
        
        # elif choice == 'S':
        #     print(number1, '-', number2, '=', subtract(number1, number2))
        
        # elif choice == "M":
        #     print(number1, '*', number2, '=', multiply(number1, number2))
        
        # elif choice == "D":
        #     print(number1, '/', number2, '=', divide(number1, number2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else: 
        print("Invalid Input")