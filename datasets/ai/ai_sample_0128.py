def compress_sequence(nums):
    output = []
    temp = []

    for i in range(1, len(nums)):
        if nums[i-1] * nums[i] >= 0:
            temp.append(nums[i-1])
        else:
            temp.append(nums[i-1])
            output.append(temp)
            temp = []
    temp.append(nums[i])
    output.append(temp)

    return output

print(compress_sequence([9, -2, 6, 0, -7]))