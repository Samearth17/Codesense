# Kadane's algorithm
def max_sum_subarray(array):
    max_so_far = 0
    max_ending_here = 0

    for i in range(len(array)):
        max_ending_here += array[i]
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sum_subarray(array))