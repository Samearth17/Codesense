def order_items_by_popularity(items):
    """Function to order items by their popularity."""
    items_dict = {}
 
    # Create a dictionary of item and its count
    for item in items:
        if item in items_dict:
            items_dict[item] += 1
        else:
            items_dict[item] = 1
 
    # Sort the items by their count in descending order
    sorted_items = sorted(items_dict.items(), key=lambda i: i[1], reverse=True)
 
    # Store the sorted items in a list
    sorted_items_list = [item[0] for item in sorted_items]
 
    return sorted_items_list