def optimization(items, cost):  
    """
    Function to optimize cost production
    """
    total_cost = 0
    total_items = len(items)
    while total_items > 0:
        # Produce one item at a time
        total_items -= 1
        total_cost += cost
    return total_cost

items = [4]
cost = 1

total_cost = optimization(items, cost)
print("Total cost is:", total_cost)