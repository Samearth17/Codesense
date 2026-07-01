def binary_search(arr, num):
    # define start and end point
    start = 0 
    end = len(arr)-1

    while start <= end:
        mid = (start + end)//2

        # check if num is present at mid 
        if arr[mid] == num: 
            return mid 

        # If num is greater, ignore left half 
        elif arr[mid] < num: 
            start = mid + 1

        # If num is smaller, ignore right half 
        else: 
            end = mid - 1
  
    # If we reach here, then the element was not present 
    return -1