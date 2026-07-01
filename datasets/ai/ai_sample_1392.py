# Function to find sum of all elements in a list 
def list_sum_recursive(nums): 
    # Base case 
	if len(nums) == 1: 
		return nums[0] 
	else: 
		# Divide & Conquer
		mid = len(nums) // 2
		leftsum = list_sum_recursive(nums[:mid])
		rightsum = list_sum_recursive(nums[mid:])
		return leftsum + rightsum
	
# Driver code 
nums = [1, 2, 3, 4, 5] 
sum_nums = list_sum_recursive(nums) 
print(sum_nums)