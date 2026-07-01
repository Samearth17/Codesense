def move_zeroes(nums):
    """
    Moves all the zeros in a given list to the end.
    @param nums: List
    @return: List
    """
    i = 0
    for num in nums:
        if num != 0:
            nums[i] = num
            i += 1
    while i < len(nums):
        nums[i] = 0
        i += 1
    return nums