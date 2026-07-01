def binarySearch(arr, number):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == '__main__':
    arr = [1, 3, 5, 7, 8, 9]
    number = 7
    result = binarySearch(arr, number)
    print(result)