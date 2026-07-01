def pyramid(height): 
 
    # Dot symbol for each row
    dots = "."
  
    # loop for printing the pyramid
    for i in range(height): 
        # insert spaces
        for j in range(height-i-1): 
            print("  ", end='') 
        for j in range(i+1): 
            # print dots and concatenate
            print(dots + " ", end='') 
            dots += ".."
  
        # moving to the new line 
        print("\r")