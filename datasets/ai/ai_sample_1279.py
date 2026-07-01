def sort_by_freq(nums):
    """
    A sort function to order a list of numbers by their frequency.

    Parameters
    ----------
    nums : List
        A list of numbers

    Returns
    -------
    List
        The given list of numbers sorted by their frequency
    """
    freq_map = {}
    for num in nums:
        if num not in freq_map:
            freq_map[num] = 0
        freq_map[num] += 1

    sorted_nums = sorted(freq_map, key=freq_map.get, reverse=True)
    return sorted_nums