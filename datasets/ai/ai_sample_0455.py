def index_of(number, lst): 
    hi = len(lst) 
    lo = 0
    index = -1

    while hi > lo: 
        mid = (hi + lo)//2
        if lst[mid] < number: 
            lo = mid + 1
        elif lst[mid] > number: 
            hi = mid 
        else: 
            index = mid 
            return index 
    return index