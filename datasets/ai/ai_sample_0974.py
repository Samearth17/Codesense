def sum_natural_numbers(start, end):
    """
    Computes the sum of all natural numbers in a given range.
    
    Parameters:
    start (int): start of the range
    end (int): end of the range
    
    Returns:
    int: the sum of the natural numbers in the range
    """
    total = 0
    for i in range(start, end+1):
        total += i
    return total