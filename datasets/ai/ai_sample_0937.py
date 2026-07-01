def generate_tree(h): 
    # h is the height of the tree
    # Initialize the number of spaces per line 
    n_spaces = h - 1
  
    # Generate the tree structure 
    for i in range(1, h+1): 
        # Print h-i spaces at the beginning of each line 
        for j in range(n_spaces): 
            print(end=" ") 
              
        # Print i stars at the end of each line 
        for j in range(i): 
            print("* ", end="") 
              
        # Move to the next line (Print a newline character) 
        print() 
          
        # Update the number of spaces used 
        n_spaces -= 1