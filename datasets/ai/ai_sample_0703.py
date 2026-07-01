def sortList(arr):
    if len(arr) == 0:
        return []
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = sortList(left)
    right = sortList(right)
    return merge(left, right)

def merge(left, right):
    result = []
    leftIndex = 0
    rightIndex = 0

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

    result += left[leftIndex:]
    result += right[rightIndex:]
    return result