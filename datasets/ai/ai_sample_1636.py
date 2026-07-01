def fibonacci(n):
 # Initialize a memoization dictionary
 memo = {
 0: 0,
 1: 1
 }
 
 # If n is in the memoization dictionary, return the value
 if n in memo:
 return memo[n]
 
 # Calculate the Fibonacci number
 if n > 1:
 memo[n] = fibonacci(n-1) + fibonacci(n-2)
 
 return memo[n]

print(fibonacci(10))