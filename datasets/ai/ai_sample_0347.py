def maxPairSum(input_list):

    #assume the first and second elements are the max pair
    max_pair_sum = input_list[0] + input_list[1]

    # Keep track of the max pair
    pair_index_one = 0
    pair_index_two = 1

    # iterate through the entire list
    for index_one in range(0, len(input_list)):
        for index_two in range(index_one + 1, len(input_list)):

            # if the current pair sum is greater than the max pair sum
            # update the max pair sum and the pair indices
            if input_list[index_one] + input_list[index_two] > max_pair_sum:
                max_pair_sum = input_list[index_one] + input_list[index_two]
                pair_index_one = index_one
                pair_index_two = index_two

    #return the max pair sum
    return max_pair_sum