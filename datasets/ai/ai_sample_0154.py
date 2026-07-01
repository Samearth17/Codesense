def sierpinski_triangle(n): 
    # Drawing lines for first row 
    for i in range(2**n): 
        print(' ', end=" ") 
    
    # loop for printing n rows 
    for i in range(1, n+1): 
        # bit pattern for first and 
        # last line of each row 
        for j in range(2**(i-1), 2**i): 
            print('1', end=" ") 
        print() 
        
        # inner rows have opposite bit pattern 
        if i > 1: 
            for j in range(2**(i-1)+1, 2**i-1):  
                print('0', end=" ") 
            print() 
       
sierpinski_triangle(6)