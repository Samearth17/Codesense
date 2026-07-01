def generate_fibonacci(n):  
    #first two Fibonacci numbers  
    a = 0
    b = 1
    #check if the number of terms is valid  
    if n <=0:  
        print("Please enter a positive integer")  
    elif n == 1:  
        print("Fibonacci sequence upto",n,":")  
        print(a)  
    else:  
        print("Fibonacci sequence:")  
        for i in range(0,n):  
            print(a)  
            c = a + b  
            #update values  
            a = b  
            b = c  
# Driver function  
generate_fibonacci(10000)