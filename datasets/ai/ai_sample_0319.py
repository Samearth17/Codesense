import math

def find_closest_point(input_coordinates, coordinates_set):
    # Calculate the euclidean distance for each point in the set
    distances = []
    for c in coordinates_set:
        dist = math.sqrt((input_coordinates[0] - c[0]) **2 + (input_coordinates[1] - c[1]) **2)
        distances.append(dist)
        
    # Find the index of the point with the smallest distance
    idx = distances.index(min(distances))
    
    # Return the closest point
    return coordinates_set[idx]
    
# Input coordinates
input_coordinates = (2, 3)

# Set of coordinates
coordinates_set = [(2.1, 3.1), (1, 1), (0.5, 2.5)]

# Find and print the closest point
closest_point = find_closest_point(input_coordinates, coordinates_set)
print('Closest point: ', closest_point)