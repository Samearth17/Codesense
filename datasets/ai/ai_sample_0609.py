def Fibonacci(a): 
    if a<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif a==1: 
        return 0
    # Second Fibonacci number is 1 
    elif a==2: 
        return 1
    else: 
        return Fibonacci(a-1)+Fibonacci(a-2) 
  
# Driver Program 

limit = int(input('Enter the limit of fibonacci series:'))
for i in range(1,limit+1): 
    print(Fibonacci(i))