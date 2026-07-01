def combinations(arr, r): 
    # Get the length of array 
    n = len(arr) 
      
    # Create an array to store indexes of elements 
    # taken for combination 
    data = [0]*r 
      
    combinationUtil(arr, data, 0, n-1, 0, r) 
      
# arr[]  -->> Input Array 
# data[] -->> Temporary array to store current combination 
# start & end -->> Staring and Ending indexes in arr[] 
# index -->> Current index in data[]  
# r -->> Size of a combination to be printed 
def combinationUtil(arr, data, start, end, index, r): 
    # Current combination is ready to be printed, print it 
    if (index == r): 
        for j in range(r): 
            print(data[j], end = " ") 
        print() 
        return
  
    # Replace index with all possible elements. The condition 
    # "end-i+1 >= r-index" makes sure that including one element 
    # at index will make a combination with remaining elements 
    # at remaining positions 
    i = start
    while(i <= end and end - i + 1 >= r - index): 
        data[index] = arr[i] 
        combinationUtil(arr, data, i + 1, end, index + 1, r) 
        i += 1

combinations(["A","B","C"], 2)
# A B 
# A C 
# B C