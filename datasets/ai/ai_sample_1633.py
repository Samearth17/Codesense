"""
Generate a solution for finding all possible subsets of a given set in Python.
"""

def find_subsets(nums):
  subsets = [[]]

  for current_num in nums:
    for i in range(len(subsets)):
      set_to_add = subsets[i] + [current_num]
      subsets.append(set_to_add)

  return subsets

nums = [1, 2, 3]
print(find_subsets(nums))