def calculater(num1, num2, operator):

if operator == '+':
 return num1 + num2
elif operator == '-':
 return num1 - num2
elif operator == '*':
 return num1 * num2
elif operator == '/':
 return num1 / num2

print('Sum:', calculater(3, 4, '+'))
print('Subtraction:', calculater(3, 4, '-'))
print('Multiplication:', calculater(3, 4, '*'))
print('Division:', calculater(3, 4, '/'))