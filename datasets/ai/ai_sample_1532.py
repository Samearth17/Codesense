#Program to implement a basic calculator

#Define a function to perform the operation
def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2

#Take the numbers and operation as input
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
operation = input('Select an operation (add, subtract, multiply, divide): ')

#Call the function to perform the operation
result = calculate(num1, num2, operation)

#Print the result
print('Result:',result)