def Fibonacci(n):
  
  # Setting up the base cases
  if n == 0:
    return 0
  elif n == 1:
    return 1
  
  # Calculating the Fibonacci sequence
  num1, num2 = 0, 1
  for i in range(2, n+1):
    num1, num2 = num2, num1 + num2
    
  return num2

# Driver Code
n = 10
print(Fibonacci(n))