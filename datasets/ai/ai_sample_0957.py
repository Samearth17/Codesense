#!/usr/bin/env python3

# This program is a basic calculator that can take in two values and an operator

# The corresponding operations when the operator input is given
operations = {
    "+": lambda x, y: x + y, 
    "-": lambda x, y: x - y, 
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}

# Take in the values and operator from the user
num1 = int(input("Enter the first number: "))
operator = input("Enter the operator: ")
num2 = int(input("Enter the second number: "))

# Assert that the operator is valid
assert operator in operations, f"The given operator {operator} is not a valid operator"

# Calculate the result
result = operations[operator](num1, num2)

print(f"Result: {num1} {operator} {num2} = {result}")