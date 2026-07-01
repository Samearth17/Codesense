def count_frequency(arr):
    # Create empty dictionary
    frequency = {}

    # Iterate through array
    for item in arr:
        # Iterate through elements of each dictionary
        for element in item.values():
            # Increment the counter for each element
            if element in frequency:
                frequency[element] += 1
            else:
                frequency[element] = 1

    return frequency