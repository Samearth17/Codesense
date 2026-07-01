def insertionSort(arr): 
    for i in range(1, len(arr)): 
  
        j = i-1
        key = arr[i] 
  
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
arr = [3,8,15,2,6,10]
insertionSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i])