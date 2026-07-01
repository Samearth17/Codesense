def normalize(nums):
  min_num = min(nums)
  max_num = max(nums)

  for i, n in enumerate(nums):
    if n > min_num and n < max_num:
      if n - min_num > max_num - n:
        nums[i] = max_num
      else:
        nums[i] = min_num

  return nums

print(normalize([5, 4, 3, 4, 8, 6, 7]))
# [5, 4, 3, 5, 8, 6, 7]