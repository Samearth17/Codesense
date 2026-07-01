# Program to generate a Fibonacci series using an algorithm

# function to generate Fibonacci series
def generate_fibonacci_series(n):
    a, b = 0, 1 
    result = [] 
    while b < n:
        result.append(b)
        a, b = b, a + b 
    return result

# Driver code 
n = 10
result = generate_fibonacci_series(n)
print("The Fibonacci number up to", n, "is", result)