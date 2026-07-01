def max_sum_subarray(arr):
    max_sum = None
 
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            total_sum = 0
            for y in range(i, len(arr)):
                for x in range(j, len(arr[y])):
                    total_sum += arr[y][x]
 
            if max_sum is None or total_sum > max_sum:
                max_sum = total_sum
 
    return max_sum
 
arr = [[1, -2, 3], [4, 5, -6], [7, 8, 9]]
print(max_sum_subarray(arr))

# Output should be 19