# function to generate the nth term of the Fibonacci sequence
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
      
# take input from the user
nterms = 10

# check if the number of terms is valid
if nterms<=0: 
    print("Please enter a positive integer") 
else: 
    print("Fibonacci sequence:")
    for i in range(1,nterms+1):
        print(Fibonacci(i))

# Output: Fibonacci sequence: 0 1 1 2 3 5 8 13 21 34