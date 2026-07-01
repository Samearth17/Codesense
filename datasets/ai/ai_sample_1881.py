def calculate_median_and_mode(data):
    median = 0
    mode = 0

    data_length = len(data)

    data.sort()

    # Calculate median
    if data_length % 2 == 0:
        median = (data[int(data_length/2)] + data[int(data_length/2) - 1])/2
    else:
        median = data[int(data_length/2)]

    # Calculate mode
    lst = []
    max_freq = 1

    for i in range(data_length): 
        freq = 1
        for j in range(data_length):
            if (data[i] == data[j] and i != j): 
                freq += 1

        if freq > max_freq:
            lst.clear()
            max_freq = freq
            lst.append(data[i])
        elif freq == max_freq and data[i] not in lst:
            lst.append(data[i])

    # If no elements have maximum frequency, function return mode equal to 0 
    if len(lst) == 0:
        mode = 0
    else:
        mode = lst

    return (median, mode)

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6]
    median_and_mode = calculate_median_and_mode(data)
    print("The median of given data set is :", median_and_mode[0])
    print("The mode of given data set is :", median_and_mode[1])