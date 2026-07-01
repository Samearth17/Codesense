# find the most frequent number in a given array
def get_most_frequent(arr):
    freq_map = dict()
    
    # build frequency map
    for num in arr:
        if num not in freq_map:
            freq_map[num] = 1
        else:
            freq_map[num] += 1
    
    # find the most frequent number
    max_freq = -1
    most_frequent_num = 0
    for key, value in freq_map.items():
        if value > max_freq:
            max_freq = value
            most_frequent_num = key
    
    return most_frequent_num

# Test
arr = [10, 8, 8, 9, 10, 11, 12, 12, 11]
most_frequent_num = get_most_frequent(arr)
print(most_frequent_num) # Output: 11