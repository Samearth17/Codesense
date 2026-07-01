class Calculator(object):
    def __init__(self):
        pass
    
    def add(self, x, y):
        return x + y
   
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y

#Main Program
c = Calculator()
print(c.add(4, 8))
print(c.subtract(4, 8))
print(c.multiply(4, 8))
print(c.divide(4, 8))