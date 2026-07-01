def Fibonacci(limit): 
 
    # Initializing first two Fibonacci numbers 
    num1 = 0
    num2 = 1
  
    # Initialize empty list
    fibonacci_numbers = []
  
    # Add the initialized numbers to the list
    fibonacci_numbers.append(num1)
    fibonacci_numbers.append(num2)
  
    # Calculate remaining Fibonacci numbers and add them to the list
    for i in range(2, limit):
        num3 = num1 + num2
        fibonacci_numbers.append(num3)
   
        # Re-initialize numbers for next iteration
        num1 = num2 
        num2 = num3
          
    return fibonacci_numbers
  
# Driver code
limit = 10
print(Fibonacci(limit))