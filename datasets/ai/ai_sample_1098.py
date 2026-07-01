class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        denom = self.denominator * other.denominator
        num1 = self.numerator * other.denominator
        num2 = other.numerator * self.denominator
        numerator = num1 + num2
        return Fraction(numerator, denom)

    def __sub__(self, other):
        denom = self.denominator * other.denominator
        num1 = self.numerator * other.denominator
        num2 = other.numerator * self.denominator
        numerator = num1 - num2
        return Fraction(numerator, denom)