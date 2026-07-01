def PascalTriangle(n) : 
      
    # An auxiliary array to store 
    # generated pscal triangle values 
    arr = [0 for i in range(n)] 
      
    # Iterate through every line and 
    # print integer(s) in it 
    for line in range(0, n) : 
          
        # Every line has number of  
        # integers equal to line  
        # number 
        for i in range (0, line + 1) : 
              
            # First and last values  
            # in every row are 1 
            if (i == 0 or i == line) : 
                arr[i] = 1
                  
            # Other values are sum of  
            # values just above and  
            # left of above 
            else : 
                arr[i] = arr[i] + arr[i - 1]  
              
        # Printing array in 
        # mantainence of order          
        for i in range (0, line + 1) : 
            print(arr[i], end =" ")  
        print()   
  
# Driver Code 
n = 5
PascalTriangle(n)