def computeSum(L):
    """Computes the sum of a list

    Parameters
    ----------
    L : list
        A list of numbers

    Returns
    -------
    total : int
        The sum of all the numbers in the list
    """
    total = 0
    for x in L:
        total += x
    return total