def largest_even(arr):
    even_nums = []
    for num in arr:
        if num % 2 == 0:
            even_nums.append(num)
    
    if len(even_nums) == 0:
        return None
    
    largest = even_nums[0]
    for num in even_nums:
        if num > largest:
            largest = num
    
    return largest

result = largest_even([2, 5, 7, 6])
print(result)