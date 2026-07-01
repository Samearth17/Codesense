def find_min_max_avg(arr):
    # set the min, max numbers to the first item in the array
    min_num = arr[0]
    max_num = arr[0]

    # keep track of the sum of all the numbers
    sum_num = 0

    # iterate through the array
    for item in arr:
        # find smallest number
        if item < min_num:
            min_num = item
        # find largest number
        elif item > max_num:
            max_num = item
        # add each number to the sum
        sum_num += item

    # calculate the average
    avg_num = sum_num / len(arr)
    print("Smallest Number: {}\nLargest Number: {}".format(min_num, max_num))
    return avg_num