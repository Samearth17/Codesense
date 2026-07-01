def Fibonacci(n): 
   if n<0: 
      print("Incorrect input") 
# First Fibonacci number is 0 
   elif n==1: 
      return 0
# Second Fibonacci number is 1 
   elif n==2: 
      return 1
   else: 
      return Fibonacci(n-1)+Fibonacci(n-2) 

# Input number of terms in the Fibonacci sequence
nterms = 10

# Check if the input number is valid
if nterms <= 0:
   print("Incorrect input")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(Fibonacci(i))
       
# This can be used to solve the Fibonacci Sequence puzzle
# The puzzle is -
# Given a number n, find the nth Fibonacci number
# That can be easily done using the above code