def most_frequent(input_list):
    # Create a dictionary to store frequency of each item
    frequency_dict = {}
    for item in input_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1

    # Find the most frequent item
    most_frequent_item = max(frequency_dict, key=frequency_dict.get)

    return most_frequent_item

input_list = [1, 2, 3, 4, 1, 2, 5, 2, 4]
most_frequent_item = most_frequent(input_list)

print(most_frequent_item)