# Function to generate multiplication table  
def multiplication_table(n): 
    # set the initial value and iters
    num = 1
    iters = n + 1
      
    # outer loop
    for i in range(1, iters): 
          
        # inner loop 
        for j in range(1, iters): 
              
            # print statement 
            print(num, end = " ") 
              
            num = num + 1
        print()
  
# Driver code
n = 3
multiplication_table(n)