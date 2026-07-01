def custom_sort(list_a):
    # Creating a list to store the sorted elements
    sorted_list = []

    while list_a:
        # Find the smallest number from the list
        min_item = min(list_a)
        
        # Append the smallest number to the sorted list
        sorted_list.append(min_item)
        
        # Remove the number from the original list
        list_a.remove(min_item)
    
    # Return the sorted list
    return sorted_list

print(custom_sort([3, 2, 1, 4]))