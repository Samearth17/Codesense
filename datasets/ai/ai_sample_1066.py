# Function to implement an optimized memory sorting algorithm 
def memory_optimized_sort(items):
    # Find the length of the list
    n = len(items) 
    # Initialize the sorted list to the same size
    sorted_items = [None] * n 
    # Set the counter for even and odd
    even_count = 0
    odd_count = 0

    # Iterate over the items in the list
    for item in items:
        # If item is even, add it to the end of the list
        if item % 2 == 0:
            sorted_items[n - 1 - even_count] = item
            even_count += 1
        else:
            # If item is odd, add it to the beginning of the list
            sorted_items[odd_count] = item
            odd_count += 1

    return sorted_items