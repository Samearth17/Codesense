class Factorial:
    @staticmethod
    def compute_factorial(n):
        if n < 0:
            return None
            
        if n == 0 or n == 1:
            return 1
        
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
            
        return factorial
    
# Compute factorial of 5
result = Factorial.compute_factorial(5)
print(result)