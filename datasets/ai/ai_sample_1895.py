class Arithmetic:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

a = Arithmetic(2, 4)
print(a.addition()) # Output: 6
print(a.subtraction()) # Output: -2
print(a.multiplication()) # Output: 8
print(a.division()) # Output: 0.5