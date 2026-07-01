def print_triangle(rows):
    """
    This function prints a triangle of stars with a given number of rows.
    
    Parameters:
    rows (int): The number of rows
    
    Returns:
    None
    """
    
    for i in range(rows):  
        for j in range(i+1): 
            print("* ", end="")
        print('\r')