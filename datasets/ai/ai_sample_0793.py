def calculateMeanMedianMode(lst):
    lst.sort()
    length = len(lst)
    mean = sum(lst) / length
    if length % 2 == 0:
        idx1 = (length / 2) - 1
        idx2 = length / 2
        median = (lst[int(idx1)] + lst[int(idx2)]) / 2
    else:
        median = lst[int(length / 2)]

    count = 0
    max_occurance = 0
    for i in range(length):
        if lst[i] == lst[i + 1]:
            count += 1
            if count > max_occurance:
                max_occurance = count
                mode = lst[i]
        else:
            count = 0
    return mean, median, mode

mean, median, mode = calculateMeanMedianMode([1, 2, 2, 3, 5, 8, 10])
print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)