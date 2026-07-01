def sort_list(array): 
    n = len(array) 
  
    for i in range(n): 
  
        min_idx = i 
        for j in range(i+1, n): 
            if array[min_idx] > array[j]: 
                min_idx = j 
        array[i], array[min_idx] = array[min_idx], array[i]

if __name__ == "__main__":
    array = [4, 2, 6, 7, 1]
    sort_list(array)
    print(array)