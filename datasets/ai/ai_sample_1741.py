import itertools

# Define the travelling salesman problem (TSP)
def calc_dist(a, b):
    # calculate Euclidean distance between points 'a' and 'b'
    dist =  # your code
    return dist

def travelling_salesman(points):
    # "points" is a list of tuples [(x1, y1), (x2, y2), ...]
    best_solution = None
    min_dist = float('inf')
    solutions = itertools.permutations(points) 
    for solution in solutions:
        # calculate the total distance of the route
        dist = 0
        for i in range(len(solution) - 1):
            dist += calc_dist(solution[i], solution[i+1])
        # check if it is the shortest route 
        if dist < min_dist:
            min_dist = dist
            best_solution = solution
    return best_solution

solution = travelling_salesman([(0, 0), (2, 2), (3, 1), (1, 3)])
print(solution)  # [(0, 0), (2, 2), (3, 1), (1, 3)]