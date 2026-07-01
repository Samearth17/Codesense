def most_common(nums):
    # Create a dictionary to store the counts
    counts = {}

    # Iterate over the elements
    for num in nums:
        # If the element is not present in the dictionary, add it
        if num not in counts:
            counts[num] = 0

        # Update the count
        counts[num] += 1

    # Get the maximum count
    max_count = max(counts.values())

    # Return the elements that have maximum count
    return [num for num, count in counts.items() if count == max_count]