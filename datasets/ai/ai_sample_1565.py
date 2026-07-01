# This program is used to calculate the median of a given list of integers.

# The input list of integers
nums = [1,2,3,4,5]

# Function to calculate the median
def median(nums):
  nums.sort()
  if len(nums) % 2 == 0:
    median = (nums[len(nums)//2 - 1] + nums[len(nums)//2])/2 
  else:
    median = nums[len(nums)//2]
  return median

# Main program
if __name__== "__main__":
  print(median(nums))