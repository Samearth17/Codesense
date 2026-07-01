def bubble_sort(arr): 
    # go through each element in the list
    for elem in arr: 
        # compare one elem with each of the successive elements
        for i in range(len(arr)-1): 
            if arr[i] > arr[i+1]: 
                temp = arr[i] 
                arr[i] = arr[i+1] 
                arr[i+1] = temp 
  
    return arr 
  
arr = [7,2,5,1,3]
sorted_arr = bubble_sort(arr)
print("Sorted array:",sorted_arr)

Output: Sorted array: [1,2,3,5,7]