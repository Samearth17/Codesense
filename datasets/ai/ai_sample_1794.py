# Fibonacci series program
def fibonacci(n, f_values):
 # base case
 if n == 0:
  return 0
 elif n == 1:
  return 1
 if n in f_values:
  return f_values[n]
 else:
  f_values[n] = fibonacci(n-1, f_values) + fibonacci(n-2, f_values)
  return f_values[n]

# calculate the fibonacci series
def calculate_fibonacci(n):
 f_values = {}
 for i in range(n+1):
  value = fibonacci(i, f_values)
  print(f"{i}: {value}")