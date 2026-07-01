"""
Write a python code to a randomly select a number of items, but with a given algorithm
"""

import random

def select_with_algorithm(items, size):
    # Create a list from 0 to len(items)-1
    item_indices = list(range(len(items)))
    # Create a list of size 0
    selection = []
    # Iterate for the size desired
    for _ in range(size):
        # Select one of the indices randomly
        index = random.choice(item_indices)
        # Store it in the selection list
        selection.append(items[index])
        # Then remove it from the item_indices list
        item_indices.remove(index)
    # Return the selection
    return selection

if __name__ == '__main__':
    items = [1, 2, 3, 4, 5, 6, 7]
    size = 5
    selection = select_with_algorithm(items, size)
    print(selection)