def calculator():
    operator = input("Please enter an operator: ")
    num1 = float(input("Please enter your first number: "))
    num2 = float(input("Please enter your second number: "))

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("Invalid operator")

calculator()