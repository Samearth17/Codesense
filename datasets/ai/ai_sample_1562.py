def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

arr = [1, 2, 3, 4]

reverse_array(arr)

print(arr)  # [4, 3, 2, 1]