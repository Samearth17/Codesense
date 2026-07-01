def find_closest_sum_of_two(arr):
    if len(arr) < 2:
        return None
    
    # initialize the closest sum and indicies
    closest_sum = arr[0] + arr[1]
    first_index = 0
    second_index = 1
    
    # loop through the array and check for closer sums
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i] + arr[j]) < abs(closest_sum):
                closest_sum = arr[i] + arr[j]
                first_index = i
                second_index = j
    
    return arr[first_index], arr[second_index], closest_sum