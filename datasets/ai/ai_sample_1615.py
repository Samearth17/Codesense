def sum_integer(arr):
    """
    Args :
        arr (list): List of integer
    
    Returns :
        int : Sum of integers
    """
    
    res = 0
    
    for num in arr:
        res += num
    
    return res

sum_integer([5, 2, 8, 4, 23])
# output: 42