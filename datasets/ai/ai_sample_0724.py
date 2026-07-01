def search(sorted_list, item):
    low = 0
    high = len(sorted_list) - 1
    found = False

    while low <= high and not found:
        mid = (low + high) // 2
        if sorted_list[mid] == item:
            found = True
        else:
            if item < sorted_list[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return found

sorted_list = [2, 3, 4, 5, 8, 9, 10] 
item = 8
print(search(sorted_list, item))