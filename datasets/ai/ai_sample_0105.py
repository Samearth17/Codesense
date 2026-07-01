def first_non_repeating_char(lst):
    dct = {}
    
    for l in lst:
        if l in dct:
            dct[l] += 1
        else:
            dct[l] = 1
            
    for l in lst:
        if dct[l] == 1:
            return l
            
    return None

lst = [1, 2, 3, 4, 4, 3, 2, 1]
print(first_non_repeating_char(lst))