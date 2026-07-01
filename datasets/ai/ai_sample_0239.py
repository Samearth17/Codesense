def insertion_sort(input_list):
    # creating a copy of input list so that the original list is not modified
    sorted_list = input_list.copy()
    # Iterating through input list and inserting elements in the right place in the sorted list
    for i in range(1, len(sorted_list)):
        j = i-1
        key = sorted_list[i] 
        while sorted_list[j] > key and j >= 0:
            sorted_list[j+1] = sorted_list[j]
            j -= 1
        sorted_list[j+1] = key

    return sorted_list

sorted_list = insertion_sort(unsorted_list)