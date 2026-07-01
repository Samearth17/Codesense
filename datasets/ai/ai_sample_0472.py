def binarySearch2D(arr, key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid][0] == key:
            return True
        elif arr[mid][0] > key:
            end = mid - 1
        else:
            start = mid + 1
    return False

arr = [[1, 5, 8], [2, 15, 20], [3, 25, 30], [11, 13, 16]]
key = 3

if binarySearch2D(arr, key):
    print(True) 
else :
    print(False)