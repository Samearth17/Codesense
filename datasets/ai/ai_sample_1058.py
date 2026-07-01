"""
Generate a python program to generate a subset of random numbers from the given array
"""

import random

# Function to generate a subset of random numbers
def generate_subset(array, subset_size):
    # Get a list of indices
    indices = random.sample(range(len(array)), subset_size)
    
    # Get a list of elements from the array
    subset = [array[i] for i in indices]
    
    return subset

if __name__ == '__main__':
    array = [4, 5, 2, 9, 8, 6, 2, 3, 7, 1]
    subset_size = 5
    print(generate_subset(array, subset_size))