def algorithm(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == 0:
                result.append((arr[i], arr[j]))
    return result

def optimizedAlgorithm(arr):
    result = []
    seen = set()
    for num in arr:
        if -num in seen:
            result.append((num, -num))
        seen.add(num)
    return result