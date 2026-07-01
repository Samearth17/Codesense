def most_frequent(arr):
    arr.sort()
    max_count = 1
    max_item = arr[0]
    curr_count = 1
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            curr_count += 1
            if curr_count > max_count:
                max_count = curr_count
                max_item = arr[i]
        else:
            curr_count = 1
    
    return max_item