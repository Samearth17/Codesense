def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        x = 0
        y = 1
        for i in range(2, n): 
            z = x+y 
            x = y 
            y = z 
        return z 
  
for i in range(1, 11): 
    print(Fibonacci(i))