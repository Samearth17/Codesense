def pascal_triangle(n): 
  
    # Array to store generated pascal triangle values 
    pascal = [] 
  
    for i in range(n): 
        pascal.append([]) 
        pascal[i].append(1) 
          
        for j in range(1, i+1): 
            # Generate next row values from previous row values 
            x = pascal[i-1][j-1] + pascal[i-1][j] if j!=0 else 1
            pascal[i].append(x) 
  
    # Print last row of Pascal's Triangle 
    for i in range(n): 
        print(pascal[n-1][i], end = " ") 
  
n = 5
pascal_triangle(n) 

# Output: 1 5 10 10 5 1