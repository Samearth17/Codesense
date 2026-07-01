def insertion_sort(list):
    """
    Sort a given list using insertion sort.
    list: the list to be sorted
    """
    # loop through each element in the list, starting from the second element
    for i in range(1, len(list)):  
        temp = list[i] 
  
        # find the position where the current element should be inserted
        j = i-1
        while j >= 0 and temp < list[j] : 
                list[j+1] = list[j] 
                j -= 1
        list[j+1] = temp 
  
    return list