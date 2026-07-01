def findMinMax(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        maximum = num1
        minimum = num3 if num3 <= num2 else num2
    elif num2 >= num1 and num2 >= num3:
        maximum = num2
        minimum = num1 if num1 <= num3 else num3
    else:
        maximum = num3
        minimum = num1 if num1 <= num2 else num2
    return (maximum, minimum)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

maximum, minimum = findMinMax(num1, num2, num3)

print("Maximum of three numbers is:", maximum)
print("Minimum of three numbers is:", minimum)