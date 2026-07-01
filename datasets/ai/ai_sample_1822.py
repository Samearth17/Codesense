class Calculate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b
        
    def multiply(self):
        return self.a*self.b

calc = Calculate(3,4) 
add = calc.add()
multiply = calc.multiply()
print("Addition result: {}".format(add))
print("Multiplication result: {}".format(multiply))