def get_max_min(arr):
    max_num = None
    min_num = None

    for n in arr:
        if max_num is None or n > max_num:
            max_num = n

        if min_num is None or n < min_num:
            min_num = n

    return max_num, min_num

max_num, min_num = get_max_min([-5, 7, 2, 11, -9])
print(f"max = {max_num}, min = {min_num}")