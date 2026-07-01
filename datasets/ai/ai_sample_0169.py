def closest_num(arr, num):
    arr.sort()
    n = len(arr)
    left = 0
    right = n - 1
 
    if arr[right] <= num:
        return arr[right]
    elif arr[left] >= num:
        return arr[left]
    while right-left > 1:
        mid = (right+left)//2
        if arr[mid] == num:
            return arr[mid]
        elif arr[mid] > num:
            right = mid
        else:
            left = mid
    return sorted([arr[right], arr[left]])[0]

arr = [5, 4, 8, 7]
num = 5
closest = closest_num(arr, num)
print(closest)