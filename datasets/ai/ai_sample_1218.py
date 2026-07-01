# Menu Driven Program
print('Welcome to the Simple Calculator')

# Define the calculator functions
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def logarithm(a):
    return math.log(a)

# Create a main loop
while True:
    # Show the user the options
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Logarithm')
    print('6. Quit')

    # Ask the user to choose
    choice = int(input('Choose a number from 1 to 6: '))

    # Create a condition for each calculator function
    if choice == 1: # Addition
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))
        print('Result: {}'.format(addition(a, b)))

    elif choice == 2: # Subtraction
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))
        print('Result: {}'.format(subtraction(a, b)))

    elif choice == 3: # Multiplication
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))
        print('Result: {}'.format(multiplication(a, b)))

    elif choice == 4: # Division
        a = float(input('Enter the first number: '))
        b = float(input('Enter the second number: '))
        print('Result: {}'.format(division(a, b)))
        
    elif choice == 5: # Logarithm
        a = float(input('Enter the first number: '))
        print('Result: {}'.format(logarithm(a)))
        
    elif choice == 6: # Quit
        print('Thank you for using the Simple Calculator.')
        break

    else: # Invalid number
        print('Please enter a valid number')