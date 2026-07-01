def sum_numbers(arr):
    result = 0
    for num in arr:
        result += num
    return result

arr = [2, 4, 6, 8]

print(sum_numbers(arr))

# optimized version
def optimised_sum_numbers(arr):
    return sum(arr)

print(optimised_sum_numbers(arr))