def permute(nums):
    if len(nums) <= 1:
        return [nums]

    permutations = []
    for i in range(len(nums)):
        v = nums[i]
        left = nums[:i] + nums[i+1:]
        subpermute = permute(left)
        for item in subpermute:
            permutations.append([v] + item)
    return permutations

def descending_order(nums):
    permutations = permute(nums)
    best_permutation = []
    for permutation in permutations:
        if is_descending_order(permutation):
            best_permutation = permutation
    return best_permutation

def is_descending_order(arr):
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            return False
    return True

result = descending_order([4,7,2,1])
print(result)