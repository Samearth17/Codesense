def max_val(num1, num2):
    # function to find the maximum value of two numbers
    if(num1 > num2):
        return num1
    else:
        return num2

# get the input values from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# call the max_val() function
max_val = max_val(a,b)

print("The maximum value is:", max_val)