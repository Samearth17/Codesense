def sort_list(nums):
    for i in range(len(nums)):
        min_index = i
        
        for j in range(i+1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        
        nums[i], nums[min_index] = nums[min_index], nums[i]
        
    return nums
    
print(sort_list([3, 7, 2, 1, 19]))

# Output: [1, 2, 3, 7, 19]