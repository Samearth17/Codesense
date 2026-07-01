def calculate_factorial(num): 
    if num < 0: 
        return 0
    elif num == 0 or num == 1: 
        return 1
    else: 
        factorial = 1
        while num > 1:             
            factorial = factorial * num 
            num = num - 1
        return factorial 

# get user input 
number = int(input("Enter a number: "))

# call the function
factorial = calculate_factorial(number)

# print the result 
print("Factorial of", number, "is", factorial)