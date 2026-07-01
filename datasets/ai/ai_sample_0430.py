class Computer: 
    def __init__(self, name): 
        self.name = name 

    def calculate(self): 
        pass

# Let's create a class to add two numbers
class Add(Computer): 
    def calculate(self, x, y): 
        return x + y

# Let's create a class to multiply two numbers
class Multiply(Computer): 
    def calculate(self, x, y): 
        return x * y

# Client code to use the classes above 
class Client(Computer): 
    # Utility method to calculate sum 
    def sum(self, a, b): 
        s = Add(self.name)
        m = Multiply(self.name)
        total = s.calculate(a, b) + m.calculate(a, b) 
        print("Result of sum and multiply", total)
        return total 

# Create a client object
c = Client("Comp")
c.sum(2, 6)  # Result of sum and multiply 14