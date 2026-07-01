def findPairs(nums, t_sum):
    '''Function to find all the unique pairs of numbers 
    that add up to the target sum.'''
    num_set = set(nums)
    found_pairs = []
    for num in nums:
        if (t_sum - num) in num_set:
            found_pair = (min(num, t_sum - num), max(num, t_sum - num))
            if found_pair not in found_pairs:
                found_pairs.append(found_pair)
    return found_pairs
    
nums = [2, 3, 5, 7]
t_sum = 10
print(findPairs(nums, t_sum))