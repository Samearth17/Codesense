"""
Clustering Algorithm for Mission Planning
"""

import numpy as np

def create_cluster_matrix(dataset):
    # Get required data
    num_satellites = dataset['mission_details']['num_of_satellites']
    target_region = dataset['mission_details']['target_region']
    mission_duration = dataset['mission_details']['mission_duration']

    # Create the matrix
    matrix = np.zeros((num_satellites, mission_duration))

    # Fill the matrix with the target region
    for i in range(num_satellites):
        matrix[i]= np.ones((1, mission_duration))*target_region

    return matrix

if __name__ == '__main__':
    dataset = {
        'mission_name': 'Space Mission',
        'mission_details': {
            'num_of_satellites': 5,
            'target_region': 'South East Asia',
            'mission_duration': 24
        }
    }

    cluster_matrix = create_cluster_matrix(dataset)
    print(cluster_matrix)