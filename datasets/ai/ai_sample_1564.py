class MathOperations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2

num1 = 0
num2 = 0
math_operation = MathOperations(num1, num2)
print(math_operation.add())
print(math_operation.subtract())