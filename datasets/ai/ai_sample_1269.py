def print_pattern(n): 
  
    # outer loop to handle number of rows 
    for i in range(1,n+1): 
      
        # inner loop to handle number of columns 
        for j in range(1,i+1): 
          
            # printing stars 
            print('* ', end="") 
       
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n = 3
print_pattern(n)

Output:
* 
* * 
* * *