def fibonacci(num): 
  # Initializing first two numbers of the series 
  a = 0
  b = 1
  print("Fibonacci series: ", end = " ") 
  for i in range(num): 
    # Generating next number in the series 
    c = a + b
    a = b
    b = c 
    # printing the generated number in the series 
    print(c, end =" ") 
  
# Get number of terms to generate in the series
num = 5

#Calling fibonacci function  
fibonacci(num)