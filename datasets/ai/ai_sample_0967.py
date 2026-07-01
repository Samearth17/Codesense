def get_consecutive(arr):
    result = []
    i = 0
    while i < len(arr):
        s = i
        while (i + 1 < len(arr)) and (arr[i + 1] == arr[i] + 1):
            i += 1
        result.append((arr[s], arr[i]))
        i += 1
    return result

# Test 
arr = [1, 2, 3, 7, 8, 9, 10]
print(get_consecutive(arr))
# Output [(1, 3), (7, 10)]