def printFibo(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        print(a) 
    elif n == 1: 
        print(a,b) 
    else: 
        print(a,b,end=" ") 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
            print(b,end=" ") 

printFibo(10)