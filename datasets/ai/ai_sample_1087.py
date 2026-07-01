def find_min_max(list_of_nums):
    min_num = list_of_nums[0]
    max_num = list_of_nums[0]

    for num in list_of_nums:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    
    return (min_num, max_num)

list_of_nums = [10, 24, 55, 16, 1, 9]
(min_num, max_num) = find_min_max(list_of_nums)
print("Min Num: {}  Max Num: {}".format(min_num, max_num))